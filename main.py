import json
import turtle
import urllib.request

iss = "http://api.open-notify.org/iss-now.json"
astros = "http://api.open-notify.org/astros.json"

iss_response = urllib.request.urlopen(iss)
iss_result = json.loads(iss_response.read())
astros_response = urllib.request.urlopen(astros)
astros_result = json.loads(astros_response.read())

people = astros_result['people']
location = iss_result['iss_posit ion']

latitude = location['latitude']
longitude = location['longitude']

screen = turtle.Screen()
screen.setup(720, 360)
screen.setworldcoordinates(-180, -90, 180, 90)
screen.bgpic('assets/gifs/map.gif')

iss = turtle.Turtle()
iss.penup()
iss.shape('circle')
iss.color('yellow')
iss.goto(float(longitude), float(latitude))