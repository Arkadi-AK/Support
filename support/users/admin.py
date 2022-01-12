from django.contrib import admin

from users.models import User, UserGroup


class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'group', 'support')
    # list_display_links = ('name',)


class UserGroupAdmin(admin.ModelAdmin):
    list_display = ('name',)
    # list_display_links = ('name',)


admin.site.register(User, UserAdmin)
admin.site.register(UserGroup, UserGroupAdmin)
