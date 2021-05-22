var version = ('1.0.0')
alert('Welcome to Porportion Solver Version '+version)
var fl = '1'
var fr = 'x'
var rl = '1'
var rr = '1'
var fl = prompt(' '+fl+'          '+fr+' \n___ = ___ \n '+rl+'          '+rr+' ', '1')
alert(' '+fl+'          '+fr+' \n___ = ___ \n '+rl+'          '+rr+' ')
var rl = prompt(' '+fl+'          '+fr+' \n___ = ___ \n '+rl+'          '+rr+' ', '1')
var rr = prompt(' '+fl+'          '+fr+' \n___ = ___ \n '+rl+'          '+rr+' ', '1')
var s1 = rr/rl
var s2 = fl*s1
var fr = s2
alert(' '+fl+'          '+fr+' \n___ = ___ \n '+rl+'          '+rr+' ', '1')