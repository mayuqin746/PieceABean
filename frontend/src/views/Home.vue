<template>
  <div class="page-container">
    <div class="dashboard">
      <!-- 焦点海报 / 轮播 Banner -->
      <div class="bento-card card-hero">
        <div class="carousel">
          <div class="carousel-track" :style="{ transform: `translateX(-${currentSlide * 100}%)` }">
            <div
              v-for="(banner, i) in banners"
              :key="i"
              class="carousel-slide"
            >
              <img :src="banner.src" :alt="banner.alt" />
            </div>
          </div>
          
          <!-- 常规清透遮罩层 -->
          <div class="carousel-overlay-shadow"></div>

          <!-- 优雅的文字信息层 -->
          <div class="hero-overlay">
            <h1 class="hero-title">
              把照片变成<br /><span class="text-nowrap">治愈的像素拼豆</span>
            </h1>
            <p class="hero-desc">
              超温柔的限定图纸已更新，<br />来挑选你今天的减压手工吧！
            </p>
            <button class="hero-btn" @click="$router.push('/workspace')">
              <span>开始创作</span>
              <!-- <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" class="btn-arrow"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg> -->
            </button>
          </div>

          <!-- 精致的毛玻璃控制按钮：鼠标悬停在 Banner 上时平滑显现 -->
          <button class="carousel-btn prev" @click="prevSlide" aria-label="上一张">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="15 18 9 12 15 6"></polyline></svg>
          </button>
          <button class="carousel-btn next" @click="nextSlide" aria-label="下一张">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="9 18 15 12 9 6"></polyline></svg>
          </button>

          <!-- 现代胶囊指示器 -->
          <div class="carousel-dots">
            <span
              v-for="(_, i) in banners"
              :key="i"
              class="dot"
              :class="{ active: currentSlide === i }"
              @click="currentSlide = i"
            ></span>
          </div>
        </div>
      </div>

      <!-- 工具组件 -->
      <div class="bento-card card-tool">
        <div class="tool-upload" @click="$router.push('/workspace')">
          <img class="upload-icon" src="/uploadpic.png" alt="上传" />
          <!-- <span class="upload-text">上传照片</span> -->
        </div>
        <div class="tool-actions">
          <div class="tool-title">转换器</div>
          <select class="tool-select">
            <option>58x58 大板</option>
          </select>
          <select class="tool-select">
            <option>色彩: 24色 (推荐)</option>
          </select>
          <button class="btn-magic" @click="$router.push('/workspace')">
            一键生成
          </button>
        </div>
      </div>

      <!-- 盲盒 -->
      <div class="bento-card card-blindbox" @click="onBlindBox">
        <img class="blind-icon" src="/blindbox.png" alt="盲盒" />
        <!-- <strong class="blind-title">图纸盲盒</strong> -->
        <div class="blind-desc">不知道拼啥？抽一个！</div>
      </div>

      <!-- 色系匹配 -->
      <div class="bento-card card-mood">
        <strong class="mood-title">今日专属色</strong>
        <div class="mood-desc">选个颜色，匹配图纸</div>
        <div class="mood-colors">
          <div class="m-color" style="background: #FFB6C1" @click="$router.push('/gallery')"></div>
          <div class="m-color" style="background: #90CDF4" @click="$router.push('/gallery')"></div>
          <div class="m-color" style="background: #9AE6B4" @click="$router.push('/gallery')"></div>
          <div class="m-color" style="background: #FBD38D" @click="$router.push('/gallery')"></div>
        </div>
      </div>
    </div>

    <!-- 推荐列表 -->
    <div class="g-section-title">
      <h2>豆友都在拼</h2>
      <span class="view-all" @click="$router.push('/gallery')">查看全部图库 ></span>
    </div>

    <div class="gallery-grid">
      <div v-for="item in featuredList" :key="item.title" class="g-card">
        <div class="g-img" :style="{ background: item.bg }">
          <div class="g-tag-type">{{ item.tag }}</div>
          {{ item.emoji }}
        </div>
        <div class="g-title">{{ item.title }}</div>
        <div class="g-meta">
          <span>{{ item.size }}</span>
          <span>被收藏 {{ item.stars }}</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, onUnmounted } from 'vue'
import banner1 from '@/assets/images/banner/banner1.png'
import banner2 from '@/assets/images/banner/banner2.png'
import banner3 from '@/assets/images/banner/banner3.png'

const banners = [
  { src: banner1, alt: 'Banner 1' },
  { src: banner2, alt: 'Banner 2' },
  { src: banner3, alt: 'Banner 3' },
]

const currentSlide = ref(0)
let timer: ReturnType<typeof setInterval> | null = null

function nextSlide() {
  currentSlide.value = (currentSlide.value + 1) % banners.length
}

function prevSlide() {
  currentSlide.value = (currentSlide.value - 1 + banners.length) % banners.length
}

function startAutoPlay() {
  timer = setInterval(nextSlide, 4000)
}

function stopAutoPlay() {
  if (timer) {
    clearInterval(timer)
    timer = null
  }
}

