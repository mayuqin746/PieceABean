<template>
  <header class="navbar">
    <img
      class="logo"
      src="/logo.png"
      alt="拼了个豆"
      @click="$router.push('/')"
    />
    <div class="nav-links">
      <div
        v-for="item in navItems"
        :key="item.target"
        class="nav-item"
        :class="{ active: isActive(item.target) }"
        @click="$router.push(item.path)"
      >
        {{ item.label }}
      </div>
    </div>

    <div class="header-search">
      <input type="text" placeholder="搜索图纸、系列..." />
    </div>

    <div class="theme-switcher">
      <span class="theme-label">主题：</span>
      <div
        v-for="t in themes"
        :key="t.name"
        class="theme-dot"
        :class="{ active: store.currentTheme === t.name }"
        :style="{ background: t.color }"
        :title="t.title"
        @click="store.setTheme(t.name)"
      ></div>
    </div>

    <div class="user-profile" @click="$router.push('/profile')">
      <div class="avatar">👧🏻</div>
      <div class="user-label">我的主页</div>
    </div>
  </header>
</template>

<script setup lang="ts">
import { useRoute } from 'vue-router'
import { useThemeStore, type ThemeName } from '@/stores/theme'

const route = useRoute()
const store = useThemeStore()

const navItems = [
  { label: '首页', target: 'home', path: '/' },
  { label: '工作台', target: 'workspace', path: '/workspace' },
  { label: '分类', target: 'gallery', path: '/gallery' },
  { label: '指南', target: 'guide', path: '/guide' },
]

const themes = [
  { name: 'blue' as ThemeName, color: '#A6DDF9', title: '海盐蓝 🌊' },
  { name: 'pink' as ThemeName, color: '#FEADCF', title: '樱花粉' },
  { name: 'purple' as ThemeName, color: '#D9B6FB', title: '香芋紫' },
]

function isActive(name: string) {
  if (name === 'home') return route.path === '/'
  return route.path.startsWith(`/${name}`)
}
</script>

<style scoped>
.navbar {
  height: var(--header-height);
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(10px);
  padding: 0 40px;
  display: flex;
  align-items: center;
  position: fixed;
  top: 0;
  width: 100%;
  z-index: 1000;
  border-bottom: 1px solid var(--border-color);
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.02);
}

.logo {
  height: 100px;
  width: auto;
  margin-right: 40px;
  cursor: pointer;
  user-select: none;
  object-fit: contain;
}

.nav-links {
  display: flex;
  gap: 8px;
}

.nav-item {
  padding: 8px 18px;
  font-weight: bold;
  font-size: 15px;
  cursor: pointer;
  border-radius: 20px;
  transition: 0.2s;
  user-select: none;
}

.nav-item.active {
  background: var(--text-main);
  color: white;
}

.nav-item:hover:not(.active) {
  background: var(--primary-light);
  color: var(--primary);
}

.header-search {
  margin-left: auto;
  margin-right: 20px;
  position: relative;
}

.header-search::before {
  content: "🔍";
  position: absolute;
  left: 12px;
  top: 10px;
  font-size: 13px;
  z-index: 1;
}

.header-search input {
  padding: 10px 20px 10px 35px;
  border-radius: 20px;
  border: none;
  background: var(--bg-color);
  width: 200px;
  font-weight: bold;
  outline: none;
  transition: 0.3s;
  color: var(--text-main);
}

.header-search input:focus {
  width: 260px;
  background: white;
  box-shadow: 0 0 0 2px var(--primary-light);
}

.theme-switcher {
  display: flex;
  gap: 8px;
  margin-right: 25px;
  background: var(--bg-color);
  padding: 5px 10px;
  border-radius: 20px;
  border: 1px solid var(--border-color);
  align-items: center;
}

.theme-label {
  font-size: 12px;
  font-weight: bold;
  color: var(--text-light);
}

.theme-dot {
  width: 20px;
  height: 20px;
  border-radius: 50%;
  cursor: pointer;
  border: 2px solid transparent;
}

.theme-dot.active {
  border-color: var(--text-main);
  transform: scale(1.1);
}

.user-profile {
  display: flex;
  align-items: center;
  gap: 8px;
  cursor: pointer;
  padding: 4px 12px 4px 4px;
  border-radius: 20px;
  background: white;
  border: 1px solid var(--border-color);
}

.user-label {
  font-weight: bold;
  font-size: 13px;
}

.avatar {
  width: 32px;
  height: 32px;
  border-radius: 50%;
  background: var(--primary-light);
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 16px;
  user-select: none;
}
</style>
