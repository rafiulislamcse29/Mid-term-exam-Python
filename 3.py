# Make a method in Hall class named entry_show() which will take id, movie_name and time in string format. Make a tuple with all of the information and append it to the show_list attribute. Allocate seats with rows and cols using 2d list, initially all seats will be free. Make a key with id to the attribute seats and value will be the 2d list.

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

hall1=Hall(10,20,1)
hall1.entry_show("abc","Spider Man ","09:00 AM")
hall1.entry_show("xyz","Spider Man 2","12:00 PM")


print("Show List",hall1.show_list)
print("Seats for abc movie",hall1.seats['abc'])
print("Seats for xyz movie",hall1.seats['xyz'])