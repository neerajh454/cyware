from django.contrib import admin

# Register your models here.

from usersearch.models import UserDetails, Hits


@admin.register(UserDetails)
class UserDetailsAdmin(admin.ModelAdmin):
    search_fields = ('username', 'email', )
    readonly_fields = ('image_tag',)

@admin.register(Hits)
class HitsAdmin(admin.ModelAdmin):
    search_fields = ('key', 'value', )
    list_display = ('key', 'value', 'created_at')