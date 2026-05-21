<template>
  <NavHeader />
  <main :class="$route.name === 'workspace' ? 'workspace-layout' : 'default-layout'">
    <router-view v-slot="{ Component }">
      <transition name="fade" mode="out-in">
        <component :is="Component" />
      </transition>
    </router-view>
  </main>
  <FloatingPet
    message="点这里抽个盲盒呀！(づ￣ 3￣)づ"
    @click="onBlindBox"
  />
  <ExportModal :visible="showExportModal" @close="showExportModal = false" />
</template>

<script setup lang="ts">
import { ref, provide, watch } from 'vue'
import { useRoute } from 'vue-router'
import NavHeader from '@/components/common/NavHeader.vue'
import FloatingPet from '@/components/common/FloatingPet.vue'
import ExportModal from '@/components/common/ExportModal.vue'

const route = useRoute()
const showExportModal = ref(false)

provide('showExportModal', (val: boolean) => {
  showExportModal.value = val
})

watch(
  () => route.name,
  (name) => {
    if (name === 'workspace') {
      document.body.classList.add('immersive')
    } else {
      document.body.classList.remove('immersive')
      window.scrollTo(0, 0)
    }
  },
  { immediate: true }
)

function onBlindBox() {
  alert('恭喜抽中隐藏款：【治愈海豚】！')
}
</script>

<style>
@import '@/assets/styles/variables.css';
@import '@/assets/styles/base.css';
</style>

<style scoped>
.default-layout {
  padding-top: calc(var(--header-height) + 30px);
  padding-bottom: 80px;
  min-height: 100vh;
}

.workspace-layout {
  padding-top: var(--header-height);
  height: 100vh;
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s ease, transform 0.3s ease;
}
.fade-enter-from {
  opacity: 0;
  transform: translateY(15px);
}
.fade-leave-to {
  opacity: 0;
  transform: translateY(-15px);
}
</style>
