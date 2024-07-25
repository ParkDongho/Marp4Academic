import markdown
from markdown.preprocessors import Preprocessor
from markdown.extensions import Extension
import re

class MultiColumnPreprocessor(Preprocessor):
    def run(self, lines):
        new_lines = []
        for line in lines:
            if re.match(r'^--- start-multi-column$', line.strip()):
                new_lines.append('<div class="columns"><div class="column">')
                continue
            elif re.match(r'^--- end-column$', line.strip()):
                new_lines.append('</div><div class="column">')
                continue
            elif re.match(r'^--- end-multi-column$', line.strip()):
                new_lines.append('</div></div>')
                continue

            new_lines.append(line)
        
        return new_lines

class MultiColumnExtension(Extension):
    def extendMarkdown(self, md):
        md.preprocessors.register(MultiColumnPreprocessor(md), 'multi_column', 25)

def convert_markdown(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        text = f.read()
    
    md = markdown.Markdown(extensions=[MultiColumnExtension()])
    html = md.convert(text)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html)

# 사용 예시
convert_markdown('input.md', 'output.md')

