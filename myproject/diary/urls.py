from django.urls import path
from . import views


app_name = "diary" # アプリ名
urlpatterns = [
    path("", views.index, name="index"), #トップページなので名前はindex
    # ("どんなパスか", パスに対して動く関数, この定義の名前)
    path("page/create/", views.page_create, name="page_create"),
    path("page/list/", views.page_list, name="page_list"),
    path("page/<uuid:id>/", views.page_detail, name="page_detail"),
    # uuidはhtml側で引数を指定
    path("page/<uuid:id>/update/", views.page_update, name="page_update"),
    path("page/<uuid:id>/delete/", views.page_delete, name="page_delete"),
]
