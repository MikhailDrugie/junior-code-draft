from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("promo", views.promo, name="promo"),
    path("<int:teacher_id>/", views.view_teacher, name="view-teacher"),
    path("promo/<int:promo_id>/", views.view_promo, name="view-promo"),

]
