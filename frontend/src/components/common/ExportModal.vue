<template>
  <Teleport to="body">
    <div class="modal-overlay" :class="{ active: visible }" @click.self="$emit('close')">
      <div class="modal-content">
        <div class="close-btn" @click="$emit('close')">✖</div>
        <h2>🎉 图纸生成完毕</h2>
        <p class="modal-desc">请下载专为手工打造的保姆级指南</p>

        <div class="export-demo">
          <div class="ex-left">
            <div class="ex-label">📄 高清网格图纸</div>
            <div class="ex-grid-preview">
              <span class="ex-col-labels">A B C D E</span>
              <span class="ex-row-labels">1 2 3 4</span>
              <div class="ex-inner-grid"></div>
            </div>
            <p class="ex-tip">✅ 带有 A1, B2 等精准定位坐标系</p>
          </div>
          <div class="ex-right">
            <div class="ex-label">🛒 购物清单</div>
            <div class="ex-checklist">
              <label><input type="checkbox" /> P-01 白色 (145颗)</label>
              <label><input type="checkbox" /> P-18 黑色 (89颗)</label>
              <label><input type="checkbox" /> P-58 主题蓝 (42颗)</label>
              <label><input type="checkbox" checked /> 透明 29x29 模板 x 2</label>
              <label><input type="checkbox" /> 专用高透助烫纸 x 2</label>
            </div>
          </div>
        </div>

        <div class="export-actions">
          <button class="mock-pdf-btn btn-dark" @click="onDownloadPDF">
            ⬇️ 下载完整 PDF（推荐）
          </button>
          <button class="mock-pdf-btn btn-primary" @click="onDownloadImage">
            ⬇️ 仅保存无网格图片
          </button>
        </div>
      </div>
    </div>
  </Teleport>
</template>

<script setup lang="ts">
defineProps<{ visible: boolean }>()
defineEmits<{ close: [] }>()

function onDownloadPDF() {
  alert('正在开始下载：【拼了个豆_专属图纸清单.pdf】')
}
function onDownloadImage() {
  alert('已将高清图保存至相册！')
}
</script>

<style scoped>
.modal-overlay {
  display: none;
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
  z-index: 2000;
  justify-content: center;
  align-items: center;
  backdrop-filter: blur(5px);
}

.modal-overlay.active {
  display: flex;
}

.modal-content {
  background: white;
  width: 620px;
  border-radius: var(--radius-lg);
  padding: 30px;
  position: relative;
  box-shadow: 0 20px 50px rgba(0, 0, 0, 0.15);
}

.close-btn {
  position: absolute;
  top: 20px;
  right: 20px;
  font-size: 18px;
  cursor: pointer;
  background: var(--bg-color);
  width: 32px;
  height: 32px;
  border-radius: 50%;
  display: flex;
  justify-content: center;
  align-items: center;
  user-select: none;
}

.modal-content h2 {
  font-weight: 900;
  text-align: center;
}

.modal-desc {
  text-align: center;
  color: var(--text-light);
  font-size: 13px;
  margin-top: 5px;
}

.export-demo {
  background: var(--bg-color);
  border: 1px solid var(--border-color);
  padding: 20px;
  margin: 20px 0;
  border-radius: var(--radius-md);
  height: 260px;
  display: flex;
}

.ex-left {
  flex: 1.2;
  border-right: 2px dashed var(--border-color);
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}

.ex-right {
  flex: 1;
  padding-left: 20px;
  overflow-y: auto;
}

.ex-label {
  font-weight: bold;
  margin-bottom: 10px;
  font-size: 14px;
}

.ex-grid-preview {
  width: 120px;
  height: 120px;
  border: 1px solid #ccc;
  background: white;
  position: relative;
  display: flex;
  justify-content: center;
  align-items: center;
}

.ex-col-labels {
  position: absolute;
  top: 2px;
  left: 5px;
  font-size: 9px;
}

.ex-row-labels {
  position: absolute;
  top: 15px;
  left: 2px;
  font-size: 9px;
  writing-mode: vertical-rl;
}

.ex-inner-grid {
  width: 80%;
  height: 80%;
  background-image:
    linear-gradient(#ddd 1px, transparent 1px),
    linear-gradient(90deg, #ddd 1px, transparent 1px);
  background-size: 5px 5px;
}

.ex-tip {
  font-size: 11px;
  color: var(--text-light);
  margin-top: 10px;
}

.ex-checklist {
  font-size: 12px;
  line-height: 1.8;
}

.ex-checklist label {
  display: block;
  cursor: pointer;
}

.export-actions {
  display: flex;
  gap: 15px;
}

.mock-pdf-btn {
  color: white;
  border: none;
  padding: 14px;
  width: 100%;
  border-radius: 12px;
  font-weight: bold;
  cursor: pointer;
  transition: 0.2s;
  font-size: 14px;
}

.mock-pdf-btn:hover { opacity: 0.9; }
.btn-dark { background: var(--text-main); }
.btn-primary { background: var(--primary); }
</style>
