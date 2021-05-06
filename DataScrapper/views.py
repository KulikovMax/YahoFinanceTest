import yfinance as yf

from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics

from .models import FinDataModel
from .serializers import FinDataSerializer


def home(request):
    """
    This function shows home page where you can insert company short name and download it to database.
    :param request: ---
    :return: renders home.html page.
    """
    return render(request, "home.html")


def get_data(request):
    """
    This function is downloading data from Yahoo Finance and upload it to database.
        (Each row in db is model instance).
    :param request: contains company short name (marked as 'input symbol') from home.html
    :return: pandas dataframe with historical data of company for max period, converted to html page.
    """
    # company data from Yahoo Finance
    company = yf.Ticker(request.POST["input_symbol"])
    # historical company data
    hist = company.history(period="max")
    # here I inserted column name to make navigation through db easier
    # and to have an opportunity to navigate through company name in api
    hist["Name"] = company.info["symbol"]
    # by default 'Date' is an index of this dataframe, so we should reset it to have access to it
    hist = hist.reset_index()
    amount_of_rows = hist.shape[0]
    for i in range(amount_of_rows):
        findata = FinDataModel(
            fd_name=hist["Name"][i],
            fd_date=hist["Date"][i],
            fd_open=hist["Open"][i],
            fd_high=hist["High"][i],
            fd_low=hist["Low"][i],
            fd_close=hist["Close"][i],
            fd_volume=hist["Volume"][i],
        )
        findata.save()
    return HttpResponse(hist.to_html())


class FinDataList(generics.ListCreateAPIView):
    """
    This is just an api view where you can see all records in database.
    """

    queryset = FinDataModel.objects.all()
    serializer_class = FinDataSerializer


class FinDataDetail(generics.ListAPIView):
    """
    This is just an api view where you can see only records for specific company.
    """

    serializer_class = FinDataSerializer

    def get_queryset(self):
        """
        Method that makes queryset of data for specific company.
        :return: FinDataModel queryset
        """
        name = self.kwargs["name"]
        name = name.upper()
        return FinDataModel.objects.filter(fd_name=name)
