var version = ('1.0.0')
alert('Welcome to Task Tester '+version)
var task = prompt('What is your task?', 'Task')
alert('Your Task is '+task)
var chance = Math.floor(Math.random() * 100)
if (chance < 10) {var rate = 'Not Possible'}
if (chance >= 10 && chance < 35) {var rate = 'Possibly Possible'}
if (chance >= 35 && chance < 60) {var rate = 'Maybe Possible'}
if (chance >= 60 && chance < 80) {var rate = 'Pretty Possible'}
if (chance >= 80 && chance < 90) {var rate = 'Possible'}
if (chance >= 90 && chance <= 100) {var rate = 'for Sure Possible'}
alert('The Results are in!\nThe task, '+task+' has a '+chance+'% Chance of Getting Done. It is '+rate+'.')