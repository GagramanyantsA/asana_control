from django.db import models


class AsanaTask(models.Model):
    """
    Asana Task model
    """
    id = models.AutoField(primary_key=True)
    project = models.ForeignKey('asana_models.AsanaProject', models.DO_NOTHING)
    description = models.CharField(max_length=500)
    user = models.ForeignKey('asana_models.AsanaUser', models.DO_NOTHING)

    def __str__(self):
        return f'[{self.id}] Proj: {self.project.project_name[0:10]} Task: {self.description[0:20]}'
