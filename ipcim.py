#A feladatot Fejes Máté és Németh Imre készítette.
ip = input("Adj megy egy ip címet: ")
hexadecimal = ["0","1","2","3","4","5","6","7","8","9", "a", "b", "c", "d","e","f"]
ipv = ip.split(sep=".")
ipvhat = ip.split(sep=":")
ip4=False
if "." in ipv:
    ipv = ip.split(sep=".")
    ip4=True

elif ":" in ipvhat:
    ipvhat = ip.split(sep=":")

check = False
chech6=False
nem=True
if ip4==False:
    for i in range(8):
        for t in range(4):
            if ipvhat[i][t] not in hexadecimal:
                nem=False

 
if nem:
    print("Ez egy ipv6-os ip cím.")
if len(ipv) == 4 and check:
    print("Ez egy ipv4-es ip cím.")
elif len(ipv) != 4 and check:
    print("Nem megfelelő ip cím.")  


if ip4==True:
    try:
        if 0 <= ipv[0] and ipv[1] and ipv[2] and ipv[3] <= 255:
            check = True
        

    except:
        print("nem jó")
    
else:
    try:
        if nem:
            pass
    
    except:
        print("rossz")


