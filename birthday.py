#Birthday Paradox Simulation

import datetime, random


def getBirthdays(numberOfBirthdays):
    #return a list of number random date objects for birthdays
    birthdays = []
    for i in range(numberOfBirthdays):
        #the year is unimportant for our simulation, as long as all birthdays have the same year
        startOfYear = datetime.date(2001, 1, 1)

        #get random day into the year
        randomNumberOfDays = dateime.timedelta(random.randint(0, 364))
        birthday = startOfYear + randomNumberOfDays
        birthdays.append(birthday)
    return birthdays


def getMatch(birthdays):
    #return the date object of a birthday that occurs more than once in the birthdays list.
    if len(birthdays) == len(set(birthdays)):
        return None #all birthdays are unique, so return none