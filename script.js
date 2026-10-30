const posterData = [
  { projectId: 1, src: './1.png' },
  { projectId: 1, src: './1.1.png' },
  { projectId: 1, src: './1.2.gif' },
  { projectId: 2, src: './2.png' },
  { projectId: 2, src: './2.1.jpg' },
  { projectId: 3, src: './3.png' },
  { projectId: 4, src: './4.png' },
  { projectId: 4, src: './4.1.png' },
  { projectId: 5, src: './5.png' },
  { projectId: 6, src: './6.png' },
  { projectId: 7, src: './7.png' },
  { projectId: 8, src: './8.png' },
  { projectId: 9, src: './9.png' },
  { projectId: 10, src: './10.png' },
  { projectId: 11, src: './11.gif' },
  { projectId: 12, src: './12.gif' },
  { projectId: 12, src: './12.1.png' },
  { projectId: 13, src: './13.png' },
  { projectId: 14, src: './14.jpg' },
  { projectId: 15, src: './15.png' },
  { projectId: 16, src: './16.png' },
  { projectId: 17, src: './17.gif' },
  { projectId: 18, src: './18.png' },
  { projectId: 19, src: './19.png' },
  { projectId: 20, src: './20.png' },
  { projectId: 21, src: './21.png' },
  { projectId: 22, src: './22.png' },
  { projectId: 23, src: './23.png' },
  { projectId: 23, src: './23.1.png' },
];

const wall = document.getElementById('posterWall');
const projectOverlay = document.getElementById('projectOverlay');
const projectFrame = document.getElementById('projectFrame');
const closeProjectBtn = document.getElementById('closeProjectBtn');
const sortProjectsBtn = document.getElementById('sortProjectsBtn');
const wallIntro = document.getElementById('wallIntro');
const wallIntroEyebrow = document.getElementById('wallIntroEyebrow');
const wallIntroTitle = document.getElementById('wallIntroTitle');
const wallIntroText = document.getElementById('wallIntroText');

const projectTitles = {
  1: '透明社会 | K的自救 | 恐怖的房子分享会 + 米粉汤 Transparent Society | K\'s Self-Rescue | A Terrifying House Sharing Session + Rice Noodle Soup',
  2: 'Transparent Society | Web a Zine | Surfing, Creating, and Reading Together',
  3: '透明社会 | 去中心化服务器工作坊·上 | 下载 apt install！ Transparent Society | Decentralized Server Workshop Part 1 | Download apt install!',
  4: '透明社会 | 家是一个服务器 | 分享会与联线 | 在地茶配 Transparent Society | Home as a Server | Sharing Session & Online Connection | Local Tea Party',
  5: '透明社会 | 爱如飞鸟 | 与厄瓜多尔乐队pánico的现场连线 Transparent Society | Love Like a Bird | Live Connection with Ecuadorian Band Pánico',
  6: '透明社會 | 畢業變成失業 | 縫補易物救濟會 Transparent Society | Graduation Turns into Unemployment | Mentorship and Barter Relief Association',
  7: 'Transparent Society | China Mobile | Web a Zine Vol.2',
  8: '透明社会 | 师大公园募金音乐会 Transparent Society | Shida Park Fundraising Concert',
  9: '透明社会 | 二人转土生葡语转网路基建 Transparent Society | From Macanese Portuguese to Internet Infrastructure',
  10: '透明社会 | 如何把你的城市变成一个村庄 | 太阳能朋克制图师 Transparent Society | How to Turn Your City into a Village | Solarpunk Cartographer',
  11: '透明社会 | K的自救 | 无法修复 Transparent Society | K\'s Self-Rescue | Irreparable',
  12: '透明社会 | Z点访谈 | 世代新闻发布会 Transparent Society | Z-Point Interview | Generation Press Conference',
  13: '透明社会 | 低温的幽灵 | Web a Zine第三期 Transparent Society | The Ghost of Low Temperatures | Web a Zine Vol.3',
  14: '透明社会 | 早餐与电路改造工作坊 Transparent Society | Breakfast And Circuit Bending Workshop',
  15: '透明社会 | 复活仪式 Transparent Society | Resurrection Ritual',
  16: '透明社会 | 痛痛三轮车 | 告诉我一个有糖尿病的动漫角色 Transparent Society | Painful Tricycle | Tell me about an anime character with diabetes',
  17: '透明社会 | 天冷了我生命中的幽灵又出来了 | 鬼魂带读 Transparent Society | The Ghosts in My Life Have Resurfaced in the Cold Weather | Ghost Reading',
  18: '透明社会 | 世界是个大养老院 | 痛车音乐会 Transparent Society | The World is a Big Retirement Home | Itasha Concert',
  19: '透明社会 | 没有船的海盗 | 有关影子图书馆、著佐权和种子 Transparent Society | Pirates Without Ships | On Shadow Libraries, Copyright, and Seeds',
  20: '透明社会 | 你有一个什么样的杯子 Show me ur cup (not cop)',
  21: '透明社会 | 苏北电器开业 | 永远的计算机 Subertech-Computer forever |',
  22: '透明社会 | 早餐电焊第二集 | Breakfast And Circuit Bending Workshop Vol. 2',
  23: '再见透明社会 | lan！创造我们的离线世界 Goodbye Transparent Society | lan! Creating Our Offline World'
};

