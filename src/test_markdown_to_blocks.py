import unittest
from markdown_to_blocks import markdown_to_blocks

class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_single_paragraph(self):
        md = "This is a single paragraph with **bold** and _italic_."
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, ["This is a single paragraph with **bold** and _italic_."])

    def test_multiple_paragraphs(self):
        md = """First paragraph.

Second paragraph.

Third paragraph with `code` and **bold** text."""
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, [
            "First paragraph.",
            "Second paragraph.",
            "Third paragraph with `code` and **bold** text."
        ])

    def test_extra_blank_lines(self):
        md = """

First paragraph.



Second paragraph.


Third paragraph.
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, [
            "First paragraph.",
            "Second paragraph.",
            "Third paragraph."
        ])

    def test_single_line_break_within_paragraph(self):
        md = """This is a sentence
that should stay in the same paragraph."""
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, [
            "This is a sentence\nthat should stay in the same paragraph."
        ])

    def test_list_items(self):
        md = """- Item 1
- Item 2
- Item 3"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, ["- Item 1\n- Item 2\n- Item 3"])

    def test_mixed_content(self):
        md = """First paragraph with **bold**.

- Bullet point 1
- Bullet point 2

Another paragraph.

1. Numbered item 1
2. Numbered item 2"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, [
            "First paragraph with **bold**.",
            "- Bullet point 1\n- Bullet point 2",
            "Another paragraph.",
            "1. Numbered item 1\n2. Numbered item 2"
        ])

    def test_empty_string(self):
        md = ""
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, [])

    def test_only_whitespace(self):
        md = "     \n   \n   \n"
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, [])


if __name__ == "__main__":
    unittest.main()