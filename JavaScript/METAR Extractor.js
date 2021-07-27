var version = ('4.2.0');
alert('Welcome to METAR Extractor v'+version);

var timeSim = Number(prompt('What time is it(local)?', '1 - 24'));
var infoTime = '';
if (timeSim > 6 && timeSim < 18) {infoTime = 'Noon'} else {if (timeSim == 6) {infoTime = 'Sunrise'} else {if (timeSim == 18) {infoTime = 'Sunset'} else {infoTime = 'Night'}}}

var metar = prompt('Paste in the METAR report:');
//KDFW 170153Z 18019G28KT 10SM BKN240 BKN300 31/21 A2992 RMK AO2 SLP123 T03110211
//0123456789 123456789 123456789 123456789

var infoZulu = metar.substring(5,7) +":"+ metar.substring(7,9);
var infoAirport = metar.substring(0,4);

if(metar.charAt(metar.indexOf("KT")-3) !== 'G'){
  var infoWindDirection = metar.substring(metar.indexOf("KT")-5,metar.indexOf("KT")-2);
  var infoWindSpeed = metar.substring(metar.indexOf("KT")-2,metar.indexOf("KT"));
  var infoWindGust = 0
} else {
infoWindDirection = metar.substring(metar.indexOf("KT")-8,metar.indexOf("KT")-5);
infoWindSpeed = metar.substring(metar.indexOf("KT")-5,metar.indexOf("KT")-3);
infoWindGust = metar.substring(metar.indexOf("KT")-2,metar.indexOf("KT"));
}

var infoTurbulance = (Number(infoWindSpeed)+Number(infoWindGust))/2;
if (infoTurbulance > 0 && infoTurbulance <= 12) {infoTurbulance = 'Light'} else if (infoTurbulance > 12 && infoTurbulance <= 24) {infoTurbulance = 'Moderate'} else if (infoTurbulance > 24 && infoTurbulance <= 36) {infoTurbulance = 'Severe'} else if (infoTurbulance > 36) {infoTurbulance = 'Extreme'}
var infoVisibility = Math.round((metar.substring(metar.indexOf("SM")-3, metar.indexOf("SM")))*1.609);

if(metar.substring(metar.indexOf("SM")+3, metar.indexOf("SM")+6)==='CLR'){
  var infoClouds = 'CLR';
} else infoClouds = metar.substring(metar.indexOf("SM")+3, metar.indexOf("SM")+9);

var infoTemperature = metar.substring(metar.indexOf("/")-3, metar.indexOf("/"));

alert('METAR: '+metar+'\n\nAirport: '+infoAirport+'\nTime(Zulu): '+infoZulu+'z\n\nTime(Local): '+infoTime+'\nVisibility: '+infoVisibility+'km\nWind Direction: '+infoWindDirection+'°\nWind Velocity: '+infoWindSpeed+'kts\nWind Gusts: '+infoWindGust+'kts\nTurbulance: '+infoTurbulance+'\nTemperature: '+infoTemperature+'°C\nClouds: '+infoClouds);