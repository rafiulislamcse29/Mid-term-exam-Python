from cinema import Star_Cinema
from hall import Hall


hall1=Hall(5,5,1)
hall1.entry_show("abc","Spider Man 1","09:00 AM")
hall1.entry_show("xyz","Spider Man 2","12:00 PM")



while True:
  print(f"Welcome Cine Hall!!")

  print("1. View All Show List")
  print("2. Add a new Entry")
  print("3. Booking seats")
  print("4. Avialable seats")
  print("5. Exit")
      
  choice = int(input("Enter Your Choice : "))
  if choice == 1:
   hall1.view_show_list() 
  elif choice == 2:
   id=input("Enter id: ")
   movie_name=input("Movie Name: ")
   time=input("start show time: ")
   hall1.entry_show(id,movie_name,time)
  elif choice == 3:
   id=input("Enter id: ")
   row=int(input("Enter row: "))
   col=int(input("Enter col: "))
   hall1.book__seats(id, [(row, col)])
   hall1.view_available_seats(id)
  elif choice == 4:
    id=input("Enter id: ")
    hall1.view_available_seats(id)
  elif choice == 5:
    break
  else:
    print("Invalid Input")
