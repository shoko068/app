from django.contrib import admin
from .models import Category, Pref, Review, Tag, Profile
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_l', 'name')
    list_display_links = ('category_l',)
    list_editable = ('name',)


@admin.register(Pref)
class PrefAdmin(admin.ModelAdmin):
    list_display = ('pref', 'name')
    list_display_links = ('pref',)
    list_editable = ('name',)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('shop_id', 'shop_name', 'user', 'score',"info")
    list_display_links = ('shop_name',)
    list_editable = ('score',"info")


class ProfileInline(admin.StackedInline):
    model = Profile
    max_num = 1
    can_delete = False


class UserAdmin(AuthUserAdmin):
    inlines = [ProfileInline]


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
