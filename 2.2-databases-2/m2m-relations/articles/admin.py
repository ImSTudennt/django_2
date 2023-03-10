from django.contrib import admin

from .models import Article, Tag, Scope
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet



class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        checked = 0
        for form in self.forms:

            if form.cleaned_data.get('is_main') is True:
                checked += 1

        if checked > 1:
            raise ValidationError('Основным может быть только один раздел')

        elif checked == 0:
            raise ValidationError('Укажите основной раздел')

        return super().clean()



class ScopeInline(admin.TabularInline):
    model = Scope
    extra = 3
    formset = ScopeInlineFormset

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'text', 'published_at', 'image']
    inlines = [ScopeInline,]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

