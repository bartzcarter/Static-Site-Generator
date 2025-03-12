from textnode import TextType, TextNode
from extract_markdown_images import extract_markdown_images
import re

def split_nodes_image(nodes):
    new_nodes = []

    for node in nodes:
        # if not node.text_type.value == "text":
        #     new_nodes.append(node)
        images = extract_markdown_images(node.text)
        text = re.split(r"(!\[.*?\]\(.*?\))",node.text)
        for t in text:
            images_in_t = extract_markdown_images(t)
            if set(images_in_t).issubset(set(images)) and not images_in_t == []:
                new_nodes.append(TextNode(images_in_t[0][0], TextType.IMAGE, images_in_t[0][1]))
            elif not t == "":
                new_nodes.append(TextNode(t, node.text_type, node.url))

    return new_nodes

