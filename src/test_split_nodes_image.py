import unittest
from split_nodes_image import split_nodes_image
from textnode import TextNode, TextType

class TestSplitNodesImage(unittest.TestCase):
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_images_single_image(self):
        node = TextNode("![only image](https://i.imgur.com/abc123.png)", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("only image", TextType.IMAGE, "https://i.imgur.com/abc123.png"),
            ],
            new_nodes,
        )

    def test_split_images_no_images(self):
        node = TextNode("This is just plain text with no images.", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is just plain text with no images.", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_split_images_image_at_start(self):
        node = TextNode(
            "![start image](https://i.imgur.com/start.png) followed by text.",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("start image", TextType.IMAGE, "https://i.imgur.com/start.png"),
                TextNode(" followed by text.", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_split_images_image_at_end(self):
        node = TextNode(
            "Text before an image ![end image](https://i.imgur.com/end.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("Text before an image ", TextType.TEXT),
                TextNode("end image", TextType.IMAGE, "https://i.imgur.com/end.png"),
            ],
            new_nodes,
        )

    def test_split_images_multiple_adjacent_images(self):
        node = TextNode(
            "![img1](https://i.imgur.com/1.png)![img2](https://i.imgur.com/2.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("img1", TextType.IMAGE, "https://i.imgur.com/1.png"),
                TextNode("img2", TextType.IMAGE, "https://i.imgur.com/2.png"),
            ],
            new_nodes,
        )

    def test_split_images_text_between_images(self):
        node = TextNode(
            "![img1](https://i.imgur.com/1.png) some text ![img2](https://i.imgur.com/2.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("img1", TextType.IMAGE, "https://i.imgur.com/1.png"),
                TextNode(" some text ", TextType.TEXT),
                TextNode("img2", TextType.IMAGE, "https://i.imgur.com/2.png"),
            ],
            new_nodes,
        )

if __name__ == "__main__":
    unittest.main()