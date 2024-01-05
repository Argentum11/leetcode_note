import argparse

# parser
parser = argparse.ArgumentParser(description="Create a markdown file using --title parameters.")
parser.add_argument("--title", type=str, help="Title for the Markdown file")
parser.add_argument("--topic", type=str, help="Top for the Markdown file link in README")
args = parser.parse_args()

# create markdown from note_template.md
title = args.title
note_markdown = None
template_content = None
with open("note_template.md", 'r', encoding='utf-8') as template_file:
    template_content = template_file.read()
note_markdown = template_content.replace("# ", f"# {title}", 1)

# # save markdown to new markdown file
problem_number = title.split(".")[0]
# with open(f"{problem_number}.md", 'w', encoding='utf-8') as output_file:
#     output_file.write(note_markdown)

# find topic block
topic = args.topic
original_readme_content = None
with open("README.md", 'r', encoding='utf-8') as readme_file:
    original_readme_content = readme_file.read()
topic_index = original_readme_content.find(topic)
next_topic_index = original_readme_content.find("##", topic_index)

# add link in README
link_text = title
link_destination = f"{problem_number}.md"
link = f"[{link_text}]({link_destination})"

new_readme_content = f"{original_readme_content[:next_topic_index]}{link}\n\n{original_readme_content[next_topic_index:]}"

with open("README.md", 'w', encoding='utf-8') as readme_file:
    readme_file.write(f"{new_readme_content}")