import re
import os
import argparse

class MultiColumnPreprocessor:
    def process_lines(self, lines):
        new_lines = []
        in_multi_column = False

        for line in lines:
            if re.match(r'^--- start-multi-column$', line.strip()):
                new_lines.append('<div class="columns"><div class="column">')
                in_multi_column = True
                continue
            elif re.match(r'^--- end-column ---$', line.strip()):
                new_lines.append('</div><div class="column">')
                continue
            elif re.match(r'^--- end-multi-column$', line.strip()):
                new_lines.append('</div></div>')
                in_multi_column = False
                continue

            new_lines.append(line)
        
        return new_lines

def convert_markdown(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    preprocessor = MultiColumnPreprocessor()
    processed_lines = preprocessor.process_lines(lines)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.writelines(processed_lines)

def process_directory(input_dir, output_dir):
    # 입력 디렉토리의 모든 파일을 탐색
    for root, dirs, files in os.walk(input_dir):
        for file in files:
            if file.endswith('.md'):
                input_file_path = os.path.join(root, file)
                output_file_path = os.path.join(output_dir, os.path.relpath(input_file_path, input_dir))
                
                # 출력 디렉토리 구조를 생성
                os.makedirs(os.path.dirname(output_file_path), exist_ok=True)
                
                # 마크다운 파일 변환
                convert_markdown(input_file_path, output_file_path)

def main():
    parser = argparse.ArgumentParser(description="Convert all Markdown files in a directory to add multi-column support using inline HTML.")
    parser.add_argument('input_dir', help="Path to the input directory containing Markdown files.")
    parser.add_argument('output_dir', help="Path to the output directory for processed Markdown files.")

    args = parser.parse_args()

    process_directory(args.input_dir, args.output_dir)

if __name__ == "__main__":
    main()

