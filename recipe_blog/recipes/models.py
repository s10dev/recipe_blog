from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Recipe(models.Model):
    """Recipe structure"""
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='Автор'
        )
    title = models.CharField(max_length=40, verbose_name='Название')
    picture = models.ImageField(blank=True, null=True)
    text = models.TextField(max_length=100, blank=True, null=True)
    components = models.ManyToManyField('Component')
    tag = models.CharField()
    cooking_time = models.DateTimeField()
    slug = models.SlugField()

    class Meta:
        db_table = 'recipes'


class Component(models.Model):
    """Component structure from recipe"""
    title = models.CharField(max_length=50)
    dimension = models.CharField(choices=('шт', 'кусок', 'г'))

    class Meta:
        db_table = 'components'


class Component_quantity(models.Model):
    """Table linking quantity and recipe with component together"""
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    compotent = models.ForeignKey(Component, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    class Meta:
        db_table = 'quantity_and_recipe_linking_table'