from django.db import models

# Create your models here.
class Record(models.Model):
    created_at  = models.DateTimeField(auto_now_add = True)
    first_name  = models.CharField(max_length = 50)
    last_name   = models.CharField(max_length = 50)
    email       = models.CharField(max_length = 50, null = True, blank = True)
    phone       = models.CharField(max_length = 15, null = True, blank  = True)
    address     = models.CharField(max_length = 100)
    city        = models.CharField(max_length = 50)
    state       = models.CharField(max_length = 50)
    zipcode     = models.CharField(max_length = 10)

    # We use __str__ to define how the object is displayed
    # __init__ is for object creation
    # __str__ makes it easier to identify objects when printing or viewing them.


    def __str__(self):
        # just to show full name when printing the object (like in admin)
        return (f"{self.first_name} {self.last_name}")

        # So, if we do print(record), then it will just display the
        # first and last name, instead of the entire details.