from django.urls import path
from .views import HomePageView
# list of paths 
# as view call the class things 
urlpatterns = [
 path('',HomePageView.as_view(),name='home'),



]
