
from django.urls import path
from . import views  # Corrected import statement

urlpatterns = [
    path('', views.home, name='home'),  # Assuming you have a 'home' view function
    path('about/', views.about, name='about'),
    path('finches/<int:finch_id>/', views.finches_detail, name='finch_detail'),
    path('finches/', views.finches_index, name='finches_index'),  # New route for finches
    # Removed the duplicate path for 'finches/<int:finch_id>/'
    path('finches/create/', views.FinchCreate.as_view(), name='finches_create'),  # Corrected 'views' and 'as_view()', and added missing comma
]
