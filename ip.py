# Fejes Máté Csabával dolgoztunk együtt.
ip = input("Adj meg egy IP címet: ")

# Hexadecimális számjegyek listája az IPv6 ellenőrzéshez
hexadecimal = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]

# IPv4 ellenőrzés
if "." in ip:  # Ha pont van benne, akkor lehet IPv4
    reszek = ip.split(".")
    if len(reszek) == 4:  # IPv4 pontosan 4 részből áll
        helyes = True
        for resz in reszek:
            if not resz.isdigit() or not (0 <= int(resz) <= 255):
                helyes = False
                break
        if helyes:
            print("Ez egy érvényes IPv4 cím.")
        else:
            print("Nem érvényes IPv4 cím.")
    else:
        print("Nem érvényes IPv4 cím.")

# IPv6 ellenőrzés
elif ":" in ip:  # Ha kettőspont van benne, akkor lehet IPv6
    reszek = ip.split(":")
    if 1 <= len(reszek) <= 8:  # IPv6 legfeljebb 8 részből állhat
        helyes = True
        for resz in reszek:
            if len(resz) > 4:  # Egy rész legfeljebb 4 karakter hosszú lehet
                helyes = False
                break
            for karakter in resz:
                if karakter.lower() not in hexadecimal:  # Csak hexadecimális karakter lehet
                    helyes = False
                    break
        if helyes:
            print("Ez egy érvényes IPv6 cím.")
        else:
            print("Nem érvényes IPv6 cím.")
    else:
        print("Nem érvényes IPv6 cím.")

# Sem IPv4, sem IPv6
else:
    print("Nem érvényes IP cím.")
