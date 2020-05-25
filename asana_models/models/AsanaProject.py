from django.db import models


class AsanaProject(models.Model):
    """
    Asana Project model
    """
    id = models.CharField(primary_key=True, unique=True, max_length=20)
    project_name = models.CharField(max_length=100)

    def __str__(self):
        return f'[{self.id}] {self.project_name}'
