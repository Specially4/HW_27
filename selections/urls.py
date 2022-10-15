from django.urls import path

from selections.views import (SelectionCreateView, SelectionDestroyView,
                              SelectionListView, SelectionRetrieveView,
                              SelectionUpdateView)

urlpatterns = [
    path('', SelectionListView.as_view()),
    path('<int:pk>/', SelectionRetrieveView.as_view()),
    path('create/', SelectionCreateView.as_view()),
    path('<int:pk>/update/', SelectionUpdateView.as_view()),
    path('<int:pk>/delete/', SelectionDestroyView.as_view()),
]
