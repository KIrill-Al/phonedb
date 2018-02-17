from django.db import models

class Phone(models.Model):
    number = models.IntegerField(primary_key=True)
    reserved = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Номера телефона"
        verbose_name_plural = "Номера телефонов"

    def __str__(self):
        return self.number
