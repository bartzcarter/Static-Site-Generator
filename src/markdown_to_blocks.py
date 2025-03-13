from textnode import *

# def markdown_to_blocks(markdown):
#     blocks = markdown.split("\n\n")
#     blocks = [block.strip() for block in blocks if block.strip()]
#     return blocks


# def markdown_to_blocks(markdown):
#     blocks = markdown.split("\n\n")
#     # Strip each line in the block, not just the block itself
#     blocks = ['\n'.join([line.strip() for line in block.split('\n')]) for block in blocks if block.strip()]
#     return blocks

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    # Strip leading/trailing whitespace from each block and remove empty blocks
    blocks = [block.strip() for block in blocks if block.strip()]
    return blocks