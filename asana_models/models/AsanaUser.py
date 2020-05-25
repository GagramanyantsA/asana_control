from django.db import models


class AsanaUser(models.Model):
    """
    Asana User model
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'[{self.id}] {self.name}'
