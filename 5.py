# Make a method in Hall class named view_show_list() which will view all the shows running.

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
        if self.seats[id][row][col]==0:
          self.seats[id][row][col]=1
        else:
          print("already booked")
    else:
      print("invalid id")

  def view_show_list(self):
    if not self.show_list:
      print("No shows currently running.")
      return
    print("Current shows running:")
    
    for id,movie_name,time in self.show_list:
      print(f"ID: {id}, Movie: {movie_name}, Time: {time}")
  

hall1=Hall(10,20,1)
hall1.entry_show("abc","Spider Man 1","09:00 AM")
hall1.entry_show("xyz","Spider Man 2","12:00 PM")

hall1.book_seats("abc", [(1, 1)])
hall1.book_seats("abc", [(5, 1)]) 

hall1.view_show_list() 