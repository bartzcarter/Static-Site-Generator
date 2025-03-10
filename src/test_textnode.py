import unittest
from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_text_type_not_equal(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_url_not_equal(self):
        node = TextNode("This is a text node", TextType.BOLD, "http://google.com")
        node2 = TextNode("This is a text node", TextType.BOLD, "http://yahoo.com")
        self.assertNotEqual(node, node2)

    def test_text_not_equal(self):
        node = TextNode("This is not text node", TextType.BOLD, "http://google.com")
        node2 = TextNode("This is a text node", TextType.BOLD, "http://google.com")
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()