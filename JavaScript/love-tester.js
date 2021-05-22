var dev = 'false'
var version = ('4.0.0')
if (dev == 'true') {var version = '4.0.0 Dev Build'}
alert('Welcome to Love Tester '+version)
var p1 = prompt('Person 1', 'Person 1');
if (p1 == 'null') {var p1 = 'Someone'}
if (p1 == 'Person 1') {var p1 = 'Someone'}
alert('Person 1 is '+p1);
var p2 = prompt('Person 2', 'Person 2');
if (p2 == 'null') {var p2 = 'Someone'}
if (p2 == 'Person 2') {var p2 = 'Someone'}
alert('Person 2 is '+p2)
var chance1 = Math.floor(Math.random() * 100)
var chance2 = Math.floor(Math.random() * 100)
var chance3 = (chance1+chance2)/2
var chance = Math.round(chance3)
if (chance < 10) {var rate = 'which is terrible'}
if (chance >= 10 && chance < 35) {var rate = 'which is pretty bad'}
if (chance >= 35 && chance < 60) {var rate = 'which is meh'}
if (chance >= 60 && chance < 80) {var rate = 'which is pretty good'}
if (chance >= 80 && chance < 90) {var rate = 'which is amazing'}
if (chance >= 90 && chance <= 100) {var rate = 'which is a perfect match'}
if (chance > 100) {var rate = 'which means the relationship is mutual'}
if (dev == 'true') {alert ('Dev Mode Enabled:\n\n'+p1+' and '+p2+' love each other '+chance+'% '+rate+'.\n\nPerson 1:'+p1+'\nPerson 2:'+p2+'\nChance 1:'+chance1+'\nChance 2:'+chance2+'\nAfter Sai Changes:\n     Average Before Round:'+chance3+'\n     After Round Final:'+chance+'\nRate:'+rate)} else alert(p1+' and '+p2+' love each other '+chance+'% '+rate+'.')