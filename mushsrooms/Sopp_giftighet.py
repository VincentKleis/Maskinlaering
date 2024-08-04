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
clf = load(open("mushsrooms/model.sav", "rb"))

# promps user to describe the mushroom using the options that the model is trained on
def get_muchroom_data()->DataFrame:
    poisenous = None
    cap_shape = input("Hva er formen på soppens top? klokke=b, konisk=c, konveks=x, flat=f, med knott=k, konkav=s\n\
                      :")
    cap_shape = {"Cap shape_b":cap_shape=="b", "Cap shape_c":cap_shape=="c", "Cap shape_x":cap_shape=="x", "Cap shape_f":cap_shape=="f",
                 "Cap shape_s":cap_shape=="s"}
    
    cap_surface = input("Hvordan ville du beskrevet overflaten på soppen? fibrøst=f, riller=g, skjellete=y, glatt=s\n\
                      :")
    cap_surface = {"Cap surface_f":cap_surface=="f", "Cap surface_g":cap_surface=="g", "Cap surface_y":cap_surface=="y",
                   "Cap surface_s":cap_surface=="s"}
    
    cap_color = input("Hvilken av disse fargene beskrive best toppen på soppen?\n\
                      brun=n, buff=b, kanel=c, grå=g, grønn=r, rosa=p, lilla=u, rød=e, hvit=w, gul=y\n\
                      :")
    cap_color = {"Cap color_n":cap_color=="n", "Cap color_b":cap_color=="b", "Cap color_c":cap_color=="c", "Cap color_r":cap_color=="r", 
                 "Cap color_p":cap_color=="p", "Cap color_u":cap_color=="u", "Cap color_e":cap_color=="e", "Cap color_w":cap_color=="w",
                 "Cap color_y":cap_color=="y"}

    bruises = input("Hvilken er det noen Merker på soppen?\n\
                    ja=t, nei=f\n\
                    :")
    bruises = {"Bruises_t":bruises=="t", "Bruises_f":bruises=="f"}

    odor = input("Hvordan ville du beskrevet lukten på soppen?\n\
                    mandel=a, anis=l, kreosot=c, fiskete=y, ful/råtten egg=f, muggen=m, ingen=n, dyp/kraftig=p, pikant=s\n\
                    :")
    odor = {"Odor_a":odor=="a", "Odor_l":odor=="l", "Odor_c":odor=="c", "Odor_y":odor=="y", "Odor_f":odor=="f", "Odor_m":odor=="m", 
            "Odor_n":odor=="n", "Odor_p":odor=="p", "Odor_s":odor=="s"}
    
    gill_attachments = input("Hvordan ville du beskrevet undersiden av sopp hatten?\n\
                    festet=a, fallende=d, fri=f, hakk=n\n\
                    :")
    gill_attachments = {"Gill attachments_a": gill_attachments=="a", "Gill attachments_d": gill_attachments=="d", "Gill attachments_f": gill_attachments=="f",
                        "Gill attachments_n": gill_attachments=="n"}
    
    gill_spacing = input("Hvordan ville du beskrevet avstannden mellom strukturene på underside av sopphatten?\n\
                    nær=c, overfylt=w, fjern=d\n\
                    :")
    gill_spacing = {"Gill spacing_c": gill_spacing=="c", "Gill Spacing_w": gill_spacing=="w", "Gill spacing_d": gill_spacing=="d"}

    gill_size = input("Hvordna ville du beskrevet størelsen på strukturene under sopphatten?\n\
                    bred=b, smal=n\n\
                    :")
    gill_size = {"Gill size_b":gill_size=="b", "Gill size_n":gill_size=="n"}

    gill_color = input("Hvilken farge har strukturener på undersiden av sopphatten?\n\
                    svart=k, brun=n, buff=b, sjokolade=h, grå=g, grønn=r ,oransje=o, rosa=p, lilla=u, rød=e, hvit=w, gul=y\n\
                    :")
    gill_color = {"Gill color_k":gill_color=="k", "Gill color_n":gill_color=="n", "Gill color_h":gill_color=="h", "Gill color_g":gill_color=="g",
                  "Gill color_r":gill_color=="r", "Gill color_o":gill_color=="o", "Gill color_p":gill_color=="p", "Gill color_u":gill_color=="u",
                  "Gill color_w":gill_color=="w", "Gill color_y":gill_color=="y"}
    
    stalk_shape = input("Hvilken form har stilken til soppen?\n\
                        Forstørende=e, Avtagende=t\n\
                        :")
    stalk_shape = {"Stalk shape_e":stalk_shape=="e", "Stalk shape_t":stalk_shape=="t"}
    
    stalk_root = input("Hvilken form har bunnen på stilken?\n\
                        bulbous=b, club=c, cup=u, equal=e, rhizomorphs=z, forankret=r, mangler=?\n\
                        :")
    stalk_root = {"Stalk root_b":stalk_root=="b", "Stalk root_c":stalk_root=="c", "Stalk root_u":stalk_root=="u", "Stalk root_e":stalk_root=="e",
                  "Stalk root_z":stalk_root=="z", "Stalk root_r":stalk_root=="r", "Stalk root_?":stalk_root=="?"}
    
    stalk_surface_above_ring = input("Hvordan er overflaten på stilken?\n\
                        fibrøs=f, skjellete=y, silkeaktig=k, glatt=s\n\
                        :")
    stalk_surface_above_ring = {"Stalk surface above ring_f":stalk_surface_above_ring=="f", "Stalk surface above ring_y":stalk_surface_above_ring=="y", 
                                "Stalk surface above ring_k":stalk_surface_above_ring=="s", "Stalk surface above ring_s":stalk_surface_above_ring=="s"}
    
    stalk_surface_below_ring = input("Hvordan er overflaten på stilken over ringen?\n\
                        fibrøs=f, skjellete=y, silkeaktig=k, glatt=s\n\
                        :")
    stalk_surface_below_ring = {"Stalk surface below ring_f":stalk_surface_below_ring=="f", "Stalk surface below ring_y":stalk_surface_below_ring=="y",
                                "Stalk surface below ring_k":stalk_surface_below_ring=="k", "Stalk surface below ring_s":stalk_surface_below_ring=="s"}
    
    stalk_color_above_ring = input("Hva er fargen på stilken over ringen?\n\
                        brun=n, buff=b, kanel=c, grå=g, oransje=o, rosa=p, rød=e, hvit=w, gul=y\n\
                        :")
    stalk_color_above_ring = {"Stalk color above ring_n":stalk_color_above_ring=="n", "Stalk color above ring_b":stalk_color_above_ring=="b", "Stalk color above ring_g":stalk_color_above_ring=="g",
                              "Stalk color above ring_o":stalk_color_above_ring=="o", "Stalk color above ring_p":stalk_color_above_ring=="p", "Stalk color above ring_e":stalk_color_above_ring=="e",
                              "Stalk color above ring_w":stalk_color_above_ring=="w", "Stalk color above ring_y":stalk_color_above_ring=="y"}
    
    stalk_color_below_ring = input("Hva er fargen på stilken under ringen?\n\
                        brun=n, buff=b, kanel=c, grå=g, oransje=o, rosa=p, rød=e, hvit=w, gul=y\n\
                        :")
    stalk_color_below_ring = {"Stalk color below ring_n":stalk_color_below_ring=="n", "Stalk color below ring_b":stalk_color_below_ring=="b", "Stalk color below ring_g":stalk_color_below_ring=="g",
                              "Stalk color below ring_o":stalk_color_below_ring=="o", "Stalk color below ring_p":stalk_color_below_ring=="p", "Stalk color below ring_e":stalk_color_below_ring=="e",
                              "Stalk color below ring_w":stalk_color_below_ring=="w", "Stalk color below ring_y":stalk_color_below_ring=="y"}
    
    veil_type = input("Hvordan ville du beskrevet 'sløret' på soppen?\n\
                        partiell=p, universell=u\n\
                        :")
    veil_type = {"Veil type_p":veil_type=="p", "Veil type_u":veil_type=="u"}

    veil_color = input("Hvilken farge har sløret?\n\
                        brun=n, oransje=o, hvit=w, gul=y\n\
                        :")
    veil_color = {"Veil color_n":veil_color=="n", "Veil color_o":veil_color=="o", "Veil color_w":veil_color=="w", "Veil color_y":veil_color=="y"}

    ring_number = input("Hvor mange ringer er det på soppen?\n\
                        ingen=n, en=o, to=t\n\
                        :")
    ring_number = {"Ring number_n":ring_number=="n", "Ring number_o":ring_number=="o", "Ring number_t":ring_number=="t"}

    ring_type = input("Hvordan ville du beskrevet ringene?\n\
                        spindelvev=c, evanescent=e, fakling=f, large=l, ingen=n, anheng=p, mantel=s, sone=z\n\
                        :")
    ring_type = {"Ring type_c":ring_type=="c", "Ring type_e":ring_type=="e", "Ring type_f":ring_type=="f", "Ring type_l":ring_type=="l", "Ring type_n":ring_type=="n", "Ring type_p":ring_type=="p",
                 "Ring type_s":ring_type=="s", "Ring type_z":ring_type=="z"}
    
    spore_print_color = input("Hvilken farge lager sporene på et hvitt ark?\n\
                        svart=k, brun=n, buff=b, sjokolade=h, grønn=r, oransje=o, lilla=u, hvit=w, gul=y\n\
                        :")
    population = input("Hvor tett gror soppen?\n\
                        rikelig=a, gruppert=c, mange=n, spredt=s, flere=v, ensom=y\n\
                        :")
    habitat = input("Hvor gror soppen?\n\
                        gress=g, løv=l, enger=m, stier=p, urban=u, avfall=w, skog=d\n\
                        :")
    
    data = DataFrame({"Cap shape":[cap_shape], "Cap surface":[cap_surface], "Cap color":[cap_color], "Bruices":[bruises], "Odor":[odor], "Gill attachments":[gill_attachments], "Gill spacing":[gill_spacing], "Gill size":[gill_size], "Gill color":[gill_color], 
                      "Stalk shape":[stalk_shape], "Stalk root":[stalk_root], "Stalk surface above ring":[stalk_surface_above_ring], "Stalk surface below ring":[stalk_surface_below_ring], "Stalk color above ring":[stalk_color_above_ring], 
                      "Stalk color below ring":[stalk_color_below_ring], "Veil type":[veil_type], "Veil color":[veil_color], "Ring number":[ring_number], "Ring type":[ring_type], "Spore print color":[spore_print_color], "Population":[population], "Habitat":[habitat]})

