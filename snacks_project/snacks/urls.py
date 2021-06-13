from django.urls import path
from .views import HomePageView ,AboutView
# list of paths 
# as view call the class things 
urlpatterns = [
 path('',HomePageView.as_view(),name='home'),
 path('about/',AboutView.as_view(),name='about'),




]
