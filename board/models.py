from django.db import models

class Board(models.Model):
    b_title = models.CharField(max_length=255)
    b_writer = models.CharField(max_length=50)
    b_date = models.DateTimeField()
    
    def __str__(self):
        return self.b_title