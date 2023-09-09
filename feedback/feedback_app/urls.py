from django.urls import path

from feedback_app.views import AddFeedback, Feedback

urlpatterns = [
    path('add_feedback/', AddFeedback.as_view(), name='feedback_form'),
    path('feedback/', Feedback.as_view(), name='feedback'),
]
