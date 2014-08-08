from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.admin import AdminSite
from django.conf import settings

from models import *

class GalleryInline(admin.StackedInline):
    model = Gallery
    extra = 5

class EventAdmin(admin.ModelAdmin):
  ordering = ('-date_of_event',)
  list_display = ('title', 'category', 'venue',)
  list_filter = ['category',]
  search_fields = ['title', 'description', 'organiser',]
  date_hierarchy = 'date_of_event'
  fieldsets = [
      ('Basics', {'fields': ['title', 'category', 'description',],}),
      ('Person incharge', {'fields': ['organiser', ],}),
      ('When and Where', {'fields': ['venue', 'date_of_event',],}),
  ]
  inlines = [GalleryInline]

class ProductAdmin(admin.ModelAdmin):
  ordering = ('-launched',)
  list_display = ('name', 'category', 'launched')
  list_filter = ['category',]
  search_fields = ['name', 'description',]
  date_hierarchy = 'launched'
  fieldsets = [
      ('Basics', {'fields': 
          ['name', 'category', 'description', 'picture', 'launched',]
        }),
  ]


admin.site.register(Event, EventAdmin)
admin.site.register(Product, ProductAdmin)