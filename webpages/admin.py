from django.contrib import admin
from django.utils.html import format_html
from  .models import Slider,Team
# Register your models here.

class TeamAdmin(admin.ModelAdmin):
    def myphoto(self,object):
        return format_html('<img src={} width="40"/>'.format(object.photo.url))
    list_display = ('id','first_name','role','created_date','myphoto')
    list_display_links = ('id','first_name')
    search_fields = ('first_name','role')
    list_filter = ('role',)


admin.site.register(Slider)
admin.site.register(Team,TeamAdmin)
