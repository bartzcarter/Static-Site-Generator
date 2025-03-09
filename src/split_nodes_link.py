from textnode import TextType, TextNode
from extract_markdown_links import extract_markdown_links
import re

def split_nodes_link(nodes):
    new_nodes = []

    for node in nodes:
        links = extract_markdown_links(node.text)
        text = re.split(r"(\[.*?\]\(.*?\))",node.text)
        for t in text:
            links_in_t = extract_markdown_links(t)
            if set(links_in_t).issubset(set(links)) and not links_in_t == []:
                new_nodes.append(TextNode(links_in_t[0][0], TextType.LINK, links_in_t[0][1]))
            elif not t == "":
                new_nodes.append(TextNode(t, TextType.TEXT))

    return new_nodes