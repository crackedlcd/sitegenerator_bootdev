class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        res = ""
        if self.props is None:
            return ""
        for prop in self.props:
            res += f' {prop}="{self.props[prop]}"'

        return res

    def __repr__(self):
        return f"Tag: {self.tag}, value:{self.value}, children: {self.children}, props: {self.props} \n props_to_html{self.props_to_html()}"


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError
        if self.tag is None:
            return self.value

        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError
        if self.children is None:
            raise ValueError("No Children")

        childtags = ""
        for child in self.children:
            childtags += child.to_html()

        return f"<{self.tag}{self.props_to_html()}>{childtags}</{self.tag}>"
