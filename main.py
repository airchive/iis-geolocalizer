#!/bin/python3

import json
import turtle
import urllib.request

url = "http://api.open-notify.org/astros.json";
urlB = "http://api.open-notify.org/iss-now.json";

response = urllib.request.urlopen(url);
result = json.loads(response.read());

responseB = urllib.request.urlopen(urlB);
resultB = json.loads(responseB.read());

print('People in space: ', result['number'], '\n');

people = result['people'];

for i in people:
  print(i['name'], "in", i['craft']);

location = resultB['iss_position'];
latitude = location['latitude'];
longitude = location['longitude'];

print('\nLatitude: ', latitude);
print('Longitude: ', longitude);

screen = turtle.Screen()
screen.setup(720, 360)
screen.setworldcoordinates(-180, -90, 180, 90)
screen.bgpic('assets/gifs/map.gif')

iss = turtle.Turtle()
iss.penup()
iss.shape('circle')
iss.color('yellow')
iss.goto(float(longitude), float(latitude))
