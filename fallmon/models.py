from django.db import models


# Create your models here.

class User(models.Model):
    pw = models.CharField(max_length=255)

    def __str__(self):
        return str(self.id)

    # Meta information for django admin
    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"


class FallType(models.Model):
    name = models.CharField(max_length=255, default="", unique=True)

    def __str__(self):
        return f"[{self.id} {self.name}]"
    # Meta information for django admin

    class Meta:
        verbose_name = "FallType"
        verbose_name_plural = "FallTypes"

class FallHistory(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField()
    fall_type = models.ForeignKey(FallType, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.id} [user: {self.user_id} {self.created_at} {self.fall_type.name}]"

    class Meta:
        verbose_name = "FallHistory"
        verbose_name_plural = "FallHistories"




