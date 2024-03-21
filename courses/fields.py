from django.db import models


class OrderField(models.PositiveIntegerField):
    def __init__(self, for_fields=None, *args, **kwargs):
        self.for_field = for_fields
        super().__init__(*args, **kwargs)

