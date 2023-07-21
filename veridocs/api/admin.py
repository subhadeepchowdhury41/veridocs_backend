from django.contrib import admin
from .models import Form, Template, User

# Register your models here.
admin.site.register(Form)
admin.site.register(User)
admin.site.register(Template)