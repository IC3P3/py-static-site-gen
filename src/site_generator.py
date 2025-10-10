import os

from block_markdown import markdown_to_html_node
from extract_data import extract_title


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path) as from_file:
        markdown = from_file.read()

    with open(template_path) as template_file:
        template = template_file.read()

    html_node = markdown_to_html_node(markdown)
    html = html_node.to_html()

    title = extract_title(markdown)

    template = template.replace("{{ Content }}", html).replace("{{ Title }}", title)

    if not os.path.exists(os.path.dirname(dest_path)):
        os.makedirs(os.path.dirname(dest_path))

    with open(dest_path, "w") as dest_file:
        dest_file.write(template)

    from_file.close()
    template_file.close()
    dest_file.close()
