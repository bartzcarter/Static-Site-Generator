import unittest
from htmlnode import HTMLNode
from leafnode import LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode("text", "a", None, {"href": "http://example.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href=http://example.com target=_blank')

    def test_props_to_html2(self):
        node = HTMLNode("text", "h1", ["a","p"],
                        {"href": "http://example.com", "target": "_blank", "style": "text-decoration:none"})
        self.assertEqual(node.props_to_html(), ' href=http://example.com target=_blank style=text-decoration:none')

    def test_props_to_html_None(self):
        node = HTMLNode("text", "h1", ["a", "p"],
                        None)
        self.assertEqual(node.props_to_html(), "")

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_b(self):
        node = LeafNode("b", "this will be bold")
        self.assertEqual(node.to_html(), "<b>this will be bold</b>")

    def test_leaf_to_html_li(self):
            node = LeafNode("li", "list item")
            self.assertEqual(node.to_html(), "<li>list item</li>")





if __name__ == '__main__':
    unittest.main()
