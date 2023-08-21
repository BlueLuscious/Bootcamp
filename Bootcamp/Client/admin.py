from django.contrib import admin
from .models import ClientModel

@admin.register(ClientModel)
class ClientModel(admin.ModelAdmin):
    pass