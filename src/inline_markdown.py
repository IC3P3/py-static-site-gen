from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split = []
        sections = old_node.text.split(delimiter)

        if len(sections) % 2 == 0:
            raise ValueError("Invalid Markdown")

        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split.append(TextNode(sections[i], TextType.TEXT))
            else:
                split.append(TextNode(sections[i], text_type))

        new_nodes.extend(split)
    return new_nodes
