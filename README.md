# Django Admin Autogen

Dynamically register all fields of a model or all models in an app, in Django Admin.

## Installation

```shell
pip install django_admin_autogen
```

## Usage

Import

```python
from django_admin_autogen.admin import register_all_fields_of_model
from django_admin_autogen.admin import register_all_models_of_app
```

register_all_fields_of_model

![All fields included](https://i.imgur.com/uWW4JiP.png)

register_all_models_of_app

![Alt text](https://i.imgur.com/VYRQyUA.png)

### Register a model, with all fields included

```python
from django_admin_autogen.autogen.admin import register_all_fields_of_model
# '<app_name>', <ModelName>
fast_part_note_class = register_all_fields_of_model('notebook', 'NoteCategory')
```

If your model admin requires using custom base class, you 

```python
# '<app_name>', <ModelName>, base_class=<YourCustomBaseClass>
fast_part_note_class = register_all_fields_of_model('outsource', 'Quotation', base_class=YourCustomBaseClass)
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

# <app_name>
register_all_models_of_app('outsource')
```




