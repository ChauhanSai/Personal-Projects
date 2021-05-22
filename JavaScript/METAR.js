var version = ('2.0.0')
alert('Welcome to METAR Extractor v'+version)
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
alert('Time: '+time+'\nVisibility: '+vis+'\nWind Direction: '+wdirect+'\nWind Velocity: '+wspeed+'\nWind Gusts: '+wgust+'\nTurbulance: '+turb+'\nTemperature: '+temp)
