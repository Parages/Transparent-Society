from pathlib import Path

root = Path(r'c:\Users\20778\Desktop\WEB\ts\projects')

script = '''
    <script>
      (() => {
        const titleEl = document.querySelector('h1');
        const introEl = document.querySelector('.intro');
        const sectionHeads = document.querySelectorAll('.section h2');
        const emptyNotes = document.querySelectorAll('.empty');
        const titleText = titleEl ? titleEl.textContent.trim() : '';

        const titleMap = {
          "Transparent Society | K's Self-Rescue | A Terrifying House Sharing Session + Rice Noodle Soup": "透明社会 | K 的自救 | 一场惊悚的合租时刻 + 米线汤",
          "Transparent Society | Web a Zine | Surfing, Creating, and Reading Together": "透明社会 | 网页杂志 | 一起冲浪、创作与阅读",
          "Transparent Society | Decentralized Server Workshop Part 1 | Download apt install!": "透明社会 | 去中心化服务器工作坊 Part 1 | 下载 apt install！",
          "Transparent Society | Home as a Server | Sharing Session & Online Connection | Local Tea Party": "透明社会 | 家庭服务器 | 分享会与在线连接 | 线下茶会",
          "Transparent Society | Love Like a Bird | Live Connection with Ecuadorian Band Pánico": "透明社会 | 像鸟一样爱 | 与厄瓜多尔乐队 Pánico 的现场联线",
          "Transparent Society | Graduation Turns into Unemployment | Mentorship and Barter Relief Association": "透明社会 | 毕业变失业 | mentorship 与物物交换互助社",
          "Transparent Society | China Mobile | Web a Zine Vol.2": "透明社会 | 中国移动 | 网页杂志 Vol.2",
          "Transparent Society | Shida Park Fundraising Concert": "透明社会 | 师大公园筹款音乐会",
          "Transparent Society | From Macanese Portuguese to Internet Infrastructure": "透明社会 | 从澳门葡语到互联网基础设施",
          "Transparent Society | How to Turn Your City into a Village | Solarpunk Cartographer": "透明社会 | 如何把你的城市变成村庄 | 太阳朋克制图师",
          "Transparent Society | K's Self-Rescue | Irreparable": "透明社会 | K 的自救 | 无法修复",
          "Transparent Society | Z-Point Interview | Generation Press Conference": "透明社会 | Z 点访谈 | 青年新闻发布会",
          "Transparent Society | The Ghost of Low Temperatures | Web a Zine Vol.3": "透明社会 | 低温幽灵 | 网页杂志 Vol.3",
          "Transparent Society | Breakfast And Circuit Bending Workshop": "透明社会 | 早餐与电路改造工作坊",
          "Transparent Society | Resurrection Ritual": "透明社会 | 复活仪式",
          "Transparent Society | Painful Tricycle | Tell me about an anime character with diabetes": "透明社会 | 痛苦三轮车 | 告诉我一个患糖尿病的动漫角色",
          "Transparent Society | The Ghosts in My Life Have Resurfaced in the Cold Weather | Ghost Reading": "透明社会 | 我生命中的幽灵在寒冷中重现 | 读幽灵",
          "Transparent Society | The World is a Big Retirement Home | Itasha Concert": "透明社会 | 世界是一座巨大的养老院 | 痛车音乐会",
          "Transparent Society | Pirates Without Ships | On Shadow Libraries, Copyright, and Seeds": "透明社会 | 没有船的海盗 | 关于影子图书馆、版权与种子的讨论",
          "Goodbye Transparent Society | lan! Creating Our Offline World": "再见透明社会 | LAN！创造我们的离线世界",
          "Transparent Society is still operating": "透明社会仍在持续运作",
          "项目 20": "项目 20",
          "项目 22": "项目 22",
          "项目 23": "项目 23",
          "Project 20": "项目 20",
          "Project 22": "项目 22",
          "Project 23": "项目 23"
        };

        const getChineseTitle = (value) => titleMap[value] || value;

        function applyLanguage(lang) {
          const isEn = lang === 'en';
          document.documentElement.lang = isEn ? 'en' : 'zh-CN';

          if (titleEl) {
            const current = titleEl.textContent.trim();
            const nextTitle = isEn ? (current.includes('透明') || /[\\u4E00-\\u9FFF]/.test(current) ? getChineseTitle(current) : current) : (titleMap[current] || current);
            titleEl.textContent = isEn ? (current.includes('透明') || /[\\u4E00-\\u9FFF]/.test(current) ? current : nextTitle) : (titleMap[current] || current);
            if (!isEn && titleMap[current]) {
              titleEl.textContent = titleMap[current];
            }
            if (isEn && !/[\\u4E00-\\u9FFF]/.test(current) && titleMap[current]) {
              titleEl.textContent = current;
            }
            if (isEn && /[\\u4E00-\\u9FFF]/.test(current) && titleMap[current]) {
              titleEl.textContent = current;
            }
          }

          if (introEl) {
            const current = introEl.textContent.trim();
            if (isEn && /[\\u4E00-\\u9FFF]/.test(current)) {
              introEl.textContent = current;
            }
            if (!isEn && /[A-Za-z]/.test(current) && current.includes('Transparent Society')) {
              introEl.textContent = current;
            }
          }

          sectionHeads.forEach((node, index) => {
            const pair = [
              ['项目海报', 'Project Posters'],
              ['相关照片', 'Related Photos']
            ][index] || ['', ''];
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
      })();
    </script>
'''

for path in sorted(root.glob('*/index.html')):
    text = path.read_text(encoding='utf-8')
    if 'ts-lang' in text or 'window.addEventListener(\'message\'' in text or 'window.addEventListener("message"' in text:
        continue
    if '</body>' in text:
        text = text.replace('</body>', script + '\n  </body>')
        path.write_text(text, encoding='utf-8')

print(f'patched {len(list(root.glob("*/index.html")))} pages')
