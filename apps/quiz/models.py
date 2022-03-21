from django.db import models
from django.utils.translation import gettext_lazy as _


class Quiz(models.Model):
    """
    Quiz model
    """

    name = models.CharField(_("Name"), max_length=255)

    def __str__(self):
        return self.name


class Question(models.Model):
    """
    Question model
    """

    quiz = models.ForeignKey(
        Quiz,
        verbose_name=_("Quiz"),
        on_delete=models.CASCADE,
        related_name="%(class)s",
    )
    text = models.CharField(_("Text"), max_length=255)
    order = models.SmallIntegerField(_("Order"))

    class Meta:
        ordering = ("order",)
        abstract = True

    def __str__(self):
        return self.text


class MCQuestion(Question):
    number_of_answers = models.SmallIntegerField(_("Number of answers"))


class BooleanQuestion(Question):
    is_true = models.BooleanField(_("Is true"))
