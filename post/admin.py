from django.db import models
from parler.models import TranslatableModel, TranslatedFields
from django.contrib import admin
from parler.admin import TranslatableAdmin
from .models import Yangiliklar,Image,Videolar,OAV,Tabrik,Elon,Turi,Korporativ,Intraktiv


class ImageInline(admin.TabularInline):
    model = Image

@admin.register(Intraktiv)
class IntraktivAdmin(TranslatableAdmin):
    list_display = ('id', 'nomi', 'date')  # 'nomi' translyatsiya maydonidan keladi
    readonly_fields = ('date',)  # Faqat o'qish uchun
    fieldsets = (
        (None, {
            'fields': ('nomi', 'image', 'file', 'matn', 'date'),
        }),
    )
    def has_module_permission(self, request):
        return getattr(request.user, 'role', None) in ['admin', 'hodim']

    def has_view_permission(self, request, obj=None):
        return getattr(request.user, 'role', None) in ['admin', 'hodim']

    def has_change_permission(self, request, obj=None):
        return getattr(request.user, 'role', None) in ['admin', 'hodim']

    def has_delete_permission(self, request, obj=None):
        return getattr(request.user, 'role', None) in ['admin', 'hodim']

@admin.register(Turi)
class TurAdmin(admin.ModelAdmin):
    def has_module_permission(self, request):
        return getattr(request.user, 'role', None) in ['admin', 'hodim']

    def has_view_permission(self, request, obj=None):
        return getattr(request.user, 'role', None) in ['admin', 'hodim']

    def has_change_permission(self, request, obj=None):
        return getattr(request.user, 'role', None) in ['admin', 'hodim']

    def has_delete_permission(self, request, obj=None):
        return getattr(request.user, 'role', None) in ['admin', 'hodim']


class TurAdmin(TranslatableAdmin):
    list_display = ['nomi']
    
    fields = ['nomi']  # Bu joyda kiritish uchun kerakli maydonlarni qo'shing

    def has_module_permission(self, request):
        return getattr(request.user, 'role', None) in ['admin', 'jurnalist']

    def has_view_permission(self, request, obj=None):
        return getattr(request.user, 'role', None) in ['admin', 'jurnalist']

    def has_change_permission(self, request, obj=None):
        return getattr(request.user, 'role', None) in ['admin', 'jurnalist']

    def has_delete_permission(self, request, obj=None):
        return getattr(request.user, 'role', None) in ['admin', 'jurnalist']

    def has_add_permission(self, request):
        return getattr(request.user, 'role', None) in ['admin', 'jurnalist']

@admin.register(Korporativ)
class KorportaivAdmin(TranslatableAdmin):
    list_display = ('nomi', 'date')
    list_filter = ('date',)
    ordering = ('-date',)
    readonly_fields = ('date',)

    def has_module_permission(self, request):
        return getattr(request.user, 'role', None) in ['admin', 'hodim']

    def has_view_permission(self, request, obj=None):
        return getattr(request.user, 'role', None) in ['admin', 'hodim']

    def has_change_permission(self, request, obj=None):
        return getattr(request.user, 'role', None) in ['admin', 'hodim']

    def has_delete_permission(self, request, obj=None):
        return getattr(request.user, 'role', None) in ['admin', 'hodim']

    def has_add_permission(self, request):
        return getattr(request.user, 'role', None) in ['admin', 'hodim']

#jurnalist

@admin.register(Yangiliklar)
class YangiliklarAdmin(TranslatableAdmin):
    inlines = [ImageInline]
    list_display = ('sarlavha', 'date', 'main_image')
    list_filter = ('date',)
    ordering = ('-date',)
    readonly_fields = ('date',)

    def has_module_permission(self, request):
        return getattr(request.user, 'role', None) in ['admin', 'jurnalist']

    def has_view_permission(self, request, obj=None):
        return getattr(request.user, 'role', None) in ['admin', 'jurnalist']

    def has_change_permission(self, request, obj=None):
        return getattr(request.user, 'role', None) in ['admin', 'jurnalist']

    def has_delete_permission(self, request, obj=None):
        return getattr(request.user, 'role', None) in ['admin', 'jurnalist']

    def has_add_permission(self, request):
        return getattr(request.user, 'role', None) in ['admin', 'jurnalist']

@admin.register(Videolar)
class VideolarAdmin(TranslatableAdmin):
    list_display = ('sarlavha', 'date')
    list_filter = ('date',)
    ordering = ('-date',)
    readonly_fields = ('date',)

    def has_module_permission(self, request):
        return getattr(request.user, 'role', None) in ['admin', 'jurnalist']

    def has_view_permission(self, request, obj=None):
        return getattr(request.user, 'role', None) in ['admin', 'jurnalist']

    def has_change_permission(self, request, obj=None):
        return getattr(request.user, 'role', None) in ['admin', 'jurnalist']

    def has_delete_permission(self, request, obj=None):
        return getattr(request.user, 'role', None) in ['admin', 'jurnalist']

    def has_add_permission(self, request):
        return getattr(request.user, 'role', None) in ['admin', 'jurnalist']

@admin.register(OAV)
class OavAdmin(TranslatableAdmin):
    list_display = ('sarlavha', 'date')
    list_filter = ('date',)
    ordering = ('-date',)
    readonly_fields = ('date',)

    def has_module_permission(self, request):
        return getattr(request.user, 'role', None) in ['admin', 'jurnalist']

    def has_view_permission(self, request, obj=None):
        return getattr(request.user, 'role', None) in ['admin', 'jurnalist']

    def has_change_permission(self, request, obj=None):
        return getattr(request.user, 'role', None) in ['admin', 'jurnalist']

    def has_delete_permission(self, request, obj=None):
        return getattr(request.user, 'role', None) in ['admin', 'jurnalist']

    def has_add_permission(self, request):
        return getattr(request.user, 'role', None) in ['admin', 'jurnalist']

@admin.register(Tabrik)
class TabrikAdmin(TranslatableAdmin):
    list_display = ('sarlavha', 'date')
    list_filter = ('date',)
    ordering = ('-date',)
    readonly_fields = ('date',)

    def has_module_permission(self, request):
        return getattr(request.user, 'role', None) in ['admin', 'jurnalist']

    def has_view_permission(self, request, obj=None):
        return getattr(request.user, 'role', None) in ['admin', 'jurnalist']

    def has_change_permission(self, request, obj=None):
        return getattr(request.user, 'role', None) in ['admin', 'jurnalist']

    def has_delete_permission(self, request, obj=None):
        return getattr(request.user, 'role', None) in ['admin', 'jurnalist']

    def has_add_permission(self, request):
        return getattr(request.user, 'role', None) in ['admin', 'jurnalist']

@admin.register(Elon)
class ElonAdmin(TranslatableAdmin):
    list_display = ('sarlavha', 'date')
    list_filter = ('date',)
    ordering = ('-date',)
    readonly_fields = ('date',)

    def has_module_permission(self, request):
        return getattr(request.user, 'role', None) in ['admin', 'jurnalist']

    def has_view_permission(self, request, obj=None):
        return getattr(request.user, 'role', None) in ['admin', 'jurnalist']

    def has_change_permission(self, request, obj=None):
        return getattr(request.user, 'role', None) in ['admin', 'jurnalist']

    def has_delete_permission(self, request, obj=None):
        return getattr(request.user, 'role', None) in ['admin', 'jurnalist']

    def has_add_permission(self, request):
        return getattr(request.user, 'role', None) in ['admin', 'jurnalist']
