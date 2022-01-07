
from django.urls import path

import product
from .views import (
                   product_detail_view, 
                   product_create_view,
                   product_list_view,
                   product_update_view, 
                   product_delete_view
                   )



# app_name = product
urlpatterns = [
    path('', product_list_view, name='listview'),
    path('<int:id>/', product_detail_view, name='detailview'),
    path('<int:id>/update/', product_update_view, name='updateview'),
    path('<int:id>/delete/', product_delete_view, name='deleteview'),
    path('create/', product_create_view, name='createview'),




]
