//1 kt = 1.151
//1nm = 1.151
var version = ('1.0.0')
alert('Welcome to Flight Time Calculator v'+version)
var length = Number(prompt('What is your route length (nm)?','ex. 156'))
var cruise = Number(prompt('What is your cruising altititude (ft)?','ex. 32000'))
var tod = Number((Math.floor(cruise/1000)*3))
//tod = length of the decent phase in nm
//250kts/287mph/4.8mpm
//19.2 mi/4 min in acsent at 250kts
var lengthlength = Math.ceil(length*1.151)
//lengthlength = lenth of flight in mi
var todlength = Math.ceil(tod*1.151)
//todlength = length of the decent phase at 250kts in mi
var todtime = Math.ceil((tod*1.151)/4.8)
//todtime =  length of the decent phase at 250kts in min
var cruiselength = Math.ceil((length*1.151)-((tod*1.151)+(19.2)))
//cruiselength = length of cruise at 300kts/345mph/5.8mpm in mi
var cruisetime = Math.ceil(cruiselength/5.8)
//cruisetime = length of cruise at 300kts/345mph/5.8mpm in min
var flighttime = Math.ceil(cruisetime+todtime+4+10)
//flighttime = total ammount of time in min
var flighttimehr = Math.round((flighttime/60)*10)/10
//flighttimehr = total ammount of time in hr
alert(
  '19mi of acsent at 250kts(4 min)\n'+cruiselength+'mi of cruise at 300kts('+cruisetime+'min)\n'+todlength+'mi of decent at ~250kts('+todtime+'min)\n'+lengthlength+'mi of flight for a total of '+flighttime+' minute(s) or '+flighttimehr+' hour(s)'
)
