import cv2
from checkbox_groups import get_group_for_checkbox

def is_checkbox_filled(checkbox_contour, image):
	x, y, w, h = cv2.boundingRect(checkbox_contour)

	# Vertical scan
	vertical_white_pixels = 0
	for i in range(x, x+w):
		white_pixel_count = 0
		for j in range(y, y + h):
			if image[j, i] == 255:
				white_pixel_count += 1
		if white_pixel_count > 2:
			vertical_white_pixels += 1

	# Horizontal scan
	horizontal_white_pixels = 0
	for j in range(y, y + h):
		white_pixel_count = 0
		for i in range(x, x + w):
			if image[j, i] == 255:
				white_pixel_count += 1
		if white_pixel_count > 2:
			horizontal_white_pixels += 1

	# Check if a significant amount of scan lines encountered a checkmark
	vertical_threshold = w * 0.45
	horizontal_threshold = h * 0.45

	return (vertical_white_pixels >= vertical_threshold or 
			horizontal_white_pixels >= horizontal_threshold)

def classify_checkboxes(contours, image):
	# Sort from top left to bottom right.
	contours.sort(key=lambda ctr: (cv2.boundingRect(ctr)[1], cv2.boundingRect(ctr)[0]))
	checkbox_status = []
	
	for i, contour in enumerate(contours):
		x, y, w, h = cv2.boundingRect(contour)
		status = "filled" if is_checkbox_filled(contour, image) else "unfilled"
		group = get_group_for_checkbox(i)
		
		checkbox_status.append({
			"id": i,
			"x": x,
			"y": y,
			"width": w,
			"height": h,
			"status": status,
			"group": group
		})

	return checkbox_status