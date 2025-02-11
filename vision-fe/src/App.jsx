import FormGenerator from './components/form-generator/FormGenerator'

function App() {
  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-gray-100 p-4">
      <h1 className="text-4xl font-bold text-gray-800 mb-8">Homevision Form Validator</h1>
      <FormGenerator />
    </div>
  )
}

export default App
