from django.urls import path
from . import views

urlpatterns = [
    path("",views.ReviewView.as_view()),
    path("thank-you",views.ThankView.as_view()),
    path("reviews",views.ReviewListView.as_view()),
    path("/review/favorite"),
    path("reviews/<int:id>",views.SingleReviewView.as_view())
]
