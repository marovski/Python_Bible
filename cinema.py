films={"Finding Dory":[3,5],
       "Tarzan":[18,5],
       "Django":[18,9]}

while 1:
    choice=input("What film do you wish to watch?: ").strip().title()

    if choice in films:
        age=input("What is your age?: ").strip()
        if int(age) >= films[choice][0]:
            ticket=int(input("How many tickets?: ").strip())
            if films[choice][1] >= ticket:
                print("Thank you! Have great session!")
                films[choice][1]-=ticket
            else:
                print("Sorry, but there's isn't enough seats available.")
        else:
            print("The film is not recommend for your age! Please choose again.")
    

    else:
        print("We don't have the film available!")
    
