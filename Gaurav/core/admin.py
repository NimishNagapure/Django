from django.contrib import admin

# Register your models here.
from core.models import CheckList,CheckListItem,Book

admin.site.register(CheckListItem)
admin.site.register(CheckList)
admin.site.register(Book)
