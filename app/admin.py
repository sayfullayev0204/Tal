from django.contrib import admin
from .models import Tashriflar,Murojatlar
from datetime import date

@admin.register(Tashriflar)
class VisitAdmin(admin.ModelAdmin):
    list_display = ('ip_address', 'visit_date', 'today_visitors_count')

    def today_visitors_count(self, obj):
        return Tashriflar.objects.filter(visit_date=date.today()).count()
    
    today_visitors_count.short_description = "Bugungi tashriflar soni"

    # Foydalanuvchi rollari uchun ruxsatni cheklash
    def has_module_permission(self, request):
        return getattr(request.user, 'role', None) in ['admin']

    def has_view_permission(self, request, obj=None):
        return getattr(request.user, 'role', None) in ['admin']

    def has_change_permission(self, request, obj=None):
        return getattr(request.user, 'role', None) in ['admin']

    def has_delete_permission(self, request, obj=None):
        return getattr(request.user, 'role', None) in ['admin']

    def has_add_permission(self, request):
        return getattr(request.user, 'role', None) in ['admin']

@admin.register(Murojatlar)
class MurojatlarAdmin(admin.ModelAdmin):
    list_display = ('name', 'title')

    # Foydalanuvchi rollari uchun ruxsatni cheklash
    def has_module_permission(self, request):
        return getattr(request.user, 'role', None) in ['admin']

    def has_view_permission(self, request, obj=None):
        return getattr(request.user, 'role', None) in ['admin']

    def has_change_permission(self, request, obj=None):
        return getattr(request.user, 'role', None) in ['admin']

    def has_delete_permission(self, request, obj=None):
        return getattr(request.user, 'role', None) in ['admin']

    def has_add_permission(self, request):
        return getattr(request.user, 'role', None) in ['admin']
