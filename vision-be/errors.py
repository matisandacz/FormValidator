class Error:
    def __init__(self, error_name, error_message):
        self.error_name = error_name
        self.error_message = error_message

    def to_dict(self):
        return {
            "error_name": self.error_name,
            "error_message": self.error_message
        }

class ErrorResponse:
    def __init__(self, success, errors, error_image=None):
        self.success = success
        self.errors = errors
        self.error_image = error_image

    def to_dict(self):  
        return {
            "success": self.success,
            "errors": [error.to_dict() for error in self.errors],
            "error_image": self.error_image
        }

