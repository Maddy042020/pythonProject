
from faker import Faker

faker = Faker()
def create_booking():
 json_payload = {
     "firstname": "Maddy",
     "lastname": "Brown",
     "totalprice": 111,
     "depositpaid": "true",
     "bookingdates": {
         "checkin": "2018-01-01",
         "checkout": "2019-01-01"
     },
     "additionalneeds": "Breakfast"
 }

 return json_payload


def payload_create_booking_dynamic():
    payload = {
        "firstname": faker.firstname(),
        "lastname": faker.lastname(),
        "totalprice": faker.random_int(min=100,max=1000),
        "depositpaid": faker.boolean,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": faker.random_element(elements="Breakfast")
    }
    return payload


def payload_create_token():
    payload = {
        "username": "admin",
        "password": "password123"

    }
    return payload

