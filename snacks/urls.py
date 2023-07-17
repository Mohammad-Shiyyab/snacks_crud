from django.urls import path
from .views import SnacksListViews,SnacksCreateViews,SnacksDetailsViews,SnacksUpdateViews,SnacksDeleteViews


urlpatterns = [


    path('', SnacksListViews.as_view(),name = 'snack_list'),
    path('create/', SnacksCreateViews.as_view(),name = 'snack_create'),
    path('detail/<int:pk>/', SnacksDetailsViews.as_view(),name = 'snack_detail'),
    path('update/<int:pk>/', SnacksUpdateViews.as_view(),name = 'snack_update'),
    path('delete/<int:pk>/', SnacksDeleteViews.as_view(),name = 'snack_delete'),
    
]