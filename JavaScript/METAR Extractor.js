var version = ('4.0.0');
alert('Welcome to METAR Extractor v'+version);

var timeSim = Number(prompt('What time is it(local)?', '1 - 24'));
if (timeSim > 6 && timeSim < 18) {var infoTime = 'Noon'} else if (timeSim == 6) {var infoTime = 'Sunrise'} else if (timeSim == 18) {var infoTime = 'Sunset'} else {var infoTime = 'Night'}

var metar = prompt('Paste in the METAR report:');
//KDFW 170153Z 18019G28KT 10SM BKN240 BKN300 31/21 A2992 RMK AO2 SLP123 T03110211
var infoZulu = metar.substring(5,7) +":"+ metar.substring(7,9);
var infoAirport = metar.substring(0,4);

var infoWindDirection = metar.substring(13,16);
var infoWindSpeed = metar.substring(16,18);
if(metar.charAt(18) == 'G'){
  var infoWindGust = metar.substring(19,21);
} else var infoWindGust = 0;
var infoTurbulance = (Number(infoWindSpeed)+Number(infoWindGust))/2;
if (infoTurbulance > 0 && infoTurbulance <= 12) {var infoTurbulance = 'Light'} else if (infoTurbulance > 12 && infoTurbulance <= 24) {var infoTurbulance = 'Moderate'} else if (infoTurbulance > 24 && infoTurbulance <= 36) {var infoTurbulance = 'Severe'} else if (infoTurbulance > 36) {var infoTurbulance = 'Extreme'}
var infoVisibility = Math.round((metar.substring(metar.indexOf("SM")-3, metar.indexOf("SM")))*1.609);
var infoClouds = metar.substring(metar.indexOf("SM")+3, metar.indexOf("SM")+9);
var infoTemperature = metar.substring(metar.indexOf("/")-3, metar.indexOf("/"));

alert('METAR: '+metar+'\n\nAirport: '+infoAirport+'\nTime(Zulu): '+infoZulu+'z\n\nTime(Local): '+infoTime+'\nVisibility: '+infoVisibility+'\nWind Direction: '+infoWindDirection+'\nWind Velocity: '+infoWindSpeed+'\nWind Gusts: '+infoWindGust+'\nTurbulance: '+infoTurbulance+'\nTemperature: '+infoTemperature+'\nClouds: '+infoClouds);
