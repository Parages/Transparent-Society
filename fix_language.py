from pathlib import Path
import re

root = Path(r'c:\Users\20778\Desktop\WEB\ts')
project_dir = root / 'projects'

replacement_script = """
    <script>
      const titleEl = document.querySelector('h1');
      const introEl = document.querySelector('.intro');
      const sectionHeads = document.querySelectorAll('.section h2');
      const emptyNotes = document.querySelectorAll('.empty');
      const projectNo = Number((window.location.pathname.match(/projects\\/(\\d+)/) || [])[1] || 0);

      const sourceTitle = titleEl ? titleEl.textContent.trim() : '';
      const sourceIntro = introEl ? introEl.textContent.trim() : '';
      const zhTitle = sourceTitle;
      const enTitle = sourceTitle;
      const zhIntro = sourceIntro;
      const enIntro = sourceIntro;

      function applyLanguage(lang) {
        const isEn = lang === 'en';
        document.documentElement.lang = isEn ? 'en' : 'zh-CN';

        if (titleEl) {
          titleEl.textContent = isEn ? enTitle : zhTitle;
        }
        if (introEl) {
          introEl.textContent = isEn ? enIntro : zhIntro;
        }

        sectionHeads.forEach((node, index) => {
          const values = [
            ['项目海报', 'Project Posters'],
            ['相关照片', 'Related Photos']
          ];
          const pair = values[index] || ['', ''];
          node.textContent = isEn ? pair[1] : pair[0];
        });

        emptyNotes.forEach((node) => {
          const text = node.textContent.trim();
          if (text.includes('项目海报') || text.includes('Project Posters')) {
            node.textContent = isEn ? 'Drop the project poster into the assets/posters folder.' : '把项目海报图放进 assets/posters 文件夹即可。';
          }
          if (text.includes('相关照片') || text.includes('Related Photos')) {
            node.textContent = isEn ? 'Drop related photos into the assets/photos folder.' : '把相关照片放进 assets/photos 文件夹即可。';
          }
        });
      }

      window.addEventListener('message', (event) => {
        if (event.data && event.data.type === 'ts-lang') {
          applyLanguage(event.data.lang);
        }
      });

      applyLanguage(localStorage.getItem('ts-lang') || 'zh');
    </script>
"""

for p in sorted(project_dir.glob('*/index.html')):
    text = p.read_text(encoding='utf-8')

    text = re.sub(
        r'\n\s*<style>\s*\.language-switch\s*\{.*?\}\s*\.lang-btn\s*\{.*?\}\s*\.lang-btn\.active\s*\{.*?\}\s*</style>\s*',
        '\n',
        text,
        flags=re.S,
    )
    text = re.sub(r'\n\s*<div class="language-switch"[^>]*>.*?</div>\s*', '\n', text, flags=re.S)

    # Replace every script block with the shared listener script.
    text = re.sub(r'\n\s*<script>.*?</script>\s*', '\n', text, flags=re.S)
    text = text.replace('</body>', replacement_script + '\n</body>')
    p.write_text(text, encoding='utf-8')

print(f'Patched {len(list(project_dir.glob("*/index.html")))} project pages.')
