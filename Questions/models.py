from django.db import models


class Questions(models.Model):
    question_id = models.IntegerField(primary_key=True)
    question = models.CharField(max_length=255)

    def __str__(self):
        return self.question
