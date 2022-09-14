### `Exercise 1` even or odd

#siffra = int(input("Skriv en siffra: "))
#if siffra % 2 == 0:
#    print("Even")
#else:
#    print("Odd") 

### `Exercise 2` VIP

#vip_check = str(input("Hej, skriv in ditt namn för att se om du står på listan: "))
#vip_lista = ("Marc", "Adam", "Victor", "Christian", "Martin")

#if vip_check in vip_lista:
#    print("You are on the list!")
#else:
#    print("Sorry, you are not on the list!")

### `Exercise 3` Repeat word

#word = str(input("Please say something: "))

#for w in range(len(word)):
#    print(word)

### `Exercise 4` Sum

#start_nr = int(input("Please input start nr: "))
#stop_nr = int(input("Please input stop nr: "))

#total = 0
#for i in range(start_nr, stop_nr):
#    print(i)
#    total += i
  
#print("Sum: ", total)

### `Exercise 5` Until stop

while True:
    safe_word = input("Just say stop and i'll stop! ")
    if safe_word == "stop":
        break
    print(f"{safe_word} is {len(safe_word)} letters long and totally or slightly the wrong word!")


