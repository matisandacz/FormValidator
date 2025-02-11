from preprocessing import preprocess_image
from checkbox_detection import (
    are_bounding_dimensions_correct,
    detect_checkboxes
)
from checkbox_classification import classify_checkboxes
from validations import validate


def validate_form(original_image):
    """Process an image and detect/classify checkboxes"""
    preprocessed_image, binary_thresholded_image = preprocess_image(original_image)
    checkboxes = detect_checkboxes(preprocessed_image, are_bounding_dimensions_correct)    
    classified_checkboxes = classify_checkboxes(checkboxes, binary_thresholded_image)
    return validate(original_image, classified_checkboxes).to_dict()
