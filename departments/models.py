from django.db import models

from common.models import CommonModel


class Department(CommonModel):

    """Department Model Definition"""

    name = models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = "Departments"
