from textnode import TextNode, TextType
from htmlnode import HTMLNode

def main():
    txt_node = TextNode('This is some anchor text', TextType.LINK, 'https://www.boot.dev')
    print(txt_node)

    html_node = HTMLNode('a', "", [], {"href": "https://www.google.com","target": "_blank"})
    print(html_node.props_to_html())

main()