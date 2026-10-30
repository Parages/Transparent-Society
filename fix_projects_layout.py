from pathlib import Path
import re
root = Path(r'c:\Users\20778\Desktop\WEB\ts\projects')
for p in sorted(root.glob('*/index.html')):
    project_no = p.parent.name.lstrip('0') or '0'
    text = p.read_text(encoding='utf-8')
    text = re.sub(r'\s*<section class="section">.*?</section>\s*', '\n', text, flags=re.S)
    text = re.sub(r'\s*<h2>.*?</h2>\s*', '\n', text, flags=re.S)
    text = re.sub(r'\s*<p class="empty">.*?</p>\s*', '\n', text, flags=re.S)
    img_block = f'<div class="gallery">\n      <img src="../../{project_no}.png" alt="项目 {project_no} 海报" />\n    </div>'
    text = re.sub(r'\s*<div class="gallery">.*?</div>\s*', '\n' + img_block + '\n', text, count=1, flags=re.S)
    p.write_text(text, encoding='utf-8')
print('project pages normalized')
