# Author: Sean Chen, sean@appar.com.tw
# Date: 2023/12/05

from django.apps import apps
from django.contrib import admin


def _all_fields_in_model(app_label, model_name):
    model = apps.get_model(app_label=app_label, model_name=model_name)
    fields = model._meta.concrete_fields
    field_names = [field.name for field in fields]
    return field_names


def register_all_fields_of_model(app_name, model_name_camel, base_class=None):
    """
    Dynamically create admin class and register to django admin for a certain model class
    https://stackoverflow.com/questions/15247075/how-can-i-dynamically-create-derived-classes-from-a-base-class
    https://stackoverflow.com/questions/547829/how-to-dynamically-load-a-python-class
    """

    # dynamically create "XXXAdmin" class from model, second param is parent class
    if base_class is None:
        base_class = admin.ModelAdmin
    dynamic_admin_class = type(f"{model_name_camel}Admin", (base_class, ), {})

    # assigning class property
    dynamic_admin_class.list_display = _all_fields_in_model(app_name, model_name_camel)

    # dynamically import model
    management_module = __import__(app_name)
    models_module = getattr(management_module, 'models')
    model_class = getattr(models_module, model_name_camel)

    admin.site.register(model_class, admin_class=dynamic_admin_class)
    return dynamic_admin_class

# Register your models here.
def register_all_models_of_app(app_name):
    all_models = apps.get_models()
    for model in all_models:
        if model._meta.app_label == app_name:
            print(model.__name__)
            register_all_fields_of_model(app_name, model.__name__)