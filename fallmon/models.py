from django.db import models


# Create your models here.

class User(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    pw = models.CharField(max_length=256)

    def __str__(self):
        return self.id


class FallType(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=256, default="")


class FallHistory(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField()
    fall_type = models.ForeignKey(FallType, on_delete=models.DO_NOTHING)




