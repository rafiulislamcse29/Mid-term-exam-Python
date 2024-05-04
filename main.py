class Star_Cinema:
  __hall_list=[] 

  @classmethod
  def entry_hall(cls, hall):
    cls.__hall_list.append(hall)
  
  @classmethod
  def get_show_halls(cls):
      return cls.__hall_list
 

class Hall(Star_Cinema):
  def __init__(self,rows,cols,hall_no) -> None:
    super().entry_hall(self)
    self.__seats={}
    self.__show_list=[]
    self._rows=rows
    self._cols=cols
    self._hall_no=hall_no
  
  def entry_show(self,id,movie_name,time):
    if id in self.__seats:
      print("Show Already running")
      return
    self.__show_list.append((id,movie_name,time))
    self.__seats[id] = [[0 for _ in range(self._cols)] for _ in range(self._rows)]

  def book__seats(self,id,seat_list):
    if id in self.__seats:
      for row,col in seat_list:
        if 0 <= row < self._rows and 0 <= col < self._cols: 
          if self.__seats[id][row-1][col-1]==0:
            self.__seats[id][row-1][col-1]=1
          else:
            print("Already Booked")
        else:
          print("invalid id")
    else:
      print("invalid id")

  def view_show_list(self):
    if not self.__show_list:
      print("No shows currently running.")
      return
    
    print("Current shows running:")
    for id,movie_name,time in self.__show_list:
      print(f"ID: {id}, Movie: {movie_name}, Time: {time}")
  
  def view_available_seats(self,id):
      if id in self.__seats:
        print(f"Available set for shoe ID {id}:")
        for row in range(self._rows):
          print(self.__seats[id][row])
      else:
        print("Invalid Show ID")


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
