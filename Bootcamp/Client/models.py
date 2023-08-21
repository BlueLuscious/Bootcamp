from django.db import models

class WorkLineChoices(models.TextChoices):
    BAKER = "Baker"
    BEAT_MAKER = "Beat Maker"
    JEWELER = "Jeweler"
    LAWYER = "Lawyer"
    STRIPPER = "Stripper"
    IS_NONE = "None"
    
class ClientModel(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=256)
    password = models.CharField(max_length=50)
    cuit = models.CharField(max_length=11)
    work_line = models.CharField(choices=WorkLineChoices.choices, max_length=256, default=WorkLineChoices.IS_NONE)
    interest = models.CharField(max_length=256)
    is_seller = models.BooleanField(default=False)
    is_buyer = models.BooleanField(default=True)
    province = models.CharField(max_length=100)
    city = models.CharField(max_length=150)
    area_code = models.CharField(max_length=6)
    
    def __str__(self) -> str:
        return f"First name: {self.first_name}, Last name: {self.last_name}"