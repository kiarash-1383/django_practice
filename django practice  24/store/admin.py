from .models import Product
from django.contrib import admin

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category', 'is_active']
    list_display_links = ['id', 'name']

    fieldsets = (
        ('Identification', {
            'fields': ('name', 'price', 'is_active')
        }),
        ('Details', {
            'classes': ('collapse',),
            'fields': ( 'category' , 'company')
        }),
    )

    list_editable = ('is_active',)

    actions = ['make_inactive']

    def make_inactive(self, request, queryset):
        updated_count = queryset.update(is_active=False)

    make_inactive.short_description = 'Make inactive'
  
        
        