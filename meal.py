def main():
   time=input("what is the time: ")
   time=convert(time)
   meal(time)

def convert(time):
   hours,minutes=time.split(":")
   hours= float(hours)
   minutes=float(minutes)
   minutes=minutes/60
   time=hours+minutes
   return time

def meal(time):
   if 7.0 <= time <=8.0 :
      print("breakfast time")
   elif 12.0 <= time <= 13.0 :
      print("lunch time")
   elif 18.0 <= time <= 19.0 :
      print("dinner time")




if __name__ == "__main__":
   main()
