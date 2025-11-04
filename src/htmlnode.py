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
