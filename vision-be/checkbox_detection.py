import cv2
import numpy as np

def is_correct_area(contour, expected_area=625, tolerance=200):
	area = cv2.contourArea(contour)
	return abs(area - expected_area) <= tolerance

def are_bounding_dimensions_correct(contour, expected_area=625, tolerance=200, squareness_tolerance=5):
	area = cv2.contourArea(contour)
	x, y, w, h = cv2.boundingRect(contour)
	return abs(area - expected_area) <= tolerance and abs(w - h) <= squareness_tolerance

def is_contour_square(contour, contour_tolerance=0.0015, square_side=25, area_tolerance=200):
	expected_area = square_side * square_side
	area = cv2.contourArea(contour)
	template = np.array([[[0, 0]], [[0, 1]], [[1, 1]], [[1, 0]]], dtype=np.int32)
	return cv2.matchShapes(template, contour, 1, 0.0) <= contour_tolerance and abs(area - expected_area) <= area_tolerance

def detect_checkboxes(img_bin, func):
	contours, _ = cv2.findContours(img_bin, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
	return [x for x in contours if func(x)] 