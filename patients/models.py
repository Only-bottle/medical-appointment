from django.db import models

from common.models import CommonModel


class Patient(CommonModel):

    """Model Definition for Patient"""

    name = models.CharField(max_length=140)

    def __str__(self) -> str:
        return self.name
