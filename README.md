# What Happened That Day API

<br>

## About The Project

The goal of the project was to implement a simple REST API that would provide interesting fact about a day of a month along with remembering and aggregating every case certain date was requested.

The project is deployed to Heroku at: https://what-happened-that-day.herokuapp.com.

### Features

#### Available Operations

* Adding new date info
* Removing entry with remembered case of requesting the date info
* Obtain whole collection of all remembered date requests
* Get aggregate of date requests in form of popularity ranking

#### API Endpoints

* <b>POST</b> /dates/
* <b>DELETE</b> /dates/{id}/
* <b>GET</b> /dates/
* <b>GET</b> /popular/

#### Deployability

* Local Dev
    * Docker Stack
* Heroku Cloud PaaS

### Stack

* Interpreter
    * Python 3.10
* Containerization
    * Docker
* Web Frameworks
    * Django
    * Django REST Framework (DRF)
* Database
    * Postgres
* Heroku
    * Git
    * Heroku CLI

## Getting Started

### Prerequisites

* Containerization
    * Docker
    * Docker Compose

##### or

* Heroku
    * Heroku Account
    * Heroku CLI App

### Setting Up The Project

#### Setting Up The Docker Stack

##### Creating Environmental Variables Containing .env file having .env.example file as an example

```sh
mv .env.example .env
```

##### Launching The API

```sh
docker-compose -p "what-happened-that-day" up api -d
```

##### Launching The Example Test Suite With Verbosity Level Set In .env File

```sh
docker-compose -p "what-happened-that-day" up tests
```

###### Or If Want To Also Close Database Service When Tests Finish

```sh
docker-compose -p "what-happened-that-day" up tests --exit-code-from tests
```

#### Setting Up The Heroku Deployment

* Set Up An Account
    * https://signup.heroku.com/
* Install Heroku CLI
    * https://devcenter.heroku.com/articles/heroku-cli#install-the-heroku-cli
* Using Heroku CLI Set SECRET_KEY As Environmental Variable
    * <code>heroku config:set SECRET_KEY=SECRET_API_KEY</code>
* Deploy The App
    * https://devcenter.heroku.com/articles/getting-started-with-python#deploy-the-app

## Usage

#### Endpoints Described More In Depth In APPENDIX

### Sample Gists Including Requests And Responses

##### Another way of using this REST API would be e.g. utilizing it via web browser

```sh
virtualenv venv; source venv/bin/activate
pip install --no-cache-dir requests
```

```python
import requests
import json
```

```python
r = requests.post('https://what-happened-that-day.herokuapp.com/dates/',
                  json={'month': 5, 'day': 4})
print(json.dumps(r.json(), indent=4))

{
    "id": 7,
    "month": 5,
    "day": 4,
    "fact": "May 4th is the day in 1869 that the Naval Battle of Hakodate Bay is fought in Japan."
}
```

```python
r = requests.get('http://0.0.0.0:8000/dates/')
print(json.dumps(r.json(), indent=4))

[
    {
        "id": 3,
        "month": "January",
        "day": 14,
        "fact": "January 14th is the day in 1907 that an earthquake in Kingston, Jamaica kills more than 1,000."
    },
    {
        "id": 4,
        "month": "January",
        "day": 1,
        "fact": "January 1st is the day in 1948 that the Constitution of Italy comes into force."
    },
    {
        "id": 5,
        "month": "December",
        "day": 14,
        "fact": "December 14th is the day in 1903 that the Wright brothers make their first attempt to fly with the Wright Flyer at Kitty Hawk, North Carolina."
    }
]
```

```python
r = requests.delete('https://what-happened-that-day.herokuapp.com/dates/11/')
print(json.dumps(r.json(), indent=4))

{
    "detail": "Authentication credentials were not provided."
}
```

