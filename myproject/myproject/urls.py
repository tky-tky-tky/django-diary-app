"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include # includeを追加
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("diary/", include("diary.urls")),
    # diary/のURLはdiary.urlsを参照する
    path("accounts/", include("accounts.urls")),
    path("", include("django.contrib.auth.urls"))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# static = 開発環境のみで動作
# 画像はクラウド利用が一般的なので仮実装を取る
# static(含まれるURL, 画像の保存フォルダ)
