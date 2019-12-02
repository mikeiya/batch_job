# Django_Rest_framework
This repo shows how to create a simple RESTful API using the Django web framework. Among the included features, you'll see how to:
* Return custom status codes and headers ⚡️
* Create resources using POST requests 📬
* Get resources using GET requests 📭
```bash
a production approach would set up a server for the db(adding proper security measures) and might use a MQ and background task processor for the batch uploads
```
## Install guide

##### Clone the repo

```bash
$ git clone https://github.com/mikeiya/batch_job.git
$ cd batch_job
```

##### Create the virtualenv
```bash
$ mkvirtualenv batch_job/endpoints
```

##### Install dependencies
```bash
$ pip install -r requirements.txt
```

##### Run the app
```bash
$ python manage.py makemigrations api
$ python manage.py migrate
$ python manage.py runserver
```

## Running the app
```bash
uses a browseable API or curl or postman
you should upload to the localhost/upload endpoint before making a get request
POST request e.g
http://127.0.0.1:8000/upload/ filename=file.csv
GET request e.g
http://127.0.0.1:8000/member -> returns current members in db or None
GET request e.g
http://127.0.0.1:8000/member/phone_number=9097775645 -> -> returns member whose number equals phone_number or None
GET request e.g
http://127.0.0.1:8000/member/client_member_id=9 > returns member whose client_id equals client_member_id or None

```


## Test
$ not available yet
```bash
$ make test
```
