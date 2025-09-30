from django.db import models

class Image(models.Model):
    image_name = models.CharField(max_length=255)
    description = models.TextField()
    image_file = models.ImageField(upload_to='uploads/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.image_name
