from django.urls import path
from .views import JobViews, CandidateViews, CandidateFinderViews

#Mapping between url path to the relevent fanction (end-point) in views.py file.
urlpatterns = [
    path('job', JobViews.as_view()),
    path('candidate', CandidateViews.as_view()),
    path('match/<int:job_id>', CandidateFinderViews.as_view())
]