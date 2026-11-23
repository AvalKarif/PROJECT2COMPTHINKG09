Bn = 3 # Building number
Rn = 4 # Room number
oh = 18 # Operational hours (Max 24)
BA = [[(i+1) for i in range(Bn)],[],[],[],[],[],[(oh) for j in range(Bn)],[],[]] # Array Building 1
hours = 3 # How many hours the user wants to book
sh = 4 # Opening hour
ch = sh+oh # Closing hour
opt = [] # Options array
mo = ["January", "February", "March", "August", "May", "June", "July", "August", "September", "October", "November", "December"]
td = "12/02/25" # Today's date

# Room array populating
for i in range(Bn):
    po=[(j+1) for j in range(Rn)]
    BA[1].append(po)

# Starting hour and hours populating
for l in range(Rn):
    m=l+2
    for i in range(Bn):
        BA[m].append([])
        for j in range(Rn):
            BA[m][i].append([])
# Date populating
for o in range(Rn):
    m=o+5
    for i in range(Bn):
        BA[m].append([])
        for j in range(Rn):
            BA[m][i].append([])

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
def icc(num): 
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
def dv(m,d,y): 
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
    if(year<3000 or year>=2000):
        if(year>=int(ntd("y", td))):
            stat="VALID"
    return stat

# Fully free building
def fb(arr, num, date): 
    vi = False
    while(vi==False): # Input loop
        print(f"Building {num} is fully free")
        hc = input(f"Please type the starting hour you want to book ({sh}-{ch-hours}) [c to cancel | n to pick other building]: ")
        # Starting hours input section
        # ----------------------------
        if(icc(hc)=="INT" and (int(hc)>=sh) and (int(hc)<=(ch-hours))): # Starting hours correct input
            while(vi==False):
                room=input(f"Please type the room number desired (1-{Rn}) [c to cancel]: ")
                # Room input section
                # ------------------
                if(icc(room)=="INT" and (int(room)>0) and (int(room)<=Rn)): # Room correct input
                    name=str(input("Please type the booker's name: "))
                    print(f"Okay Mr./Mrs./Ms. {name}, your booking has been made between {hc}-{int(hc)+hours}")
                    # Input everything to building array
                    arr[2][num-1][int(room)-1].append(hc)
                    arr[3][num-1][int(room)-1].append(hours)
                    arr[4][num-1][int(room)-1].append(name)
                    arr[5][num-1][int(room)-1].append(date)
                    arr[6][num-1]=int(arr[6][num-1])-hours
                    if(date not in arr[7]):
                        od(date, arr)
                    arr[8][arr[7].index(date)][int(num)-1]="OCCUPIED"
                    print(arr)
                    opt.clear()
                    vi=True
                elif(icc(room)=="FAIL"): # Room invalid input
                    print("Input must be a whole number!")
                elif(icc(room)=="SIGINT"): # Room break
                    vi=True
                    print("Booking cancelled.")
                else: # Room out of range
                    print("Input must be in the range given!")
                # --------------------
        elif(icc(hc)=="FAIL"): # Starting hours invalid input
            print("Input must be a whole number!")
        elif(icc(hc)=="SIGINT"): # Starting hours break
            print("Booking cancelled.")
            vi=True
        elif(icc(hc)=="SKIP"): # Skip to the next building
            print("Picking other building")
            opt.append(f"{num} (Full day)")
            return "PICK"
        else: # Hours out of range
            print("Input must be in the range given!")
        # ------------------------------

# Occupied building
def nfb(arr,num):
    shp=sh
    #for i in range(oh):
     #   if(shp not in arr[3][num]

# Building checker
def check(arr, num, date):
    if(date.title()=="Today"):
        date=td
        if(arr[5][num]==oh):
            fb(arr,num,date)
        elif(hours>arr[5][num]):
            print(f"Building {num} is full")
            if(num==Bn):
                print("Moving to the next building")
    else:
        if(date in arr[7]):
            if(arr[8][arr[7].index(date)][num-1]=="FREE"):
                fb(arr,num,date)
            else:
                nfb
        else:
            fb(arr,num,date)

#print(dtn("d", 12)+dtn("m", "January")+dtn("y", 2013))
fb(BA, 2, td)
