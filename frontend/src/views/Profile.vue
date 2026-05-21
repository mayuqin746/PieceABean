<template>
  <div class="page-container">
    <div class="profile-header">
      <div class="p-avatar">👧🏻</div>
      <div>
        <h1>Halo_同学</h1>
        <p class="p-bio">入坑拼豆的第 42 天，已经完成了 5 个作品啦！</p>
      </div>
    </div>

    <div class="p-tabs">
      <div
        v-for="tab in tabs"
        :key="tab.key"
        class="p-tab"
        :class="{ active: activeTab === tab.key }"
        @click="activeTab = tab.key"
      >{{ tab.label }}</div>
    </div>

    <div class="gallery-grid">
      <div v-for="item in displayItems" :key="item.title" class="g-card">
        <div class="g-img" :style="{ background: item.bg }">{{ item.emoji }}</div>
        <div class="g-title">{{ item.title }}</div>
        <div class="g-meta"><span>{{ item.size }}</span></div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, computed } from 'vue'

const activeTab = ref('favorites')

const tabs = [
  { key: 'favorites', label: '❤️ 我的收藏 (12)' },
  { key: 'creations', label: '🎨 我的创作 (3)' },
]

const favoritesList = [
  { emoji: '🍓', title: '收藏：草莓奶油蛋糕', size: '29x29', bg: '#FFF0F5' },
  { emoji: '🐳', title: '收藏：治愈蓝鲸', size: '58x58', bg: '#EBF0F5' },
]

const creationsList = [
  { emoji: '🐶', title: '创作：我的可爱修勾', size: '58x58', bg: '#FFFACD' },
]

const displayItems = computed(() => {
  return activeTab.value === 'favorites' ? favoritesList : creationsList
})
</script>

<style scoped>
.page-container { max-width: 900px; margin: 0 auto; padding-left: 20px; padding-right: 20px; }

.profile-header {
  display: flex; align-items: center; gap: 20px; margin-bottom: 30px;
  background: white; padding: 30px; border-radius: var(--radius-lg);
  box-shadow: var(--shadow-soft); border: 1px solid var(--border-color);
}

.p-avatar {
  width: 80px; height: 80px; border-radius: 50%;
  background: var(--primary-light); font-size: 40px;
  display: flex; justify-content: center; align-items: center; user-select: none;
}

.profile-header h1 { font-weight: 900; margin-bottom: 5px; }
.p-bio { color: var(--text-light); font-size: 14px; }

.p-tabs { display: flex; gap: 25px; margin-bottom: 25px; border-bottom: 2px solid var(--border-color); }
.p-tab {
  padding: 10px 5px; font-weight: 900; font-size: 18px; cursor: pointer;
  color: var(--text-light); position: relative; user-select: none;
}
.p-tab.active { color: var(--text-main); }
.p-tab.active::after {
  content: ''; position: absolute; bottom: -2px; left: 0;
  width: 100%; height: 4px; background: var(--primary); border-radius: 2px;
}

.gallery-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 25px; }
.g-card { background: white; border-radius: var(--radius-md); padding: 15px; cursor: pointer; box-shadow: var(--shadow-soft); transition: 0.3s; }
.g-card:hover { transform: translateY(-5px); }
.g-img { height: 160px; border-radius: 12px; display: flex; justify-content: center; align-items: center; font-size: 60px; margin-bottom: 12px; }
.g-title { font-weight: 900; font-size: 15px; margin-bottom: 5px; }
.g-meta { font-size: 12px; color: var(--text-light); display: flex; justify-content: space-between; }
</style>
