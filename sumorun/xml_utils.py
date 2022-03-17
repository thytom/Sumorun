import xml.etree.ElementTree as ET

def load_xml_file(file_location:str) -> ET.ElementTree:
    """Load an XML file from disk as an element tree"""
    tree = ET.parse(file_location)
    return tree

def write_xml_file(tree: ET.ElementTree, file_location:str) -> ET.ElementTree:
    tree.write(file_location)

def filter_tags_from_xml_tree(tree : ET.ElementTree, tag:str):
    """Remove specific tag from an XML file."""
    for t in tree.findall(tag):
        tree.getroot().remove(t)

def add_elem_to_tree_root(tree : ET.ElementTree, elem : ET.Element):
    """Insert a tag under a  given element"""
    tree.getroot().append(elem)