from django.db import models


class AsanaUser(models.Model):
    """
    Asana User model
    """
    id = models.CharField(primary_key=True, unique=True, max_length=20)
    name = models.EmailField(max_length=100, unique=True, blank=False)

    def __str__(self):
        return f'[{self.id}] {self.name}'
