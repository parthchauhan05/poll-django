from django.db import models


class poll(models.Model):
    text = models.CharField(max_length=255)
    pub_date = models.DateField()

    def __str__(self):
        return self.text


class choice(models.Model):
    question = models.ForeignKey(poll, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=255)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return "{} - {}".format(self.question.text[:25], self.choice_text[:25])