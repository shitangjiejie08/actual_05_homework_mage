# enconding: utf-8
from django.contrib import admin

# Register your models here.
from  .models import User2
from utils.crypt import CryptUtils



class User2Admin(admin.ModelAdmin):
    list_display = ('username', 'age','tel')
    search_fields = ('username', 'age','tel')
    list_filter = ('username','age', 'tel')

    def save_model(self, request, obj, form, change):   #####调用models password md5 加密
        obj.password = CryptUtils.md5(obj.password)
        super(User2Admin, self).save_model(request, obj, form, change)

admin.site.register(User2, User2Admin)