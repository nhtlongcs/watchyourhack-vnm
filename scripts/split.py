import re
import os

def split_readme(input_file, output_folder):
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split content based on Markdown headings and capture both heading and content
    sections = re.split(r'^(#{1,3}\s.+)$', content, flags=re.MULTILINE)[1:]

    new_sections = [sections[i] + sections[i+1] for i in range(0, len(sections)-1, 2)]
    sections = new_sections

    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Write sections to separate files
    for i, section in enumerate(sections):
        # Extract heading level and text
        match = re.match(r'^(#{1,3})\s(.+)$', section, flags=re.MULTILINE)
        if match:
            level, heading_text = match.groups()
            level = len(level)  # Calculate level based on the number of '#'

            # Ensure the level is within a valid range
            level = min(max(1, level), 3)

            if level < 2:
                output_file = os.path.join(output_folder, f'section_{i}.md')
                with open(output_file, 'w', encoding='utf-8') as f:
                    f.write(section.strip())
            elif level == 2:
                # Create a subfolder based on heading text
                # subfolder_name = re.sub(r'\s+', '_', heading_text.lower())
                subfolder_name = f'section_{i}'
                subfolder_path = os.path.join(output_folder, subfolder_name)
                os.makedirs(subfolder_path, exist_ok=True)
                # Write to a file inside the subfolder
                output_file = os.path.join(subfolder_path, f'section_{i}.md')
                with open(output_file, 'w', encoding='utf-8') as f:
                    f.write(section.strip())
            else:
                # Write to a file inside the subfolder
                output_file = os.path.join(subfolder_path, f'section_{i}.md')
                with open(output_file, 'w', encoding='utf-8') as f:
                    f.write(section.strip())
if __name__ == "__main__":
    input_file = 'README.md'  # Change this to your input README file
    output_folder = 'output'   # Change this to the desired output folder

    split_readme(input_file, output_folder)