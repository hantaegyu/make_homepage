from django.views.generic import ListView, DetailView
from . import models


class CategoryView(ListView):

    """HomeView"""

    model = models.Category
