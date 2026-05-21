import { defineStore } from 'pinia'
import { ref } from 'vue'

export type ThemeName = 'blue' | 'pink' | 'green'

export const useThemeStore = defineStore('theme', () => {
  const currentTheme = ref<ThemeName>('blue')

  function setTheme(name: ThemeName) {
    currentTheme.value = name
    if (name === 'blue') {
      document.documentElement.removeAttribute('data-theme')
    } else {
      document.documentElement.setAttribute('data-theme', name)
    }
  }

  return { currentTheme, setTheme }
})
