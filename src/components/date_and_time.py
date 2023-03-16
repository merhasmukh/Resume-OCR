from datetime import datetime



def getDate():
    try:
        date_now=datetime.now().date().strftime("%m-%d-%Y")

        return date_now
    except Exception as e:
        return str(e)
    
def getTime():
    try:
        time_now=datetime.now().time().strftime("%H:%M:%S")
        return time_now
    except Exception as e:
        return str(e)

print(getDate())
print(getTime())
