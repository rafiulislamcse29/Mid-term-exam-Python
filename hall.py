from cinema import Star_Cinema

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
