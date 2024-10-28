from django.db import models

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=100)
    user_password = models.CharField(max_length=100)
    user_nickname = models.CharField(max_length=100, blank=True, null=True)
    user_address = models.CharField(max_length=100)
    user_tel = models.CharField(max_length=100)
    user_icon_url = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'