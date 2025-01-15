import re
import os
import argparse
import yaml

class DataviewPreprocessor:
    def process_lines(self, lines):
        new_lines = []
        yaml_content = {}
        in_yaml_block = False
        yaml_lines = []
        line_number = 0
        graphical_abstract = ""
        in_second_slide = False

        for line in lines:
            # Check for the start of a YAML header
            if line.strip() == "---" and not in_yaml_block and line_number == 0:
                in_yaml_block = True
                new_lines.append(line)
            elif in_yaml_block and line.strip() != "---":
                yaml_lines.append(line)
                new_lines.append(line)
            # Check for the end of the YAML header
            elif line.strip() == "---" and in_yaml_block:
                in_yaml_block = False
                try:
                    yaml_content = yaml.safe_load("".join(yaml_lines))
                    
                    # Extract 'title' and 'tldr' if they exist
                    title = yaml_content.get('title')
                    subtitle = yaml_content.get('subtitle')
                    tldr = yaml_content.get('tldr')
                    doi = yaml_content.get('doi')
                    key = yaml_content.get('key')

                    if title or tldr:
                        graphical_abstract = f"\n\n### {title}  <sup style=\"text-align: right;\">[\[doi\]](https://doi.org/{doi}) [\[semantic\]](https://www.semanticscholar.org/paper/{key}) [\[obsidian\]](obsidian://adv-uri?vault=Research-Vault&filepath=20_Work%2FProjects%2FPaperReader%2Fposts%2Fsemantic%2F{key}.md) [\[pdf\]](http://localhost:8080/posts/semantic/{key}.md?pdf)</sup>\n\n{subtitle}\n\n{tldr}"
                except yaml.YAMLError as e:
                    print(f"Error parsing YAML header in file: {e}")
                new_lines.append(line)
                new_lines.append(graphical_abstract)
            elif not in_yaml_block and line_number != 0 and  re.match(r'^-+', line.strip()) and not in_second_slide:
                in_second_slide = True
                new_lines.append(line)
            elif not in_second_slide and line.strip() == "# Abstract":
                new_lines.append("\n\n------\n\n" + line)
            else:
                new_lines.append(line)
            
            line_number += 1
        
        return new_lines

def convert_markdown(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    preprocessor = DataviewPreprocessor()
    processed_lines = preprocessor.process_lines(lines)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(processed_lines)

def process_directory(input_dir, output_dir):
    for root, dirs, files in os.walk(input_dir):
        for file in files:
            if file.endswith('.md'):
                input_file_path = os.path.join(root, file)
                output_file_path = os.path.join(output_dir, os.path.relpath(input_file_path, input_dir))
                
                os.makedirs(os.path.dirname(output_file_path), exist_ok=True)
                
                convert_markdown(input_file_path, output_file_path)

def main():
    parser = argparse.ArgumentParser(description="Convert all Markdown files in a directory to extract and add title and tldr fields under YAML headers.")
    parser.add_argument('input_dir', help="Path to the input directory containing Markdown files.")
    parser.add_argument('output_dir', help="Path to the output directory for processed Markdown files.")

    args = parser.parse_args()

    process_directory(args.input_dir, args.output_dir)

if __name__ == "__main__":
    main()

