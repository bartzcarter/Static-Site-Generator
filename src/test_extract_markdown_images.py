import unittest
from extract_markdown_images import extract_markdown_images

class TestExtractMarkdownImages(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_multiple_images(self):
        matches = extract_markdown_images(
            "Here is an image ![first](https://example.com/1.png) and another ![second](https://example.com/2.jpg)."
        )
        self.assertListEqual(
            [("first", "https://example.com/1.png"), ("second", "https://example.com/2.jpg")],
            matches
        )

    def test_extract_image_with_no_alt_text(self):
        matches = extract_markdown_images(
            "This is an image with no alt text ![](https://example.com/image.png)"
        )
        self.assertListEqual([("", "https://example.com/image.png")], matches)

    def test_extract_image_with_spaces_in_alt_text(self):
        matches = extract_markdown_images(
            "This is an image ![My Image](https://example.com/image.jpg)"
        )
        self.assertListEqual([("My Image", "https://example.com/image.jpg")], matches)

    def test_extract_image_with_special_chars_in_alt_text(self):
        matches = extract_markdown_images(
            "Special chars ![@#*!&](https://example.com/special.png)"
        )
        self.assertListEqual([("@#*!&", "https://example.com/special.png")], matches)

    def test_extract_no_images(self):
        matches = extract_markdown_images("This text has no images.")
        self.assertListEqual([], matches)

    def test_extract_broken_markdown_image(self):
        matches = extract_markdown_images(
            "This is not a valid image ![alt text(https://example.com/image.png)"
        )
        self.assertListEqual([], matches)


if __name__ == '__main__':
    unittest.main()