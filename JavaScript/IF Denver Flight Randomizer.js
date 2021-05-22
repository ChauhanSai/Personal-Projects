var version = ('1.0.0')
alert('Welcome to IF Denver Airport Randomizer v'+version)

var airports = [
'KAEJ',
'KAFF',
'KANK',
'KAPA',
'KASE',
'KBJC',
'KBKF',
'KCFO',
'KCOS',
'KDEN',
'KEGE',
'KFCS',
'KGUC',
'KGWS',
'KLXV',
'KMTJ',
'KPUB',
'KRIL'
]

var random = Math.round(Math.random()*(airports.length))
alert('Your random airport is '+airports[random]+' because you rolled '+random)
