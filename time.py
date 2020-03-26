#Matthew Zhang
#CS 102 Spring 2020
#March 10th
#Program: time
#Time class which allows the user to input any amount of hours and minutes, in which an over entry of either minutes or hours
#will automatically be converted to the appropriate standard time format of HH:MM

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