test_data = DataFrame({"Cap shape":["b"], "Cap surface":["f"], "Cap color":["n"], "Bruices":["t"], "Odor":["a"], "Gill attachments":["a"], "Gill spacing":["c"], "Gill size":["b"], "Gill color":["k"], 
                      "Stalk shape":["e"], "Stalk root":["b"], "Stalk surface above ring":["f"], "Stalk surface below ring":["f"], "Stalk color above ring":["b"], 
                      "Stalk color below ring":["b"], "Veil type":["p"], "Veil color":["n"], "Ring number":["n"], "Ring type":["c"], "Spore print color":["k"], "Population":["a"], "Habitat":["g"]})

def pred_muchroom_data(data):

    df = get_dummies(data)
    print(df)

    prediction = clf.predict(df)

data = None

while True:
    os.system(clear)
    choise = input("skriv en bukstav og trykk enter\n\
                   For å legge til en sopp i dataen = w, for å slette dataen = d, for å analysere soppen og si om det er giftig = g\n\
                   test = t:")

    if choise == "w":
        os.system(clear)
        data = get_muchroom_data()
    
    if choise == "d":
        os.system(clear)
        data = None
    
    if choise == "g":
        pred_muchroom_data(data)

    if choise == "t":
        pred_muchroom_data(test_data)