from django.db import models
class Organization(models.Model):
    OrganizationName = models.CharField(max_length=100)
    CeoName = models.CharField(max_length = 100)
    email = models.EmailField(max_length=100)
    data = models.DateField(auto_now_add=True)
