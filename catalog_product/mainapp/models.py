from django.db import models


class ProductCategory(models.Model):
    name = models.CharField('имя', max_length=64)
    description = models.TextField('описание', blank=True)
    short_desc = models.CharField(
        'краткое описание', max_length=200, blank=True)
    is_active = models.BooleanField('активность', db_index=True, default=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'категория продукта'
        verbose_name_plural = 'категории продукта'
        ordering = ['name']


class Product(models.Model):
    category = models.ManyToManyField(
        ProductCategory, default=None)
    name = models.CharField('имя', max_length=64)
    add_dt = models.DateTimeField('время', auto_now_add=True)
    price = models.DecimalField(
        'цена', max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField('количество на складе', default=0)
    is_active = models.BooleanField('активность', db_index=True, default=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ['name']
