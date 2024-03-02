from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Questions #Answer

# Register your models here.

class PostAdmin(SummernoteModelAdmin):
    summernote_fields ='__all__'
    list_display=['author','draft','created_at']
    list_filter=['author','created_at']
    search_fields=['question','author']



admin.site.register(Questions,PostAdmin)
# admin.site.register(Answer)