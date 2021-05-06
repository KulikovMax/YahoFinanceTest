import DataScrapper.views as dsv

from django.urls import path

urlpatterns = [
    path("", dsv.home, name="home"),
    path("get_data/", dsv.get_data, name="get_data"),
    path("api/", dsv.FinDataList.as_view()),
    path("api/<slug:name>/", dsv.FinDataDetail.as_view()),
]
