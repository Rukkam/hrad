def otevreno(a,b):
    if a==1:
        vysledek="zavřeno"
            
    else: 
        if int(b)>=9 and int(b)<=17 :
            vysledek="otevřeno"
    
        else:
            vysledek="zavřeno"
    return "Nyní je {}.".format(vysledek)

def otevreno_den(a):
    if a==1:
        vysledek1="Dnes je celý den zavřeno."
    else:
        vysledek1="Dnes je otevřeno od 9:00 do 18:00"
    return "{}.".format(vysledek1)



