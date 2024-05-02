class Star_Cinema:
  __hall_list=[] 

  
  @classmethod
  def entry_hall(cls, hall):
    cls.__hall_list.append(hall)
  
  @classmethod
  def get_show_halls(cls):
      return cls.__hall_list
 