from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView

urlpatterns = [
    # 管理画面
    path("admin/", admin.site.urls),

    # API
    path("api/restaurants/", include("restaurants.urls")),

    # ルート
    path("", TemplateView.as_view(template_name="index.html"), name="root"),

    # React Router 用フォールバック
    # api / admin / static / media は除外する
    re_path(
        r"^(?!api/|admin/|static/|media/).*$",
        TemplateView.as_view(template_name="index.html"),
    ),
]