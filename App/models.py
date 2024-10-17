from django.db import models

class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add = True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=13)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    pincode = models.IntegerField()

    def __str__(self):
        return(f"{self.first_name} {self.last_name}")
