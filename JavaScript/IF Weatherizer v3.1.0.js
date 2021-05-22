var version = ('3.1.0')
alert('Welcome to Infinite Flight Weatherizer '+version)
var preset = prompt('What is your preset\nNone\nFlightRadar24\nWeather.com\nMETAR','')
if (preset == 'None') {
var im_time = Number(prompt('What hour is it?', '1 - 24'))
if (im_time > 6 && im_time < 18) {var time = 'Noon'} else if (im_time == 6) {var time = 'Sunrise'} else if (im_time == 18) {var time = 'Sunset'} else {var time = 'Night'}
var im_weather = prompt('What weather is it?', 'Rain, Clouds, Clear')
var vist = prompt('What unit will the visibility be in?', 'SM, MI, KM')
var im_vis = Number(prompt('What is the visibility in '+vist+'?', '0'))
if (vist == 'SM') {var visa = Math.round(im_vis*1.609)}
if (vist == 'MI') {var visa = Math.round(im_vis*1.609)}
if (vist == 'KM') {var visa = im_vis}
if (im_weather == 'Rain') {var vis = visa-10} else if (im_weather == 'Clouds') {var vis = visa-3} else {var vis = visa}
var wspeedt = prompt('What unit will the wind speed be in?', 'MPH, KT')
var im_wspeed = Number(prompt('What is the wind speed in '+wspeedt+'?', '0'))
if (wspeedt == 'MPH') {var wspeed = Math.round(im_wspeed/1.151)}
if (wspeedt == 'KT') {var wspeed = im_wspeed}
var wgustt = prompt('What unit will the wind gusts be in?', 'MPH, KT')
var im_wgust = Number(prompt('What is the wind gusts in '+wgustt+'?', '0'))
if (wgustt == 'MPH') {var wgust = Math.round(im_wgust/1.151)}
if (wgustt == 'KT') {var wgust = im_wgust}
var im_wdirect = prompt('What is the wind direction?', '0 - 359, NNW')
if (im_wdirect == 'N') {var wdirect = '0'} else if (im_wdirect == 'NNE') {var wdirect = '23'} else if (im_wdirect == 'NE') {var wdirect = '45'} else if (im_wdirect == 'ENE') {var wdirect = '68'} else if (im_wdirect == 'E') {var wdirect = '90'} else if (im_wdirect == 'ESE') {var wdirect = '113'} else if (im_wdirect == 'SE') {var wdirect = '135'} else if (im_wdirect == 'SSE') {var wdirect = '158'} else if (im_wdirect == 'S') {var wdirect = '180'} else if (im_wdirect == 'SSW') {var wdirect = '203'} else if (im_wdirect == 'SW') {var wdirect = '225'} else if (im_wdirect == 'WSW') {var wdirect = '248'} else if (im_wdirect == 'W') {var wdirect = '270'} else if (im_wdirect == 'WNW') {var wdirect = '293'} else if (im_wdirect == 'NW') {var wdirect = '315'} else if (im_wdirect == 'NNW') {var wdirect = '338'} else {var wdirect = im_wdirect}
var tempt = prompt('What unit will the temperature be in?', 'F, C')
var im_temp = Number(prompt('What is the temperature in '+tempt+'?', '0'))
if (tempt == 'F') {var temp = Math.round((im_temp-32)*(5/9))}
if (tempt == 'C') {var temp = im_temp}
var turba = (wspeed+wgust)/2
if (turba == 0) {var turb = 'None'}
if (turba > 0 && turba <= 12) {var turb = 'Light'}
if (turba > 12 && turba <= 24) {var turb = 'Moderate'}
if (turba > 24 && turba <= 36) {var turb = 'Severe'}
if (turba > 36) {var turb = 'Extreme'}
}
if (preset == 'FlightRadar24') {
var im_time = Number(prompt('What hour is it?', '1 - 24'))
if (im_time > 6 && im_time < 18) {var time = 'Noon'} else if (im_time == 6) {var time = 'Sunrise'} else if (im_time == 18) {var time = 'Sunset'} else {var time = 'Night'}
var im_weather = prompt('What weather is it?', 'Rain, Clouds, Clear')
var im_vis = Number(prompt('What is the visibility in SM?', '0'))
var visa = Math.round(im_vis*1.609)
if (im_weather == 'Rain') {var vis = visa-10} else if (im_weather == 'Clouds') {var vis = visa-3} else {var vis = visa}
var im_wspeed = Number(prompt('What is the wind speed in KT?', '0'))
var wspeed = im_wspeed
var im_wgust = Number(prompt('What is the wind gusts in KT?', '0'))
var wgust = im_wgust
var im_wdirect = prompt('What is the wind direction?', '0 - 359, NNW')
if (im_wdirect == 'N') {var wdirect = '0'} else if (im_wdirect == 'NNE') {var wdirect = '23'} else if (im_wdirect == 'NE') {var wdirect = '45'} else if (im_wdirect == 'ENE') {var wdirect = '68'} else if (im_wdirect == 'E') {var wdirect = '90'} else if (im_wdirect == 'ESE') {var wdirect = '113'} else if (im_wdirect == 'SE') {var wdirect = '135'} else if (im_wdirect == 'SSE') {var wdirect = '158'} else if (im_wdirect == 'S') {var wdirect = '180'} else if (im_wdirect == 'SSW') {var wdirect = '203'} else if (im_wdirect == 'SW') {var wdirect = '225'} else if (im_wdirect == 'WSW') {var wdirect = '248'} else if (im_wdirect == 'W') {var wdirect = '270'} else if (im_wdirect == 'WNW') {var wdirect = '293'} else if (im_wdirect == 'NW') {var wdirect = '315'} else if (im_wdirect == 'NNW') {var wdirect = '338'} else {var wdirect = im_wdirect}
var im_temp = Number(prompt('What is the temperature in C?', '0'))
var temp = im_temp
var turba = (wspeed+wgust)/2
if (turba == 0) {var turb = 'None'}
if (turba > 0 && turba <= 12) {var turb = 'Light'}
if (turba > 12 && turba <= 24) {var turb = 'Moderate'}
if (turba > 24 && turba <= 36) {var turb = 'Severe'}
if (turba > 36) {var turb = 'Extreme'}
}
if (preset == 'Weather.com') {
var im_time = Number(prompt('What hour is it?', '1 - 24'))
if (im_time > 6 && im_time < 18) {var time = 'Noon'} else if (im_time == 6) {var time = 'Sunrise'} else if (im_time == 18) {var time = 'Sunset'} else {var time = 'Night'}
var im_weather = prompt('What weather is it?', 'Rain, Clouds, Clear')
var im_vis = Number(prompt('What is the visibility in MI?', '0'))
var visa = Math.round(im_vis*1.609)
if (im_weather == 'Rain') {var vis = visa-10} else if (im_weather == 'Clouds') {var vis = visa-3} else {var vis = visa}
var im_wspeed = Number(prompt('What is the wind speed in MPH?', '0'))
var wspeed = Math.round(im_wspeed/1.151)
var im_wgust = Number(prompt('What is the wind gusts in MPH?', '0'))
var wgust = Math.round(im_wgust/1.151)
var im_wdirect = prompt('What is the wind direction?', '0 - 359, NNW')
if (im_wdirect == 'N') {var wdirect = '0'} else if (im_wdirect == 'NNE') {var wdirect = '23'} else if (im_wdirect == 'NE') {var wdirect = '45'} else if (im_wdirect == 'ENE') {var wdirect = '68'} else if (im_wdirect == 'E') {var wdirect = '90'} else if (im_wdirect == 'ESE') {var wdirect = '113'} else if (im_wdirect == 'SE') {var wdirect = '135'} else if (im_wdirect == 'SSE') {var wdirect = '158'} else if (im_wdirect == 'S') {var wdirect = '180'} else if (im_wdirect == 'SSW') {var wdirect = '203'} else if (im_wdirect == 'SW') {var wdirect = '225'} else if (im_wdirect == 'WSW') {var wdirect = '248'} else if (im_wdirect == 'W') {var wdirect = '270'} else if (im_wdirect == 'WNW') {var wdirect = '293'} else if (im_wdirect == 'NW') {var wdirect = '315'} else if (im_wdirect == 'NNW') {var wdirect = '338'} else {var wdirect = im_wdirect}
var im_temp = Number(prompt('What is the temperature in F?', '0'))
var temp = Math.round((im_temp-32)*(5/9))
var turba = (wspeed+wgust)/2
if (turba == 0) {var turb = 'None'}
if (turba > 0 && turba <= 12) {var turb = 'Light'}
if (turba > 12 && turba <= 24) {var turb = 'Moderate'}
if (turba > 24 && turba <= 36) {var turb = 'Severe'}
if (turba > 36) {var turb = 'Extreme'}
}
if (preset == 'METAR') {
var im_time = Number(prompt('What hour is it?', '1 - 24'))
if (im_time > 6 && im_time < 18) {var time = 'Noon'} else if (im_time == 6) {var time = 'Sunrise'} else if (im_time == 18) {var time = 'Sunset'} else {var time = 'Night'}
var METAR = prompt('What is your whole METAR?','')
var wdirect = Number(METAR.slice(13,16))
var wspeed = Number(METAR.slice(16,18))
var visa = Number(METAR.slice(21,23))
var visb = Math.round(visa*1.609)
var METAR_sky = prompt('What is your METAR sky conditions?\nEX. BKN009 BKN012','')
var vis = Math.round(visb-(((Number(METAR_sky.slice(3,6)))+(Number(METAR_sky.slice(10,13))))/6))
var METAR_temp = prompt('What is your METAR temperature?\nEX. 22/21 A2967 RMK AO2 T02170206','')
var temp = METAR_temp.slice(0,2)
//KDFW 191715Z 22008KT 10SM BKN009 BKN012 22/21 A2967 RMK AO2 T02170206
//KDFW 191715Z 22008KT 10SM
//BKN009 BKN012
//22/21 A2967 RMK AO2 T02170206
//KCLE 220136Z 31006KT 10SM FEW020 BKN024 OVC049 22/21 A2984 RMK AO2 RAE04 P0000 T02220206
//KCLE 220136Z 31006KT 10SM
//FEW020 BKN024 OVC049
//22/21 A2984 RMK AO2 RAE04 P0000 T02220206
var im_wgust = Number(prompt('What is the wind gusts in KT?', '0'))
var wgust = im_wgust
var turba = (wspeed+wgust)/2
if (turba == 0) {var turb = 'None'}
if (turba > 0 && turba <= 12) {var turb = 'Light'}
if (turba > 12 && turba <= 24) {var turb = 'Moderate'}
if (turba > 24 && turba <= 36) {var turb = 'Severe'}
if (turba > 36) {var turb = 'Extreme'}
}
alert('Time: '+time+'\nVisibility: '+vis+'\nWind Direction: '+wdirect+'\nWind Velocity: '+wspeed+'\nWind Gusts: '+wgust+'\nTurbulance: '+turb+'\nTemperature: '+temp)
