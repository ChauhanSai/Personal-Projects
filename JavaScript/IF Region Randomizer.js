var version = ('3.0.0')
alert('Welcome to Infinite Flight Region Randomizer '+version)

var regions = [
'Charlotte',
'Denver',
'Chicago/Oshkosh',
'Sydney',
'California',
'Amsterdam']

var random = Math.round(Math.random()*(regions.length))
alert('Your random region is '+regions[random]+' because you rolled '+random+'\nAllow pop-ups to randomize an airport within '+regions[random])

var randomizers = [
'https://jsfiddle.net/ChauhanSai/nfepj0q6/',
'https://jsfiddle.net/ChauhanSai/583zhfr9/',
'https://jsfiddle.net/ChauhanSai/9L6hav37/',
'https://jsfiddle.net/ChauhanSai/2h3oczsp/',
'https://jsfiddle.net/ChauhanSai/ht98gLw3/',
'https://jsfiddle.net/ChauhanSai/6t89z7nf/']

window.open(randomizers[random]);
