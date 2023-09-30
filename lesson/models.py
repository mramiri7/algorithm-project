from django.db import models


class Lesson(models.Model):
    
    subject = models.CharField(max_length=255)
    description = models.TextField()
    handouts = models.FileField(upload_to='handouts/', blank=True, null=True)
    videos = models.URLField(blank=True)
    
    
    def __str__(self) -> str:
        return self.subject
