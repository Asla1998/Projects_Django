from django.contrib import admin
from .models import donor,receiver,blood_req,blog

admin.site.register(donor)
admin.site.register(receiver)
admin.site.register(blood_req)
admin.site.register(blog)

# Register your models here.
