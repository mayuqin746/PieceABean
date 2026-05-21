import { useThemeStore } from '@/stores/theme'
import type { ThemeName } from '@/stores/theme'

export function useTheme() {
  const store = useThemeStore()
  return {
    theme: store.currentTheme,
    switchTheme: (name: ThemeName) => store.setTheme(name),
  }
}
