from checkbox_groups import get_total_checkboxes, get_groups
from errors import Error, ErrorResponse
import cv2
import base64


def validate(original_image, checkbox_data):
	validate_checkbox_data = validate_checkbox_count(checkbox_data)
	if validate_checkbox_data.success is False:
		return validate_checkbox_data

	validate_groups = validate_group_restrictions(original_image, checkbox_data)
	if validate_groups.success is False:
		return validate_groups

	return ErrorResponse(
		True,
		[]
	)

# Sanity check to ensure that the number of checkboxes detected is correct.
def validate_checkbox_count(checkbox_data):
	total_checkboxes = get_total_checkboxes()
	detected_checkboxes = len(checkbox_data)
	if detected_checkboxes != total_checkboxes:
		return ErrorResponse(
			False,
			[
				Error(
					"Checkbox Count",
					"The document could not be processed correctly. Total checkboxes detected: " + str(detected_checkboxes) + " Total checkboxes expected: " + str(total_checkboxes)
				)
			]

		)
	return ErrorResponse(
		True,
		[]
	)

# Validate that the checkboxes meet the group restrictions.
def validate_group_restrictions(original_image, checkbox_data):
	groups = get_groups()
	grouped_checkboxes = get_checkboxes_for_group(checkbox_data)
	error_coordinates = {}
	errors = []

	for group_idx, group in enumerate(groups):
		validate_group_restriction(group_idx, group, grouped_checkboxes, error_coordinates, errors)

	if len(errors) > 0: 
		error_image_path = save_error_image(grouped_checkboxes, original_image, error_coordinates)
		return ErrorResponse(
			False,
			errors,
			error_image_path
		)

	return ErrorResponse(
		True,
		[]
	)

def get_checkboxes_for_group(checkbox_data):
	grouped_checkboxes = {}
	for checkbox in checkbox_data:
		group = checkbox["group"]
		if group not in grouped_checkboxes:
			grouped_checkboxes[group] = []
		grouped_checkboxes[group].append(checkbox)
	return grouped_checkboxes


def set_error_coordinates(group_idx, checkboxes, error_coordinates):
	first_checkbox = checkboxes[0]
	last_checkbox = checkboxes[-1]			
	error_coordinates[group_idx] = {
		"top_left": (
			int(first_checkbox["x"] - 0.3 * first_checkbox["width"]), 
			int(first_checkbox["y"] - 0.3 * first_checkbox["height"])
		),
		"bottom_right": (
			int(last_checkbox["x"] + last_checkbox["width"] + 0.3 * last_checkbox["width"]), 
			int(last_checkbox["y"] + last_checkbox["height"] + 0.3 * last_checkbox["height"])
		)
	}


def save_error_image(grouped_checkboxes, original_image, error_coordinates):
	error_image = original_image.copy()
	
	for group_idx, coordinates in error_coordinates.items():    
		cv2.rectangle(error_image, coordinates["top_left"], coordinates["bottom_right"], (0, 0, 255), 2)
		for checkbox in grouped_checkboxes[group_idx]:
			if checkbox["status"] == "filled":
				x, y, w, h = checkbox["x"], checkbox["y"], checkbox["width"], checkbox["height"]
				cv2.rectangle(error_image, (x - 3, y - 3), (x + w + 3, y + h + 3), (0, 255, 0), 2)

	_, buffer = cv2.imencode('.jpg', error_image)
	base64_image = base64.b64encode(buffer).decode('utf-8')
	return f"data:image/jpeg;base64,{base64_image}"


def validate_group_restriction(group_idx, group, grouped_checkboxes, error_coordinates, errors):
	filled_count = sum(1 for checkbox in grouped_checkboxes[group_idx] if checkbox["status"] == "filled")
	if ((group["exactlyOneMatch"] and filled_count != 1) or (group["atMostOneMatch"] and filled_count > 1)):
		set_error_coordinates(group_idx, grouped_checkboxes[group_idx], error_coordinates)
		errors.append(Error(group["name"], group["errorMessage"]))