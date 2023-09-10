from django.urls import path
from . import views

urlpatterns = [
    path("", views.review.as_view()),
    path("thank-you/", views.Thank_you.as_view(), name="thank"),
    path("reviews/", views.ReviewList.as_view()),
    path("reviews/favourite/", views.AddFavouriteView.as_view()),
    path("reviews/<int:pk>/", views.Detail_page.as_view()),
]
