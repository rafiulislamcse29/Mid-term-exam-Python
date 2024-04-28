# Make the information of the classes as protected/private as you can so that the attributes can’t be accessed outside the class.	


class Hall:
  def __init__(self,rows,cols,hall_no) -> None:
    self._seats={}
    self._show_list=[]
    self._rows=rows
    self._cols=cols
    self._hall_no=hall_no
  
  def entry_show(self,id,movie_name,time):
    self._show_list.append((id,movie_name,time))
    self._seats[id] = [[0 for _ in range(self._cols)] for _ in range(self._rows)]

  def book_seats(self,id,seat_list):
    if id in self._seats:
      for row,col in seat_list:
        if 0 <= row < self._rows and 0 <= col < self._cols: 
          if self._seats[id][row][col]==0:
            self._seats[id][row][col]=1
          else:
            print("Already Booked")
        else:
          print("invalid id")
    else:
      print("invalid id")

  def view__show_list(self):
    if not self._show_list:
      print("No shows currently running.")
      return
    print("Current shows running:")
    
    for id,movie_name,time in self._show_list:
      print(f"ID: {id}, Movie: {movie_name}, Time: {time}")
  
  def view_available_seats(self,id):
      if id in self._seats:
        print(f"Available set for shoe ID {id}:")
        available__seats=[]
        for row in range(self._rows):
          for col in range(self._cols):
            if self._seats[id][row][col]==0:
              available__seats.append((row,col))
        
        for row, col in available__seats:
          print(f"Row {row}, Seat {col}")
        else:
          print("No available _seats.")

      else:
        print("Invalid Show ID")


hall1=Hall(5,5,1)
hall1.entry_show("abc","Spider Man 1","09:00 AM")
hall1.entry_show("xyz","Spider Man 2","12:00 PM")


while True:
  print(f"Welcome Cine Hall!!")
  print("1. View All Show List")
  print("2. Add a new Entry")
  print("3. Booking _seats")
  print("4. Avialable _seats")
  print("5. Exit")
      
  choice = int(input("Enter Your Choice : "))
  if choice == 1:
   hall1.view__show_list() 
  elif choice == 2:
   id=input("Enter id: ")
   movie_name=input("Movie Name: ")
   time=input("start show time: ")
   hall1.entry_show(id,movie_name,time)
  elif choice == 3:
  #  id,seat_list
   id=input("Enter id: ")
   row=int(input("Enter row: "))
   col=int(input("Enter col: "))
   hall1.book_seats(id, [(row, col)])
   print(hall1._seats[id])
  elif choice == 4:
    id=input("Enter id: ")
    hall1.view_available_seats(id)
  elif choice == 5:
    break
  else:
    print("Invalid Input")
