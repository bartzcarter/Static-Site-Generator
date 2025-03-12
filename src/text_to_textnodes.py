from textnode import TextType, TextNode
from split_nodes_delimiter import split_nodes_delimiter
from split_nodes_image import split_nodes_image
from split_nodes_link import split_nodes_link

def text_to_textnodes(text):
    node = TextNode(text, TextType.TEXT)
    textnodes_list = [node]

    try:
        textnodes_list = split_nodes_delimiter(textnodes_list, "**", TextType.BOLD)
        textnodes_list = split_nodes_delimiter(textnodes_list, "_", TextType.ITALIC)
        textnodes_list = split_nodes_delimiter(textnodes_list, "`", TextType.CODE)
    except Exception:
        raise Exception("invalid Markdown syntax")

    textnodes_list = split_nodes_image(textnodes_list)
    textnodes_list = split_nodes_link(textnodes_list)
    return textnodes_list
