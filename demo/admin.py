from django.contrib import admin
from dummy.demo.models import Building, BuildingImage, Location

class ImageInLine(admin.StackedInline):
    model = BuildingImage

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ['name']
    list_display = ('name', 'location')
    inlines = [
        ImageInLine
    ]

class LocAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Building, PostAdmin)
admin.site.register(Location, LocAdmin)