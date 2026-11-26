# Prequisites
import time
from time import sleep
import os
import platform

# Asciis
mascii=
"""
 ____   __    __  __ _     __     ____   ___  _  _  ____  ____  _  _  __    ____ 
(  _ \ /  \  /  \(  / )   / _\   / ___) / __)/ )( \(  __)(    \/ )( \(  )  (  __)
 ) _ ((  O )(  O ))  (   /    \  \___ \( (__ ) __ ( ) _)  ) D () \/ (/ (_/\ ) _) 
(____/ \__/  \__/(__\_)  \_/\_/  (____/ \___)\_)(_/(____)(____/\____/\____/(____)

"""
oascii=
"""
   ___                  
  /___\_ __   ___ _ __  
 //  // '_ \ / _ \ '_ \ 
/ \_//| |_) |  __/ | | |
\___/ | .__/ \___|_| |_|
      |_|               

"""
cascii=
"""
   ___ _                    _ 
  / __\ | ___  ___  ___  __| |
 / /  | |/ _ \/ __|/ _ \/ _` |
/ /___| | (_) \__ \  __/ (_| |
\____/|_|\___/|___/\___|\__,_|
                              

"""
ttascii=
"""
   ___              _                        _                   
  / __|   __ _     | |     ___    _ _     __| |   __ _      _ _  
 | (__   / _` |    | |    / -_)  | ' \   / _` |  / _` |    | '_| 
  \___|  \__,_|   _|_|_   \___|  |_||_|  \__,_|  \__,_|   _|_|_  
_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""|_|"""""| 
"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-'"`-0-0-' 

"""

Bn = 0 # Building number
Rn = 0 # Room number
oh = 18 # Operational hours (Max 24)
BA = [[(i+1) for i in range(Bn)],[],[],[],[],[],[(oh) for j in range(Bn)],[],[]] # Building Array
sh = 4 # Opening hour
ch = sh+oh # Closing hour
opt = [] # Options array 
mo = ["January", "February", "March", "August", "May", "June", "July", "August", "September", "October", "November", "December"]
td = "12/02/25" # Today's date

def cc(): # Console clearing function
    oss = platform.system()
    if oss=="Windows":
        os.system("cls")
    elif oss=="Darwin" or oss=="Linux":
        os.system("clear")

# Room array populating
for i in range(Bn):
    po=[(j+1) for j in range(Rn)]
    BA[1].append(po)

# Starting hour and hours populating
for l in range(4):
    m=l+2
    for i in range(Bn):
        BA[m].append([])
        for j in range(Rn):
            BA[m][i].append([])

# Options Array
for m in range(3):
    opt.append([])

# Date free building availability
def od(inp,arr): 
    arr[7].append(inp)
    arr[8].append(["FREE" for i in range(Bn)])

# Validating if an input is integer or not (For non-main functions)
def icc(num): 
    if(num!="q" and num!="c" and num!="n"): # If the input is not meant to quit the program
        try:
            int(num)
        except ValueError:
            return "FAIL" 
        else:
            return "INT"
    elif(num=="n"):
        return "SKIP"
    else:
        return "SIGINT"

# Validating if an input is integer or not (For main function)
def icm(num): 
    if(num!="q" and num!="c"): # If the input is not meant to quit the program
        try:
            int(num)
        except ValueError:
            return "FAIL" 
        else:
            return "INT"
    else:
        return "SIGINT"

# Month validator
def mv(m): 
    if((str(m).title()) in mo):
        return "VALID"

# Date validator
def dv(d,m,y): 
    stat="INVALID"
    if(d>0):
        if(m=="February"): # Leap year
            if(y%4==0 and d<=29):
                stat="VALID"
            elif(y%4!=0 and d<=28):
                stat="VALID"
        elif(((mo.index(m)+1)%2)==0 and d<=31):
            stat="VALID"
        elif(((mo.index(m)+1)%2)!=0 and d<=30):
            stat="VALID"
    return stat


# Number format to date
def ntd(mode, date): 
    if(mode=="f"):
        return ((date[0]+date[1])+" "+str(mo[int(date[3]+date[4])-1])+" "+("20"+date[5]+date[6]))
    if(mode=="y"):
        return ("20"+date[5]+date[6])
    if(mode=="m"):
        return str(mo[int(date[3]+date[4])-1])
    if(mode=="d"):
        return (date[0]+date[1])

# Date to number format
def dtn(mode, inp): 
    end=""
    if(mode=="y"):
        end=str(inp)[2]+str(inp)[3]
    if(mode=="m"):
        if(mo.index((inp.title()))+1<10):
            end=("0"+str(mo.index(inp.title())+1))
        else:
            end=str(mo.index(inp.title())+1)
    if(mode=="d"):
        end=str(inp)
    return end

# Year validator
def yv(year):
    stat="INVALID"
    if(year<3000 and year>=2000):
        if(year>=int(ntd("y", td))):
            stat="VALID"
    return stat

# Total validator
def tv(date):
    invalid="NONE"
    if(len(date)!=8):
        invalid="FORMAT"
    elif(yv(ntd("y", date))!="VALID"):
        invalid="YEAR"
        if(mv(ntd("m", date))!="VALID"):
            invalid="MONTH"
            if(dv(ntd("d", date), ntd("m", date), ntd("y", date))!="VALID"):
                invalid="DATE"
    return invalid

# Fully free building
def fb(arr, num, date, hour): 
    vi = False
    while(vi==False): # Input loop
        cc()
        print(f"Building {num} is fully free")
        hc = input(f"Please type the starting hour you want to book ({sh}-{ch-hour}) [c to cancel | n to pick other building]: ")
        # Starting hours input section
        # ----------------------------
        if(icc(hc)=="INT" and (int(hc)>=sh) and (int(hc)<=(ch-hour))): # Starting hours correct input
            while(vi==False):
                room=input(f"Please type the room number desired (1-{Rn}) [c to cancel]: ")
                # Room input section
                # ------------------
                if(icc(room)=="INT" and (int(room)>0) and (int(room)<=Rn)): # Room correct input
                    name=str(input("Please type the booker's name: "))
                    print(f"Okay Mr./Mrs./Ms. {name}, your booking has been made between {hc}-{int(hc)+hour}")
                    # Input everything to building array
                    arr[2][num-1][int(room)-1].append(hc)
                    arr[3][num-1][int(room)-1].append(hour)
                    arr[4][num-1][int(room)-1].append(name)
                    arr[5][num-1][int(room)-1].append(date)
                    arr[6][num-1]=int(arr[6][num-1])-hour
                    if(date not in arr[7]):
                        od(date, arr)
                    arr[8][arr[7].index(date)][int(num)-1]="OCCUPIED"
                    print(arr)
                    opt.clear()
                    vi=True
                elif(icc(room)=="FAIL"): # Room invalid input
                    print("Input must be a whole number!")
                    time.sleep(2)
                elif(icc(room)=="SIGINT"): # Room break
                    vi=True
                    print("Booking cancelled.")
                    time.sleep(3)
                else: # Room out of range
                    print("Input must be in the range given!")
                    time.sleep(2)
                # --------------------
        elif(icc(hc)=="FAIL"): # Starting hours invalid input
            print("Input must be a whole number!")
        elif(icc(hc)=="SIGINT"): # Starting hours break
            print("Booking cancelled.")
            vi=True
        elif(icc(hc)=="SKIP"): # Skip to the next building
            print("Picking other building")
            opt[0].append(f"{num}")
            opt[1].append(f"FBN")
            opt[2].append(f"{sh}")
            return "PICK"
        else: # Hours out of range
            print("Input must be in the range given!")
        # ------------------------------

# Occupied building
def nfb(arr, num, date, hour):
    shp=sh
    for i in range(Rn):
        if not arr[2][num-1][i]: # Empty Schedule Room
            reps=(oh%hour)
            for k in range(reps):
                opt[0].append(f"{num}")
                opt[1].append(f"{Rn+1}")
                opt[2].append(f"{shp}")
        else: # Non empty schedule room
            move=False
            for j in range(len(arr[5][num-1][i])):
                if(arr[5][num-1][i][j]==date):
                    while(shp<oh):
                        if(shp!=arr[2][num-1][i][j]):
                            if((shp+hour)<=arr[2][num-1][i][j]):
                                opt[0].append(f"{num}")
                                opt[1].append(f"{Rn+1}")
                                opt[2].append(f"{shp}")
                                shp+=hour
                            else:
                                move=True
                        else:
                            move=True
                        if(move==True):
                            shp=arr[3][num-1][i][j]
                            move=False
                shp=sh

# Choosing an option (non free)
def choice(arr, date, hour):
    if not arr[0]: # All buildings are full
        cc()
        print(f"Sorry, all buildings are full at the date you chose ({ntd("f", date)})")
        time.sleep(1)
        print("Please try on another date.")
        time.sleep(3)
    else:
        vav=False
        while(vav==False):
            cc()
            optn=0
            for q in range(arr[0]): # Printing options
                optn=q
                if(arr[1][q]=="FBN"): # Free building
                    print(f"[{q+1}] Building {arr[0][q]} (Full day)")
                else: # Specific hour ranges.
                    print(f"[{q+1}] Building {arr[0][q]} | Room {arr[1][q]} -> {arr[2][q]}.00 - {arr[2][q]+hour}.00")
            
            cho=int(input(f"Please pick an option using the option's number. 1-{optn}: "))
            # Input verifier
            if(icm(cho)=="INT" and (cho>0) and (cho<=optn)): 
                name=str(input("Please enter the booker's name: "))
                print(f"Okay Mr./Mrs./Ms. {name}, your booking has been made between {arr[2][cho-1]}-{arr[2][cho-1]+hour}")
                # Input everything to building array
                arr[2][num-1][int(room)-1].append(arr[2][cho-1])
                arr[3][num-1][int(room)-1].append(hour)
                arr[4][num-1][int(room)-1].append(name)
                arr[5][num-1][int(room)-1].append(date)
                arr[6][num-1]=int(arr[6][num-1])-hour
                vav=True
                time.sleep(5)
            elif(icm(cho)=="FAIL"): 
                print("Input must be a whole number!")
                time.sleep(2)
            elif(icm(cho)=="SIGINT"):
                vav=True
                print("Booking cancelled.")
                time.sleep(2)
            else: 
                print("Input must be in the range given!")
                time.sleep(2)

# Building booking
def book(arr, num, date, hour):
    rotate=True
    while(rotate==True): # Loop
        cc()
        if(date.title()=="Today"): # If the date picked is today
            date=td
            if(arr[5][num-1]==oh): # Free building
                fb(arr,num,date,hour)
            elif(hours>arr[5][num-1]): # Full building
                print(f"Building {num} is full")
                if(num==Bn):
                    print("Moving to the next building")
                    time.sleep(3)
                else:
                    choice(arr,date,hour)
            else:
                nfb(arr,num,date,hour)
                choice(arr,date,hour)
            rotate=False
        else: # Another date
            if(date in arr[7]): # Free building
                if(arr[8][arr[7].index(date)][num-1]=="FREE"):
                    fb(arr,num,date,hour)
                    rotate=False
                else: # Occupied Building
                    nfb(arr,num,date,hour)
                    choice(arr,date,hour)
                    rotate=False
            else:
                fb(arr,num,date,hour)
                rotate=False

# Main function
main=True
opcl="OPEN"
ct=sh
while(main==True):
    cc()
    print(mascii)
    if(opcl=="OPEN"):
        print(oascii)
        print(f"We are open from {sh}.00-{sh+oh}.00")
    else:
        print(cascii)
        print(f"We are currently closed")
        print(f"Booking and calendar feature can be used only on the opening hours between {sh}.00-{sh+oh}.00")
    print(f"Current time: {ct}.00")
    
    for i in range(Bn): # Booking cleaner
        for j in range(Rn):
            for k in range(len(BA[2][i][j])):
                if(td==(BA[5][i][j][k])):
                    if(ct==(BA[2][i][j][k]+BA[3][i][j][k])):
                        BA[6][i]+=BA[3][i][j][k]
                        BA.remove(BA[2][i][j][k])
                        BA.remove(BA[3][i][j][k])
                        BA.remove(BA[4][i][j][k])
                        BA.remove(BA[5][i][j][k])
    if(td in BA[7]): # Occupied Status Cleaner After Today's Date is fulfilled
        indx=BA[7].index(td)
        BA[7].remove(td)
        BA[8].remove(BA[8][indx])

    mai=str(input("'Book' to book a schedule | 'Calendar' to view the occupied schedule | 'Quit' to quit the program | Enter to pass time: "))
    if(mai.title()=="Book"):
        vdi=False
        dp=""
        while(vdi==False):
            cc()
            din=str(input("Please enter the date of your booking in the format of dd/mm/yy ['Today' for today's date] ['c' to Cancel Booking]: "))
            if(din=="Today"):
                dp="Today"
                vdi=True
            elif(tv(din)=="FORMAT"):
                print("Invalid date format!")
                time.sleep(2)
            elif(tv(din)=="YEAR"):
                print("Year must be below 3000 and above 2000!")
                time.sleep(2)
            elif(tv(din)=="MONTH"):
                print("Invalid month!")
            elif(tv(din)=="DAY"):
                print("Invalid date! Check the month and year inputted.")
            else:
                dp=din
                vdi=True
        vhi=False
        hi=""
        while(vhi==False):
            cc()
            hin=str(input(f"Enter the duration of the booking in hour(s) [1-{oh}] ['c' to cancel]: "))
            if(icm(hin)=="INT" and (hin>0) and (hin<=oh)): 
                for i in range(Bn):
                    book(BA,i,dp,int(hin))
                    cc()
                opt[0].clear()
                opt[1].clear()
                opt[2].clear()
                time.sleep(5)
            elif(icm(hin)=="FAIL"): 
                print("Input must be a whole number!")
                time.sleep(2)
            elif(icm(hin)=="SIGINT"):
                vav=True
                print("Booking cancelled.")
                time.sleep(2)
            else: 
                print("Input must be in the range given!")
                time.sleep(2)
    elif(mai.title()=="Calendar"):
        print(ttascii)
        j
    ct+=1
    if(ct==24):
        ct=0
