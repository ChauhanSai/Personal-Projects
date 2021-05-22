var version = ('3.4.3')
alert('Welcome to Top of Decent Calculator v'+version)
var altititude_cruise = Number(prompt('What is your cruising altititude (ft)?','ex. 32000'))
var altititude_airport = Number(prompt('What is the altititude of the arrival airport(ft)?','ex. 83'))
var minutes_a = Number(Math.floor((altititude_cruise-(3000+altititude_airport))/2500))
if (minutes_a <= 5) {var minutes = minutes_a+4} else {var minutes = minutes_a+2}
var nm = Number((Math.floor(altititude_cruise/1000)*3))
var altititude_msl = Number(3000+altititude_airport)
var altititude_msl_round = Number((Math.floor((3000+altititude_airport)/100))*100)
//if(minutes <= 10) {
//var minutes_slow = minutes
//var arrival_text = ''
//} else {
//var minutes_slow = Number(minutes-5)
//var nm_slow = Math.floor((nm*minutes_slow)/minutes)
//var arrival_text = '\nAt '+minutes_slow+' minutes until arrival or '+nm_slow+'nm until arrival'
//}
alert('TOD is at '+minutes+' minutes until arrival or '+nm+'nm until arrival\n          Set altititude to '+altititude_msl+'ft ('+altititude_msl_round+'ft)\n          Set VS to -2500ft/min\n          Set spoilers flight\n          Set speed to 180kts\nWhen glideslope indicator is in the middle\nOR\nPAPI lights are centered\n          Set spoliers armed\n          Gear down\n          Set speed to landing speed(135kts-160kts)\n          Adjust flaps as needed\n          Take over plane or autoland')
