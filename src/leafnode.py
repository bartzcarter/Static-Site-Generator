from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if not self.value:
            raise ValueError("All leaf nodes must have a value")

        # Handling link <a> tag
        if self.tag == 'a' and self.props:
            href = self.props.get('href')
            title = self.props.get('title', '')  # Optional title for the link
            if not href:
                raise ValueError("The link tag requires an href attribute.")
            return f'<a href="{href}" title="{title}">{self.value}</a>'

        # Handling image <img> tag
        elif self.tag == 'img' and self.props:
            src = self.props.get('src')
            alt = self.props.get('alt', '')  # Alt text for the image
            if not src:
                raise ValueError("The img tag requires a src attribute.")
            return f'<img src="{src}" alt="{alt}" />'

        # Handling other tags
        elif self.tag:
            return f"<{self.tag}>{self.value}</{self.tag}>"

        return self.value