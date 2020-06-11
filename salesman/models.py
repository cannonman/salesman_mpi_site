from django.db import models
from django.contrib.auth.models import User


class Files(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(null=False, blank=False, upload_to='media/')
    file_name = models.CharField(max_length=50)
    date_uploaded = models.DateTimeField()
    finished = models.BooleanField(default=False)
    result = models.CharField(max_length=500, default='')

    def print_result(self):
        if self.finished:
            return self.result
        else:
            return 'Not completed yet'

    # def __str__(self):
    #     return self.index + self.file_name
