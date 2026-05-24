import api from './index'

export interface PatternItem {
  id: number
  title: string
  description: string | null
  category: string
  image_url: string | null
  full_image_url: string | null
  width: number
  height: number
  beads_count: number
  views: number
  likes: number
  created_at: string
}

export interface PatternListResponse {
  total: number
  items: PatternItem[]
}

export async function fetchPatterns(category?: string, page = 1, pageSize = 20, sort?: string) {
  const { data } = await api.get<PatternListResponse>('/patterns/', {
    params: { category, sort, page, page_size: pageSize },
  })
  return data
}

export async function fetchCategories() {
  const { data } = await api.get<{ categories: string[] }>('/patterns/categories')
  return data.categories
}
