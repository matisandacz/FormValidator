import cv2
import random
import base64
from checkbox_detection import detect_checkboxes, are_bounding_dimensions_correct
from checkbox_classification import is_checkbox_filled
from preprocessing import preprocess_image

def draw_cross(image, x, y, w, h, color=(0, 0, 0), thickness=2):
	"""Draw an X mark inside the checkbox"""
	padding = 8
	# Draw the first diagonal line (\)
	pt1 = (x + padding, y + padding)
	pt2 = (x + w - padding, y + h - padding)
	cv2.line(image, pt1, pt2, color, thickness)
	
	# Draw the second diagonal line (/)
	pt3 = (x + padding, y + h - padding)
	pt4 = (x + w - padding, y + padding)
	cv2.line(image, pt3, pt4, color, thickness)
	return image

def generate(image, overlay=False, fill_probability=0.3):
	preprocessed_image, binary_thresholded_image = preprocess_image(image)
	checkboxes = detect_checkboxes(preprocessed_image, are_bounding_dimensions_correct)

	# First clean all checkboxes
	padding = 2
	for contour in checkboxes:
		x, y, w, h = cv2.boundingRect(contour)
		image[y+padding:y+h-padding, x+padding:x+w-padding] = 255
		if random.random() < fill_probability:
			x, y, w, h = cv2.boundingRect(contour)
			image = draw_cross(image, x, y, w, h)

	if overlay:
		preprocessed_image, binary_thresholded_image = preprocess_image(image)
		checkboxes = detect_checkboxes(preprocessed_image, are_bounding_dimensions_correct)

		for contour in checkboxes:
			x, y, w, h = cv2.boundingRect(contour)
			color = (0, 255, 0) if is_checkbox_filled(contour, binary_thresholded_image) else (0, 0, 255)
			cv2.rectangle(image, (x, y), (x + w, y + h), color, 2)

	return image


def generate_random_form(fill_probability=0.45):
	"""Generate a random form and return base64 encoded image"""
	try:
		image = cv2.imread("form.jpg")
		if image is None:
			raise ValueError(f"Could not read image at {input_path}")
		random_image = generate(image, fill_probability=fill_probability)
		_, buffer = cv2.imencode('.jpg', random_image)
		image_bytes = buffer.tobytes()
		base64_image = base64.b64encode(image_bytes).decode('utf-8')
		return f"data:image/jpeg;base64,{base64_image}"
	except Exception as e:
		raise ValueError(f"Failed to generate random form: {str(e)}") 

