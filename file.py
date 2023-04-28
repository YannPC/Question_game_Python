print ("Welcome to The Quiz ")

playing = input("Do you want to Play? ")

if playing.lower() != "yes":  #!= not equal 
    quit()
    
print (" Great! Let's Play :) ")
score = 0

answer =  input ("What Does WAN Stand for: ")

if answer == "Wide Area Network":
    print(" Correct Answer")
    score +=1
    
else: 
    print(" Incorrect Answer ")

answer =  input ("What Does LAN Stand for: ")

if answer == "Local Area Network":
    print(" Correct Answer")
    score +=1
    
else: 
    print(" Incorrect Answer ")

answer =  input ("What Does SQL Stand for: ")

if answer == "Structured Query language ":
    print(" Correct Answer")
    score +=1
    
else: 
    print(" Incorrect Answer ")

answer =  input ("What Does CPU Stand for: ")

if answer== "Central Processing Unit":
    print(" Correct Answer")
    score +=1
    
else: 
    print(" Incorrect Answer ")

answer =  input ("What Does HTML Stand for: ")

if answer == "HyperText Markup Language":
    print(" Correct Answer")
    score +=1
    
else: 
    print(" Incorrect Answer ")

answer =  input ("What Does Css Stand for: ")

if answer == "Cascading Style Sheets":
    print(" Correct Answer")
    score +=1
    
else: 
    print(" Incorrect Answer ")
    
print (" Your Result is : " + str (score) + " Correct Answer ")
