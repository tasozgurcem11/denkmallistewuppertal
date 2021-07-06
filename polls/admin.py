from django.contrib import admin
from django.http import HttpResponse, HttpResponseRedirect, request # noqa: 401
from .models import Data
import csv


def false(*args, **kwargs):
    return False




class UserInfo(admin.ModelAdmin):

    list_display = ("address", "created_at")
    
    readonly_fields = [
       "address", "created_at"
    ]

    has_delete_permission = false
    has_add_permission = false
    log_change = false
    message_user = false

admin.site.register(Data, UserInfo)

admin.site.site_header = "Hallo Denkmal Liste Team!"
admin.site.site_title = "Denkmal Liste Admin"
admin.site.index_title = "Datenmanagement"