function randomBetween(min, max) {
  return Math.random() * (max - min) + min;
}

function getProjectCover(projectId) {
  const item = posterData.find((entry) => entry.projectId === projectId);
  return item ? item.src : './bk.png';
}

function applyPosterLayout(mode = 'mixed') {
  const posters = Array.from(document.querySelectorAll('.poster'));

  posters.forEach((poster, index) => {
    if (mode === 'ordered') {
      poster.style.transform = 'none';
      poster.style.margin = '0';
      poster.style.setProperty('--rotation', '0deg');
      return;
    }

    const offset = index % 2 === 0 ? 1 : -1;
    const driftX = randomBetween(-12, 12);
    const driftY = offset * 6;
    poster.style.transform = `rotate(${randomBetween(-10, 10)}deg) translate(${driftX}px, ${driftY}px)`;
    poster.style.margin = '0 0 2px';
  });
}

function renderWall(mode = 'mixed') {
  wall.innerHTML = '';
  wall.classList.toggle('ordered', mode === 'ordered');

  if (mode === 'ordered') {
    const projectIds = [...new Set(posterData.map((item) => item.projectId))].sort((a, b) => a - b);

    projectIds.forEach((projectId) => {
      const card = document.createElement('article');
      card.className = 'poster';
      card.style.cursor = 'pointer';
      const projectTitle = projectTitles[projectId] || `项目 ${projectId}`;
      card.title = projectTitle;

      const img = document.createElement('img');
      img.src = getProjectCover(projectId);
      img.alt = `${projectTitle} 图片`;
      img.loading = 'lazy';

      const meta = document.createElement('div');
      meta.className = 'project-order-meta';

      const title = document.createElement('h3');
      title.textContent = projectTitle;

      const desc = document.createElement('p');
      desc.textContent = '点击查看项目详情';

      meta.appendChild(title);
      meta.appendChild(desc);

      card.addEventListener('click', () => {
        const folderName = String(projectId).padStart(2, '0');
        projectFrame.src = `./projects/${folderName}/index.html`;
        projectOverlay.classList.add('active');
        projectOverlay.setAttribute('aria-hidden', 'false');
        document.body.classList.add('modal-open');
      });

      card.appendChild(img);
      card.appendChild(meta);
      wall.appendChild(card);
    });

    applyPosterLayout(mode);
    return;
  }

  const items = [...posterData].sort(() => Math.random() - 0.5);

  items.forEach((item) => {
    const card = document.createElement('article');
    card.className = 'poster';
    card.style.cursor = 'pointer';
    card.title = `打开项目 ${item.projectId}`;

    const rotation = randomBetween(-9, 9);
    card.style.setProperty('--rotation', `${rotation}deg`);

    const img = document.createElement('img');
    img.src = item.src;
    img.alt = `项目 ${item.projectId} 图片`;
    img.loading = 'lazy';

    card.addEventListener('click', () => {
      const folderName = String(item.projectId).padStart(2, '0');
      projectFrame.src = `./projects/${folderName}/index.html`;
      projectOverlay.classList.add('active');
      projectOverlay.setAttribute('aria-hidden', 'false');
      document.body.classList.add('modal-open');
    });

    card.appendChild(img);
    wall.appendChild(card);
  });

  applyPosterLayout(mode);
}

function closeProject() {
  projectOverlay.classList.remove('active');
  projectOverlay.setAttribute('aria-hidden', 'true');
  document.body.classList.remove('modal-open');
  projectFrame.src = 'about:blank';
}

closeProjectBtn.addEventListener('click', closeProject);
projectOverlay.addEventListener('click', (event) => {
  if (event.target === projectOverlay) {
    closeProject();
  }
});

window.addEventListener('keydown', (event) => {
  if (event.key === 'Escape' && projectOverlay.classList.contains('active')) {
    closeProject();
  }
});

projectFrame.addEventListener('load', () => {
  try {
    const doc = projectFrame.contentDocument;
    if (!doc) return;

    const backLink = doc.querySelector('.back');
    if (backLink) {
      backLink.setAttribute('href', '#');
      backLink.addEventListener('click', (event) => {
        event.preventDefault();
        closeProject();
      });
    }
  } catch (error) {
    console.warn('Unable to wire project detail close behavior:', error);
  }
});

sortProjectsBtn.addEventListener('click', () => {
  const isOrdered = wall.classList.contains('ordered');
  renderWall(isOrdered ? 'mixed' : 'ordered');
});

renderWall('mixed');
