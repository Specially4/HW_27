from django.urls import path

from ads.views import CategoryDetailView, CategoryCreateView, CategoryUpdateView, CategoryDeleteView, \
    CategoriesListView

urlpatterns = [
    path('', CategoriesListView.as_view()),
    path('<int:pk>', CategoryDetailView.as_view()),
    path('create/', CategoryCreateView.as_view()),
    path('update/<int:pk>', CategoryUpdateView.as_view()),
    path('delete/<int:pk>', CategoryDeleteView.as_view()),
]
