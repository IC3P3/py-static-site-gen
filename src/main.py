
from copy_static import copy_static_content
from site_generator import generate_pages_recursive


dir_path_origin = "./static/"
dir_path_destination = "./public/"
dir_path_content = "./content/"
temaplte_path = "./template.html"


def main():
    copy_static_content(dir_path_origin, dir_path_destination)
    generate_pages_recursive(
        dir_path_content,
        temaplte_path,
        dir_path_destination
    )


main()
