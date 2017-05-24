from django.contrib import admin
from .models import Activity, Feeling, Memo, Report, Time
# Register your models here.
@admin.register(Activity, Feeling, Memo, Report, Time)
class AuthorAdmin(admin.ModelAdmin):
    pass
