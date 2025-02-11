function FormDisplay({ image }) {
  return (
    <div className="mt-4 border-2 border-gray-200 rounded-lg p-2 bg-white w-2/3">
      <img 
        src={image} 
        alt="Generated Form"
        className="max-w-full h-auto"
      />
    </div>
  )
}

export default FormDisplay 