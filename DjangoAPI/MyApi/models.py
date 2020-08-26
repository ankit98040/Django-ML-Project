from django.db import models

class MyFile(models.Model):
    image = models.ImageField()


    #TO APPLY OR CHANGE OR ADD TO DATABASE, DO THE FOLLOWING STEPS BELOW

#python manage.py makemigrations MyApi
#python manage.py migrate