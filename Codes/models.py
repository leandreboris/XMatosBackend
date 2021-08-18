from django.db import models
from Users.models import User
import random 



# Create your models here.


# Code model for the login code 
class Code(models.Model):
    number = models.CharField(max_length=5, blank=True)
    user =models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user) + ' : ' + self.number 

    def save(self, *args, **kwargs):
        numbers_range = [n for n in range(10)]
        code_items = []
        for i in range(5):
            digit = random.choice(numbers_range)
            code_items.append(digit)

        code_string = "".join(str(item) for item in code_items)
        self.number = code_string
        super().save(*args, **kwargs)

