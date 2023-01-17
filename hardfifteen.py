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

def date_option():
    isHappy = False
    while isHappy == False: 
      entertianment = (random.choice(fun_time))
      print(f"Your evening event consist of {entertianment}")
      good_night = input("Do you like this event?")
      if good_night == "yes":
          round_trip.append(entertianment)
          print("Good Evening of Fun!", round_trip)
          isHappy = True
      else: 
          continue

      return(entertianment)

date_option()


def luxury():
    isHappy = False
    while isHappy == False: 
      transportation = (random.choice(wheels))
      print(f"Your ride consist of {transportation}")
      good_wheels = input("Do you like your choice of wheels?")
      if good_wheels == "yes":
        round_trip.append(transportation)
        print("Not bad!!", round_trip)
        isHappy = True
      else:
          continue
      
      return(transportation)
    
luxury()


day_trip = input("Your day trip consist of")
epic_night = input("Enjoy The Experience! Take plenty of pictures")
round_trip = []
print("day_trip", "round_trip", "epic_night")






