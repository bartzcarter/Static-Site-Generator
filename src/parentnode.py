from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError("every parent node must have a tag")
        elif not self.children:
            raise ValueError("every parent node must have a children")

        str = f""
        for child in self.children:
            str += child.to_html()

        return f"<{self.tag}>{str}</{self.tag}>"