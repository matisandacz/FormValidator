import { API_URL } from '../config'

export async function generateRandomForm(fillProbability = 0.5) {
  const response = await fetch(`${API_URL}/random-form`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ fillProbability })
  })

  const data = await response.json()

  if (!data.success) {
    throw new Error('Failed to generate form')
  }

  return data.image
} 