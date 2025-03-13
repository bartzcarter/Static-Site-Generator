def extract_title(markdown):
    """Extracts the first H1 header (# Header) from markdown and returns its text."""
    for line in markdown.split("\n"):
        line = line.strip()
        if line.startswith("# "):  # Ensure it's an H1 header
            return line[2:].strip()  # Remove "# " and strip any extra whitespace

    raise ValueError("No H1 header found in the markdown")

