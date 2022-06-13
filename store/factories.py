import factory
from factory.django import DjangoModelFactory

from store.models import Product, Collection


class UserFactory(DjangoModelFactory):
    class Meta:
        model = Collection

    name = factory.Faker("first_name")
    description = factory.Faker("paragra")