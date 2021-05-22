var version = ('1.0.0')
alert('Welcome to Infinite Flight Smooth VNAV Decent Calculator v'+version)
var height1 = Number(prompt('What is your starting vector VNAV altitude set to?'))
var height2 = Number(prompt('What is your ending vector VNAV altitude set to?'))
var ammt = Number(prompt('How many vectors are between these vectors?\nMax of 6'))
if (height1 == null) {var height1 = 32000}
if (height1 == '') {var height1 = 32000}
if (height2 == null) {var height2 = 1000}
if (height2 == '') {var height2 = 1000}
if (ammt == null) {var ammt = 6}
if (ammt == '') {var ammt = 6}
var ammt2 = ammt+1
var each = Math.ceil((height1-height2)/ammt2)
var a = height1-each
var b = a-each
var c = b-each
var d = c-each
var e = d-each
var f = e-each
if (ammt == '1') {alert('1: '+height1+'ft\n2: '+a+'ft\n3: '+height2+'ft\n\nYour decent rate is: -'+each)}
if (ammt == '2') {alert('1: '+height1+'ft\n2: '+a+'ft\n3: '+b+'ft\n4: '+height2+'ft\n\nYour decent rate is: -'+each)}
if (ammt == '3') {alert('1: '+height1+'ft\n2: '+a+'ft\n3: '+b+'ft\n4: '+c+'ft\n5: '+height2+'ft\n\nYour decent rate is: -'+each)}
if (ammt == '4') {alert('1: '+height1+'ft\n2: '+a+'ft\n3: '+b+'ft\n4: '+c+'ft\n5: '+d+'ft\n6: '+height2+'ft\n\nYour decent rate is: -'+each)}
if (ammt == '5') {alert('1: '+height1+'ft\n2: '+a+'ft\n3: '+b+'ft\n4: '+c+'ft\n5: '+d+'ft\n6: '+e+'ft\n7: '+height2+'ft\n\nYour decent rate is: -'+each)}
if (ammt == '6') {alert('1: '+height1+'ft\n2: '+a+'ft\n3: '+b+'ft\n4: '+c+'ft\n5: '+d+'ft\n6: '+e+'\n7: '+f+'ft\n8: '+height2+'ft\n\nYour decent rate is: -'+each)}
