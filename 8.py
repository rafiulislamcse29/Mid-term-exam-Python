# You need to handle the errors, for example-				
# If someone gives a wrong id of a show
# If someone tries to book a seat that is invalid
# If someone tries to book a seat that is already booked


class Hall:
  def __init__(self,rows,cols,hall_no) -> None:
    self.seats={}
    self.show_list=[]
    self.rows=rows
    self.cols=cols
    self.hall_no=hall_no
  
  def entry_show(self,id,movie_name,time):
    self.show_list.append((id,movie_name,time))
    self.seats[id] = [[0 for _ in range(self.cols)] for _ in range(self.rows)]

  def book_seats(self,id,seat_list):
    if id in self.seats:
      for row,col in seat_list:
        if 0 <= row < self.rows and 0 <= col < self.cols: 
          if self.seats[id][row][col]==0:
            self.seats[id][row][col]=1
          else:
            print("Already Booked")
        else:
          print("invalid id")
    else:
      print("invalid id")

  def view_show_list(self):
    if not self.show_list:
      print("No shows currently running.")
      return
    print("Current shows running:")
    
    for id,movie_name,time in self.show_list:
      print(f"ID: {id}, Movie: {movie_name}, Time: {time}")
  
  def view_available_seats(self,id):
      if id in self.seats:
        print(f"Available set for shoe ID {id}:")
        available_seats=[]
        for row in range(self.rows):
          for col in range(self.cols):
            if self.seats[id][row][col]==0:
              available_seats.append((row,col))
        
        for row, col in available_seats:
          print(f"Row {row}, Seat {col}")
        else:
          print("No available seats.")

      else:
        print("Invalid Show ID")


hall1=Hall(5,5,1)
hall1.entry_show("abc","Spider Man 1","09:00 AM")
hall1.entry_show("xyz","Spider Man 2","12:00 PM")


while True:
  print(f"Welcome Cine Hall!!")
  print("1. View All Show List")
  print("2. Add a new Entry")
  print("3. Booking Seats")
  print("4. Avialable Seats")
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
  #  id,seat_list
   id=input("Enter id: ")
   row=int(input("Enter row: "))
   col=int(input("Enter col: "))
   hall1.book_seats(id, [(row, col)])
   print(hall1.seats[id])
  elif choice == 4:
    id=input("Enter id: ")
    hall1.view_available_seats(id)
  elif choice == 5:
    break
  else:
    print("Invalid Input")
