import random

location = ["oakland", "seattle", "san jose", "san diego", "boston", "detroit"]
destination = random.choice(location)

eat_eat = ["tacos", "seafood gallery", "coney island", "steakhouse", "roscos"]
restuarant = (random.choice(eat_eat))

fun_time = ["paintball", "movies", "naked wrestling", "bowling", "hookah"]
entertianment = (random.choice(fun_time))

wheels = ["jet", "viper", "hellcat", "infiniti coupe", "yukon",]
transportation = (random.choice(wheels))

round_trip = []



def arrival():

    isHappy = False
    while isHappy == False:
        destination = (random.choice(location))
        print(f"Your destination is {destination}")
        good_choice = input("Do you want to travel here?")
        if good_choice == "yes":
            round_trip.append(destination)
            print("Awesome.", round_trip)
            isHappy = True
        else:
            continue

    return(destination)
    
arrival()


#Im attemping to perform a function where itye will print a random city location and upon agreement, it will be added to a list


def dinner():
    isHappy = False
    while isHappy == False:
        restuarant = (random.choice(eat_eat))
        print(f"Your date is {restuarant}")
        good_date = input("Do you want to eat here?")
        if good_date == "yes":
            round_trip.append(restuarant)
            print("Good Date Idea", round_trip)
            isHappy = True
        else:
            continue

        return(restuarant)
    
dinner()






