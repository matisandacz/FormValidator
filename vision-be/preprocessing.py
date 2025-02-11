import cv2


def preprocess_image(image):
	# TODO: Allign the image.
	binary_img = apply_binary_threshold(image)
	return apply_morphological_ops(binary_img), binary_img

def apply_binary_threshold(img):
	img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	_, thresholded_img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
	return cv2.bitwise_not(thresholded_img)

def apply_morphological_ops(img):
	vertical_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 19))
	horizontal_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (19, 1))
	vertical = cv2.morphologyEx(img, cv2.MORPH_OPEN, vertical_kernel, iterations=1)
	horizontal = cv2.morphologyEx(img, cv2.MORPH_OPEN, horizontal_kernel, iterations=1)
	img_opened = cv2.addWeighted(vertical, 0.5, horizontal, 0.5, 0.0)
	_, img_opened = cv2.threshold(img_opened, 0, 255, cv2.THRESH_BINARY)
	closing_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (4, 4))
	return cv2.morphologyEx(img_opened, cv2.MORPH_CLOSE, closing_kernel, iterations=1) 