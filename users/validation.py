from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_studentnumber(value):
    if len(value) != 10:
        raise ValidationError("학번을 정확히 입력해주세요")