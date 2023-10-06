import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

OWM_endpoint = "https://api.openweathermap.org/data/2.5/onecall"

"""Environment variable - OWN_API_KEY & AUTH_TOKEN"""

my_key = os.environ.get("OWM_API_KEY")
account_sid = "ACa8b1492a8c846ea0b0f840debd5455cc"
auth_token = os.environ.get("AUTH_TOKEN")

parameters = {
    "lat": 13.082680,
    "lon": 80.270721,
    "appid": my_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_endpoint, params=parameters)
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]
will_rain = False
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if condition_code < 700:
        will_rain = True

if will_rain:
    client = Client(username=account_sid, password=auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today, remember to bring an ☂️ .",
        from_="+13346001556",
        to='+919600353572'
    )

    print(message.status)
