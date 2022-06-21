import uuid
from uuid import uuid4

from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.PositiveIntegerField()
    last_updated = models.DateTimeField(auto_now=True)
    collection = models.ForeignKey(
        to='Collection', on_delete=models.SET_NULL, blank=True, null=True)
    promotions = models.ManyToManyField(
        to='Promotion', blank=True, related_name='products')

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ['title']


class Address(models.Model):
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=255)
    last_updated = models.DateTimeField(auto_now=True)
    customer = models.ForeignKey(to='Customer', on_delete=models.CASCADE)


class Customer(models.Model):
    MEMBERSHIP_BRONZE = 'BRONZE'
    MEMBERSHIP_SILVER = 'SILVER'
    MEMBERSHIP_GOLD = 'GOLD'

    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_BRONZE, 'Bronze'),
        (MEMBERSHIP_SILVER, 'Silver'),
        (MEMBERSHIP_GOLD, 'Gold')
    ]

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    birth_date = models.DateField(null=True, blank=True)
    membership = models.CharField(
        choices=MEMBERSHIP_CHOICES, default=MEMBERSHIP_BRONZE, max_length=10)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        ordering = ['first_name', 'last_name']


class Collection(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ['name']


class Order(models.Model):
    PAYMENT_STATUS_PENDING = 'PENDING'
    PAYMENT_STATUS_COMPLETE = 'COMPLETED'
    PAYMENT_STATUS_FAIL = 'FAILED'

    PAYMENT_STATUS = [
        (PAYMENT_STATUS_PENDING, 'Pending'),
        (PAYMENT_STATUS_COMPLETE, 'Completed'),
        (PAYMENT_STATUS_FAIL, 'Failed'),
    ]

    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(
        max_length=255, choices=PAYMENT_STATUS, default=PAYMENT_STATUS_PENDING)
    customer = models.ForeignKey(to='Customer', on_delete=models.PROTECT)


class OrderItem(models.Model):
    product = models.ForeignKey(to='Product', on_delete=models.PROTECT, related_name='orderitems')
    quantity = models.PositiveIntegerField()
    order = models.ForeignKey(to='Order', on_delete=models.PROTECT)
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)


class Cart(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)


class CartItem(models.Model):
    cart = models.ForeignKey(to='Cart', on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(to='Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    class Meta:
        unique_together = [['cart', 'product']]


class Promotion(models.Model):
    description = models.CharField(max_length=255)
    discount = models.DecimalField(max_digits=6, decimal_places=2)


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    name = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField(auto_now_add=True)
