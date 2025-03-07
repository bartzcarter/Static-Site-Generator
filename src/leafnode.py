from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value):
        super().__init__(tag, value)

    def to_html(self):
        if not self.value:
            raise ValueError("All leaf nodes must have a value")
        if self.tag:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        return self.value