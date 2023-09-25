import re

from django.forms import ValidationError

REGEX_EMAIL= '^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

def email_validate(email):
    if not re.match(REGEX_EMAIL, email):
                raise ValidationError("이메일 형식이 아닙니다.")