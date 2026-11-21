Bn = 3 # Building number
Rn = 4 # Room number
oh = 18 # Operational hours (Max 24)
BA = [[(i+1) for i in range(Bn)],[],[],[],[],[],[(oh) for j in range(Bn)]] # Array Building 1
hours = 3 # How many hours the user wants to book
sh = 4 # Opening hour
ch = sh+oh # Closing hour
opt = [] # Options array
mo = ["January", "February", "March", "August", "May", "June", "July", "August", "September", "October", "November", "December"]
td = "171126"

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

def icc(num): # Validating if an input is integer or not (For non-main functions)
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

def mv(m):
    if((str(m).title())=="Today"):
        return "TODAY"
    elif((str(m).title()) in mo):
        return "VALID"

def fb(arr, num): # Fully free building
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
                    arr[2][num-1][int(room)-1].append(sh)
                    arr[3][num-1][int(room)-1].append(hours)
                    arr[4][num-1][int(room)-1].append(name)
                    arr[5][num-1]=int(arr[5][num-1])-hours
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

def nfb(arr,num):
    shp=sh
    #for i in range(oh):
     #   if(shp not in arr[3][num]

def check(arr, num):
    da=str(input("Type in the intended date of the booking"))
    if(arr[5][num]==oh):
        #if
        fb(arr,num)
    elif(hours>arr[5][num]):
        print(f"Building {num} is full")
        if(num==Bn):
            print("Moving to the next building")

#fb(BA, 1)
