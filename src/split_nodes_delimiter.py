from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for node in old_nodes:
        if not node.text_type.value == "text":
            new_nodes.append(node)
        else:
            temp_lst = node.text.split(delimiter)
            if len(temp_lst) % 2 == 0:
                raise Exception("invalid Markdown syntax")
            for i in range(len(temp_lst)):
                if i % 2 == 0:
                    new_nodes.append(TextNode(temp_lst[i], TextType.TEXT))
                else:
                    new_nodes.append(TextNode(temp_lst[i], text_type))

    return new_nodes

