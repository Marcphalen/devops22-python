'''Exercise 1 and 2

firstname = "marc"
lastname = "phalen"
tele = "00468123456789"
fullname = (firstname + " " + lastname)

#print(f"Name: {firstname}, Surname: {lastname}, Phone nr: {tele}")
#print(fullname)
#print(len(fullname + firstname + lastname)-1)
#print(f"Name: {fullname} \n{tele}")

#print(fullname + " " + tele)
#print(f"{fullname} {tele}")
#print('{}'.format(fullname),'{}'.format(tele))
#print('Name: %s' % fullname, 'with phone nr: %s' % tele)

#print(fullname[:5])
#print(fullname[::2])
#print(fullname[::-1])
#print(fullname[5:5])
'''
'''Exercise 3
lyxbil = 5000

bilpris = int(input("Vad kostar din bil?: "))
if bilpris >= lyxbil:
    print("\N{smiling face with halo}")
print(f"Din bil kostar: \u20ac{bilpris}")
'''

#Exercise 4
from locale import currency


salary = 2500
currency = 'EUR'
print(f"You recieve {salary} {currency} per month")

salary_request = int(input("How much more do you request?: "))
percentage_increase = salary_request / salary * 100

q = True
print(f"Hmm, {percentage_increase}% is a bit much. You have to go lower!")
salary_request_2 = int(input("Please input a lower request."))
decision_x = "Yes!"
decision_y = "No!"
new_salary_increase = salary_request_2 / salary *100

if new_salary_increase <= 20:
    print(f"Well that's a big {decision_x}")

else:
    print(f"Well I have to give you a {decision_y}")
    