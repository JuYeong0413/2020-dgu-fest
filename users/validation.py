from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_studentnumber(value):
    if len(value) != 10:
        if value < 2000000000 and 2020999999 < value :
            raise ValidationError("학번을 정확히 입력해주세요")


def validate_phonenumber(value):
        if len(value) !=11:
            raise ValidationError("올바른 번호를 입력해주세요")