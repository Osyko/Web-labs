from django.db import models

class Company(models.Model):
    class Meta:
        ordering = ['id']
        unique_together = ('nameofcompany', 'typeofbeer')

    id = models.AutoField(primary_key=True)
    nameofcompany = models.CharField(max_length=50)
    typeofbeer = models.CharField(max_length=50)

    def __str__(self):
        return self.nameofcompany
