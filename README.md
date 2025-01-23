# Django Admin Autogen

Dynamically register all fields of a model or all models in an app, in Django Admin.

## Installation

```shell
pip install django_admin_autogen
```

## Usage

Import

```python
from django_admin_autogen.autogen.admin import register_all_fields_of_model
from django_admin_autogen.autogen.admin import register_all_models_of_app
```

Functions:

`register_all_fields_of_model`

![All fields included](https://i.imgur.com/uWW4JiP.png)

`register_all_models_of_app`

![Alt text](https://i.imgur.com/VYRQyUA.png)

---

# How to?

### Register a model, with all fields included

```python
from django_admin_autogen.autogen.admin import register_all_fields_of_model

fast_part_note_class = register_all_fields_of_model('<app_name>', '<ModelName>')
```

If your model admin requires using custom base class, you 

```python
fast_part_note_class = register_all_fields_of_model('<app_name>', '<ModelName>', base_class=<YourCustomBaseClass>)
```

Override the default behavior by setting custom properties on the `YourCustomBaseClass` class.

```python
# YourCustomBaseClass 
quotation.field_to_group_by = 'currency__name'
quotation.field_to_sum = 'total_price'

class Media:
    js = (
        'js/add_button.js',
    )

fast_part_note_class.Media = Media
```

### Register all models in an app

Register all models of an app in Django Admin, with all of their fields included

```python
from django_admin_autogen.autogen.admin import register_all_models_of_app

register_all_models_of_app('<app_name>')
```

### Make list display only certain fields

```
a_model_registered = register_all_fields_of_model('<app_name>', '<ModelName>')

a_model_registered = ['id', 'field_a', 'field_b', 'field_c']

```


### Add inline

```python
class ChatSystemPromptl10nInline(admin.TabularInline):
    model = apps.get_model('openai_core', 'ChatSystemPromptl10n')
    extra = 1

chat_system_prompt.inlines = [ChatSystemPromptl10nInline]
```



