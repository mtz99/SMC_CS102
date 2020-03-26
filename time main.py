#Matthew Zhang
#CS 102 Spring 2020
#March 10th
#Program: time
#Time class which allows the user to input any amount of hours and minutes, in which an over entry of either minutes or hours
#will automatically be converted to the appropriate standard time format of HH:MM

####
## INSERT YOUR TIME CLASS HERE TO TEST
import math

class Time:
    def __str__(self):
        return(str(self.hours) + " hours, " + str(self.minutes) + " minutes")

    def __init__(self, hours = 0, minutes = 0):
        self.hours = hours
        self.minutes = minutes
        if(self.minutes > 60):
            self.hours += round(self.minutes/60)
            leftoverMin = minutes % 60
            self.minutes =  leftoverMin 
        elif(self.hours % 1 > 0):
            self.minutes = 60 * (self.hours % 1)
            self.hours = math.floor(self.hours)
    
    def __add__(self, other):
        if(other == Time):
            return Time(str(self.hours + other.hours) + " hours, " + str(self.minutes + other.minutes) + " minutes ")
        else:
            newHours = self.hours + other.hours
            newMin = self.minutes + other.minutes
            print(newHours, " hours, ", newMin, " minutes ")
            


def main():
    time0 = Time()
    print( time0 ) # prints: 0 hours, 0 minutes
    time1 = Time(6)
    print( time1 ) # prints: 6 hours, 0 minutes
    time2 = Time(3, 30)
    print( time2 ) # prints: 3 hours, 30 minutes
    time3 = Time(30, 75)
    print( time3 ) # prints: 31 hours, 15 minutes
    time4 = Time(3.5)
    print( time4 ) # prints: 3 hours, 30 minutes
    print( time3 + time4 ) # prints: 34 hours, 45 minutes
    print( time3 ) # still prints: 31 hours, 15 minutes
    print( time1 + 10 ) # prints: 16 hours, 0 minutes
    print( 0.75 + time2 ) # prints: 4 hours, 15 minutes

main()
