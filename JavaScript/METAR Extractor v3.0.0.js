var version = ('3.2.0')
alert('Welcome to METAR Extractor v'+version)
var im_time = Number(prompt('What hour is it?', '1 - 24'))
if (im_time > 6 && im_time < 18) {var time = 'Noon'} else if (im_time == 6) {var time = 'Sunrise'} else if (im_time == 18) {var time = 'Sunset'} else {var time = 'Night'}
var METAR = prompt('What is your whole METAR?','')
var METAR_time = prompt('What is your METAR time?\nEX. KDFW 141953Z','')
var zulu_hour = Number(METAR_time.slice(7,9))
var zulu_minute = Number(METAR_time.slice(9,11))
if(zulu_minute < 30) {var zulu = zulu_hour} else {var zulu = zulu_hour+1}
var airport = (METAR_time.slice(0,4))
var datea = Number(METAR_time.slice(5,7))
if (datea == 1) {var date = '1st'}
if (datea == 2) {var date = '2nd'}
if (datea == 3) {var date = '3rd'}
if (datea >= 4) {var date = datea+'th'}
var METAR_wind = prompt('What is your METAR wind?\nEX. 22008KT, 18019G28KT','')
var wdirect = Number(METAR_wind.slice(0,3))
var wspeed = Number(METAR_wind.slice(3,5))
var gcheck = (METAR_wind.slice(5,6))
if (gcheck == 'G') {var wgust=Number(METAR_wind.slice(6,8))} else {var wgust=0}
var turba = (wspeed+wgust)/2
if (turba == 0) {var turb = 'None'}
if (turba > 0 && turba <= 12) {var turb = 'Light'}
if (turba > 12 && turba <= 24) {var turb = 'Moderate'}
if (turba > 24 && turba <= 36) {var turb = 'Severe'}
if (turba > 36) {var turb = 'Extreme'}
var METAR_sky = prompt('What is your METAR sky conditions?\nEX. 10SM BKN009 BKN012','')
var visa = Number(METAR_sky.slice(0,2))
var visb = Math.round(visa*1.609)
var vis = Math.round(visb-(((Number(METAR_sky.slice(8,11)))+(Number(METAR_sky.slice(15,18))))/6))
var METAR_temp = prompt('What is your METAR temperature?\nEX. 22/21 A2967 RMK AO2 T02170206','')
var temp = METAR_temp.slice(0,2)
alert('METAR: '+METAR+'\nAirport: '+airport+'\nDate: '+date+'\nZulu(UTC) Time: '+zulu+'z\nTime: '+time+'\nVisibility: '+vis+'\nWind Direction: '+wdirect+'\nWind Velocity: '+wspeed+'\nWind Gusts: '+wgust+'\nTurbulance: '+turb+'\nTemperature: '+temp)
