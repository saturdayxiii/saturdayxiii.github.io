import os
import re
import yaml
import shutil
import unicodedata

# Define the root folder and subfolders
posts_folder = "_posts"
tags_folder = "tags"

# Create the tags folder if it doesn't exist
if not os.path.exists(tags_folder):
    os.makedirs(tags_folder)

# Clear the existing files in the tags folder (moved outside of the loop)
for tag_filename in os.listdir(tags_folder):
    tag_file_path = os.path.join(tags_folder, tag_filename)
    if os.path.isfile(tag_file_path):
        os.remove(tag_file_path)

# Function to process and format tags
def process_tags(tags):
    processed_tags = []
    for tag in tags:
        # Remove spaces, replace apostrophes with empty string, convert to lowercase,
        # and replace special characters with their basic equivalents
        if tag:
            print(f"Processing tag: {tag}")
            processed_tag = tag.replace(' ', '_').replace('-', '_').replace("'", '').lower()
            # Replace special characters with basic equivalents
            processed_tag = ''.join(c for c in unicodedata.normalize('NFKD', processed_tag)
                                    if not unicodedata.combining(c))
            processed_tags.append(processed_tag)
    return processed_tags

# Process each .md file in the _posts folder
for filename in os.listdir(posts_folder):
    if filename.endswith(".md"):
        post_file = os.path.join(posts_folder, filename)
        print(f"Processing file: {post_file}")

        with open(post_file, "r", encoding="utf-8") as f:  # Specify the encoding as utf-8
            content = f.read()
            # Use regular expressions to extract the tags from the YAML front matter
            match = re.search(r'^tags:(.*?)(?=\w+:|$)', content, re.DOTALL | re.MULTILINE)
            if match and match.group(0).strip() == 'tags:':
                match = re.search(r'^tags:\s*(.*?)(?=\n[^\s])', content, re.DOTALL | re.MULTILINE)
                print("Found tag list:")
                print(match)
                tags_content = match.group(1).strip()
                # Use re.findall() to extract tags
                tags_list = re.findall(r'\s*-\s*(?:"([^"]*)"|\'([^\']*)\'|(\S+))', tags_content)
                processed_tags = process_tags([tag for tag in sum(tags_list, ()) if tag])
                print(f"Processed tags: {processed_tags}")

                # Create tag files in the tags folder
                for tag in processed_tags:
                    tag_file_path = os.path.join(tags_folder, f"{tag}.md")
                    tag_yaml = f"---\nlayout: tags\ntitle: \"Tag: {tag}\"\ntag-name: {tag}\n---"
                    with open(tag_file_path, "w") as tag_file:
                        tag_file.write(tag_yaml)
            else:
                print("Found tag string:")
                print(match)
                tags_content = match.group(1).strip()
                tags_list = yaml.safe_load(tags_content)
                if tags_list:
                    processed_tags = process_tags(tags_list)
                    print(f"Processed tags: {processed_tags}")

                    # Create tag files in the tags folder
                    for tag in processed_tags:
                        tag_file_path = os.path.join(tags_folder, f"{tag}.md")
                        tag_yaml = f"---\nlayout: tags\ntitle: \"Tag: {tag}\"\ntag-name: {tag}\n---"
                        with open(tag_file_path, "w") as tag_file:
                            tag_file.write(tag_yaml)

# Your tags should now be processed, and files created in the tags folder