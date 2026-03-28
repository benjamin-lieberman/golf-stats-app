from django.urls import path
from . import views

urlpatterns = [
    path("", views.round_list, name="round_list"),
    path("new/", views.round_create, name="round_create"),
    path("<int:round_id>/", views.round_detail, name="round_detail"),

    # 🔥 NEW
    path(
        "<int:round_id>/hole/<int:hole_number>/",
        views.hole_entry,
        name="hole_entry"
    ),
]