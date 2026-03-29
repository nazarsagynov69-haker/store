from .models import *
from modeltranslation.translator import TranslationOptions,register

@register(Job)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('owner','description')



@register(Application)
class ProductCategoryTranslationOptions(TranslationOptions):
    fields = ('job',)


@register(Resume)
class ProductCategoryTranslationOptions(TranslationOptions):
    fields = ('user',)