onMounted(startAutoPlay)
onUnmounted(stopAutoPlay)

const featuredList = [
  { emoji: '🍓', title: '草莓千层蛋糕', size: '29x29小板', stars: '2.1k', tag: '附成品实拍', bg: '#FFF0F5' },
  { emoji: '🐳', title: '治愈系夏日海豚', size: '58x58大板', stars: '1.8k', tag: '像素图纸', bg: '#E0FFFF' },
  { emoji: '🧀', title: '奶酪陷阱(新手友好)', size: '29x29小板', stars: '3.5k', tag: '附成品实拍', bg: '#FFFACD' },
  { emoji: '🔮', title: '魔法少女水晶球', size: '58x58大板', stars: '996', tag: '像素图纸', bg: '#E6E6FA' },
]

function onBlindBox() {
  alert('恭喜抽中隐藏款：【治愈海豚】！')
}
</script>

<style scoped>
.page-container { max-width: 1100px; margin: 0 auto; padding-left: 20px; padding-right: 20px; }

.dashboard { display: grid; grid-template-columns: repeat(4, 1fr); gap: 25px; }

.bento-card {
  background: white;
  border-radius: var(--radius-lg);
  padding: 25px;
  box-shadow: var(--shadow-soft);
  transition: 0.3s;
  position: relative;
  overflow: hidden;
  display: flex;
  flex-direction: column;
}
.bento-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 0 0 2px var(--primary), 0 8px 30px var(--shadow-soft);
}

/* 焦点海报 / 轮播 */
.card-hero {
  grid-column: span 2; grid-row: span 2;
  padding: 0; border: 2px solid white;
}

.carousel {
  width: 100%; height: 100%;
  position: relative; overflow: hidden;
  border-radius: var(--radius-lg);
}

/* 常规薄层遮罩 */
.carousel-overlay-shadow {
  position: absolute;
  inset: 0;
  background: rgba(0, 0, 0, 0.18); /* 清澈且不压抑的纯色薄遮罩 */
  pointer-events: none;
  z-index: 1;
}

.carousel-track {
  display: flex; width: 100%; height: 100%;
  transition: transform 0.5s cubic-bezier(0.4, 0, 0.2, 1);
}

.carousel-slide {
  min-width: 100%; height: 100%;
}

.carousel-slide img {
  width: 100%; height: 100%;
  object-fit: cover; display: block;
}

/* 胶囊指示点 */
.carousel-dots {
  position: absolute; bottom: 20px; left: 50%;
  transform: translateX(-50%);
  display: flex; gap: 8px; z-index: 3;
  background: rgba(0, 0, 0, 0.25);
  padding: 6px 10px;
  border-radius: 20px;
  backdrop-filter: blur(4px);
}

.dot {
  width: 5px; height: 5px; border-radius: 50%;
  background: rgba(255, 255, 255, 0.4);
  cursor: pointer; transition: all 0.3s ease;
}

.dot.active {
  background: white; 
  width: 10px;
  border-radius: 4px;
}

/* 轮播毛玻璃切换按钮 */
.carousel-btn {
  position: absolute; top: 50%; transform: translateY(-50%);
  width: 32px; height: 32px; border-radius: 50%;
  border: 1px solid rgba(255, 255, 255, 0.25); 
  background: rgba(255, 255, 255, 0.15);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  color: white; 
  cursor: pointer; display: flex; justify-content: center; align-items: center;
  z-index: 4; line-height: 1;
  opacity: 0;
  visibility: hidden;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

/* 悬停展示控制手柄 */
.carousel:hover .carousel-btn {
  opacity: 1;
  visibility: visible;
}

.carousel-btn:hover { 
  background: white; 
  color: #1a202c;
  border-color: white;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.15);
}
.carousel-btn.prev { left: 16px; }
.carousel-btn.next { right: 16px; }

/* 文本信息图层 */
.hero-overlay {
  position: absolute; top: 0; left: 0;
  width: 60%; height: 100%;
  padding: 40px 40px 40px 60px; /* 优化左间距，避开切换按钮 */
  display: flex; flex-direction: column;
  justify-content: center;
  z-index: 2;
  pointer-events: none;
  box-sizing: border-box;
}
.hero-overlay > * { pointer-events: auto; }

.hero-title {
  font-size: 34px; font-weight: 800; line-height: 1.35;
  color: white; text-shadow: 0 2px 10px rgba(0,0,0,0.3);
  margin: 0;
}

/* 强制该重点词组不换行，防止落单折行 */
.text-nowrap {
  white-space: nowrap;
}

.hero-desc {
  color: rgba(255,255,255,0.9); font-size: 15px; line-height: 1.6;
  text-shadow: 0 1px 4px rgba(0,0,0,0.25);
  margin: 16px 0 24px 0;
}

/* 开始创作按钮 */
.hero-btn {
  /* 默认状态：毛玻璃半透明灰样式，与未悬停的左右箭头相同 */
  background: rgba(255, 255, 255, 0.15); 
  color: #ffffff;
  border: 1px solid rgba(255, 255, 255, 0.25); 
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  
  padding: 10px 20px; border-radius: 30px;
  font-weight: 600; cursor: pointer;
  font-size: 15px; width: fit-content;
  display: inline-flex; align-items: center; gap: 8px;
  box-shadow: 0 4px 15px rgba(0,0,0,0.1);
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.hero-btn:hover { 
  /* 悬浮状态：纯白色背景与深色字体，与悬停时的左右箭头相同 */
  background: white; 
  color: #1a202c;
  border-color: white;
  transform: translateY(-2px); 
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.2);
}

.hero-btn .btn-arrow {
  transition: transform 0.3s ease;
}
.hero-btn:hover .btn-arrow {
  transform: translateX(4px);
}

/* 工具组件 */
.card-tool { grid-column: span 2; display: flex; flex-direction: row; gap: 20px; align-items: center; }
.tool-upload { flex: 1; height: 100%; min-height: 140px; border: 2px dashed var(--border-color); border-radius: var(--radius-md); display: flex; flex-direction: column; justify-content: center; align-items: center; cursor: pointer; background: #F8FAFC; transition: 0.2s; }
.tool-upload:hover { border-color: var(--primary); background: var(--blindbox-bg); }
.upload-icon { width: 100px; height: 100px; margin-bottom: 5px; object-fit: contain; }
.upload-text { font-size: 13px; font-weight: bold; color: var(--text-main); }
.tool-actions { flex: 1; display: flex; flex-direction: column; gap: 10px; }
.tool-title { font-weight: 900; font-size: 16px; }
.tool-select { width: 100%; padding: 10px 15px; border-radius: 12px; border: 1px solid var(--border-color); font-weight: bold; outline: none; background: #F8FAFC; color: var(--text-main); }
/* .btn-magic { background: linear-gradient(135deg, var(--blindbox-bg), var(--primary-light)); color: white; border: none; padding: 12px; border-radius: 12px; font-weight: bold; font-size: 15px; cursor: pointer; box-shadow: 0 4px 10px rgba(0,0,0,0.05); } */
/* .btn-magic { background: var(--primary); color: white; border: none; padding: 12px; border-radius: 12px; font-weight: bold; font-size: 15px; cursor: pointer; box-shadow: 0 4px 10px rgba(0,0,0,0.05); } */
.btn-magic { background: var(--primary); color: white; border: none; padding: 12px; border-radius: 12px; font-weight: bold; font-size: 15px; cursor: pointer; box-shadow: 0 4px 10px rgba(0,0,0,0.05); }

/* 盲盒 */
/* .card-blindbox { grid-column: span 1; background: var(--blindbox-bg); align-items: center; justify-content: center; text-align: center; cursor: pointer; } */
/* .card-blindbox { grid-column: span 1; background: white; align-items: center; justify-content: center; text-align: center; cursor: pointer; } */
.card-blindbox { grid-column: span 1; background: var(--blindbox-bg); align-items: center; justify-content: center; text-align: center; cursor: pointer; }

.blind-icon { width: 140px; height: 140px; margin:10px auto; display: block;}
.blind-title { font-size: 18px; color: var(--text-main); }
.blind-desc { font-size: 12px; margin-top: 5px; color: var(--theme-text-dark); opacity: 0.8; }

/* 色系 */
/* .card-mood { grid-column: span 1; background: var(--blindbox-bg); align-items: center; justify-content: center; text-align: center; } */
/* .card-mood { grid-column: span 1; background: white; align-items: center; justify-content: center; text-align: center; } */
.card-mood { grid-column: span 1; background: var(--blindbox-bg); align-items: center; justify-content: center; text-align: center; }

.mood-title { font-size: 16px; }
.mood-desc { font-size: 12px; color: #718096; margin-top: 4px; }
.mood-colors { display: flex; gap: 10px; margin-top: 15px; }
.m-color { width: 24px; height: 24px; border-radius: 50%; cursor: pointer; border: 2px solid white; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }

/* 推荐区 */
.g-section-title { display: flex; justify-content: space-between; align-items: center; margin: 75px 0 40px; }
.g-section-title h2 { font-weight: 900; }
.view-all { font-size: 14px; color: var(--text-light); cursor: pointer; font-weight: bold; }

.gallery-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 25px; }
.g-card { background: white; border-radius: var(--radius-md); padding: 15px; cursor: pointer; box-shadow: var(--shadow-soft); transition: 0.3s; }
.g-card:hover { transform: translateY(-5px); }
.g-img { height: 160px; background: var(--bg-color); border-radius: 12px; display: flex; justify-content: center; align-items: center; font-size: 60px; margin-bottom: 12px; position: relative; }
.g-tag-type { position: absolute; top: 10px; right: 10px; background: rgba(255,255,255,0.9); padding: 4px 8px; border-radius: 10px; font-size: 11px; font-weight: bold; }
.g-title { font-weight: 900; font-size: 15px; margin-bottom: 5px; }
.g-meta { font-size: 12px; color: var(--text-light); display: flex; justify-content: space-between; }
</style>