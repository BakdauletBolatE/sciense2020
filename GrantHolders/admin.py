from django.contrib import admin
from .models import GrantHolders
from django import forms
# Register your models here.
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class GrantHoldersForm(forms.ModelForm):
    ways_project = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = GrantHolders
        fields = '__all__'

class GrantHoldersAdmin(admin.ModelAdmin):
    form = GrantHoldersForm
admin.site.register(GrantHolders,GrantHoldersAdmin)