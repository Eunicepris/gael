
# Register your models here.
# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models

from django.utils.safestring import mark_safe

class PageAdmin(admin.ModelAdmin):

    list_display = (
        'titre',
        'nom',
        'status',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'status',
        'date_add',
        'date_upd',
    )

    search_fields = ('titre',)
    actions = ('active', 'desactive') 
    def active(self, request, queryset):
        queryset.update(status=True)
        self.message_user(request, 'Les Elements selectionnés on été desactivité avec Succes')
    active.short_description = 'Activer les  Elements selectionnés'

    def desactive(self, request, queryset):
        queryset.update(status=False)
        self.message_user(request, 'Les Elements selectionnés on été desactivité avec Succes')
    desactive.short_description = 'Desactiver les  Elements selectionnés'
    ordering = ('titre',)
    date_hierarchy = ('date_add')
                    
    fieldsets = [
        ('les informations de header', {'fields': ['titre', 'nom', 'content', 'adresse', 'contact', 'mail',]}),
        ('les champs standards', {'fields': ['status',]}),
    ]

class CommentaireAdmin(admin.ModelAdmin):

    list_display = (
        'nom',
        'email',
        'status',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'status',
        'date_add',
        'date_upd',
    )

    search_fields = ('nom',)
    actions = ('active', 'desactive') 
    def active(self, request, queryset):
        queryset.update(status=True)
        self.message_user(request, 'Les Elements selectionnés on été desactivité avec Succes')
    active.short_description = 'Activer les  Elements selectionnés'

    def desactive(self, request, queryset):
        queryset.update(status=False)
        self.message_user(request, 'Les Elements selectionnés on été desactivité avec Succes')
    desactive.short_description = 'Desactiver les  Elements selectionnés'
    ordering = ('nom',)
    date_hierarchy = ('date_add')
                        
    fieldsets = [
        ('les informations de header', {'fields': ['nom', 'email', 'message', ]}),
        ('les champs standards', {'fields': ['status',]}),
    ]

def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Page, PageAdmin)
_register(models.Commentaire, CommentaireAdmin)
