from django.db import models


class Cart (models.Model):
    cart_id = models.CharField(max_length=32, primary_key=True, unique=True)