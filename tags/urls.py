from django.urls import path
from tags.views import TagView, TagsView

urlpatterns = [
    path('', TagsView.as_view()),
    path('<int:id>', TagView.as_view())
]