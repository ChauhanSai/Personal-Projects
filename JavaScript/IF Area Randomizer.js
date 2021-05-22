var version = ('1.0.0')
alert('Welcome to Infinite Flight(16.13.6356.26173) Area Randomizer '+version)
var chance_area = Math.floor(Math.random() * 100)
if (chance_area < 6) {var area = 'Amsterdam'}
if (chance_area < 12 && chance_area >= 6) {var area = 'Caribbean'}
if (chance_area < 18 && chance_area >= 12) {var area = 'Charlotte'}
if (chance_area < 24 && chance_area >= 18) {var area = 'Chicago'}
if (chance_area < 30 && chance_area >= 24) {var area = 'Denver'}
if (chance_area < 36 && chance_area >= 30) {var area = 'Hawaii'}
if (chance_area < 42 && chance_area >= 36) {var area = 'London'}
if (chance_area < 48 && chance_area >= 42) {var area = 'New York'}
if (chance_area < 54 && chance_area >= 48) {var area = 'Oshkosh'}
if (chance_area < 60 && chance_area >= 54) {var area = 'Paris'}
if (chance_area < 66 && chance_area >= 60) {var area = 'San Francisco'}
if (chance_area < 72 && chance_area >= 66) {var area = 'Seattle'}
if (chance_area < 78 && chance_area >= 72) {var area = 'Singapore & Kuala Lumpur'}
if (chance_area < 84 && chance_area >= 78) {var area = 'Southern California'}
if (chance_area < 92 && chance_area >= 84) {var area = 'South Florida'}
if (chance_area <= 100 && chance_area >= 92) {var area = 'Sydney'}
alert('Area: '+area)