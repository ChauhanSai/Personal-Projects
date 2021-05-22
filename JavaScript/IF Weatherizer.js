var version = ('1.0.0')
alert('Welcome to Infinite Flight(16.13.6356.26173) Weatherizer '+version)
var im_time = Number(prompt('What hour is it?', '1 - 24'))
var im_weather = prompt('What weather is it?', 'Rain, Cloudy, Thunder, Clear')
var im_vis = Number(prompt('What is the visibility in miles?', '0 - 30'))
var im_wspeed = Number(prompt('What is the wind speed in mph?', 'mph'))
var im_wdirect = Number(prompt('What is the wind direction?', '0 - 359'))
var im_temp = Number(prompt('What is the tempreture in fahrenheit?', '-130 - 158'))
if (im_time >= 6 && im_time <= 8) {var time = 'Sunrise'}
if (im_time > 8 && im_time < 18) {var time = 'Noon'}
if (im_time >= 18 && im_time <= 20) {var time = 'Sunset'}
if (im_time > 20 && im_time < 6) {var time = 'Night'}
if (im_weather == 'Rain') {var vis = Math.round(((im_vis/1.609)+15)/2)}
if (im_weather == 'Cloudy') {var vis = Math.round(((im_vis/1.609)+10)/2)}
if (im_weather == 'Thunder') {var vis = Math.round(((im_vis/1.609)+5)/2)}
if (im_weather == 'Clear') {var vis = Math.round((im_vis/1.609)/2)}
var wspeed = Math.round(im_wspeed/1.151)
var gspeed = wspeed+2
var wdirect = im_wdirect
var temp = Math.round((im_temp-32)*(5/9))
if (wspeed <= 4) {var turb = 'None'}
if (wspeed > 4 && wspeed <= 8) {var turb = 'Light'}
if (wspeed > 8 && wspeed <= 12) {var turb = 'Moderate'}
if (wspeed > 12 && wspeed <= 16) {var turb = 'Severe'}
if (wspeed > 20) {var turb = 'Extreme'}
alert('Time: '+time+'\nVisibility: '+vis+'\nWind Direction: '+wdirect+'\nWind Velocity: '+wspeed+'\nWind Gusts: '+gspeed+'\nTurbulance: '+turb+'\nTemperature: '+temp)