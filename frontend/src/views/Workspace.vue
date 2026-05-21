<template>
  <div class="workspace">
    <!-- 左侧参数面板 -->
    <aside class="ws-sidebar">
      <div class="ws-header">
        参数设置
        <span class="step-label">步骤 1/2</span>
      </div>
      <div class="ws-body">
        <button class="reupload-btn">
          📸 重新上传照片
        </button>

        <div class="control-group">
          <span class="control-label">1. 拼豆品牌色卡库</span>
          <select class="tool-select">
            <option>🔴 Perler (帕尔 - 推荐)</option>
            <option>🔵 Artkal (阿特卡 - 颜色丰富)</option>
            <option>🟢 Hama (哈玛)</option>
          </select>
        </div>

        <div class="control-group">
          <span class="control-label">2. 目标板子尺寸 (格子数)</span>
          <input
            type="range"
            class="range-slider"
            min="15"
            max="120"
            :value="gridSize"
            @input="gridSize = +($event.target as HTMLInputElement).value"
          />
          <div class="size-val">{{ gridSize }} x {{ gridSize }}</div>
        </div>

        <div class="control-group">
          <span class="control-label">3. 色彩风格滤镜</span>
          <div class="filter-grid">
            <div
              v-for="(f, i) in filters"
              :key="i"
              class="filter-card"
              :class="{ active: activeFilter === i }"
              @click="activeFilter = i"
            >
              {{ f.name }}
              <div class="f-color-bar">
                <div v-for="(c, j) in f.bar" :key="j" :style="{ background: c }"></div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </aside>

    <!-- 中央画布 -->
    <section class="ws-center" id="canvas-area">
      <div class="floating-toolbar">
        <button class="tool-btn" title="拖拽">✋</button>
        <button
          class="tool-btn"
          :class="{ active: activeTool === 'brush' }"
          title="画笔"
          @click="activeTool = 'brush'"
        >🖌️</button>
        <button
          class="tool-btn"
          :class="{ active: activeTool === 'picker' }"
          title="吸管"
          @click="activeTool = 'picker'"
        >💉</button>
        <button class="tool-btn" title="橡皮擦">🧽</button>
        <div class="tool-divider"></div>
        <div class="current-color" title="当前选中颜色"></div>
      </div>

      <div class="canvas-wrapper" :style="{ transform: `scale(${zoom})` }">
        <div class="canvas-grid">
          <span class="canvas-emoji">🐶</span>
        </div>
      </div>

      <div class="zoom-controls">
        <span class="zoom-btn" @click="changeZoom(-0.1)">➖</span>
        <span class="zoom-text">{{ Math.round(zoom * 100) }}%</span>
        <span class="zoom-btn" @click="changeZoom(0.1)">➕</span>
      </div>
    </section>

    <!-- 右侧清单 -->
    <aside class="ws-sidebar ws-sidebar-right">
      <div class="ws-header">🛒 实时豆子清单</div>
      <div class="ws-body ws-body-flex">
        <p class="ws-tip">
          提示：使用左侧画笔对图纸进行微调后，此清单的数据会实时联动。
        </p>

        <div class="color-list">
          <div v-for="item in colorItems" :key="item.name" class="color-list-item">
            <div class="c-left">
              <div class="c-dot" :style="{ background: item.color }"></div>
              {{ item.name }}
            </div>
            <span>{{ item.count }} 颗</span>
          </div>
        </div>

        <div class="ws-footer">
          <div class="total-row">
            <span>总豆数：</span>
            <span class="total-count">486 颗</span>
          </div>
          <button class="btn-export" @click="onExport">📥 保姆级导出 (PDF/高清图)</button>
        </div>
      </div>
    </aside>
  </div>
</template>

<script setup lang="ts">
import { ref, inject } from 'vue'

const showExport = inject<(val: boolean) => void>('showExportModal', () => {})

const gridSize = ref(58)
const activeFilter = ref(0)
const activeTool = ref('brush')
const zoom = ref(1)

const filters = [
  { name: '真实相片', bar: ['#555', '#888', '#ccc'] },
  { name: '马卡龙系', bar: ['#FFB6C1', '#A0C4FF', '#98FB98'] },
  { name: '复古像素', bar: ['#FF5722', '#4CAF50', '#2196F3'] },
  { name: '冷淡极简', bar: ['#E2E8F0', '#94A3B8', '#fff'] },
]

const colorItems = [
  { name: 'P-01 白色', color: '#FFFFFF', count: 145 },
  { name: 'P-18 黑色', color: '#111111', count: 89 },
  { name: 'P-58 主题色', color: 'var(--primary)', count: 42 },
  { name: 'P-20 浅棕色', color: '#D2B48C', count: 210 },
]

function changeZoom(delta: number) {
  zoom.value = Math.min(2.5, Math.max(0.5, zoom.value + delta))
}

function onExport() {
  showExport(true)
}
</script>

<style scoped>
.workspace { display: flex; height: calc(100vh - var(--header-height)); }

.ws-sidebar {
  width: 320px;
  background: white;
  height: 100%;
  display: flex;
  flex-direction: column;
  box-shadow: 2px 0 15px rgba(0,0,0,0.02);
  z-index: 10;
  flex-shrink: 0;
}
.ws-sidebar-right {
  box-shadow: -2px 0 15px rgba(0,0,0,0.02);
  border-left: 1px solid var(--border-color);
}

