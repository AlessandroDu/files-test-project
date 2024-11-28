from django.db import models

class File(models.Model):
    name = models.CharField(max_length=1024)
    file_type = models.CharField(max_length=10)
    upload_timestamp = models.DateTimeField(auto_now_add=True, null=True)
    file = models.FileField(null=True)

    def __str__(self):
        return self.name
