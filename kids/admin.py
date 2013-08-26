# from tinymce.widgets import TinyMCE
from django.contrib import admin
from kids.models import *
from sorl.thumbnail.admin import AdminImageMixin
from django import forms
from datetime import *


class GroupAdminForm(forms.ModelForm):
    groupclasses = (
          ('baby', 'baby'),
          ('dreumes', 'dreumes'),
          ('peuter', 'peuter'),
          )
    groupclass = forms.ChoiceField(label='Groepsklasse', choices=(groupclasses))

    class Meta:
        model = Group


class GroupAdmin(AdminImageMixin, admin.ModelAdmin):
    form = GroupAdminForm

    pass

admin.site.register(Group, GroupAdmin)

class KidAdmin(AdminImageMixin, admin.ModelAdmin):
    list_display = ('name', 'fullname', 'age', 'slug')
    filter_horizontal = ('parents',)
    pass

admin.site.register(Kid, KidAdmin)


class ParentAdminForm(forms.ModelForm):
    sex_classes = (
          ('vader', 'vader'),
          ('moeder', 'moeder'),
          )
    sex = forms.ChoiceField(label='Groepsklasse', choices=(sex_classes))

    class Meta:
        model = Parent


class ParentAdmin(AdminImageMixin, admin.ModelAdmin):
    list_display = ('name', 'fullname')
    form = ParentAdminForm
    pass

admin.site.register(Parent, ParentAdmin)


class CaretakerAdmin(AdminImageMixin, admin.ModelAdmin):
    list_display = ('name', 'fullname')
    pass

admin.site.register(Caretaker, CaretakerAdmin)
