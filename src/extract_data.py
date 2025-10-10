def extract_title(markdown):
    for line in markdown.split("\n"):
        if line.startswith("# "):
            return line.replace("# ", "")

    raise Exception("No title found!")