.ws-header {
  padding: 20px;
  border-bottom: 1px solid var(--border-color);
  font-weight: 900;
  font-size: 16px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.step-label { font-size: 12px; color: var(--text-light); font-weight: normal; }

.ws-body { padding: 20px; overflow-y: auto; flex: 1; }
.ws-body-flex { display: flex; flex-direction: column; }

.reupload-btn {
  width: 100%; padding: 15px;
  background: #F8FAFC; border: 2px dashed var(--primary);
  border-radius: 12px; cursor: pointer;
  font-weight: bold; color: var(--primary); margin-bottom: 20px;
}

.control-group { margin-bottom: 25px; }
.control-label { font-size: 13px; font-weight: bold; color: var(--text-light); margin-bottom: 10px; display: block; }

.tool-select { width: 100%; padding: 10px 15px; border-radius: 12px; border: 1px solid var(--border-color); font-weight: bold; outline: none; background: #F8FAFC; color: var(--text-main); }

.range-slider {
  width: 100%; -webkit-appearance: none; height: 6px;
  background: var(--border-color); border-radius: 3px; outline: none; margin: 10px 0;
}
.range-slider::-webkit-slider-thumb {
  -webkit-appearance: none; width: 18px; height: 18px; border-radius: 50%;
  background: var(--primary); cursor: pointer; border: 2px solid white; box-shadow: 0 2px 5px rgba(0,0,0,0.15);
}
.size-val { text-align: right; font-weight: bold; color: var(--primary); font-size: 14px; margin-top: 5px; }

.filter-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; }
.filter-card {
  border: 2px solid var(--border-color); padding: 10px; border-radius: 12px;
  text-align: center; cursor: pointer; transition: 0.2s; font-size: 13px; font-weight: bold; background: white;
}
.filter-card.active { border-color: var(--primary); background: var(--primary-light); color: var(--primary); }
.f-color-bar { display: flex; height: 6px; border-radius: 3px; overflow: hidden; margin-top: 5px; }
.f-color-bar div { flex: 1; }

/* 画布 */
.ws-center {
  flex: 1; position: relative;
  display: flex; justify-content: center; align-items: center;
  overflow: hidden; background: #EAEAEF;
}

.floating-toolbar {
  position: absolute; left: 20px; top: 20px;
  background: white; padding: 5px; border-radius: 12px;
  box-shadow: var(--shadow-soft); display: flex; flex-direction: column; gap: 5px;
  border: 1px solid var(--border-color);
}
.tool-btn {
  width: 40px; height: 40px; border-radius: 8px;
  display: flex; justify-content: center; align-items: center;
  cursor: pointer; font-size: 18px; transition: 0.2s; border: none; background: white;
}
.tool-btn:hover { background: var(--primary-light); }
.tool-btn.active { background: var(--primary); color: white; }
.tool-divider { width: 100%; height: 1px; background: var(--border-color); margin: 5px 0; }
.current-color {
  width: 26px; height: 26px; border-radius: 50%; background: var(--primary);
  margin: 0 auto; border: 2px solid white; box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.canvas-wrapper {
  width: 400px; height: 400px;
  background: white;
  box-shadow: 0 10px 40px rgba(0,0,0,0.08);
  transition: transform 0.2s ease-out;
}
.canvas-grid {
  width: 100%; height: 100%;
  background-image:
    linear-gradient(var(--border-color) 1px, transparent 1px),
    linear-gradient(90deg, var(--border-color) 1px, transparent 1px);
  background-size: 10px 10px;
  display: flex; justify-content: center; align-items: center;
}
.canvas-emoji { font-size: 100px; opacity: 0.9; pointer-events: none; user-select: none; }

.zoom-controls {
  position: absolute; right: 20px; bottom: 20px;
  display: flex; gap: 10px; background: white; padding: 8px 15px;
  border-radius: 20px; box-shadow: var(--shadow-soft);
  font-weight: bold; align-items: center; border: 1px solid var(--border-color);
}
.zoom-btn { cursor: pointer; user-select: none; }
.zoom-text { min-width: 44px; text-align: center; }

/* 清单 */
.ws-tip { font-size: 12px; color: var(--text-light); margin-bottom: 15px; line-height: 1.5; }
.color-list { flex: 1; overflow-y: auto; padding-right: 5px; }

.color-list-item {
  display: flex; justify-content: space-between; align-items: center;
  padding: 12px 15px; border: 1px solid var(--border-color);
  border-radius: 10px; margin-bottom: 8px; font-size: 13px; font-weight: bold; background: #F8FAFC;
}
.c-left { display: flex; align-items: center; gap: 8px; }
.c-dot { width: 18px; height: 18px; border-radius: 50%; border: 1px solid rgba(0,0,0,0.1); }

.ws-footer { border-top: 1px solid var(--border-color); padding-top: 15px; margin-top: 15px; }
.total-row { display: flex; justify-content: space-between; font-weight: 900; margin-bottom: 10px; }
.total-count { color: var(--primary); }

.btn-export {
  background: var(--primary); color: white; border: none;
  padding: 16px; border-radius: 16px; font-size: 16px;
  font-weight: 900; cursor: pointer; width: 100%;
  transition: 0.2s; box-shadow: 0 6px 15px rgba(0,0,0,0.05);
}
.btn-export:hover { transform: translateY(-2px); box-shadow: 0 10px 20px rgba(123, 164, 219, 0.3); }
</style>
