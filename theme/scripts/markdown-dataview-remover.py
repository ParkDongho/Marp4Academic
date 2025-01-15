import re
import os
import argparse

class DataviewPreprocessor:
    def process_lines(self, lines):
        new_lines = []
        in_multi_column = False
        in_dataview_block = False

        for line in lines:
            # Check for the start of a multi-column block
            # Check for the start of a dataview code block
            if re.match(r'^```dataview$', line.strip()):
                in_dataview_block = True
                continue
            # Check for the end of a dataview code block
            elif re.match(r'^```$', line.strip()) and in_dataview_block:
                in_dataview_block = False
                continue

            # If inside a dataview block, skip the line
            if in_dataview_block:
                continue

            new_lines.append(line)
        
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
    parser = argparse.ArgumentParser(description="Convert all Markdown files in a directory to add multi-column support and remove dataview code blocks.")
    parser.add_argument('input_dir', help="Path to the input directory containing Markdown files.")
    parser.add_argument('output_dir', help="Path to the output directory for processed Markdown files.")

    args = parser.parse_args()

    process_directory(args.input_dir, args.output_dir)

if __name__ == "__main__":
    main()

