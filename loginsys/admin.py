from django.contrib import admin
from loginsys.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ( 'username', 'first_name', 'last_name', 'email','registration_time','last_login')


admin.site.register(User, UserAdmin)

# Register your models here.
