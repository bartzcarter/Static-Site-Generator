import unittest

from src.block_to_block_type import block_to_block_type
from src.blocktype import BlockType


class TestBlockToBlockType(unittest.TestCase):
    def test_block_to_block_type_heading(self):
        block = "##### this is a heading"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type.value, BlockType.HEADING.value)

    def test_block_to_block_type_code(self):
        block = "```this is a code block```"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type.value, BlockType.CODE.value)

    def test_block_to_block_type_quote(self):
        block = "> This is a quoted line\n> Another quoted line"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type.value, BlockType.QUOTE.value)

    def test_block_to_block_type_unordered_list(self):
        block = "- Item 1\n- Item 2\n- Item 3"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type.value, BlockType.UNORDERED_LIST.value)

    def test_block_to_block_type_ordered_list(self):
        block = "1. Item 1\n2. Item 2\n3. Item 3"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type.value, BlockType.ORDERED_LIST.value)

    def test_block_to_block_type_normal_paragraph(self):
        block = "This is a simple paragraph with no markdown syntax."
        block_type = block_to_block_type(block)
        self.assertEqual(block_type.value, BlockType.PARAGRAPH.value)

if __name__ == '__main__':
    unittest.main()