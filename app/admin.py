from django.contrib import admin
from app.models import Todo
# Register your models here.

class TodoAdmin(admin.ModelAdmin):
    list_display = (
        "title", 
        "user", 
        "status",
        'priority', 
        'updated_date',
        'created_date',
        )
    list_filter = ("user", )
    search_fields = ("title__startswith", )
    
admin.site.register(Todo, TodoAdmin)