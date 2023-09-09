from django.db import models


# Create your models here.
class Countries(models.Model):
    country = models.CharField(max_length=100, verbose_name="Страна")

    def __str__(self):
        return self.country


class Rating(models.Model):
    rating = models.CharField(max_length=20, verbose_name="Оценка")

    def __str__(self):
        return self.rating


class FeedbackModel(models.Model):
    fio = models.CharField(max_length=100, verbose_name="ФИО")
    country = models.ForeignKey(Countries, on_delete=models.CASCADE, verbose_name="Страна",
                                default=Countries.objects.get(pk=1).id)
    rating = models.ForeignKey(Rating, on_delete=models.CASCADE, verbose_name="Оценка",
                               default=Rating.objects.get(pk=1).id)
    feedback = models.TextField(verbose_name="Отзыв")

    def __str__(self):
        return self.fio
