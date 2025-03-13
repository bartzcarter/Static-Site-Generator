from markdown_to_html_node import *
from extract_title import *

import os

def generate_page(from_path, template_path, dest_path):
    """Generates an HTML page from a markdown file using a template."""
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    # Read the markdown file
    with open(from_path, "r", encoding="utf-8") as md_file:
        markdown_content = md_file.read()

    # Read the template file
    with open(template_path, "r", encoding="utf-8") as template_file:
        template_content = template_file.read()

    # Convert Markdown to HTML
    html_content = markdown_to_html_node(markdown_content).to_html()

    # Extract the title
    title = extract_title(markdown_content)

    # Replace placeholders in template
    final_html = template_content.replace("{{ Title }}", title).replace("{{ Content }}", html_content)

    # Ensure the destination directory exists
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    # Write the generated HTML to the destination file
    with open(dest_path, "w", encoding="utf-8") as dest_file:
        dest_file.write(final_html)

    print(f"Page successfully generated: {dest_path}")

