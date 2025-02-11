import form_validator as form_validator
import random_form_generator as random_form_generator

from errors import ErrorResponse, Error

import cv2
import numpy as np
import base64
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/random-form', methods=['POST'])
def generate_random_form():
	data = request.get_json()
	try:
		fill_probability = data.get('fillProbability', 0.45)
		base64_image = random_form_generator.generate_random_form(
			fill_probability=fill_probability
		)
		return jsonify({
			"success": True,
			"image": base64_image
		})
	except Exception as e:
		return ErrorResponse(
			False,
			[
				Error(
					"Form Generation Error",
					str(e)
				)
			]
		).to_dict()
	
# TODO: Dockerize the app for deployment.
@app.route('/validate-form', methods=['POST'])
def validate_form():
	data = request.get_json()
	if not data or not 'image' in data:
		return ErrorResponse(
			False,
			[
				Error(
					"Missing Data",
					"No data provided"
				)
			]
		).to_dict()
	try:
		image = decode_base64_image(data['image'])
		result = form_validator.validate_form(image)
		return jsonify(result)
	except Exception as e:
		return ErrorResponse(
			False,
			[
				Error(
					"Image Processing Error",
					str(e)
				)
			]
		).to_dict()
	
def decode_base64_image(base64_data):
	if ',' in base64_data:
		base64_data = base64_data.split(',')[1]
	img_bytes = base64.b64decode(base64_data)
	nparr = np.frombuffer(img_bytes, np.uint8)
	return cv2.imdecode(nparr, cv2.IMREAD_COLOR)

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=5000)