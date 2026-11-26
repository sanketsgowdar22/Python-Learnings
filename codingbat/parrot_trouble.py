def parrot_trouble(talking, hour):
  if (0 < hour <= 23):
      if talking and (hour < 7 or hour > 20):
          return True
      else:
          return False
      

# print(parrot_trouble(True, 6))
# print(parrot_trouble(True, 7)) 
# print(parrot_trouble(False, 6)) 
print(parrot_trouble(False, 23)) 
print(parrot_trouble(True, 23)) 
