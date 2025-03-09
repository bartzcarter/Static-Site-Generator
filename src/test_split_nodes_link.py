import unittest
from split_nodes_link import split_nodes_link
from textnode import TextNode, TextType

class TestSplitNodesLink(unittest.TestCase):
    def test_split_links(self):
        node = TextNode(
            "This is text with an [link](https://i.imgur.com/zjjcJKZ.png) and another [second link](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second link", TextType.LINK, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_links_single_link(self):
        node = TextNode("A single [example](https://example.com) link.", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("A single ", TextType.TEXT),
                TextNode("example", TextType.LINK, "https://example.com"),
                TextNode(" link.", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_split_links_multiple_links_adjacent(self):
        node = TextNode(
            "[First](https://first.com)[Second](https://second.com)", TextType.TEXT
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("First", TextType.LINK, "https://first.com"),
                TextNode("Second", TextType.LINK, "https://second.com"),
            ],
            new_nodes,
        )

    def test_split_links_link_at_start(self):
        node = TextNode("[Start](https://start.com) of the text.", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("Start", TextType.LINK, "https://start.com"),
                TextNode(" of the text.", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_split_links_link_at_end(self):
        node = TextNode("Text before a [link](https://end.com)", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("Text before a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://end.com"),
            ],
            new_nodes,
        )

    def test_split_links_no_links(self):
        node = TextNode("This text has no links.", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This text has no links.", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_split_links_link_with_spaces(self):
        node = TextNode("Here is a [spaced link](https://spaced.com) in text.", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("Here is a ", TextType.TEXT),
                TextNode("spaced link", TextType.LINK, "https://spaced.com"),
                TextNode(" in text.", TextType.TEXT),
            ],
            new_nodes,
        )


    def test_split_links_link_surrounded_by_text(self):
        node = TextNode("Start [middle](https://middle.com) end.", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("Start ", TextType.TEXT),
                TextNode("middle", TextType.LINK, "https://middle.com"),
                TextNode(" end.", TextType.TEXT),
            ],
            new_nodes,
        )
if __name__ == '__main__':
    unittest.main()