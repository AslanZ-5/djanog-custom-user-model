from django.forms import ModelForm
from .models import Comment


class PostInterestForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
