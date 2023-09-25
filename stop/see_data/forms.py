from django import forms
from .models import Post

class Askform(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            "author",
            "phone_number",
            "description",
        )