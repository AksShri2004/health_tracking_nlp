import requests
import datetime
import os

api_key = os.environ["api_key"]
app_id = os.environ["app_id"]
headers = {
    'Content-Type': 'application/json',
    'x-app-id': app_id,
    'x-app-key':api_key,
  }
item = str(input("What did you do today?"))
initial = requests.post(url="https://trackapi.nutritionix.com/v2/natural/exercise",
                        headers=headers,
                        json= {"query":item})

data = initial.json()["exercises"][0]
print(data)

now= datetime.datetime.now()

date = now.strftime("%x")
time = now.strftime("%X")
exercise = data["name"]
duration = data["duration_min"]
cal = data["nf_calories"]
print(exercise)

data = {
  "workout": {
      "date": date,
      "time": time,
      "exercise": exercise.title(),
      "duration": duration,
      "calories": cal,
    }
}
sheet_endpoint= os.environ["sheety_endpoint"]
auth = os.environ["auth"]

second = requests.post(url=sheet_endpoint, json= data,
                       headers = {"Content-Type": "application/json",
                                  "Authorization": auth})
print(second.text)