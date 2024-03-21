from pickle import load
from pandas import DataFrame, get_dummies
import os
from platform import system

# detects what system you are running and choses the appropriate console command for clearing console based on the result
sys = system()
if sys == "Linux" or sys == "Darwin":
    clear = 'clear'
else:
    clear = 'cls'

# load a pretrained model from the "dependenciec" directory
clf = load(open("Ai/task_1 mushsrooms/model.sav", "r"))

# promps user to describe the mushroom using the options that the model is trained on
def get_muchroom_data()->DataFrame:
    poisenous = None
    cap_shape = input("Hva er formen på soppens top? klokke=b, konisk=c, konveks=x, flat=f, med knott=k, konkav=s\n\
                      :")
    cap_surface = input("Hvordan ville du beskrevet overflaten på soppen? fibrøst=f, riller=g, skjellete=y, glatt=s\n\
                      :")
    cap_color = input("Hvilken av disse fargene beskrive best toppen på soppen?\n\
                      brun=n, buff=b, kanel=c, grå=g, grønn=r, rosa=p, lilla=u, rød=e, hvit=w, gul=y\n\
                      :")
    bruises = input("Hvilken er det noen Merker på soppen?\n\
                    ja=t, nei=f\n\
                    :")
    odor = input("Hvordan ville du beskrevet lukten på soppen?\n\
                    mandel=a, anis=l, kreosot=c, fiskete=y, ful/råtten egg=f, muggen=m, ingen=n, dyp/kraftig=p, pikant=s\n\
                    :")
    gill_attachments = input("Hvordan ville du beskrevet undersiden av sopp hatten?\n\
                    festet=a, fallende=d, fri=f, hakk=n\n\
                    :")
    gill_spacing = input("Hvordan ville du beskrevet avstannden mellom strukturene på underside av sopphatten?\n\
                    nær=c, overfylt=w, fjern=d\n\
                    :")
    gill_size = input("Hvordna ville du beskrevet størelsen på strukturene under sopphatten?\n\
                    bred=b, smal=n\n\
                    :")
    gill_color = input("Hvilken farge har strukturener på undersiden av sopphatten?\n\
                    svart=k, brun=n, buff=b, sjokolade=h, grå=g, grønn=r ,oransje=o, rosa=p, lilla=u, rød=e, hvit=w, gul=y\n\
                    :")
    stalk_shape = input("Hvilken form har stilken til soppen?\n\
                        Forstørende=e, Avtagende=t\n\
                        :")
    stalk_root = input("Hvilken form har bunnen på stilken?\n\
                        bulbous=b, club=c, cup=u, equal=e, rhizomorphs=z, forankret=r, mangler=?\n\
                        :")
    stalk_surface_above_ring = input("Hvordan er overflaten på stilken?\n\
                        fibrøs=f, skjellete=y, silkeaktig=k, glatt=s\n\
                        :")
    stalk_surface_below_ring = input("Hvordan er overflaten på stilken over ringen?\n\
                        fibrøs=f, skjellete=y, silkeaktig=k, glatt=s\n\
                        :")
    stalk_color_above_ring = input("Hva er fargen på stilken over ringen?\n\
                        brun=n, buff=b, kanel=c, grå=g, oransje=o, rosa=p, rød=e, hvit=w, gul=y\n\
                        :")
    stalk_color_below_ring = input("Hva er fargen på stilken under ringen?\n\
                        brun=n, buff=b, kanel=c, grå=g, oransje=o, rosa=p, rød=e, hvit=w, gul=y\n\
                        :")
    veil_type = input("Hvordan ville du beskrevet 'sløret' på soppen?\n\
                        partiell=p,universell=u\n\
                        :")
    veil_color = input("Hvilken farge har sløret?\n\
                        brown=n,orange=o,white=w,yellow=y\n\
                        :")
    ring_number = input("Hvor mange ringer er det på soppen?\n\
                        ingen=n, en=o, to=t\n\
                        :")
    ring_type = input("Hvordan ville du beskrevet ringene?\n\
                        spindelvev=c, evanescent=e, fakling=f, large=l, ingen=n, anheng=p, mantel=s, sone=z\n\
                        :")
    spore_print_color = input("Hvilken farge lager sporene på et hvitt ark?\n\
                        svart=k, brun=n, buff=b, sjokolade=h, grønn=r, oransje=o, lilla=u, hvit=w, gul=y\n\
                        :")
    population = input("Hvor tett gror soppen?\n\
                        rikelig=a, gruppert=c, mange=n, spredt=s, flere=v, ensom=y\n\
                        :")
    habitat = input("Hvor gror soppen?\n\
                        gress=g, løv=l, enger=m, stier=p, urban=u, avfall=w, skog=d\n\
                        :")
    data = DataFrame([cap_shape, cap_surface, cap_color, bruises, odor, gill_attachments, gill_spacing, gill_size, gill_color, 
                      stalk_shape, stalk_root, stalk_surface_above_ring, stalk_surface_below_ring, stalk_color_above_ring, 
                      stalk_color_below_ring, veil_type, veil_color, ring_number, ring_type, spore_print_color, population, habitat])
    return data

def pred_muchroom_data(data):
    df = get_dummies(data)
    prediction = clf.predict(df)

data = None

while True:
    os.system(clear)
    choise = input("skriv en bukstav og trykk enter\n\
                   For å legge til en sopp i dataen = w, for å slette dataen = d, for å analysere soppen og si om det er giftig = g\n\
                   :")

    if choise == "w":
        os.system(clear)
        data = get_muchroom_data()
    
    if choise == "d":
        os.system(clear)
        data = None
    
    if choise == "g":
        pred_muchroom_data(data)
