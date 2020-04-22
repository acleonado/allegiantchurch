from django.db import models

class Message(models.Model):
    name = models.CharField(max_length = 50)
    email = models.EmailField()
    subject = models.CharField(max_length = 100)
    msg = models.TextField(max_length = 1000)

    def __str__(self):
        return self.subject + ' | ' + str(self.name)