import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_b(self):
        node = LeafNode("b", "this will be bold")
        self.assertEqual(node.to_html(), "<b>this will be bold</b>")

    def test_leaf_to_html_li(self):
        node = LeafNode("li", "list item")
        self.assertEqual(node.to_html(), "<li>list item</li>")

    def test_leaf_to_html_no_value_errors(self):
        with self.assertRaises(ValueError) as context:
            node = LeafNode("li", None)  # This should raise a ValueError
            node.to_html()
        self.assertEqual(str(context.exception), "All leaf nodes must have a value")

if __name__ == '__main__':
    unittest.main()
