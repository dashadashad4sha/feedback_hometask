from django.contrib import admin
from .models import FeedbackModel, Countries, Rating
# Register your models here.
admin.site.register(FeedbackModel)
admin.site.register(Countries)
admin.site.register(Rating)
