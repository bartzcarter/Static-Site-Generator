from blocktype import BlockType

def block_to_block_type(block):
    # check for heading
    heading = block.split(" ")
    lines = block.split("\n")
    if 1 <= len(heading[0]) <= 6 and all(c == '#' for c in heading[0]):
        return BlockType.HEADING

    # check for code
    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE

    # check for quote

    if all(line.startswith(">") for line in lines):
        return BlockType.QUOTE

    # check for unordered list
    if all(line.startswith("- ") for line in lines):
        return BlockType.UNORDERED_LIST

    # check for ordered list
    for i in range(len(lines)):
        if not lines[i].startswith(f"{i+1}. "):
            break

    else:
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH

