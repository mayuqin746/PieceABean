<template>
  <div class="page-container">
    <!-- 三级筛选器 -->
    <div class="gallery-header">
      <!-- 一级：主题 -->
      <div class="filter-row">
        <div class="f-label">主题</div>
        <div class="f-tags">
          <div
            v-for="t in themes"
            :key="t"
            class="f-tag"
            :class="{ active: activeTheme === t }"
            @click="activeTheme = t"
          >{{ t }}</div>
        </div>
      </div>

      <!-- 二级：色系 -->
      <div class="filter-row">
        <div class="f-label">色系</div>
        <div class="f-tags">
          <div
            v-for="c in colors"
            :key="c.name"
            class="color-tag"
            :class="{ active: activeColor === c.name }"
            :style="{ background: c.value }"
            :title="c.name"
            @click="activeColor = c.name"
          ></div>
        </div>
      </div>

      <!-- 三级：系列 -->
      <div class="filter-row">
        <div class="f-label">系列</div>
        <div class="f-tags">
          <div
            v-for="s in series"
            :key="s"
            class="f-tag"
            :class="{ active: activeSeries === s }"
            @click="activeSeries = s"
          >{{ s }}</div>
        </div>
      </div>

      <!-- 交叉过滤状态栏 -->
      <div class="active-filters">
        <span class="af-label">当前检索：</span>
        <span
          v-if="activeTheme !== '全部'"
          class="af-tag"
        >{{ activeTheme }} ✖</span>
        <span
          v-if="activeSeries !== '全部'"
          class="af-tag"
        >{{ activeSeries }} ✖</span>
        <span class="clear-btn" @click="clearFilters">清空筛选</span>
      </div>
    </div>

    <!-- 结果 -->
    <div class="g-result-title">共检索到 {{ filteredList.length }} 张精致图纸</div>

    <div class="gallery-grid">
      <div v-for="item in filteredList" :key="item.title" class="g-card">
        <div class="g-img">{{ item.emoji }}</div>
        <div class="g-title">{{ item.title }}</div>
        <div class="g-meta">
          <span>{{ item.size }}</span>
          <span>{{ item.tags }}</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue'

const themes = ['全部', '📺 动漫/IP', '🐾 萌宠动物', '🍔 美食饮品', '🌿 生活日常', '🌟 明星应援']
const colors = [
  { name: '全部色系', value: 'conic-gradient(red, yellow, lime, aqua, blue, magenta, red)' },
  { name: '粉色系', value: '#FFB6C1' },
  { name: '橙黄色系', value: '#FFD166' },
  { name: '绿色系', value: '#98FB98' },
  { name: '蓝色系', value: '#87CEFA' },
  { name: '紫色系', value: '#E6E6FA' },
  { name: '黑白灰', value: '#A0AEC0' },
]
const series = ['全部', '三丽鸥', '线条小狗', '星之卡比', '马里奥', '吉伊卡哇(Chiikawa)']

const activeTheme = ref('📺 动漫/IP')
const activeColor = ref('全部色系')
const activeSeries = ref('三丽鸥')

const allItems = [
  { emoji: '🎀', title: 'Hello Kitty', size: '29x29小板', tags: '#三丽鸥 #粉色系', theme: '📺 动漫/IP', series: '三丽鸥' },
  { emoji: '🐶', title: '线条小狗', size: '29x29小板', tags: '#线条小狗 #白灰系', theme: '🐾 萌宠动物', series: '线条小狗' },
  { emoji: '💖', title: '星之卡比吃大福', size: '58x58大板', tags: '#星之卡比 #粉色系', theme: '📺 动漫/IP', series: '星之卡比' },
  { emoji: '☁️', title: '大耳狗玉桂狗', size: '58x58大板', tags: '#三丽鸥 #蓝色系', theme: '📺 动漫/IP', series: '三丽鸥' },
]

const filteredList = computed(() => {
  return allItems.filter((item) => {
    if (activeTheme.value !== '全部' && item.theme !== activeTheme.value) return false
    if (activeSeries.value !== '全部' && item.series !== activeSeries.value) return false
    return true
  })
})

function clearFilters() {
  activeTheme.value = '全部'
  activeColor.value = '全部色系'
  activeSeries.value = '全部'
}
</script>

<style scoped>
.page-container { max-width: 1100px; margin: 0 auto; padding-left: 20px; padding-right: 20px; }

.gallery-header {
  background: white; padding: 25px 30px; border-radius: var(--radius-lg);
  box-shadow: var(--shadow-soft); margin-bottom: 30px; border: 1px solid var(--border-color);
}

.filter-row { display: flex; align-items: flex-start; margin-bottom: 15px; padding-bottom: 15px; border-bottom: 1px dashed var(--border-color); }
.filter-row:last-of-type { margin-bottom: 0; padding-bottom: 0; border-bottom: none; }

.f-label { width: 70px; font-weight: 900; color: var(--text-light); margin-top: 6px; flex-shrink: 0; }
.f-tags { display: flex; flex-wrap: wrap; gap: 10px; flex: 1; align-items: center; }

.f-tag {
  padding: 6px 16px; border-radius: 20px; font-size: 13px; font-weight: bold;
  cursor: pointer; background: var(--bg-color); color: var(--text-main);
  transition: 0.2s; border: 1px solid transparent; user-select: none;
}
.f-tag:hover { background: var(--primary-light); color: var(--primary); }
.f-tag.active { background: var(--primary); color: white; }

.color-tag {
  width: 28px; height: 28px; border-radius: 50%;
  border: 2px solid white; box-shadow: 0 2px 5px rgba(0,0,0,0.1);
  cursor: pointer; padding: 0; display: flex; justify-content: center; align-items: center;
  font-size: 14px; transition: transform 0.2s;
}
.color-tag.active { border: 2px solid var(--text-main); transform: scale(1.15); }

.active-filters {
  display: flex; gap: 10px; align-items: center; margin-top: 15px;
  background: var(--bg-color); padding: 10px 15px; border-radius: 12px; font-size: 13px; font-weight: bold;
}
.af-label { color: var(--text-light); margin-right: 10px; }
.af-tag { background: white; padding: 4px 12px; border-radius: 12px; border: 1px solid var(--border-color); }
.clear-btn { color: var(--primary); cursor: pointer; font-weight: bold; margin-left: auto; user-select: none; }

.g-result-title { margin: 20px 0; font-weight: 900; font-size: 18px; }

.gallery-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 25px; }
.g-card { background: white; border-radius: var(--radius-md); padding: 15px; cursor: pointer; box-shadow: var(--shadow-soft); transition: 0.3s; }
.g-card:hover { transform: translateY(-5px); }
.g-img { height: 160px; background: var(--bg-color); border-radius: 12px; display: flex; justify-content: center; align-items: center; font-size: 60px; margin-bottom: 12px; }
.g-title { font-weight: 900; font-size: 15px; margin-bottom: 5px; }
.g-meta { font-size: 12px; color: var(--text-light); display: flex; justify-content: space-between; }
</style>
