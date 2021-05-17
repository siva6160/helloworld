import calendar
y=int(input("enter the year"))
c=calendar.Textcalendar(calendar.SUNDAY)
i=1
while i<=12:
    c.prmonth(y,i)
    i+=1
    
