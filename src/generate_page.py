from markdown_blocks import markdown_to_html_node
from extract_title import extract_title

def generate_page(base_path, from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    markdown_content = ''
    with open(from_path) as f:
        markdown_content = f.read()
    template_content = ''
    with open(template_path) as f:
        template_content = f.read()
    html_block = markdown_to_html_node(markdown_content)
    html_node = html_block.to_html()
    title = extract_title(markdown_content)

    template_content = template_content.replace("{{ Title }}", title)
    template_content = template_content.replace("{{ Content }}", html_node)
    template_content = template_content.replace('href="/', f'href="{base_path}/')
    template_content = template_content.replace('src="/', f'src="{base_path}/')

    with open(dest_path, "w") as f:
        f.write(template_content)