import unittest

from htmlnode import HTMLNode

class TestTextNode(unittest.TestCase):
    def test_not_implemented(self):
        node = HTMLNode('a', "", [], {"href": "https://www.google.com","target": "_blank"})
        with self.assertRaises(NotImplementedError):
            node.to_html()

    def test_props_to_html(self):
        node = HTMLNode('a', "", [], {"href": "https://www.google.com","target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')


if __name__ == "__main__":
    unittest.main()