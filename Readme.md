Manual run:
1. Install python and pip to your local machine.
2. Go to the folder of project and inside bash/cmd print "pip install -r requirements.txt".
3. Print "py manage.py runserver" and go to 127.0.0.1:8000 inside your browser.

Docker run:
1. Iside bash/cmd go to the directory of project(where Dockerfile is).
2. (If you are using Windows, make sure that docker for windows is running)
3. Print docker-compose up
4. Go to the 127.0.0.1:8000

URLS:
127.0.0.1:8000 - homepage of project. Here you can print any company short name from YahooFinance and add it to db
127.0.0.1:8000/get_data - you get here when you paste new company short name and app will load data for you.
127.0.0.1:8000/api - list of JSONs of all records in the db. You will see 75 JSONs per page.
127.0.0.1:8000/api/companyname - list of JSONs of specific company data. E.g. 127.0.0.1:8000/api/pins will show you JSONs of data of Pintarest company.

!!!!!!!!!!!!!!!!!!!!!!! NOTICE !!!!!!!!!!!!!!!!!!!!!!!
Please make sure that you don't add data for company that already in db. 
There was no added any filtering or update tool, so if you add data for company that already exist, you will have duplicates and ~800 more data than you need.
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
