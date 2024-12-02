'''
Assignment 1-1
Write a program that simulates a
traffic light using switch-case. The
program should take an input
representing the current light state
(e.g., "red", "yellow", "green").
In the "red" case, print "Stop!".
In the "yellow" case, print "Caution!
Light is about to change."
In the "green" case, print "Go!".
For any other input, print "Invalid
light state."
'''


light=str(input("Enter the color : red or yellow or green :  "))

match light:
    case "red":
        print("Stop")

    case "yellow":
        print("Caution!")

    case "green":
        print("Go!")
    case _:
        print("Invalid")

