from django import forms

try:
    from tags.models import Tag

    class TagForm(forms.ModelForm):
        class Meta:
            model = Tag
            fields = ["name", "recipes"]

except Exception:
    pass
