from django.contrib import admin
from .models import GrantHolders,Like,Subject
from django import forms
# Register your models here.
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class GrantHoldersForm(forms.ModelForm):
    ways_project = forms.CharField(widget=CKEditorUploadingWidget())
    expected_result = forms.CharField(widget=CKEditorUploadingWidget())
    novelty_scientific = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = GrantHolders
        fields = '__all__'

class GrantHoldersAdmin(admin.ModelAdmin):
    form = GrantHoldersForm
    prepopulated_fields = {"slug": ("name",)}
admin.site.register(GrantHolders,GrantHoldersAdmin)
admin.site.register(Subject)
admin.site.register(Like)