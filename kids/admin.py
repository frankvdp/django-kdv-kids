from django.contrib import admin
from kids.models import *
from sorl.thumbnail.admin import AdminImageMixin
from django import forms
from datetime import *


class GroupAdmin(AdminImageMixin, admin.ModelAdmin):
    """ 
      GroupAdmin, actually only for supplying AdminImageMixin
    """
    pass

admin.site.register(Group, GroupAdmin)


class KidAdmin(AdminImageMixin, admin.ModelAdmin):
    list_display = ('name', 'fullname', 'age', 'slug')
    filter_horizontal = ('parents',)
    pass

admin.site.register(Kid, KidAdmin)


class ParentAdmin(AdminImageMixin, admin.ModelAdmin):
    list_display = ('name', 'fullname')
    pass

admin.site.register(Parent, ParentAdmin)


class CaretakerAdmin(AdminImageMixin, admin.ModelAdmin):
    list_display = ('name', 'fullname')
    pass

admin.site.register(Caretaker, CaretakerAdmin)
