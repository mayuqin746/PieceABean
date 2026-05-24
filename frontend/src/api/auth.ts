import api from './index'

export async function login(username: string, password: string) {
  const { data } = await api.post<{ access_token: string }>('/users/login', { username, password })
  return data
}

export async function register(username: string, email: string, password: string) {
  const { data } = await api.post('/users/register', { username, email, password })
  return data
}
