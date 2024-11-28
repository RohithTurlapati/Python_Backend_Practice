from django.db import models
from .Address import Address
import User


class ShippingAddress(Address):
    shipping = models.ForeignKey(User, many=True, on_delete=models.CASCADE)