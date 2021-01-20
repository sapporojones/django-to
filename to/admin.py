from django.contrib import admin
from .models import MasterList

# Register your models here.


class MasterListAdmin(admin.ModelAdmin):
    fields = (
        "name",
        "url",
        "category",
    )


admin.site.register(MasterList, MasterListAdmin)
