import os
import markdown
from pathlib import Path

template_path = Path('templates/base.html')
output_dir = Path('dist')
posts_dir = Path('posts')

output_dir.mkdir(exist_ok=True)

# Load template
with template_path.open('r') as f:
    base_tpl = f.read()

index_entries = []

for md_file in posts_dir.glob('*.md'):
    with md_file.open('r') as f:
        text = f.read()
    html_content = markdown.markdown(text)
    # Title is first heading
    title = text.splitlines()[0].lstrip('# ').strip()
    content = base_tpl.replace('{{ title }}', title).replace('{{ content }}', html_content)
    outfile = output_dir / (md_file.stem + '.html')
    outfile.write_text(content)
    index_entries.append(f'<li><a href="{outfile.name}">{title}</a></li>')

index_content = '<h1>My Blog</h1>\n<ul>' + '\n'.join(index_entries) + '</ul>'
index_html = base_tpl.replace('{{ title }}', 'Home').replace('{{ content }}', index_content)
(output_dir / 'index.html').write_text(index_html)
print('Site built in', output_dir)
