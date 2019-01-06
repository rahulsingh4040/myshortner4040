from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

def validate_url(value):
	url_validator = URLValidator()
	value_1_invalid = False
	value_2_invalid = False
	
	try:
		url_validator(value)
	except:
		value_1_invalid = True

	value_2_url = "http://" + value
	
	try:
		url_validator(value_2_url)
	except:
		value_2_invalid = True
	
	if value_1_invalid == True and value_2_invalid == True:
		raise ValidationError("Invalid URL")
		return;

	if "http" not in value and "www" not in value:
		raise ValidationError("Please add http and www")
	
	elif "www" not in value:
		raise ValidationError("Please add www")

	elif "http" not in value:
		raise ValidationError("Please add http")
	
	return value;

	
