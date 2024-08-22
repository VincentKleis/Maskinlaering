from pickle import load
from pandas import DataFrame, get_dummies
from time import sleep
from sklearn.model_selection import train_test_split
import os
from platform import system

# detects what system you are running and choses the appropriate console command for clearing console based on the result
sys = system()
if sys == "Linux" or sys == "Darwin":
    clear = 'clear'
else:
    clear = 'cls'

# load a pretrained model from the "mushrooms" directory
clf = load(open("mushrooms/model.sav", "rb"))

# promps user to describe the mushroom using the options that the model is trained on
def get_muchroom_data()->DataFrame:
    poisenous = None
    cap_shape = input("Hva er formen på soppens top? klokke=b, konisk=c, flat=f, med knott=k, konkav=s, konveks=x\
                      \n:")
    cap_shape = {"Cap Shape_b":cap_shape=="b", "Cap Shape_c":cap_shape=="c", "Cap Shape_f":cap_shape=="f",
                 "Cap Shape_k":cap_shape=="k", "Cap Shape_s":cap_shape=="s", "Cap Shape_x":cap_shape=="x",}
    
    cap_surface = input("Hvordan ville du beskrevet overflaten på soppen? fibrøst=f, riller=g, skjellete=y, glatt=s\
                      \n:")
    cap_surface = {"Cap Surface_f":cap_surface=="f", "Cap Surface_g":cap_surface=="g",
                   "Cap Surface_s":cap_surface=="s", "Cap Surface_y":cap_surface=="y",}
    
    cap_color = input("Hvilken av disse fargene beskrive best toppen på soppen?\
                      \nbrun=n, buff=b, kanel=c, grå=g, grønn=r, rosa=p, lilla=u, rød=e, hvit=w, gul=y\
                      \n:")
    cap_color = {"Cap Color_b":cap_color=="b", "Cap Color_c":cap_color=="c", "Cap Color_e":cap_color=="e", "Cap Color_g":cap_color=="g", 
                 "Cap Color_n":cap_color=="n", "Cap Color_p":cap_color=="p", "Cap Color_r":cap_color=="r", "Cap Color_u":cap_color=="u", 
                 "Cap Color_w":cap_color=="w", "Cap Color_y":cap_color=="y"}

    Bruices = input("Hvilken er det noen Merker på soppen?\
                    \nja=t, nei=f\
                    \n:")
    Bruices = {"Bruices_f":Bruices=="f", "Bruices_t":Bruices=="t"}

    odor = input("Hvordan ville du beskrevet lukten på soppen?\
                    \nmandel=a, anis=l, kreosot=c, fiskete=y, ful/råtten egg=f, muggen=m, ingen=n, dyp/kraftig=p, pikant=s\
                    \n:")
    odor = {"Odor_a":odor=="a", "Odor_c":odor=="c", "Odor_f":odor=="f", "Odor_l":odor=="l", "Odor_m":odor=="m", "Odor_n":odor=="n", 
            "Odor_p":odor=="p", "Odor_s":odor=="s", "Odor_y":odor=="y",}
    
    gill_attachments = input("Hvordan ville du beskrevet undersiden av sopp hatten?\
                    \nfestet=a, fri=f\
                    \n:")
    gill_attachments = {"Gill Attatchment_a": gill_attachments=="a", "Gill Attatchment_f": gill_attachments=="f",}
    
    gill_spacing = input("Hvordan ville du beskrevet avstannden mellom strukturene på underside av sopphatten?\
                    \nnær=c, overfylt=w\
                    \n:")
    gill_spacing = {"Gill Spacing_c": gill_spacing=="c", "Gill Spacing_w": gill_spacing=="w"}

    gill_size = input("Hvordna ville du beskrevet størelsen på strukturene under sopphatten?\
                    \nbred=b, smal=n\
                    \n:")
    gill_size = {"Gill Size_b":gill_size=="b", "Gill Size_n":gill_size=="n"}

    gill_color = input("Hvilken farge har strukturener på undersiden av sopphatten?\
                    \nsvart=k, brun=n, buff=b, sjokolade=h, grå=g, grønn=r ,oransje=o, rosa=p, lilla=u, rød=e, hvit=w, gul=y\
                    \n:")
    gill_color = {"Gill Color_b":gill_color=="b", "Gill Color_e":gill_color=="e", "Gill Color_g":gill_color=="g", "Gill Color_h":gill_color=="h", 
                  "Gill Color_k":gill_color=="k", "Gill Color_n":gill_color=="n", "Gill Color_o":gill_color=="o", "Gill Color_p":gill_color=="p",
                  "Gill Color_r":gill_color=="r", "Gill Color_u":gill_color=="u", "Gill Color_w":gill_color=="w", "Gill Color_y":gill_color=="y"}
    
    stalk_shape = input("Hvilken form har stilken til soppen?\
                        \nForstørende=e, Avtagende=t\
                        \n:")
    stalk_shape = {"Stalk Shape_e":stalk_shape=="e", "Stalk Shape_t":stalk_shape=="t"}
    
    stalk_root = input("Hvilken form har bunnen på stilken?\
                        \nbulbous=b, klomp=c, equal=e, forankret=r, mangler=?\
                        \n:")
    stalk_root = {"Stalk Root_?":stalk_root=="?", "Stalk Root_b":stalk_root=="b", "Stalk Root_c":stalk_root=="c", "Stalk Root_e":stalk_root=="e",
                  "Stalk Root_r":stalk_root=="r"}
    
    stalk_surface_above_ring = input("Hvordan er overflaten på stilken?\
                        \nfibrøs=f, skjellete=y, silkeaktig=k, glatt=s\
                        \n:")
    stalk_surface_above_ring = {"Stalk Surface Above Ring_f":stalk_surface_above_ring=="f", "Stalk Surface Above Ring_k":stalk_surface_above_ring=="k",
                                "Stalk Surface Above Ring_s":stalk_surface_above_ring=="s", "Stalk Surface Above Ring_y":stalk_surface_above_ring=="y"}
    
    stalk_surface_below_ring = input("Hvordan er overflaten på stilken over ringen?\
                        \nfibrøs=f, skjellete=y, silkeaktig=k, glatt=s\
                        \n:")
    stalk_surface_below_ring = {"Stalk Surface Below Ring_f":stalk_surface_below_ring=="f", "Stalk Surface Below Ring_k":stalk_surface_below_ring=="k", 
                                "Stalk Surface Below Ring_s":stalk_surface_below_ring=="s", "Stalk Surface Below Ring_y":stalk_surface_below_ring=="y",}
    
    stalk_color_above_ring = input("Hva er fargen på stilken over ringen?\
                        \nbrun=n, buff=b, kanel=c, grå=g, oransje=o, rosa=p, rød=e, hvit=w, gul=y\
                        \n:")
    stalk_color_above_ring = {"Stalk Color Above Ring_b":stalk_color_above_ring=="b", "Stalk Color Above Ring_c":stalk_color_above_ring=="c", "Stalk Color Above Ring_e":stalk_color_above_ring=="e",
                              "Stalk Color Above Ring_g":stalk_color_above_ring=="g", "Stalk Color Above Ring_n":stalk_color_above_ring=="n", "Stalk Color Above Ring_o":stalk_color_above_ring=="o",
                              "Stalk Color Above Ring_p":stalk_color_above_ring=="p", "Stalk Color Above Ring_w":stalk_color_above_ring=="w", "Stalk Color Above Ring_y":stalk_color_above_ring=="y"}
    
    stalk_color_below_ring = input("Hva er fargen på stilken under ringen?\
                        \nbrun=n, buff=b, kanel=c, grå=g, oransje=o, rosa=p, rød=e, hvit=w, gul=y\
                        \n:")
    stalk_color_below_ring = {"Stalk Color Below Ring_b":stalk_color_below_ring=="b", "Stalk Color Below Ring_c":stalk_color_below_ring=="c", "Stalk Color Below Ring_e":stalk_color_below_ring=="e", 
                              "Stalk Color Below Ring_g":stalk_color_below_ring=="g", "Stalk Color Below Ring_n":stalk_color_below_ring=="n", "Stalk Color Below Ring_o":stalk_color_below_ring=="o", 
                              "Stalk Color Below Ring_p":stalk_color_below_ring=="p", "Stalk Color Below Ring_w":stalk_color_below_ring=="w", "Stalk Color Below Ring_y":stalk_color_below_ring=="y"}
    
    veil_type = {"Veil Type_p":True}

    veil_color = input("Hvilken farge har sløret?\
                        \nbrun=n, oransje=o, hvit=w, gul=y\
                        \n:")
    veil_color = {"Veil Color_n":veil_color=="n", "Veil Color_o":veil_color=="o", "Veil Color_w":veil_color=="w", "Veil Color_y":veil_color=="y"}

    ring_number = input("Hvor mange ringer er det på soppen?\
                        \ningen=n, en=o, to=t\
                        \n:")
    ring_number = {"Ring Number_n":ring_number=="n", "Ring Number_o":ring_number=="o", "Ring Number_t":ring_number=="t"}

    ring_type = input("Hvordan ville du beskrevet ringene?\
                        \nevanescent=e, fakling=f, large=l, ingen=n, anheng=p\
                        \n:")
    ring_type = {"Ring Type_e":ring_type=="e", "Ring Type_f":ring_type=="f", "Ring Type_l":ring_type=="l", "Ring Type_n":ring_type=="n", "Ring Type_p":ring_type=="p"}
    
    spore_print_color = input("Hvilken farge lager sporene på et hvitt ark?\
                        \nsvart=k, brun=n, buff=b, sjokolade=h, grønn=r, oransje=o, lilla=u, hvit=w, gul=y\
                        \n:")
    spore_print_color = {"Spore Print Color_b":spore_print_color=="b", "Spore Print Color_h":spore_print_color=="h", "Spore Print Color_k":spore_print_color=="k", 
                         "Spore Print Color_n":spore_print_color=="n", "Spore Print Color_o":spore_print_color=="o", "Spore Print Color_r":spore_print_color=="r", 
                         "Spore Print Color_u":spore_print_color=="u", "Spore Print Color_w":spore_print_color=="w", "Spore Print Color_y":spore_print_color=="y"}
    
    population = input("Hvor tett gror soppen?\
                        \nrikelig=a, gruppert=c, mange=n, spredt=s, flere=v, ensom=y\
                        \n:")
    population = {"Population_a":population=="a", "Population_c":population=="c", "Population_n":population=="n", "Population_s":population=="s", "Population_v":population=="v", "Population_y":population=="y"}

    habitat = input("Hvor gror soppen?\
                        \ngress=g, løv=l, enger=m, stier=p, urban=u, avfall=w, skog=d\
                        \n:")
    habitat = {"Habitat_b":habitat=="b", "Habitat_g":habitat=="g", "Habitat_l":habitat=="l", "Habitat_m":habitat=="m", "Habitat_p":habitat=="p", "Habitat_u":habitat=="u", "Habitat_w":habitat=="w"}

    data = DataFrame({**cap_color, **cap_shape, **cap_surface, **Bruices, **odor, **gill_attachments, **gill_color, **gill_size, **gill_spacing, **stalk_color_above_ring, **stalk_color_below_ring, **stalk_root, 
                      **stalk_shape, **stalk_surface_above_ring, **stalk_surface_below_ring, **veil_color, **veil_type, **ring_number, **ring_type, **spore_print_color, **population, **habitat}, index=[0])

