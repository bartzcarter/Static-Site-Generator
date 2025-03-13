from parentnode import *
from block_to_block_type import block_to_block_type
from markdown_to_blocks import *
from text_to_textnodes import *
from text_node_to_html_node import *

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    html_nodes = []
    for node in text_nodes:
        html_nodes.append(text_node_to_html_node(node))
    return html_nodes


def markdown_to_html_node(md):
    blocks = markdown_to_blocks(md)
    children = []

    for block in blocks:
        match(block_to_block_type(block).value):
            case "paragraph":
                temp = text_to_children(block)
                children.append(ParentNode("p", children=temp))
            case "heading":
                # Count the number of '#' characters in the heading
                heading_level = len(block.split()[0])

                # Ensure heading level is between 1 and 6
                if 1 <= heading_level <= 6:
                    tag = f"h{heading_level}"
                else:
                    tag = "h1"  # Default to h1 if somehow out of range

                heading_text = block.lstrip('#').lstrip()
                temp = text_to_children(heading_text)
                children.append(ParentNode(tag, children=temp))
            case "code":
                # Remove the triple backticks and any surrounding newlines
                code_content = block.strip("`").strip()

                text_node = TextNode(code_content, TextType.CODE)
                temp = [text_node_to_html_node(text_node)]
                children.append(ParentNode("pre", children=temp))
            case "quote":
                # Remove the leading "> " from each line and join them
                stripped_block = "\n".join(line.lstrip("> ") for line in block.split("\n"))
                temp = text_to_children(stripped_block)
                children.append(ParentNode("blockquote", children=temp))
            case "unordered_list":
                # Split block into lines and strip the "- " prefix
                list_items = [line.lstrip("- ").strip() for line in block.split("\n")]
                temp = [ParentNode("li", children=text_to_children(item)) for item in list_items]
                children.append(ParentNode("ul", children=temp))
            case "ordered_list":
                # Split block into lines and remove "1. ", "2. ", etc.
                list_items = [line.split(". ", 1)[1].strip() for line in block.split("\n")]
                temp = [ParentNode("li", children=text_to_children(item)) for item in list_items]
                children.append(ParentNode("ol", children=temp))

    return ParentNode("div", children=children)


