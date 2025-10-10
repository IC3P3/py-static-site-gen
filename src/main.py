from copy_static import copy_static_content
from site_generator import generate_page


dir_path_origin = "./static/"
dir_path_destination = "./public/"


def main():
    copy_static_content(dir_path_origin, dir_path_destination)
    generate_page("./content/index.md", "template.html", "./public/index.html")


main()
