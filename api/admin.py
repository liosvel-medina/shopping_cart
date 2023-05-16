from django.contrib import admin
from api import models

# Register your models here.


@admin.register(models.Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ['name', 'hex_value']
    list_display_links = list_display


@admin.register(models.Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = list_display


@admin.register(models.Cap)
class CapAdmin(admin.ModelAdmin):
    list_display = ['main_color', 'brand', 'price', 'is_deleted']
    list_display_links = list_display
    filter_horizontal = ['secondary_colors']


class CompositionTabInline(admin.TabularInline):
    model = models.Composition


@admin.register(models.TShirt)
class TShirtAdmin(admin.ModelAdmin):
    list_display = ['main_color', 'brand',
                    'price', 'size', 'sizing', 'is_deleted']
    list_display_links = list_display
    filter_horizontal = ['secondary_colors']
    inlines = [CompositionTabInline]


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['main_color', 'brand', 'price', 'is_deleted']
    list_display_links = list_display
    filter_horizontal = ['secondary_colors']