```python
r = requests.delete('https://what-happened-that-day.herokuapp.com/dates/11/',
                    headers={'X-API-KEY': 'SECRET_API_KEY'})
print(json.dumps(r.json(), indent=4))

{
    "res": "Object deleted!"
}
```

```python
r = requests.get('http://0.0.0.0:8000/popular/')
print(json.dumps(r.json(), indent=4))

[
    {
        "month": "January",
        "days_checked": 2
    },
    {
        "month": "December",
        "days_checked": 1
    }
]
```

## APPENDIX

<table>
	<tr>
		<th>Endpoint</th>		
		<th>Description</th>
	</tr>
	<tr>
		<td>POST /dates/</td>
		<td>
			<b>Request:</b><br>
			<samp>
				{<br>
					&nbsp;&nbsp;&nbsp;&nbsp;"month": &ltmonth_number&gt,<br>
					&nbsp;&nbsp;&nbsp;&nbsp;"day": &ltday_number&gt<br>
				}
			</samp>
			<br><br>
			<b>Response:</b><br>
			<samp>
				{<br>
					&nbsp;&nbsp;&nbsp;&nbsp;"id": &ltdate_id&gt,<br>
					&nbsp;&nbsp;&nbsp;&nbsp;"month": &ltmonth_name&gt,<br>
					&nbsp;&nbsp;&nbsp;&nbsp;"day": &ltday_number&gt,<br>
					&nbsp;&nbsp;&nbsp;&nbsp;"fact": &ltfact_str&gt<br>
				}
			</samp>
			<br><br>
			<ul>
				<li>month_number - int validated to be in range 1..12</li>
				<li>day_number - int validated to be in range 1..31</li>
				<li>date_id - int, id of the date entry saved in database</li>
				<li>month_name - str, month number converted into month name</li>
				<li>fact_str - str containing fact about the requested day of the month; the fact is checked accessing external service: http://numbersapi.com/</li>
			</ul>
		</td>
	</tr>
	<tr>
		<td>DELETE /dates/{id/}</td>
		<td>
			<ul>
				<li>providing the X-API-KEY in header is needed to successfully request removing desired entry</li><br>
				<li>id - id of the checked date entry in database</li>
			</ul>
		</td>
	</tr>
	<tr>
		<td>GET /dates/</td>
		<td>
			<samp>
				[<br>
					&nbsp;&nbsp;&nbsp;&nbsp;...,<br>
					&nbsp;&nbsp;&nbsp;&nbsp;{<br>
						&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"id": &ltdate_id&gt,<br>
						&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"month": &ltmonth_name&gt,<br>
						&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"day": &ltday_number&gt,<br>
						&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"fact": &ltfact_str&gt<br>
					&nbsp;&nbsp;&nbsp;&nbsp;},<br>
					&nbsp;&nbsp;&nbsp;&nbsp;...<br>
				]
			</samp>
			<br><br>
			<ul>
				<li>this endpoint is used for fetching all  the entries present in the database</li><br>
				<li>month_number - int validated to be in range 1..12</li>
				<li>day_number - int validated to be in range 1..31</li>
				<li>date_id - int, id of the date entry saved in database</li>
				<li>month_name - str, month number converted into month name</li>
				<li>fact_str - str containing fact about the requested day of the month; the fact is checked accessing external service: http://numbersapi.com/</li>
			</ul>
		</td>
	</tr>
	<tr>
		<td>GET /popular/</td>
		<td>
			<b>Response:</b><br>
			<samp>
				{<br>
					&nbsp;&nbsp;&nbsp;&nbsp;"month": &ltmonth_name&gt,<br>
					&nbsp;&nbsp;&nbsp;&nbsp;"days_checked": &ltdays_checked&gt,<br>
				}
			</samp>
			<br><br>
			<ul>
				<li>this endpoint is used for fetching sort of a popularity ranking among months</li><br>
				<li>month_name - str, month number converted into month name</li>
				<li>days_checked - int number of days of the month checked</li>	
			</ul>
		</td>
	</tr>
</table>
