import { useState } from 'react'
import { generateRandomForm } from '../../services/generationService'
import { validateForm } from '../../services/validationService'
import FormDisplay from './FormDisplay'
import FormError from './FormError'

function FormGenerator() {
  const [formImage, setFormImage] = useState(null)
  const [error, setError] = useState(null)
  const [validationResult, setValidationResult] = useState(null)
  const [validationErrors, setValidationErrors] = useState([])

  const handleGenerateForm = async () => {
    try {
      setError(null)
      setValidationResult(null)
      setValidationErrors([])
      const image = await generateRandomForm()
      setFormImage(image)
    } catch (err) {
      setError('Failed to generate form. Please try again.')
      console.error('Error generating form:', err)
    }
  }

  const handleValidate = async () => {
    try {
      setError(null)
      const result = await validateForm(formImage)

      if (!result.success) {
        setFormImage(result.error_image)
        setValidationResult(result.success)
        setValidationErrors(result.errors)
      }

    } catch (err) {
      setError('Failed to validate form. Please try again.')
      console.error('Error validating form:', err)
    }
  }

  return (
    <div className="flex flex-col items-center">

      <button
        onClick={handleGenerateForm}
        className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded mb-4"
      >
        Generate Random Form
      </button>

      {error && <FormError message={error} />}
      
      {formImage && (
        <>
          <FormDisplay image={formImage} />
          {validationResult === null && (
            <button
              onClick={handleValidate}
              className="bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 rounded mt-4"
            >
              Validate Form
            </button>
          )}
          
          {validationResult === false && (
            <div className="mt-4 p-4 bg-red-100 rounded-lg">
              <h3 className="font-bold text-red-800 mb-2">Validation Errors:</h3>
              <ul className="list-disc pl-5">
                {validationErrors.map((error, index) => (
                  <li key={index} className="text-red-700">
                    <span className="font-semibold">{error.error_name}:</span> {error.error_message}
                  </li>
                ))}
              </ul>
            </div>
          )}
        </>
      )}

    </div>
  )
}

export default FormGenerator