var version = ('2.3.0')
alert('Welcome to Math Quiz 1 v'+version)
var amt = 0;
var percent = 0;
var q1 = prompt('Q1: 123-321');
if(q1 == 123-321){var a1 = ('Correct')} else {var a1 = ('Incorrect')}
alert('Question 1 is '+a1)
var q2 = prompt('Q2: 31 x 56');
if(q2 == 31*56){var a2 = ('Correct')} else {var a2 = ('Incorrect')}
alert('Question 2 is '+a2)
var q3 = prompt('Q3: 11+199');
if(q3 == 11+199){var a3 = ('Correct')} else {var a3 = ('Incorrect')}
alert('Question 3 is '+a3)
var q4 = prompt('Q4: 1888/4');
if(q4 == 1888/4){var a4 = ('Correct')} else {var a4 = ('Incorrect')}
alert('Question 4 is '+a4)
var q5 = prompt('Q5: (66+11*5+1)/2-71*11');
if(q5 == 1342){var a5 = ('Correct')} else {var a5 = ('Incorrect')}
alert('Question 5 is '+a5)
var done = confirm('Did you finish the quiz? Ok is Yes and Cancel is No');
if(a1 == 'Correct'){amt++}
if(a2 == 'Correct'){amt++}
if(a3 == 'Correct'){amt++}
if(a4 == 'Correct'){amt++}
if(a5 == 'Correct'){amt++}
if(a1 == 'Correct'){percent = percent + 20}
if(a2 == 'Correct'){percent = percent + 20}
if(a3 == 'Correct'){percent = percent + 20}
if(a4 == 'Correct'){percent = percent + 20}
if(a5 == 'Correct'){percent = percent + 20}
if(percent < 70){var fail = 'Failed'}
if(percent >= 70){var fail = 'Passed'}
if(done = true){} else {alert('Bad,\nRestart The Quiz')}
alert('Quiz Finished!\nResults:\nQ1: '+a1+'\nQ2: '+a2+'\nQ3: '+a3+'\nQ4: '+a4+'\nQ5: '+a5+'\n\n'+amt+'/5 Answers Correct\nYou got a '+percent+'%\nYou Have '+fail+'.')