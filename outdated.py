def main():
     while True:
                try:
                    date=input("Date: ")
                    if "/" in date:
                        month,day,year=date.split("/")
                    else:
                        month,day,year=date.replace(",","").split(" ")
                    month=convert(month)
                    month,day=int(month),int(day)
                    if 0<month<=12 and 0<day<=31:
                        print(f"{year}-{month:02}-{day:02}")
                        break
                except ValueError:
                    pass

def convert(month):
    months=[
            "January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December"
            ]
    try:
        m=months.index(month)
        return m+1
    except ValueError:
         return month
main()
