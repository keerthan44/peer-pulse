from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class Users(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=128)
    # photo = models.ImageField(upload_to='pics')

class UserProfiles(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    contact_email = models.EmailField()
    contact_phone = PhoneNumberField()
    about = models.TextField()
    f_name = models.CharField(max_length=50)
    l_name = models.CharField(max_length=50)
    srn = models.CharField(max_length=10)
    company = models.CharField(max_length=50)
    is_recruiter = models.BooleanField(default=False)


