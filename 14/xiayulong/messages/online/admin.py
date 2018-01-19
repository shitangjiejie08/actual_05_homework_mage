from django.contrib import admin

# Register your models here.

from .models import message2
class message2Admin(admin.ModelAdmin):
    list_display = ('username','title')
    search_fields = ('username','title','publish_date')
    list_filter = ('username','title','content','publish_date')

admin.site.register(message2,message2Admin)