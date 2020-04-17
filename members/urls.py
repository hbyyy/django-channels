from django.urls import path

from members.apis import UserListView, UserRetrieveView

urlpatterns = [
    path('', UserListView.as_view()),
    path('<int:pk>/', UserRetrieveView.as_view()),
]
