import os
import pathlib

from block_markdown import markdown_to_html_node
from extract_data import extract_title


def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    dest_path_pathlib = pathlib.Path(dest_path)
    if not os.path.exists(str(dest_path_pathlib.parent)):
        os.makedirs(str(dest_path_pathlib.parent))

    with open(from_path, "r") as from_file:
        markdown = from_file.read()

    with open(template_path, "r") as template_file:
        template = template_file.read()

    html_node = markdown_to_html_node(markdown)
    html = html_node.to_html()

    title = extract_title(markdown)

    template = template.replace("{{ Content }}", html).replace("{{ Title }}", title).replace("href=\"/", f"href=\"{basepath}").replace("src=\"/", f"src=\"{basepath}")

    if not os.path.exists(os.path.dirname(dest_path)):
        os.makedirs(os.path.dirname(dest_path))

    with open(dest_path, "w") as dest_file:
        dest_file.write(template)

    from_file.close()
    template_file.close()
    dest_file.close()


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath="/"):
    entries = os.listdir(dir_path_content)

    for entry in entries:
        if os.path.isfile(os.path.join(dir_path_content, entry)):
            generate_page(
                os.path.join(dir_path_content, entry),
                template_path,
                os.path.join(dest_dir_path, entry).replace(".md", ".html"),
                basepath
            )
        else:
            generate_pages_recursive(os.path.join(dir_path_content, entry), template_path, os.path.join(dest_dir_path, entry))
