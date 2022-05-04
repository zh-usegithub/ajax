from django.db import models

# Create your models here.
class user_table(models.Model):
    username = models.CharField(name='name',max_length=30)
    password = models.CharField(name='password',max_length=60)
    created_time = models.DateTimeField(name='created_time',auto_now_add=True)
    update_time = models.DateTimeField(name='update_time',auto_now_add=True)
    class Meta:
        db_table = 'user_information'
