# Make a class named Star_Cinema which will have one class attribute named hall_list which is an empty list initially. Make a method named entry_hall() to insert an object of class Hall (Described below) inside its hall_list. 

class Star_Cinema:
  hall_list=[]  #class attribute

  def entry_hall(self,hall):
    self.hall_list.append(hall)

class Hall:
  def __init__(self,hall_name) -> None:
    self.hall_name=hall_name

  def hall_name(self):
        return self.hall_name
  
hall1=Hall("Rup kotha")
hall2=Hall("Sun Mon")

star_cinema=Star_Cinema()
star_cinema.entry_hall(hall1)
star_cinema.entry_hall(hall2)

for hall in star_cinema.hall_list:
    print(hall.hall_name)

