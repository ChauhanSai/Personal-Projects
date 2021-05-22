var version = ('5.0.0')
alert('Welcome to Number Generator '+version)
var amount = prompt('Numbers to Generate', 'Integer OR Dice Ex. 6')
if(amount == 'Dice' || amount == 'dice'){
  var dice1 = Math.floor((Math.random() * 6) + 1);
  var dice2 = Math.floor((Math.random() * 6) + 1);
  var die = dice1+dice2;
  alert ('You rolled '+dice1+' & '+dice2+'\nSum: '+(dice1+dice2)+'    Mean: '+((dice1+dice2)/2));
} else {
if(amount == 'Integer OR Dice Ex. 6') amount = 100;

var min = prompt('What is your minimum number(inclusive)?');
if (min == null) min = 1;
if (min == '') min = 1;
var max = prompt('What is your maximum number(exclusive)?');
if (max == null) max = 11;
if (max == '') max = 11;
min = Math.ceil(min);
max = Math.floor(max);

var numbers = new Array();
var sum = 0;
for(var i = 0; i < amount; i++){
  numbers[i] = Math.floor(Math.random() * (max - min) + min);
  sum += numbers[i];
}
var sorted = new Array();
for(var i = 0; i < amount; i++){
  sorted[i] = numbers[i];
}

sorted.sort(function(a, b){return a-b});
low = sorted[0];
high = sorted[(sorted.length-1)];
if(numbers.length%2 == 0){
  median = 0.5*(sorted[sorted.length/2]+sorted[(sorted.length/2)-1]);
}
if(numbers.length%2 == 1){
  median = sorted[Math.floor(sorted.length/2)];
}
average = sum/numbers.length;

alert(i+' Numbers: \n'+numbers.join(' ')+'\n\nSum: '+sum+'    Mean: '+average+'    Median: '+median+'    Low: '+low+'    High: '+high+'\nSorted: \n'+sorted.join(' '));
}
