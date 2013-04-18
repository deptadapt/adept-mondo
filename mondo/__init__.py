"""
Used for the COMMENTS_APP setting in settings.py

Only the Form is changed. The model from django.contrib.comments
is used.
"""
from django.contrib import comments
from .forms import CrispyCommentForm


def get_model():
    return comments.models.Comment


def get_form():
    return CrispyCommentForm
