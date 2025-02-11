import { API_URL } from '../config'

export async function validateForm(imageData) {
  const response = await fetch(`${API_URL}/validate-form`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ image: imageData })
  })

  return await response.json()
} 