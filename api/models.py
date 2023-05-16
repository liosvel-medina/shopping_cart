from django.db import models
from colorfield.fields import ColorField

# Create your models here.


class Color(models.Model):
    name = models.CharField(max_length=32)
    hex_value = ColorField(format='hex', default='#000000')

    def __str__(self) -> str:
        return f'{self.name} ({self.hex_value})'


class Brand(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f'{self.name}'


class Product(models.Model):
    main_color = models.ForeignKey(
        Color, on_delete=models.RESTRICT, related_name='%(app_label)s_%(class)s')
    secondary_colors = models.ManyToManyField(Color, blank=True)
    brand = models.ForeignKey(Brand, on_delete=models.RESTRICT)
    created_date = models.DateField()
    image = models.ImageField(
        upload_to='images/products', null=True, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    initial_stock = models.IntegerField()
    current_stock = models.IntegerField()
    is_deleted = models.BooleanField(default=False)
    deleted_date = models.DateField(null=True, blank=True)

    def __str__(self) -> str:
        # prduct_type + brand + colors + year + size + composition
        return f'{self.brand}-{self.main_color.name}-{self.created_date.year}'


class Cap(Product):
    logo_color = models.ForeignKey(
        Color, on_delete=models.RESTRICT, null=True, blank=True, related_name='caps')

    class Meta:
        verbose_name = 'cap'
        verbose_name_plural = 'caps'

    def __str__(self) -> str:
        return f'{self._meta.verbose_name}-{super().__str__()}'


size_choices = [
    ('xxs', 'XXS'),
    ('xs', 'XS'),
    ('s', 'S'),
    ('m', 'M'),
    ('l', 'L'),
    ('xl', 'XL'),
    ('xxl', 'XXL'),
]

material_choices = [
    (1, 'Cotton'),   # algodón
    (2, 'Linen'),   # lino
    (3, 'Hemp'),   # cáñamo
    (4, 'Polyester'),   # poliéster
    (5, 'Nylon'),   # nylon
    (6, 'Wool'),   # lana
    (7, 'Silk'),   # seda
]


def getMaterial(value):
    _material = next(y for (x, y) in material_choices if x == value)
    return _material


sizing_choices = [
    ('m', 'Male'),  # Hombre
    ('f', 'Female'),  # Mujer
    ('u', 'Unisex'),  # Unisex
]


class TShirt(Product):
    size = models.CharField(max_length=3, choices=size_choices)
    sizing = models.CharField(max_length=2, choices=sizing_choices)
    has_sleeves = models.BooleanField(default=False)

    class Meta:
        verbose_name = 't-shirt'
        verbose_name_plural = 't-shirts'

    def __str__(self) -> str:
        _composition = [
            f'{getMaterial(item.material)}{item.percent}' for item in self.composition_set.all()]
        _composition_str = ''
        for item in _composition:
            _composition_str += f'{item}-'
        _composition_str = _composition_str[:-1]
        _size = next(y for (x, y) in size_choices if x == self.size)
        return f'{self._meta.verbose_name}-{super().__str__()}-{_size}-{_composition_str}'


class Composition(models.Model):
    tshirt = models.ForeignKey(TShirt, on_delete=models.CASCADE)
    material = models.IntegerField(choices=material_choices)
    percent = models.FloatField()
