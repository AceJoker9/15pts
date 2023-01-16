import random

location = ["oakland", "seattle", "san jose", "san diego", "boston", "detroit"]
destination = (random.choice (location))

eat_eat = [ "tacos", "seafood gallery", "coney island", "steakhouse", "roscos"]
restuarant = (random.choice(eat_eat))

fun_time = ["paintball", "movies", "naked wrestling", "bowling", "hookah"]
entertianment = (random.choice(fun_time))

wheels = ["jet", "viper", "hellcat", "infiniti coupe", "yukon",]
transportation = (random.choice(wheels))
round_trip = ["landscape:", "food:", "event:", "vehicle:"]

def arrival(city):
    good_choice = input("Do you want to travel here?")
    for i in destination:
        print(destination, good_choice)
        if good_choice == "yes":
            round_trip.append(destination[0])
        return(destination)




