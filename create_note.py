import argparse

# parser
parser = argparse.ArgumentParser(description='Create a markdown file using --title parameters.')
parser.add_argument('--title', type=str, help='Title for the Markdown file')
args = parser.parse_args()

# create markdown from note_template.md
title = args.title
note_markdown = None
template_content = None
with open("note_template.md", 'r', encoding='utf-8') as template_file:
    template_content = template_file.read()
note_markdown = template_content.replace("# ", f"# {title}", 1)

# save markdown to new markdown file
problem_number = title.split(".")[0]
with open(f"{problem_number}.md", 'w', encoding='utf-8') as output_file:
    output_file.write(note_markdown)

# add link in README
link_text = title
link_destination = f"{problem_number}.md"
link = f"[{link_text}]({link_destination})"
readme_content = None
with open("README.md", 'r', encoding='utf-8') as readme_file:
    readme_content = readme_file.read()
with open("README.md", 'w', encoding='utf-8') as readme_file:
    readme_file.write(f"{readme_content}\n{link}\n")