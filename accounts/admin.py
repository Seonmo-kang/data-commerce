from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group

from .forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
#For using customized User model, we need a funtion : get_user_model
User = get_user_model()


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'firstName', 'lastName','is_seller' , 'is_active', 'is_superuser', 'date_joined', 'last_login')
    list_display_links = ('email',)
    list_filter = ('is_superuser', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (('Personal info'), {'fields': ('firstName', 'lastName','is_seller')}),
        (('Permissions'), {'fields': ('is_active', 'is_superuser',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'firstName', 'password1', 'password2')}
         ),
    )
    search_fields = ('email','firstName','lastName')
    ordering = ('-date_joined',)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)