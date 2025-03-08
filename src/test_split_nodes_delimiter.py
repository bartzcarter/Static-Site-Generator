import unittest
from split_nodes_delimiter import split_nodes_delimiter
from textnode import TextNode, TextType

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_split_nodes_delimiter_one_node(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ])

    def test_split_nodes_delimiter_no_delimiter(self):
        node = TextNode("This is just normal text", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [
            TextNode("This is just normal text", TextType.TEXT)
        ])

    def test_split_nodes_delimiter_at_edges(self):
        node = TextNode("`start` code and end `finish`", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [
            TextNode("", TextType.TEXT),  # Empty before the first code block
            TextNode("start", TextType.CODE),
            TextNode(" code and end ", TextType.TEXT),
            TextNode("finish", TextType.CODE),
            TextNode("", TextType.TEXT)  # Empty after the last code block
        ])

    def test_split_nodes_delimiter_empty_text(self):
        node = TextNode("", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [
            TextNode("", TextType.TEXT)
        ])

    def test_split_nodes_delimiter_other_text_types(self):
        node1 = TextNode("`This is first code block`", TextType.CODE)
        node2 = TextNode("`And this is another code block`", TextType.CODE)
        new_nodes = split_nodes_delimiter([node1, node2], "`", TextType.CODE)
        self.assertEqual(new_nodes, [
            TextNode("`This is first code block`", TextType.CODE),
            TextNode("`And this is another code block`", TextType.CODE)
        ])

    def test_split_nodes_delimiter_multiple_positions(self):
        node = TextNode("This is `code` at `multiple` places", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [
            TextNode("This is ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" at ", TextType.TEXT),
            TextNode("multiple", TextType.CODE),
            TextNode(" places", TextType.TEXT),
        ])

    def test_split_nodes_delimiter_empty_between(self):
        node = TextNode("`code``block`", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [
            TextNode("", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode("", TextType.TEXT),
            TextNode("block", TextType.CODE),
            TextNode("", TextType.TEXT)
        ])

    def test_split_nodes_delimiter_mixed_text_types(self):
        node1 = TextNode("This is **bold** and", TextType.TEXT)
        node2 = TextNode(" **more bold** here", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node1, node2], "**", TextType.BOLD)
        self.assertEqual(new_nodes, [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" and", TextType.TEXT),
            TextNode(" ", TextType.TEXT),
            TextNode("more bold", TextType.BOLD),
            TextNode(" here", TextType.TEXT)
        ])

    def test_split_nodes_delimiter_missing_closing_delimiter(self):
        node = TextNode("`start code block without end", TextType.TEXT)
        with self.assertRaises(Exception) as context:
            split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(str(context.exception), "invalid Markdown syntax")

    def test_split_nodes_delimiter_missing_opening_delimiter(self):
        node = TextNode("code block without start `` `` `finish", TextType.TEXT)
        with self.assertRaises(Exception) as context:
            split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(str(context.exception), "invalid Markdown syntax")

    def test_split_nodes_delimiter_empty_code_blocks_valid(self):
        node = TextNode("code block without start `` ``finish", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [
            TextNode("code block without start ", TextType.TEXT),
            TextNode("", TextType.CODE),
            TextNode(" ", TextType.TEXT),
            TextNode("", TextType.CODE),
            TextNode("finish", TextType.TEXT),
        ])

if __name__ == '__main__':
    unittest.main()