import argparse


def get_problem_number(title: str) -> int:
    return title.split(".")[0]


# parser
parser = argparse.ArgumentParser(
    description="Create a markdown file using --title parameters.")
parser.add_argument("--title", type=str, help="Title for the Markdown file")
parser.add_argument("--topic", type=str,
                    help="Top for the Markdown file link in README")
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

# link markdown in README
link_text = title
link_destination = f"{problem_number}.md"
link = f"[{link_text}]({link_destination})"

# find topic block
topic = args.topic
original_readme_content = None
with open("README.md", 'r', encoding='utf-8') as readme_file:
    original_readme_content = readme_file.read()
topic_index = original_readme_content.find(topic)

new_readme_content = ""
# new topic
if topic_index == -1:
    new_topic = f"## {topic}"
    new_readme_content = f"{original_readme_content}\n{new_topic}\n\n{link}\n"
else:
    # get topic block content
    next_topic_index = original_readme_content.find("##", topic_index)
    topic_content_index = original_readme_content.find("[", topic_index)
    topic_content_raw = original_readme_content[topic_content_index:next_topic_index]

    # remove blank and newline
    topic_content = topic_content_raw.replace(" ", "").replace("\n", "")

    # get a list of topics
    topic_notes = topic_content.split("[")
    topic_notes.pop(0)

    # the original index is at the next topic, so that
    #   if the new problem number is highest among the topic,
    #   the new link should be at the next topic
    insert_index = next_topic_index
    for title in topic_notes:
        note_number = get_problem_number(title)
        if note_number > problem_number:
            insert_index = original_readme_content.find(f"[{note_number}.")
            break
    new_readme_content = f"{original_readme_content[:insert_index]}{link}\n\n{original_readme_content[insert_index:]}"

# write link into README
with open("README.md", 'w', encoding='utf-8') as readme_file:
    readme_file.write(f"{new_readme_content}")
