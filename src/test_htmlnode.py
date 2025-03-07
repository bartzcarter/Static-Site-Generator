import unittest
from htmlnode import HTMLNode

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

    def test_to_html_on_htmlnode_errors(self):
        with self.assertRaises(NotImplementedError) as context:
            node = HTMLNode("text", "h1", ["a", "p"], )
            node.to_html()
        self.assertEqual(str(context.exception), "Must impliment in child class")

if __name__ == '__main__':
    unittest.main()
