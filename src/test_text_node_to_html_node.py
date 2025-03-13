import unittest
from textnode import TextNode, TextType
from text_node_to_html_node import text_node_to_html_node
from enum import Enum


class TestTextNodeToHtmlNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("This is a bold node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a bold node")

    def test_italic(self):
        node = TextNode("This is an italic node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is an italic node")

    def test_code(self):
        node = TextNode("This is a code node", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is a code node")

    def test_link(self):
        node = TextNode("anchor text", TextType.LINK, "http://test.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "anchor text")
        self.assertEqual(html_node.props["href"], "http://test.com")

    def test_image(self):
        node = TextNode("alt text", TextType.IMAGE, "images/pic1.jpg")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "alt text")
        self.assertEqual(html_node.props["src"], "images/pic1.jpg")
        self.assertEqual(html_node.props["alt"], "alt text")

    def test_invalid_text_type_errors(self):
        test = Enum('TEST', {'TEST': 'test'})
        with self.assertRaises(Exception) as context:
            node = TextNode("alt text", test.TEST, "images/pic1.jpg")
            html_node = text_node_to_html_node(node)
        self.assertEqual(str(context.exception), "invalid text type")


if __name__ == '__main__':
    unittest.main()