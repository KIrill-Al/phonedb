from django.db import models

class Phone(models.Model):
    number = models.CharField(unique=True, max_length=16)
    reserved = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Номера телефона"
        verbose_name_plural = "Номера телефонов"

    def __str__(self):
        return "({}{}{}) {}{}{}-{}{}{}{}".format(*tuple(self.number))
