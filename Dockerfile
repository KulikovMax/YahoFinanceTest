FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /YahooFinanceTest
COPY requirements.txt /YahooFinanceTest/
RUN pip install -r requirements.txt
COPY . /YahooFinanceTest/