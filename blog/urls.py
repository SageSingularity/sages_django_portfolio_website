from django.urls import path

from . import views

urlpatterns = [
    path("blog/", views.blog_landing_page),
    path('blog/<slug:blog-slug>', views.blog_details),
]