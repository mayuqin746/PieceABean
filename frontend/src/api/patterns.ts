import api from './index'

export interface PatternItem {
  id: number
  title: string
  description: string | null
  category: string
  series: string | null
  colors: string[] | null
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

export async function fetchPatterns(params: {
  category?: string
  series?: string
  color?: string
  sort?: string
  page?: number
  page_size?: number
}) {
  const { data } = await api.get<PatternListResponse>('/patterns/', { params })
  return data
}

export async function fetchCategories() {
  const { data } = await api.get<{ categories: string[] }>('/patterns/categories')
  return data.categories
}
