#Birthday Paradox Simulation

import datetime, random


def getBirthdays(numberOfBirthdays):
    #return a list of number random date objects for birthdays
    birthdays = []
    for i in range(numberOfBirthdays):
        #the year is unimportant for our simulation, as long as all birthdays have the same year
        startOfYear = datetime.date(2001, 1, 1)

        #get random day into the year
        randomNumberOfDays = datetime.timedelta(random.randint(0, 364))
        birthday = startOfYear + randomNumberOfDays
        birthdays.append(birthday)
    return birthdays


def getMatch(birthdays):
    #return the date object of a birthday that occurs more than once in the birthdays list.
    if len(birthdays) == len(set(birthdays)):
        return None #all birthdays are unique, so return none

    #compare each birthday to every other birthday
    for a, birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays[a + 1]):
            if birthdayA == birthdayB:
                return birthdayA #return the matching
            
# display the intro:
print('''Birthday Paradox
      The Birhtday Paradox shows us that ina group of N people, the odds that two of them have mayching birthdays is suprisingly large.
      This program does a Monte Carlo simulation (that is, repeated random simulations) to explore the concept.

      (It's not actually a paradox, it's just a surprising result.)
''')
#Set up a tuple of month names in order:
MONTHS = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

while True: # keep asking until the user enters a valid amount
    print('How many birthdays shall I generate? (Max 100)')
    response = input('> ')
    if response.isdecimal() and (0 < int(response) <= 100):
        numBDays = int(response)
        break #user has entered a valid amount
print()

#Generate and display the birthdays:
print('Here are', numBDays, 'birthdays:')
birthdays = getBirthdays(numBDays)
for i, birthday in enumerate(birthdays):
    if i != 0:
        #display a comma for each birthday adter the first birthday
        print(', ', end = '')

    monthName = MONTHS[birthday.month - 1]
    dateText = '{} {}'.format(monthName, birthday.day)
    print(dateText, end='')
print()
print()

#determine if there are 2 birthdays that match.
match = getMatch(birthdays)

#display the results:
print('In this simulation, ', end='')
if match !=None:
    monthName = MONTHS[match.month - 1]
    dateText = '{} {}'.format(monthName, match.day)
    print('multiple people have a birthday on', dateText)
else:
    print('there are no matching birthdays.')
print()

#run through 100,000 simulations