from .models import Instagram
from django import forms
from django.forms import ModelForm


class InstagramForm(ModelForm):
    class Meta:
        model = Instagram
        fields = ["user_id", "password"]

    def __init__(self, *args, **kwargs):
        super(InstagramForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update(
                {
                    "class": "form-control",
                    "placeholder": f"Enter your {name}",
                    "required": "True",
                }
            )
