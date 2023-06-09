import os

if not os.path.exists("MicrosoftRewards.txt"):
    with open("MicrosoftRewards.txt", "w") as rewards:
        rewards.write("0\n")

printing = input("do you want to run this program?: ")
while printing == "":
    with open("MicrosoftRewards.txt") as Rewards: 
        lines = Rewards.readlines()
        totalpoints = lines[0].strip()
        previousadd = list()
        previoussubtract = list()
        averagedays = list()
        subtractcount = 0
        print("Your current amount of Microsoft Reward Points is " + str(totalpoints) + "!")
        addpoints = input("Do you want to add some points?: ")
        addpoints = addpoints.lower()
        while addpoints.isnumeric():
            print("bruh say yes or no, not numbers..")
            addpoints = input("Do you want to add some points?: ")
        if "yes" in addpoints:
            with open("MicrosoftRewards.txt", "w") as rewards:
                for idx, line in enumerate(lines):
                    if idx != 0:
                        previousadd.append(line.strip())
                newpoints = int(input("How many points did you want to add?: "))
                totalpoints = int(newpoints) + int(totalpoints)
                rewards.write(str(totalpoints))
                rewards.write("\n")
                for x in previousadd:
                    rewards.write(x)
                    rewards.write("\n")    
                rewards.write(str(newpoints))
                print("Your current points has been updated! \nHave a nice day!")
        else:
            removepoints = input("Do you want to remove some points?: ")
            removepoints = removepoints.lower()
            while removepoints.isnumeric():
                print("bruh say yes or no, not numbers..")
            if "yes" in removepoints:
                with open("MicrosoftRewards.txt", "w") as rewards:
                    for idx, line in enumerate(lines):
                        if idx != 0:
                            previoussubtract.append(line.strip())
                        else:
                            rewards.write("")
                    subtractedpoints = int(input("How many points did you want to remove?: "))
                    totalpoints = int(totalpoints) - int(subtractedpoints)
                    rewards.write(str(totalpoints))
                    rewards.write("\n")
                    removelastline = input("Do you wanna remove the number from the file?: ")
                    if "yes" in removelastline and str(subtractedpoints) in previoussubtract:
                        previoussubtract.remove(str(subtractedpoints))
                        #print(previoussubtract)
                    elif str(subtractedpoints) not in previoussubtract:
                        #print(previoussubtract)
                        print("The number you requested to remove is not in the file.")
                    for x in previoussubtract:
                        rewards.write(x)
                        subtractcount = subtractcount + 1
                        if subtractcount != int(len(previoussubtract)):
                            rewards.write("\n") 
                    print("Your current points has been updated! \nHave a nice day!")
            else:
                 average = input("Do you wanna see how many points you gain on average per day from all days?: ")
                 average = average.lower()
                 sum1 = 0
                 count = 0
                 if "ye" in average:
                    with open("MicrosoftRewards.txt", "r") as rewards:
                        for idx, line in enumerate(lines):
                            if idx != 0:
                                sum1 = sum1 + int(line)
                                count = count + 1
                                #rewards.write(line)
                            #else:
                                #rewards.write(totalpoints)
                                #rewards.write("\n")
                                #when I am in "w" mode, I need these lines uncommented
                        mean = int(sum1 / count)
##                      goal = input("Do you have a goal of points you want to get to?")
##                      goal = goal.lower()
##                      if "yes" in goal:
                        #unlikely potential update
                        numbergoal = int(input("What is the point goal you want?: "))
                        pointsleft = numbergoal - int(totalpoints)
                        days = round(pointsleft/mean)
                        #exactdays = pointsleft/mean
                        #if int(days) < int(exactdays):
                            #days = days + 1
                        #potential update for days 
                    print("The Average Amount of Points that you earn per day is " + str(mean) + "!")
                    print("So you will get to your goal in "  + str(days) + " days!")
                 else:
                    average7day = input("Do you wanna see how many points you gain on average from the last 7 days?: ")
                    average7day = average7day.lower()
                    counting = 0
                    if "yes" in average7day:    
                        with open("MicrosoftRewards.txt", "r") as rewards:
                            linecount = len(rewards.readlines())
                            linecountofficial = linecount
                            for idx, line in enumerate(lines):
                                linecount = linecount - 1
                                if linecount <= 6 and idx != 0:
                                        averagedays.append(int(line.strip()))
                            goalnumber = int(input("What is the point goal you want?: "))
                            leftpoints = goalnumber  - int(totalpoints)
                            day = round(leftpoints/(sum(averagedays)/len(averagedays)))
                            print("The Average Amount of Points that you have earned in the last 7 days is " + str(round(sum(averagedays)/len(averagedays))) + "!")                      
                            print("So you will get to your goal in "  + str(day) + " day(s)!")
    printing = input("do you want to run this program?: ")
if printing != "":
    with open("MicrosoftRewards.txt") as rewards:
            lines = rewards.readlines()
            totalp = lines[0].strip()
            print("You currently have " + totalp + " points! Have a nice day!")

                            #print(averagedays)
                            #update 1.0 released officially on July 17th 2021, still had fixes to do then
                            #update 1.1 released officially on July 24th 2021, added taking the average of the last 7 days accumlated points or less if there was less days than 7.
                            #for trial and error
                            #for updates maybe add having the chance to do multiple commands in
                            #one run of the code (fixed)
                            #as well as maybe add a specific date of the goals like August 2nd 2021 or August 10th 2021
                            #achieved first amazon.com gift card $10 on 7/25/21, and I got oni phantom ayy
                            #update 1.2 added, now you can run code once and do multiple runs of the code at once using a while loop.
                            #you don't need to run program everytime you want to do something again or new. Fixed some bugs with removing number from file.(Added August 20th/21st 2021)
                            #soontm August 6th 2022?
            
                            
                    
#yup 6/9/23