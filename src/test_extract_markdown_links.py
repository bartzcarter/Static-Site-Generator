import unittest
from extract_markdown_links import extract_markdown_links

class TestExtractMarkdownLinks(unittest.TestCase):
    def test_extract_single_link(self):
        matches = extract_markdown_links(
            "This is a [link](https://example.com)."
        )
        self.assertListEqual([("link", "https://example.com")], matches)

    def test_extract_multiple_links(self):
        matches = extract_markdown_links(
            "Here are two links: [first](https://example.com/1) and [second](https://example.com/2)."
        )
        self.assertListEqual(
            [("first", "https://example.com/1"), ("second", "https://example.com/2")],
            matches
        )

    def test_extract_link_with_spaces_in_text(self):
        matches = extract_markdown_links(
            "Click [this link here](https://example.com/page)."
        )
        self.assertListEqual([("this link here", "https://example.com/page")], matches)

    def test_extract_link_with_special_chars_in_text(self):
        matches = extract_markdown_links(
            "Check this [awesome-link!](https://example.com/special)"
        )
        self.assertListEqual([("awesome-link!", "https://example.com/special")], matches)

    def test_extract_no_links(self):
        matches = extract_markdown_links("This text has no links.")
        self.assertListEqual([], matches)

    def test_extract_broken_markdown_link(self):
        matches = extract_markdown_links(
            "This is not a valid link [alt text(https://example.com/page)"
        )
        self.assertListEqual([], matches)

    def test_ignore_images(self):
        matches = extract_markdown_links(
            "This is an image ![alt text](https://example.com/image.png)."
        )
        self.assertListEqual([], matches)  # Ensures image syntax is ignored

    def test_link_adjacent_to_text(self):
        matches = extract_markdown_links(
            "Click here[example](https://example.com) for details."
        )
        self.assertListEqual([("example", "https://example.com")], matches)

    def test_link_inside_parentheses(self):
        matches = extract_markdown_links(
            "(See this [example](https://example.com) for reference)"
        )
        self.assertListEqual([("example", "https://example.com")], matches)

if __name__ == "__main__":
    unittest.main()