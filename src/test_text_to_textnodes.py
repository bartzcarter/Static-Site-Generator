import unittest
from textnode import *
from text_to_textnodes import text_to_textnodes

class TestTextToTextNodes(unittest.TestCase):
    def test_text_to_textnodes(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        lst = text_to_textnodes(text)
        self.assertListEqual([
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ],
            lst,
        )

    def test_plain_text(self):
        text = "Just a normal sentence."
        lst = text_to_textnodes(text)
        self.assertListEqual([TextNode("Just a normal sentence.", TextType.TEXT)], lst)

    def test_bold_text(self):
        text = "This is **bold** text."
        lst = text_to_textnodes(text)
        self.assertListEqual([
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text.", TextType.TEXT),
        ], lst)

    def test_italic_text(self):
        text = "This is _italic_ text."
        lst = text_to_textnodes(text)
        self.assertListEqual([
            TextNode("This is ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" text.", TextType.TEXT),
        ], lst)

    def test_code_text(self):
        text = "Here is `code`."
        lst = text_to_textnodes(text)
        self.assertListEqual([
            TextNode("Here is ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(".", TextType.TEXT),
        ], lst)

    def test_image_text(self):
        text = "An image: ![alt text](https://example.com/image.jpg)"
        lst = text_to_textnodes(text)
        self.assertListEqual([
            TextNode("An image: ", TextType.TEXT),
            TextNode("alt text", TextType.IMAGE, "https://example.com/image.jpg"),
        ], lst)

    def test_link_text(self):
        text = "Visit [Google](https://google.com)."
        lst = text_to_textnodes(text)
        self.assertListEqual([
            TextNode("Visit ", TextType.TEXT),
            TextNode("Google", TextType.LINK, "https://google.com"),
            TextNode(".", TextType.TEXT),
        ], lst)

    def test_mixed_formatting(self):
        text = "**bold** _italic_ `code`"
        lst = text_to_textnodes(text)
        self.assertListEqual([
            TextNode("bold", TextType.BOLD),
            TextNode(" ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" ", TextType.TEXT),
            TextNode("code", TextType.CODE),
        ], lst)

    def test_unmatched_delimiters(self):
        text = "This is **not closed"
        with self.assertRaises(Exception) as context:
            text_to_textnodes(text)
        self.assertEqual(str(context.exception), "invalid Markdown syntax")

    def test_multiple_links_and_images(self):
        text = "Here is a ![first image](https://img1.com) and a [link](https://example.com) and another ![second image](https://img2.com)."
        lst = text_to_textnodes(text)
        self.assertListEqual([
            TextNode("Here is a ", TextType.TEXT),
            TextNode("first image", TextType.IMAGE, "https://img1.com"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://example.com"),
            TextNode(" and another ", TextType.TEXT),
            TextNode("second image", TextType.IMAGE, "https://img2.com"),
            TextNode(".", TextType.TEXT),
        ], lst)


if __name__ == '__main__':
    unittest.main()