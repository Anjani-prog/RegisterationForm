from django.db import models
from django_datatables_view.base_datatable_view import BaseDatatableView
from django.apps import apps
from django.utils.html import escape
from django.contrib.auth.models import User


def get_model_from_any_app(model_name):
    for app_config in apps.get_app_configs():
        try:
            model = app_config.get_model(model_name)
            return model
        except LookupError:
            pass
    return None


class Users(models.Model, BaseDatatableView):
    class Meta:
        # db_table = '"dashboard_user"'
        db_table = '"auth_user"'

    # Existing fields
    username = models.CharField(max_length=128, null=True)
    first_name = models.CharField(max_length=128, null=True)
    last_name = models.CharField(max_length=128, null=True)
    email = models.CharField(max_length=128, null=True)
    phone = models.CharField(max_length=15, null=True)
    file = models.FileField(upload_to='documents/%Y/%m/%d')
    page_title = 'Manage Users'
    listable = {'Username', 'First Name','Last Name','Email','Phone','File'}
    columns = ['id', 'username','first_name','last_name','email','phone','file']
    order_columns = ['id', 'username','first_name','last_name','email','phone','file']
    max_display_length = 500
    # class_view_name = 'GetAjaxViewUser'

    table_name = "auth_user"

    model_name = "Users"

    # acl_key = "dashboard.admin.users"

    # parameter_array = { 'acl_key' : 'dashboard.users' }

    show_toolbar = {"view": "Show", "add": "Add", "edit": "Edit",
                    "publish": "Publish", "unpublish": "Unpublish",
                    "trash": "Trash", "restore": "Restore", "forcedelete": "Force Delete"}

    routes = {"add_route": "adduser", "edit_route": "edituser", "view_route": "viewuser"}



