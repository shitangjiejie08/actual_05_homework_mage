from django.contrib import admin

# Register your models here.


from .models import users
from .utils import mycrypt

class usersAdmin(admin.ModelAdmin):
    list_display = ('name','age','tel')
    search_fields = ('name','age','tel')
    list_filter = ('name','age','tel')    

    def save_model(self,request,obj,form,change):
        obj.passwd = mycrypt(obj.passwd)
        super(usersAdmin,self).save_model(request,obj,form,change)

admin.site.register(users,usersAdmin)