test_data = DataFrame({"Cap Shape_b":[True], "Cap Shape_c":[False], "Cap Shape_f":[False], "Cap Shape_k":[False], "Cap Shape_s":[False], "Cap Shape_x":[False], "Cap Surface_f":[True], "Cap Surface_g":[False], "Cap Surface_s":[False], "Cap Surface_y":[False],
    "Cap Color_b":[True], "Cap Color_c":[False], "Cap Color_e":[False],  "Cap Color_g":[False], "Cap Color_n":[False], "Cap Color_p":[False], "Cap Color_r":[False], "Cap Color_u":[False], "Cap Color_w":[False],"Cap Color_y":[False], "Bruices_f":[True], "Bruices_t":[False],
    "Odor_a":[True], "Odor_c":[False], "Odor_f":[False], "Odor_l":[False], "Odor_m":[False], "Odor_n":[False], "Odor_p":[False], "Odor_s":[False], "Odor_y":[False], "Gill Attatchment_a":[True], "Gill Attatchment_f":[False],
    "Gill Spacing_c":[True], "Gill Spacing_w":[False], "Gill Size_b":[True], "Gill Size_n":[False], "Gill Color_b":[True], "Gill Color_e":[False], "Gill Color_g":[False], "Gill Color_h":[False], 
    "Gill Color_k":[False], "Gill Color_n":[False], "Gill Color_o":[False], "Gill Color_p":[False], "Gill Color_r":[False], "Gill Color_u":[False], "Gill Color_w":[False], "Gill Color_y":[False], "Stalk Shape_e":[True], "Stalk Shape_t":[False], "Stalk Root_?":[False], 
    "Stalk Root_b":[True], "Stalk Root_c":[False], "Stalk Root_e":[False], "Stalk Root_r":[False], "Stalk Surface Above Ring_f":[True], "Stalk Surface Above Ring_k":[False], "Stalk Surface Above Ring_s":[False], 
    "Stalk Surface Above Ring_y":[False], "Stalk Surface Below Ring_f":[True], "Stalk Surface Below Ring_k":[False], "Stalk Surface Below Ring_s":[False], "Stalk Surface Below Ring_y":[False], "Stalk Color Above Ring_b":[True], 
    "Stalk Color Above Ring_c":[False], "Stalk Color Above Ring_e":[False], "Stalk Color Above Ring_g":[False], "Stalk Color Above Ring_n":[False], "Stalk Color Above Ring_o":[False], "Stalk Color Above Ring_p":[False], "Stalk Color Above Ring_w":[False],
    "Stalk Color Above Ring_y":[False], "Stalk Color Below Ring_b":[False], "Stalk Color Below Ring_c":[False], "Stalk Color Below Ring_e":[False], "Stalk Color Below Ring_g":[False], "Stalk Color Below Ring_n":[True], "Stalk Color Below Ring_o":[False], 
    "Stalk Color Below Ring_p":[False], "Stalk Color Below Ring_w":[False], "Stalk Color Below Ring_y":[False], "Veil Type_p":[True], "Veil Color_n":[True], "Veil Color_o":[False], "Veil Color_w":[False], "Veil Color_y":[False], 
    "Ring Number_n":[True], "Ring Number_o":[False], "Ring Number_t":[False], "Ring Type_e":[False], "Ring Type_f":[False], "Ring Type_l":[False], "Ring Type_n":[False], "Ring Type_p":[False],
    "Spore Print Color_b":[False], "Spore Print Color_h":[False], "Spore Print Color_k":[True], "Spore Print Color_n":[False], "Spore Print Color_o":[False], "Spore Print Color_r":[False], "Spore Print Color_u":[False], 
    "Spore Print Color_w":[False], "Spore Print Color_y":[False], "Population_a":[True], "Population_c":[True], "Population_n":[False], "Population_s":[False], "Population_v":[False], "Population_y":[False], "Habitat_d":[False], "Habitat_g":[True], "Habitat_l":[False], 
    "Habitat_m":[False], "Habitat_p":[False], "Habitat_u":[False], "Habitat_w":[False]})

def pred_muchroom_data(data):

    print(data)
    df = get_dummies(data)
    prediction = clf.predict(df)
    if prediction == False:
        print("Ikke spisbar")
    else:
        print("Spisbar")
    sleep(5)
data = None

while True:
    os.system(clear)
    choise = input("skriv en bokstav og trykk enter\
                   \nFor å legge til en sopp i dataen = w, for å slette dataen = d, for å analysere soppen og si om det er giftig = g\
                   \ntest = t stop = s:")

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

    if choise == "s":
        break