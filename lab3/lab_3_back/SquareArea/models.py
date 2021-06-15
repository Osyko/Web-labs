from django.db import models

class DivRequest(models.Model):
    def __init__(self, input_value: int):
        self.input_value = input_value

class DivResponse(models.Model):
    def __init__(self, output_value: int):
        self.output_value = output_value
