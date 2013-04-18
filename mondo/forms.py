from django.contrib.comments.forms import CommentForm
from django.contrib.comments import get_form_target
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Button, Field, Div
from crispy_forms.bootstrap import FormActions


class Submit_grey(Submit):
    """
    The purpose of this class is to allow for multiple submit buttons
    on a form and still have one stand out as the primary button.
    """
    field_classes = 'submit submitButton btn'


class CrispyCommentForm(CommentForm):
    """
    Here we take django.contrib.comments.forms.CommentForm and add
    a crispy_forms.helper.FormHelper to each instance.
    """

    def __init__(self, *args, **kwargs):
        # FormHelper generates a Layout if pass its contructor a
        # form as an argument.
        super(CrispyCommentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)

        # TODO: make form_id configurable
        self.helper.form_id = "comment-form"
        self.helper.form_action = get_form_target()

        # hide the honeypot field
        self.helper['honeypot'].wrap(Div, css_class="hidden")

        # Add post and preview buttons, wrapped in a Form Actions
        # Bootstrap component.
        # TODO: this should be more configurable
        self.helper.layout.append(
            FormActions(Submit('post', 'Post', css_class="submit-post"),
                        Submit_grey('preview',
                                    'Preview',
                                    css_class="submit-preview"
                                    )
                        )
        )
