from django.contrib import admin
from .models import GrantHolders,Like,Subject
from django import forms
from modeltranslation.admin import TranslationAdmin
# Register your models here.
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class GrantHoldersForm(forms.ModelForm):
    ways_project_ru = forms.CharField(label="Жоба мақсатына жету жолдары(рус)",widget=CKEditorUploadingWidget())
    expected_result_ru = forms.CharField(label="Күтілетін нәтиже(рус)",widget=CKEditorUploadingWidget())
    novelty_scientific_ru = forms.CharField(label="Ғылыми жұмыстың жаңалығы(рус)",widget=CKEditorUploadingWidget())
    ways_project_en = forms.CharField(label="Жоба мақсатына жету жолдары(en)",widget=CKEditorUploadingWidget())
    expected_result_en = forms.CharField(label="Күтілетін нәтиже(en)",widget=CKEditorUploadingWidget())
    novelty_scientific_en = forms.CharField(label="Ғылыми жұмыстың жаңалығы(en)",widget=CKEditorUploadingWidget())
    ways_project_kk = forms.CharField(label="Жоба мақсатына жету жолдары(каз)",widget=CKEditorUploadingWidget())
    expected_result_kk = forms.CharField(label="Күтілетін нәтиже(каз)",widget=CKEditorUploadingWidget())
    novelty_scientific_kk = forms.CharField(label="Ғылыми жұмыстың жаңалығы(каз)",widget=CKEditorUploadingWidget())
    class Meta:
        model = GrantHolders
        fields = '__all__'

class GrantHoldersAdmin(TranslationAdmin):
    form = GrantHoldersForm
    prepopulated_fields = {"slug": ("name",)}
admin.site.register(GrantHolders,GrantHoldersAdmin)
admin.site.register(Subject)
admin.site.register(Like)