var version = ('1.0.0')
alert('Welcome to IF Sydney Airport Randomizer v'+version)

var airports = [
'YBID',
'YBTH',
'YCAW',
'YCRL',
'YGDO',
'YGLB',
'YJBY',
'YKAT',
'YLMQ',
'YMIG',
'YMRY',
'YMVM',
'YOAS',
'YORG',
'YQIO',
'YRBN',
'YSBK',
'YSCB',
'YSCN',
'YSHL',
'YSHW',
'YSMB',
'YSNW',
'YSRI',
'YSSY',
'YTAL',
'YWBN',
'YWDR',
'YWVA'
]

var random = Math.round(Math.random()*(airports.length))
alert('Your random airport is '+airports[random]+' because you rolled '+random)
