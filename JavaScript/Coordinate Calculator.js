var version = ('4.0.0')
alert('Welcome to Coordinate Calculator v'+version)
var a = ''
var x1 = prompt(a+'X, Y, Z and X, Y, Z\nFirst X Coordinate\nYou may also use ?','X or ?')
if(x1 == null || x1 == 'X or ?') {var x1 = '?'}
var y1 = prompt(a+''+x1+', Y, Z and X, Y, Z\nFirst Y Coordinate\nYou may also use ?','Y or ?')
if(y1 == null || y1 == 'Y or ?') {var y1 = '?'}
var z1 = prompt(a+''+x1+', '+y1+', Z and X, Y, Z\nFirst Z Coordinate\nYou may also use ?','Z or ?')
if(z1 == null || z1 == 'Z or ?') {var z1 = '?'}
var op = prompt('+ for Addition\n- for Subtraction or Difference\n* for Multiplication\n/ for Division\n+- for Distance Between', '+, -, *, /, +-')
if(op == null || op == '+, -, *, /, +-') {var op = '+'}
if(op == '-+') {var op = '+-'}
if(op == '+-') {var a = 'Distance Between '}
if(op == '+-') {var op = 'and'}
var x2 = prompt(a+''+x1+', '+y1+', '+z1+' '+op+' X, Y, Z\nSecond X Coordinate\nYou may also use ?','X or ?')
if(x2 == null || x2 == 'X or ?') {var x2 = '?'}
var y2 = prompt(a+''+x1+', '+y1+', '+z1+' '+op+' '+x2+', Y, Z\nSecond X Coordinate\nYou may also use ?','Y or ?')
if(y2 == null || y2 == 'Y or ?') {var y2 = '?'}
var z2 = prompt(a+''+x1+', '+y1+', '+z1+' '+op+' '+x2+', '+y2+', Z\nSecond X Coordinate\nYou may also use ?','Z or ?')
if(z2 == null || z2 == 'Z or ?') {var z2 = '?'}
confirm('Confirm?\n'+a+''+x1+', '+y1+', '+z1+' '+op+' '+x2+', '+y2+', '+z2)
var x1 = Number(x1)
var y1 = Number(y1)
var z1 = Number(z1)
var x2 = Number(x2)
var y2 = Number(y2)
var z2 = Number(z2)
if(op == '+') {var x = x1 + x2; var y = y1 + y2; var z = z1 + z2}
if(op == '-') {var x = x2 - x1; var y = y2 - y1; var z = z2 - z1}
if(op == '*') {var x = x1 * x2; var y = y1 * y2; var z = z1 * z2}
if(op == '/') {var x = x1 / x2; var y = y1 / y2; var z = z1 / z2}
if(op == 'and') {var x = x2 - x1; var x = Math.abs(x); var y = y2 - y1; var y = Math.abs(y); var z = z2 - z1; var z = Math.abs(z)}
if(x1 == '?' || x2 == '?') {var x = '?'}
if(y1 == '?' || y2 == '?') {var y = '?'}
if(z1 == '?' || z2 == '?') {var z = '?'}
alert(a+''+x1+', '+y1+', '+z1+', '+op+' '+x2+', '+y2+', '+z2+', = '+x+', '+y+', '+z)