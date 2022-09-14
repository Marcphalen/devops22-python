from operator import itemgetter


suspects = []

name_1 = input("Hi, please enter the name of person_1: ").lower()
age_1 = int(input("And now please enter the age of person_1: "))
shoe_1 = float(input("What is person_1's shoe size?: "))
person_1 = (name_1, age_1, shoe_1)
suspects.append(person_1)

name_2 = input("Hi, please enter the name of person_2: ").lower()
age_2 = int(input("And now please enter the age of person_2: "))
shoe_2 = float(input("What is person_2's shoe size?: "))
person_2 = (name_2, age_2, shoe_2)
suspects.append(person_2)

name_3 = input("Hi, please enter the name of person_3: ").lower()
age_3 = int(input("And now please enter the age of person_3: "))
shoe_3 = float(input("What is person_3's shoe size?: "))
person_3 = (name_3, age_3, shoe_3)
suspects.append(person_3)

sorted_shoe_size = sorted(suspects, key=itemgetter(1))
sorted_age = sorted(suspects, key=itemgetter(2))

oldest = sorted_age[2]
median_size = sorted_shoe_size[1]

print(f"The oldest person is: {oldest[0].capitalize()}, with a shoe size of: {oldest [2]}")
print(f"The person with the median shoe size is: {median_size[0].capitalize()}, Age: {median_size[1]}")

searches = {
    "age":{
        str(age_1): person_1,
        str(age_2): person_2,
        str(age_3): person_3,
    },
    "shoe": {},
    "name": {}
}

prop, value = input("Enter prop value: ").split(" ")
print(searches[prop][value])

