from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from feedback_app.forms import FeedbackForm
from feedback_app.models import FeedbackModel


class AddFeedback(CreateView):
    form_class = FeedbackForm
    template_name = 'feedback_app/feedback_form_template.html'
    raise_exception = True
    success_url = reverse_lazy('feedback')


class Feedback(ListView):
    model = FeedbackModel
    template_name = 'feedback_app/feedback.html'
    context_object_name = 'posts'



