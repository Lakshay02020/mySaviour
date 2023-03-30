from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name = "home"),
    path('<int:year>/', views.branch, name = "branch"),
    path('<int:year>/<int:branch_id>/', views.course, name = "course"),
    path('course_<int:course_id>/', views.documents, name = "documents"),
    path('course_<int:course_id>/type_<int:type_id>/', views.show_documents, name = "show_documents"),
    path('wifi/', views.wifi, name = "wifi"),
    path('gpa/', views.gpa, name = "gpa"),
    path('gpa_calc/_year_<int:year_id>/_branch_<int:branch_id>/', views.gpa_calc, name ="gpa_calc")
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
