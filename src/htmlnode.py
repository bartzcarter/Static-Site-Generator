class HTMLNode():
    def __init__(self, value, tag=None, children=None, props=None):
        self.value = value
        self.tag = tag
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        str = f""
        if self.props:
            for prop in self.props:
                str += f" {prop}={self.props[prop]}"
        return str

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props_to_html()})"
