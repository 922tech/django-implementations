import factory
# from django.contrib.auth.models import User
from shop.models import Product, ProductCategory, ProductBrand


class ProductCategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ProductCategory
    title = ''
    slug = ''
    is_active = True
    is_delete = False

class ProductBrandFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ProductBrand
    title = 'brand1'
    is_active = True

class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product
    title = "x"
    category = factory.SubFactory(ProductCategoryFactory)
    image = ""
    brand = factory.SubFactory(ProductBrandFactory)
    price = "x"
    short_description = "x"
    description = "x"
    slug = "x"
    is_active = True
    is_deleted = False