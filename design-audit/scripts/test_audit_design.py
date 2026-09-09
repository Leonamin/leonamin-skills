#!/usr/bin/env python3

import tempfile
import unittest
from pathlib import Path

from audit_design import load_config, scan_file


class AuditDesignTest(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_dir.name)

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def scan(self, source: str, suffix: str = ".tsx"):
        path = self.root / f"Example{suffix}"
        path.write_text(source, encoding="utf-8")
        return scan_file(self.root, path, {})

    def test_sibling_self_closing_cards_are_not_nested(self) -> None:
        findings = self.scan(
            """
            <Card title="One" />
            <Card
              title="Two"
            />
            """
        )

        self.assertFalse(any(finding.rule == "card-in-card" for finding in findings))

    def test_nested_cards_are_reported(self) -> None:
        findings = self.scan('<Card><Card title="Inner" /></Card>')

        self.assertTrue(any(finding.rule == "card-in-card" for finding in findings))

    def test_fragment_href_is_not_reported_as_hex_color(self) -> None:
        findings = self.scan('<a href="#abcdef">Section</a>')

        self.assertFalse(any(finding.rule == "raw-hex" for finding in findings))

    def test_css_hex_color_is_reported_as_warning(self) -> None:
        findings = self.scan(".button { color: #abcdef; }", suffix=".css")
        raw_hex = next(finding for finding in findings if finding.rule == "raw-hex")

        self.assertEqual(raw_hex.severity, "warning")

    def test_invalid_config_is_not_silently_ignored(self) -> None:
        config_dir = self.root / "design-product" / "audits"
        config_dir.mkdir(parents=True)
        (config_dir / "design-lint.config.json").write_text("{", encoding="utf-8")

        with self.assertRaisesRegex(ValueError, "Invalid design audit config"):
            load_config(self.root)


if __name__ == "__main__":
    unittest.main()
