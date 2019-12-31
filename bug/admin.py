from django.contrib import admin
from bug.models import User, EmailAddress

class EmailInline(admin.TabularInline):
    model = EmailAddress

class UserAdmin(admin.ModelAdmin):
    inlines = [EmailInline]


# Register your models here.
admin.site.register(User, UserAdmin)
