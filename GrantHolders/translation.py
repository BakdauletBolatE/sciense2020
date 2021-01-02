from modeltranslation.translator import register,TranslationOptions
from .models import GrantHolders

@register(GrantHolders)
class GrantHoldersTranslationOptions(TranslationOptions):
    fields = ('project_name','purpose_project','ways_project','expected_result','novelty_scientific')