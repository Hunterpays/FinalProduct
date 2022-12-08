from tkinter import *
from threading import Timer
from playsound import playsound
from PIL import Image, ImageTk
from io import BytesIO
import requests, json, os, random




# Send Request to Access Riot API
response = requests.get('http://ddragon.leagueoflegends.com/cdn/12.22.1/data/en_US/champion.json')


# Parse and store character data 
data = json.loads(response.text)
Aatrox = data['data']['Aatrox']['name']
Alistar = data['data']['Alistar']['name']
Anivia = data['data']['Anivia']['name']
Azir = data['data']['Azir']['name']
Caitlyn = data['data']['Caitlyn']['name']
Cassiopeia = data['data']['Cassiopeia']['name']
Darius = data['data']['Darius']['name']
Ekko = data['data']['Ekko']['name']
Graves = data['data']['Graves']['name']
Gwen = data['data']['Gwen']['name']
Irelia = data['data']['Irelia']['name']
Ivern = data['data']['Ivern']['name']
Jayce = data['data']['Jayce']['name']
Jinx = data['data']['Jinx']['name']
Kalista = data['data']['Kalista']['name']
Katarina = data['data']['Katarina']['name']
Malphite = data['data']['Malphite']['name']
Maokai = data['data']['Maokai']['name']
Nautilus = data['data']['Nautilus']['name']
Yuumi = data['data']['Yuumi']['name']


# UI Python TkInterface
root = Tk()
root.title('Character Select Tool')
root.geometry("1280x891")

def main():
    global champ_name
    champ_name = 'None'

    # Images
    readybutton = PhotoImage(file=(os.path.join(sys.path[0], "readybutton.png")))
    lockinbutton = PhotoImage(file=(os.path.join(sys.path[0], "lockinbutton.png")))
    restartbutton = PhotoImage(file=(os.path.join(sys.path[0], "restartbutton.png")))
    blank = PhotoImage(file=(os.path.join(sys.path[0], "blank.png")))
    background = PhotoImage(file=(os.path.join(sys.path[0], "background.png")))
    background1 = Label(root, image=background)
    background1.place(x=0,y=0)
    ready_button = Button(root, image=readybutton, command=lambda: [set_none(), ready_button.place_forget(), lockin_button.place(x=500,y=820), place_champs(), mytime()])
    ready_button.place(x=500,y=815)
    lockin_button = Button(root, image=lockinbutton, command=lambda: [replace_champs(), reset(), set_none()])
    restart_button = Button(root, image=restartbutton, command=lambda: [set_none(), main()])
    
    

    # Picks and Bans
    Team1p1 = Label(root, image=blank)
    Team1p1.place(x=50,y=270)
    Team2p1 = Label(root, image=blank)
    Team2p1.place(x=1160,y=270)
    Team1p2 = Label(root, image=blank)
    Team1p2.place(x=50,y=400)
    Team2p2 = Label(root, image=blank)
    Team2p2.place(x=1160,y=400)
    Team1p3 = Label(root, image=blank)
    Team1p3.place(x=50,y=530)
    Team2p3 = Label(root, image=blank)
    Team2p3.place(x=1160,y=530)
    Team1p4 = Label(root, image=blank)
    Team1p4.place(x=50,y=660)
    Team2p4 = Label(root, image=blank)
    Team2p4.place(x=1160,y=660)
    Team1p5 = Label(root, image=blank)
    Team1p5.place(x=50,y=790)
    Team2p5 = Label(root, image=blank)
    Team2p5.place(x=1160,y=790)

    # Champions

    global champ_list
    champ_list = [Aatrox, Alistar, Anivia, Azir, Caitlyn, Cassiopeia, Darius, Ekko, Graves, Gwen, Irelia, Ivern, Jayce, Jinx, Kalista, Katarina, Malphite, Maokai, Nautilus, Yuumi]


    def set_none():
        global champ_name
        champ_name = 'None'

    def setname1():
        global champ_name
        champ_name = 'Aatrox'
    def setname2():
        global champ_name
        champ_name = 'Alistar'
    def setname3():
        global champ_name
        champ_name = 'Anivia'
    def setname4():
        global champ_name
        champ_name = 'Azir'
    def setname5():
        global champ_name
        champ_name = 'Caitlyn'
    def setname6():
        global champ_name
        champ_name = 'Cassiopeia'
    def setname7():
        global champ_name
        champ_name = 'Darius'
    def setname8():
        global champ_name
        champ_name = 'Ekko'
    def setname9():
        global champ_name
        champ_name = 'Graves'
    def setname10():
        global champ_name
        champ_name = 'Gwen'
    def setname11():
        global champ_name
        champ_name = 'Irelia'
    def setname12():
        global champ_name
        champ_name = 'Ivern'
    def setname13():
        global champ_name
        champ_name = 'Jayce'
    def setname14():
        global champ_name
        champ_name = 'Jinx'
    def setname15():
        global champ_name
        champ_name = 'Kalista'
    def setname16():
        global champ_name
        champ_name = 'Katarina'
    def setname17():
        global champ_name
        champ_name = 'Malphite'
    def setname18():
        global champ_name
        champ_name = 'Maokai'
    def setname19():
        global champ_name
        champ_name = 'Nautilus'
    def setname20():
        global champ_name
        champ_name = 'Yuumi'



    Aatrox1 = "https://ddragon.leagueoflegends.com/cdn/12.4.1/img/champion/" + Aatrox + ".png"
    r = requests.get(Aatrox1)
    pilImage = Image.open(BytesIO(r.content))
    pilImage = pilImage.resize((64, 64), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(pilImage)
    Aatrox_button = Button(root, image=image, command=lambda: [setname1()])
    Aatrox_label = Label(root, image=image)

    Alistar1 = "https://ddragon.leagueoflegends.com/cdn/12.4.1/img/champion/" + Alistar + ".png"
    r = requests.get(Alistar1)
    pilImage = Image.open(BytesIO(r.content))
    pilImage = pilImage.resize((64, 64), Image.ANTIALIAS)
    image1 = ImageTk.PhotoImage(pilImage)
    Alistar_button = Button(root, image=image1, command=lambda: [setname2()])
    Alistar_label = Label(root, image=image1)

    Anivia1 = "https://ddragon.leagueoflegends.com/cdn/12.4.1/img/champion/" + Anivia + ".png"
    r = requests.get(Anivia1)
    pilImage = Image.open(BytesIO(r.content))
    pilImage = pilImage.resize((64, 64), Image.ANTIALIAS)
    image2 = ImageTk.PhotoImage(pilImage)
    Anivia_button = Button(root, image=image2, command=lambda: [setname3()])
    Anivia_label = Label(root, image=image2)


    Azir1 = "https://ddragon.leagueoflegends.com/cdn/12.4.1/img/champion/" + Azir + ".png"
    r = requests.get(Azir1)
    pilImage = Image.open(BytesIO(r.content))
    pilImage = pilImage.resize((64, 64), Image.ANTIALIAS)
    image3 = ImageTk.PhotoImage(pilImage)
    Azir_button = Button(root, image=image3, command=lambda: [setname4()])
    Azir_label = Label(root, image=image3)

    Caitlyn1 = "https://ddragon.leagueoflegends.com/cdn/12.4.1/img/champion/" + Caitlyn + ".png"
    r = requests.get(Caitlyn1)
    pilImage = Image.open(BytesIO(r.content))
    pilImage = pilImage.resize((64, 64), Image.ANTIALIAS)
    image4 = ImageTk.PhotoImage(pilImage)
    Caitlyn_button = Button(root, image=image4, command=lambda: [setname5()])
    Caitlyn_label = Label(root, image=image4)

    Cassiopeia1 = "https://ddragon.leagueoflegends.com/cdn/12.4.1/img/champion/" + Cassiopeia + ".png"
    r = requests.get(Cassiopeia1)
    pilImage = Image.open(BytesIO(r.content))
    pilImage = pilImage.resize((64, 64), Image.ANTIALIAS)
    image5 = ImageTk.PhotoImage(pilImage)
    Cassiopeia_button = Button(root, image=image5, command=lambda: [setname6()])
    Cassiopeia_label = Label(root, image=image5)

    Darius1 = "https://ddragon.leagueoflegends.com/cdn/12.4.1/img/champion/" + Darius + ".png"
    r = requests.get(Darius1)
    pilImage = Image.open(BytesIO(r.content))
    pilImage = pilImage.resize((64, 64), Image.ANTIALIAS)
    image6 = ImageTk.PhotoImage(pilImage)
    Darius_button = Button(root, image=image6, command=lambda: [setname7()])
    Darius_label = Label(root, image=image6)

    Ekko1 = "https://ddragon.leagueoflegends.com/cdn/12.4.1/img/champion/" + Ekko + ".png"
    r = requests.get(Ekko1)
    pilImage = Image.open(BytesIO(r.content))
    pilImage = pilImage.resize((64, 64), Image.ANTIALIAS)
    image7 = ImageTk.PhotoImage(pilImage)
    Ekko_button = Button(root, image=image7, command=lambda: [setname8()])
    Ekko_label = Label(root, image=image7)

    Graves1 = "https://ddragon.leagueoflegends.com/cdn/12.4.1/img/champion/" + Graves + ".png"
    r = requests.get(Graves1)
    pilImage = Image.open(BytesIO(r.content))
    pilImage = pilImage.resize((64, 64), Image.ANTIALIAS)
    image8 = ImageTk.PhotoImage(pilImage)
    Graves_button = Button(root, image=image8, command=lambda: [setname9()])
    Graves_label = Label(root, image=image8)

    Gwen1 = "https://ddragon.leagueoflegends.com/cdn/12.4.1/img/champion/" + Gwen + ".png"
    r = requests.get(Gwen1)
    pilImage = Image.open(BytesIO(r.content))
    pilImage = pilImage.resize((64, 64), Image.ANTIALIAS)
    image9 = ImageTk.PhotoImage(pilImage)
    Gwen_button = Button(root, image=image9, command=lambda: [setname10()])
    Gwen_label = Label(root, image=image9)

    Irelia1 = "https://ddragon.leagueoflegends.com/cdn/12.4.1/img/champion/" + Irelia + ".png"
    r = requests.get(Irelia1)
    pilImage = Image.open(BytesIO(r.content))
    pilImage = pilImage.resize((64, 64), Image.ANTIALIAS)
    image10 = ImageTk.PhotoImage(pilImage)
    Irelia_button = Button(root, image=image10, command=lambda: [setname11()])
    Irelia_label = Label(root, image=image10)

    Ivern1 = "https://ddragon.leagueoflegends.com/cdn/12.4.1/img/champion/" + Ivern + ".png"
    r = requests.get(Ivern1)
    pilImage = Image.open(BytesIO(r.content))
    pilImage = pilImage.resize((64, 64), Image.ANTIALIAS)
    image11 = ImageTk.PhotoImage(pilImage)
    Ivern_button = Button(root, image=image11, command=lambda: [setname12()])
    Ivern_label = Label(root, image=image11)

    Jayce1 = "https://ddragon.leagueoflegends.com/cdn/12.4.1/img/champion/" + Jayce + ".png"
    r = requests.get(Jayce1)
    pilImage = Image.open(BytesIO(r.content))
    pilImage = pilImage.resize((64, 64), Image.ANTIALIAS)
    image12 = ImageTk.PhotoImage(pilImage)
    Jayce_button = Button(root, image=image12, command=lambda: [setname13()])
    Jayce_label = Label(root, image=image12)

    Jinx1 = "https://ddragon.leagueoflegends.com/cdn/12.4.1/img/champion/" + Jinx + ".png"
    r = requests.get(Jinx1)
    pilImage = Image.open(BytesIO(r.content))
    pilImage = pilImage.resize((64, 64), Image.ANTIALIAS)
    image13 = ImageTk.PhotoImage(pilImage)
    Jinx_button = Button(root, image=image13, command=lambda: [setname14()])
    Jinx_label = Label(root, image=image13)

    Kalista1 = "https://ddragon.leagueoflegends.com/cdn/12.4.1/img/champion/" + Kalista + ".png"
    r = requests.get(Kalista1)
    pilImage = Image.open(BytesIO(r.content))
    pilImage = pilImage.resize((64, 64), Image.ANTIALIAS)
    image14 = ImageTk.PhotoImage(pilImage)
    Kalista_button = Button(root, image=image14, command=lambda: [setname15()])
    Kalista_label = Label(root, image=image14)

    Katarina1 = "https://ddragon.leagueoflegends.com/cdn/12.4.1/img/champion/" + Katarina + ".png"
    r = requests.get(Katarina1)
    pilImage = Image.open(BytesIO(r.content))
    pilImage = pilImage.resize((64, 64), Image.ANTIALIAS)
    image15 = ImageTk.PhotoImage(pilImage)
    Katarina_button = Button(root, image=image15, command=lambda: [setname16()])
    Katarina_label = Label(root, image=image15)

    Malphite1 = "https://ddragon.leagueoflegends.com/cdn/12.4.1/img/champion/" + Malphite + ".png"
    r = requests.get(Malphite1)
    pilImage = Image.open(BytesIO(r.content))
    pilImage = pilImage.resize((64, 64), Image.ANTIALIAS)
    image16 = ImageTk.PhotoImage(pilImage)
    Malphite_button = Button(root, image=image16, command=lambda: [setname17()])
    Malphite_label = Label(root, image=image16)

    Maokai1 = "https://ddragon.leagueoflegends.com/cdn/12.4.1/img/champion/" + Maokai + ".png"
    r = requests.get(Maokai1)
    pilImage = Image.open(BytesIO(r.content))
    pilImage = pilImage.resize((64, 64), Image.ANTIALIAS)
    image17 = ImageTk.PhotoImage(pilImage)
    Maokai_button = Button(root, image=image17, command=lambda: [setname18()])
    Maokai_label = Label(root, image=image17)

    Nautilus1 = "https://ddragon.leagueoflegends.com/cdn/12.4.1/img/champion/" + Nautilus + ".png"
    r = requests.get(Nautilus1)
    pilImage = Image.open(BytesIO(r.content))
    pilImage = pilImage.resize((64, 64), Image.ANTIALIAS)
    image18 = ImageTk.PhotoImage(pilImage)
    Nautilus_button = Button(root, image=image18, command=lambda: [setname19()])
    Nautilus_label = Label(root, image=image18)

    Yuumi1 = "https://ddragon.leagueoflegends.com/cdn/12.4.1/img/champion/" + Yuumi + ".png"
    r = requests.get(Yuumi1)
    pilImage = Image.open(BytesIO(r.content))
    pilImage = pilImage.resize((64, 64), Image.ANTIALIAS)
    image19 = ImageTk.PhotoImage(pilImage)
    Yuumi_button = Button(root, image=image19, command=lambda: [setname20()])
    Yuumi_label = Label(root, image=image19)


    def place_champs():
        global champ_list
        print(champ_list)
        Aatrox_button.place(x=235,y=272)
        Alistar_button.place(x=315,y=272)
        Anivia_button.place(x=395,y=272)
        Azir_button.place(x=475,y=272)
        Caitlyn_button.place(x=555,y=272)
        Cassiopeia_button.place(x=635,y=272)
        Darius_button.place(x=720,y=272)
        Ekko_button.place(x=805,y=272)
        Graves_button.place(x=890,y=272)
        Gwen_button.place(x=235,y=352)
        Irelia_button.place(x=315,y=352)
        Ivern_button.place(x=395,y=352)
        Jayce_button.place(x=475,y=352)
        Jinx_button.place(x=555,y=352)
        Kalista_button.place(x=635,y=352)
        Katarina_button.place(x=720,y=352)
        Malphite_button.place(x=805,y=352)
        Maokai_button.place(x=890,y=352)
        Nautilus_button.place(x=975,y=272)
        Yuumi_button.place(x=975,y=352)
    
    global champ_count
    champ_count = 0
    def replace_champs():
        global t
        global timer
        global champ_count
        global champ_name
        global champ_list
        if champ_name == 'None':
            return

        champ_count += 1
        if champ_count == 1:
            if champ_name == 'Aatrox':
                Aatrox_button.place_forget()
                Aatrox_label.place(x=25,y=145)
            if champ_name == 'Alistar':
                Alistar_button.place_forget()
                Alistar_label.place(x=25,y=145)
            if champ_name == 'Anivia':
                Anivia_button.place_forget()
                Anivia_label.place(x=25,y=145)
                champ_list.remove('Anivia')
            if champ_name == 'Azir':
                Azir_button.place_forget()
                Azir_label.place(x=25,y=145)
            if champ_name == 'Caitlyn':
                Caitlyn_button.place_forget()
                Caitlyn_label.place(x=25,y=145)
            if champ_name == 'Cassiopeia':
                Cassiopeia_button.place_forget()
                Cassiopeia_label.place(x=25,y=145)
            if champ_name == 'Darius':
                Darius_button.place_forget()
                Darius_label.place(x=25,y=145)
            if champ_name == 'Ekko':
                Ekko_button.place_forget()
                Ekko_label.place(x=25,y=145)
            if champ_name == 'Graves':
                Graves_button.place_forget()
                Graves_label.place(x=25,y=145)
            if champ_name == 'Gwen':
                Gwen_button.place_forget()
                Gwen_label.place(x=25,y=145)
            if champ_name == 'Irelia':
                Irelia_button.place_forget()
                Irelia_label.place(x=25,y=145)
            if champ_name == 'Ivern':
                Ivern_button.place_forget()
                Ivern_label.place(x=25,y=145)
            if champ_name == 'Jayce':
                Jayce_button.place_forget()
                Jayce_label.place(x=25,y=145)
            if champ_name == 'Jinx':
                Jinx_button.place_forget()
                Jinx_label.place(x=25,y=145)
            if champ_name == 'Kalista':
                Kalista_button.place_forget()
                Kalista_label.place(x=25,y=145)
            if champ_name == 'Katarina':
                Katarina_button.place_forget()
                Katarina_label.place(x=25,y=145)
            if champ_name == 'Malphite':
                Malphite_button.place_forget()
                Malphite_label.place(x=25,y=145)
                champ_list.remove('Malphite')
            if champ_name == 'Maokai':
                Maokai_button.place_forget()
                Maokai_label.place(x=25,y=145)
            if champ_name == 'Nautilus':
                Nautilus_button.place_forget()
                Nautilus_label.place(x=25,y=145)
            if champ_name == 'Yuumi':
                Yuumi_button.place_forget()
                Yuumi_label.place(x=25,y=145)



        if champ_count == 2:
            if champ_name == 'Aatrox':
                Aatrox_button.place_forget()
                Aatrox_label.place(x=772, y=145)
            if champ_name == 'Alistar':
                Alistar_button.place_forget()
                Alistar_label.place(x=772, y=145)
            if champ_name == 'Anivia':
                Anivia_button.place_forget()
                Anivia_label.place(x=772, y=145)
            if champ_name == 'Azir':
                Azir_button.place_forget()
                Azir_label.place(x=772, y=145)
            if champ_name == 'Caitlyn':
                Caitlyn_button.place_forget()
                Caitlyn_label.place(x=772, y=145)
            if champ_name == 'Cassiopeia':
                Cassiopeia_button.place_forget()
                Cassiopeia_label.place(x=772, y=145)
            if champ_name == 'Darius':
                Darius_button.place_forget()
                Darius_label.place(x=772, y=145)
            if champ_name == 'Ekko':
                Ekko_button.place_forget()
                Ekko_label.place(x=772, y=145)
            if champ_name == 'Graves':
                Graves_button.place_forget()
                Graves_label.place(x=772, y=145)
            if champ_name == 'Gwen':
                Gwen_button.place_forget()
                Gwen_label.place(x=772, y=145)
            if champ_name == 'Irelia':
                Irelia_button.place_forget()
                Irelia_label.place(x=772, y=145)
            if champ_name == 'Ivern':
                Ivern_button.place_forget()
                Ivern_label.place(x=772, y=145)
            if champ_name == 'Jayce':
                Jayce_button.place_forget()
                Jayce_label.place(x=772, y=145)
            if champ_name == 'Jinx':
                Jinx_button.place_forget()
                Jinx_label.place(x=772, y=145)
            if champ_name == 'Kalista':
                Kalista_button.place_forget()
                Kalista_label.place(x=772, y=145)
            if champ_name == 'Katarina':
                Katarina_button.place_forget()
                Katarina_label.place(x=772, y=145)
            if champ_name == 'Malphite':
                Malphite_button.place_forget()
                Malphite_label.place(x=772, y=145)
            if champ_name == 'Maokai':
                Maokai_button.place_forget()
                Maokai_label.place(x=772, y=145)
            if champ_name == 'Nautilus':
                Nautilus_button.place_forget()
                Nautilus_label.place(x=772, y=145)
            if champ_name == 'Yuumi':
                Yuumi_button.place_forget()
                Yuumi_label.place(x=772, y=145)


        if champ_count == 3:
            if champ_name == 'Aatrox':
                Aatrox_button.place_forget()
                Aatrox_label.place(x=130,y=145)
            if champ_name == 'Alistar':
                Alistar_button.place_forget()
                Alistar_label.place(x=130,y=145)
            if champ_name == 'Anivia':
                Anivia_button.place_forget()
                Anivia_label.place(x=130,y=145)
            if champ_name == 'Azir':
                Azir_button.place_forget()
                Azir_label.place(x=130,y=145)
            if champ_name == 'Caitlyn':
                Caitlyn_button.place_forget()
                Caitlyn_label.place(x=130,y=145)
            if champ_name == 'Cassiopeia':
                Cassiopeia_button.place_forget()
                Cassiopeia_label.place(x=130,y=145)
            if champ_name == 'Darius':
                Darius_button.place_forget()
                Darius_label.place(x=130,y=145)
            if champ_name == 'Ekko':
                Ekko_button.place_forget()
                Ekko_label.place(x=130,y=145)
            if champ_name == 'Graves':
                Graves_button.place_forget()
                Graves_label.place(x=130,y=145)
            if champ_name == 'Gwen':
                Gwen_button.place_forget()
                Gwen_label.place(x=130,y=145)
            if champ_name == 'Irelia':
                Irelia_button.place_forget()
                Irelia_label.place(x=130,y=145)
            if champ_name == 'Ivern':
                Ivern_button.place_forget()
                Ivern_label.place(x=130,y=145)
            if champ_name == 'Jayce':
                Jayce_button.place_forget()
                Jayce_label.place(x=130,y=145)
            if champ_name == 'Jinx':
                Jinx_button.place_forget()
                Jinx_label.place(x=130,y=145)
            if champ_name == 'Kalista':
                Kalista_button.place_forget()
                Kalista_label.place(x=130,y=145)
            if champ_name == 'Katarina':
                Katarina_button.place_forget()
                Katarina_label.place(x=130,y=145)
            if champ_name == 'Malphite':
                Malphite_button.place_forget()
                Malphite_label.place(x=130,y=145)
            if champ_name == 'Maokai':
                Maokai_button.place_forget()
                Maokai_label.place(x=130,y=145)
            if champ_name == 'Nautilus':
                Nautilus_button.place_forget()
                Nautilus_label.place(x=130,y=145)
            if champ_name == 'Yuumi':
                Yuumi_button.place_forget()
                Yuumi_label.place(x=130,y=145)


        if champ_count == 4:
            if champ_name == 'Aatrox':
                Aatrox_button.place_forget()
                Aatrox_label.place(x=877,y=145)
            if champ_name == 'Alistar':
                Alistar_button.place_forget()
                Alistar_label.place(x=877,y=145)
            if champ_name == 'Anivia':
                Anivia_button.place_forget()
                Anivia_label.place(x=877,y=145)
            if champ_name == 'Azir':
                Azir_button.place_forget()
                Azir_label.place(x=877,y=145)
            if champ_name == 'Caitlyn':
                Caitlyn_button.place_forget()
                Caitlyn_label.place(x=877,y=145)
            if champ_name == 'Cassiopeia':
                Cassiopeia_button.place_forget()
                Cassiopeia_label.place(x=877,y=145)
            if champ_name == 'Darius':
                Darius_button.place_forget()
                Darius_label.place(x=877,y=145)
            if champ_name == 'Ekko':
                Ekko_button.place_forget()
                Ekko_label.place(x=877,y=145)
            if champ_name == 'Graves':
                Graves_button.place_forget()
                Graves_label.place(x=877,y=145)
            if champ_name == 'Gwen':
                Gwen_button.place_forget()
                Gwen_label.place(x=877,y=145)
            if champ_name == 'Irelia':
                Irelia_button.place_forget()
                Irelia_label.place(x=877,y=145)
            if champ_name == 'Ivern':
                Ivern_button.place_forget()
                Ivern_label.place(x=877,y=145)
            if champ_name == 'Jayce':
                Jayce_button.place_forget()
                Jayce_label.place(x=877,y=145)
            if champ_name == 'Jinx':
                Jinx_button.place_forget()
                Jinx_label.place(x=877,y=145)
            if champ_name == 'Kalista':
                Kalista_button.place_forget()
                Kalista_label.place(x=877,y=145)
            if champ_name == 'Katarina':
                Katarina_button.place_forget()
                Katarina_label.place(x=877,y=145)
            if champ_name == 'Malphite':
                Malphite_button.place_forget()
                Malphite_label.place(x=877,y=145)
            if champ_name == 'Maokai':
                Maokai_button.place_forget()
                Maokai_label.place(x=877,y=145)
            if champ_name == 'Nautilus':
                Nautilus_button.place_forget()
                Nautilus_label.place(x=877,y=145)
            if champ_name == 'Yuumi':
                Yuumi_button.place_forget()
                Yuumi_label.place(x=877,y=145)


        if champ_count == 5:
            if champ_name == 'Aatrox':
                Aatrox_button.place_forget()
                Aatrox_label.place(x=235,y=145)
            if champ_name == 'Alistar':
                Alistar_button.place_forget()
                Alistar_label.place(x=235,y=145)
            if champ_name == 'Anivia':
                Anivia_button.place_forget()
                Anivia_label.place(x=235,y=145)
            if champ_name == 'Azir':
                Azir_button.place_forget()
                Azir_label.place(x=235,y=145)
            if champ_name == 'Caitlyn':
                Caitlyn_button.place_forget()
                Caitlyn_label.place(x=235,y=145)
            if champ_name == 'Cassiopeia':
                Cassiopeia_button.place_forget()
                Cassiopeia_label.place(x=235,y=145)
            if champ_name == 'Darius':
                Darius_button.place_forget()
                Darius_label.place(x=235,y=145)
            if champ_name == 'Ekko':
                Ekko_button.place_forget()
                Ekko_label.place(x=235,y=145)
            if champ_name == 'Graves':
                Graves_button.place_forget()
                Graves_label.place(x=235,y=145)
            if champ_name == 'Gwen':
                Gwen_button.place_forget()
                Gwen_label.place(x=235,y=145)
            if champ_name == 'Irelia':
                Irelia_button.place_forget()
                Irelia_label.place(x=235,y=145)
            if champ_name == 'Ivern':
                Ivern_button.place_forget()
                Ivern_label.place(x=235,y=145)
            if champ_name == 'Jayce':
                Jayce_button.place_forget()
                Jayce_label.place(x=235,y=145)
            if champ_name == 'Jinx':
                Jinx_button.place_forget()
                Jinx_label.place(x=235,y=145)
            if champ_name == 'Kalista':
                Kalista_button.place_forget()
                Kalista_label.place(x=235,y=145)
            if champ_name == 'Katarina':
                Katarina_button.place_forget()
                Katarina_label.place(x=235,y=145)
            if champ_name == 'Malphite':
                Malphite_button.place_forget()
                Malphite_label.place(x=235,y=145)
            if champ_name == 'Maokai':
                Maokai_button.place_forget()
                Maokai_label.place(x=235,y=145)
            if champ_name == 'Nautilus':
                Nautilus_button.place_forget()
                Nautilus_label.place(x=235,y=145)
            if champ_name == 'Yuumi':
                Yuumi_button.place_forget()
                Yuumi_label.place(x=235,y=145)

            
        if champ_count == 6:
            if champ_name == 'Aatrox':
                Aatrox_button.place_forget()
                Aatrox_label.place(x=982,y=145)
            if champ_name == 'Alistar':
                Alistar_button.place_forget()
                Alistar_label.place(x=982,y=145)
            if champ_name == 'Anivia':
                Anivia_button.place_forget()
                Anivia_label.place(x=982,y=145)
            if champ_name == 'Azir':
                Azir_button.place_forget()
                Azir_label.place(x=982,y=145)
            if champ_name == 'Caitlyn':
                Caitlyn_button.place_forget()
                Caitlyn_label.place(x=982,y=145)
            if champ_name == 'Cassiopeia':
                Cassiopeia_button.place_forget()
                Cassiopeia_label.place(x=982,y=145)
            if champ_name == 'Darius':
                Darius_button.place_forget()
                Darius_label.place(x=982,y=145)
            if champ_name == 'Ekko':
                Ekko_button.place_forget()
                Ekko_label.place(x=982,y=145)
            if champ_name == 'Graves':
                Graves_button.place_forget()
                Graves_label.place(x=982,y=145)
            if champ_name == 'Gwen':
                Gwen_button.place_forget()
                Gwen_label.place(x=982,y=145)
            if champ_name == 'Irelia':
                Irelia_button.place_forget()
                Irelia_label.place(x=982,y=145)
            if champ_name == 'Ivern':
                Ivern_button.place_forget()
                Ivern_label.place(x=982,y=145)
            if champ_name == 'Jayce':
                Jayce_button.place_forget()
                Jayce_label.place(x=982,y=145)
            if champ_name == 'Jinx':
                Jinx_button.place_forget()
                Jinx_label.place(x=982,y=145)
            if champ_name == 'Kalista':
                Kalista_button.place_forget()
                Kalista_label.place(x=982,y=145)
            if champ_name == 'Katarina':
                Katarina_button.place_forget()
                Katarina_label.place(x=982,y=145)
            if champ_name == 'Malphite':
                Malphite_button.place_forget()
                Malphite_label.place(x=982,y=145)
            if champ_name == 'Maokai':
                Maokai_button.place_forget()
                Maokai_label.place(x=982,y=145)
            if champ_name == 'Nautilus':
                Nautilus_button.place_forget()
                Nautilus_label.place(x=982,y=145)
            if champ_name == 'Yuumi':
                Yuumi_button.place_forget()
                Yuumi_label.place(x=982,y=145)


        if champ_count == 7:
            if champ_name == 'Aatrox':
                Aatrox_button.place_forget()
                Aatrox_label.place(x=340,y=145)
            if champ_name == 'Alistar':
                Alistar_button.place_forget()
                Alistar_label.place(x=340,y=145)
            if champ_name == 'Anivia':
                Anivia_button.place_forget()
                Anivia_label.place(x=340,y=145)
            if champ_name == 'Azir':
                Azir_button.place_forget()
                Azir_label.place(x=340,y=145)
            if champ_name == 'Caitlyn':
                Caitlyn_button.place_forget()
                Caitlyn_label.place(x=340,y=145)
            if champ_name == 'Cassiopeia':
                Cassiopeia_button.place_forget()
                Cassiopeia_label.place(x=340,y=145)
            if champ_name == 'Darius':
                Darius_button.place_forget()
                Darius_label.place(x=340,y=145)
            if champ_name == 'Ekko':
                Ekko_button.place_forget()
                Ekko_label.place(x=340,y=145)
            if champ_name == 'Graves':
                Graves_button.place_forget()
                Graves_label.place(x=340,y=145)
            if champ_name == 'Gwen':
                Gwen_button.place_forget()
                Gwen_label.place(x=340,y=145)
            if champ_name == 'Irelia':
                Irelia_button.place_forget()
                Irelia_label.place(x=340,y=145)
            if champ_name == 'Ivern':
                Ivern_button.place_forget()
                Ivern_label.place(x=340,y=145)
            if champ_name == 'Jayce':
                Jayce_button.place_forget()
                Jayce_label.place(x=340,y=145)
            if champ_name == 'Jinx':
                Jinx_button.place_forget()
                Jinx_label.place(x=340,y=145)
            if champ_name == 'Kalista':
                Kalista_button.place_forget()
                Kalista_label.place(x=340,y=145)
            if champ_name == 'Katarina':
                Katarina_button.place_forget()
                Katarina_label.place(x=340,y=145)
            if champ_name == 'Malphite':
                Malphite_button.place_forget()
                Malphite_label.place(x=340,y=145)
            if champ_name == 'Maokai':
                Maokai_button.place_forget()
                Maokai_label.place(x=340,y=145)
            if champ_name == 'Nautilus':
                Nautilus_button.place_forget()
                Nautilus_label.place(x=340,y=145)
            if champ_name == 'Yuumi':
                Yuumi_button.place_forget()
                Yuumi_label.place(x=340,y=145)


        if champ_count == 8:
            if champ_name == 'Aatrox':
                Aatrox_button.place_forget()
                Aatrox_label.place(x=1087,y=145)
            if champ_name == 'Alistar':
                Alistar_button.place_forget()
                Alistar_label.place(x=1087,y=145)
            if champ_name == 'Anivia':
                Anivia_button.place_forget()
                Anivia_label.place(x=1087,y=145)
            if champ_name == 'Azir':
                Azir_button.place_forget()
                Azir_label.place(x=1087,y=145)
            if champ_name == 'Caitlyn':
                Caitlyn_button.place_forget()
                Caitlyn_label.place(x=1087,y=145)
            if champ_name == 'Cassiopeia':
                Cassiopeia_button.place_forget()
                Cassiopeia_label.place(x=1087,y=145)
            if champ_name == 'Darius':
                Darius_button.place_forget()
                Darius_label.place(x=1087,y=145)
            if champ_name == 'Ekko':
                Ekko_button.place_forget()
                Ekko_label.place(x=1087,y=145)
            if champ_name == 'Graves':
                Graves_button.place_forget()
                Graves_label.place(x=1087,y=145)
            if champ_name == 'Gwen':
                Gwen_button.place_forget()
                Gwen_label.place(x=1087,y=145)
            if champ_name == 'Irelia':
                Irelia_button.place_forget()
                Irelia_label.place(x=1087,y=145)
            if champ_name == 'Ivern':
                Ivern_button.place_forget()
                Ivern_label.place(x=1087,y=145)
            if champ_name == 'Jayce':
                Jayce_button.place_forget()
                Jayce_label.place(x=1087,y=145)
            if champ_name == 'Jinx':
                Jinx_button.place_forget()
                Jinx_label.place(x=1087,y=145)
            if champ_name == 'Kalista':
                Kalista_button.place_forget()
                Kalista_label.place(x=1087,y=145)
            if champ_name == 'Katarina':
                Katarina_button.place_forget()
                Katarina_label.place(x=1087,y=145)
            if champ_name == 'Malphite':
                Malphite_button.place_forget()
                Malphite_label.place(x=1087,y=145)
            if champ_name == 'Maokai':
                Maokai_button.place_forget()
                Maokai_label.place(x=1087,y=145)
            if champ_name == 'Nautilus':
                Nautilus_button.place_forget()
                Nautilus_label.place(x=1087,y=145)
            if champ_name == 'Yuumi':
                Yuumi_button.place_forget()
                Yuumi_label.place(x=1087,y=145)


        if champ_count == 9:
            if champ_name == 'Aatrox':
                Aatrox_button.place_forget()
                Aatrox_label.place(x=442,y=145)
            if champ_name == 'Alistar':
                Alistar_button.place_forget()
                Alistar_label.place(x=442,y=145)
            if champ_name == 'Anivia':
                Anivia_button.place_forget()
                Anivia_label.place(x=442,y=145)
            if champ_name == 'Azir':
                Azir_button.place_forget()
                Azir_label.place(x=442,y=145)
            if champ_name == 'Caitlyn':
                Caitlyn_button.place_forget()
                Caitlyn_label.place(x=442,y=145)
            if champ_name == 'Cassiopeia':
                Cassiopeia_button.place_forget()
                Cassiopeia_label.place(x=442,y=145)
            if champ_name == 'Darius':
                Darius_button.place_forget()
                Darius_label.place(x=442,y=145)
            if champ_name == 'Ekko':
                Ekko_button.place_forget()
                Ekko_label.place(x=442,y=145)
            if champ_name == 'Graves':
                Graves_button.place_forget()
                Graves_label.place(x=442,y=145)
            if champ_name == 'Gwen':
                Gwen_button.place_forget()
                Gwen_label.place(x=442,y=145)
            if champ_name == 'Irelia':
                Irelia_button.place_forget()
                Irelia_label.place(x=442,y=145)
            if champ_name == 'Ivern':
                Ivern_button.place_forget()
                Ivern_label.place(x=442,y=145)
            if champ_name == 'Jayce':
                Jayce_button.place_forget()
                Jayce_label.place(x=442,y=145)
            if champ_name == 'Jinx':
                Jinx_button.place_forget()
                Jinx_label.place(x=442,y=145)
            if champ_name == 'Kalista':
                Kalista_button.place_forget()
                Kalista_label.place(x=442,y=145)
            if champ_name == 'Katarina':
                Katarina_button.place_forget()
                Katarina_label.place(x=442,y=145)
            if champ_name == 'Malphite':
                Malphite_button.place_forget()
                Malphite_label.place(x=442,y=145)
            if champ_name == 'Maokai':
                Maokai_button.place_forget()
                Maokai_label.place(x=442,y=145)
            if champ_name == 'Nautilus':
                Nautilus_button.place_forget()
                Nautilus_label.place(x=442,y=145)
            if champ_name == 'Yuumi':
                Yuumi_button.place_forget()
                Yuumi_label.place(x=442,y=145)


        if champ_count == 10:
            if champ_name == 'Aatrox':
                Aatrox_button.place_forget()
                Aatrox_label.place(x=1190,y=145)
            if champ_name == 'Alistar':
                Alistar_button.place_forget()
                Alistar_label.place(x=1190,y=145)
            if champ_name == 'Anivia':
                Anivia_button.place_forget()
                Anivia_label.place(x=1190,y=145)
            if champ_name == 'Azir':
                Azir_button.place_forget()
                Azir_label.place(x=1190,y=145)
            if champ_name == 'Caitlyn':
                Caitlyn_button.place_forget()
                Caitlyn_label.place(x=1190,y=145)
            if champ_name == 'Cassiopeia':
                Cassiopeia_button.place_forget()
                Cassiopeia_label.place(x=1190,y=145)
            if champ_name == 'Darius':
                Darius_button.place_forget()
                Darius_label.place(x=1190,y=145)
            if champ_name == 'Ekko':
                Ekko_button.place_forget()
                Ekko_label.place(x=1190,y=145)
            if champ_name == 'Graves':
                Graves_button.place_forget()
                Graves_label.place(x=1190,y=145)
            if champ_name == 'Gwen':
                Gwen_button.place_forget()
                Gwen_label.place(x=1190,y=145)
            if champ_name == 'Irelia':
                Irelia_button.place_forget()
                Irelia_label.place(x=1190,y=145)
            if champ_name == 'Ivern':
                Ivern_button.place_forget()
                Ivern_label.place(x=1190,y=145)
            if champ_name == 'Jayce':
                Jayce_button.place_forget()
                Jayce_label.place(x=1190,y=145)
            if champ_name == 'Jinx':
                Jinx_button.place_forget()
                Jinx_label.place(x=1190,y=145)
            if champ_name == 'Kalista':
                Kalista_button.place_forget()
                Kalista_label.place(x=1190,y=145)
            if champ_name == 'Katarina':
                Katarina_button.place_forget()
                Katarina_label.place(x=1190,y=145)
            if champ_name == 'Malphite':
                Malphite_button.place_forget()
                Malphite_label.place(x=1190,y=145)
            if champ_name == 'Maokai':
                Maokai_button.place_forget()
                Maokai_label.place(x=1190,y=145)
            if champ_name == 'Nautilus':
                Nautilus_button.place_forget()
                Nautilus_label.place(x=1190,y=145)
            if champ_name == 'Yuumi':
                Yuumi_button.place_forget()
                Yuumi_label.place(x=1190,y=145)


        if champ_count == 11:
            if champ_name == 'Aatrox':
                Aatrox_button.place_forget()
                Aatrox_label.place(x=50,y=270)
            if champ_name == 'Alistar':
                Alistar_button.place_forget()
                Alistar_label.place(x=50,y=270)
            if champ_name == 'Anivia':
                Anivia_button.place_forget()
                Anivia_label.place(x=50,y=270)
            if champ_name == 'Azir':
                Azir_button.place_forget()
                Azir_label.place(x=50,y=270)
            if champ_name == 'Caitlyn':
                Caitlyn_button.place_forget()
                Caitlyn_label.place(x=50,y=270)
            if champ_name == 'Cassiopeia':
                Cassiopeia_button.place_forget()
                Cassiopeia_label.place(x=50,y=270)
            if champ_name == 'Darius':
                Darius_button.place_forget()
                Darius_label.place(x=50,y=270)
            if champ_name == 'Ekko':
                Ekko_button.place_forget()
                Ekko_label.place(x=50,y=270)
            if champ_name == 'Graves':
                Graves_button.place_forget()
                Graves_label.place(x=50,y=270)
            if champ_name == 'Gwen':
                Gwen_button.place_forget()
                Gwen_label.place(x=50,y=270)
            if champ_name == 'Irelia':
                Irelia_button.place_forget()
                Irelia_label.place(x=50,y=270)
            if champ_name == 'Ivern':
                Ivern_button.place_forget()
                Ivern_label.place(x=50,y=270)
            if champ_name == 'Jayce':
                Jayce_button.place_forget()
                Jayce_label.place(x=50,y=270)
            if champ_name == 'Jinx':
                Jinx_button.place_forget()
                Jinx_label.place(x=50,y=270)
            if champ_name == 'Kalista':
                Kalista_button.place_forget()
                Kalista_label.place(x=50,y=270)
            if champ_name == 'Katarina':
                Katarina_button.place_forget()
                Katarina_label.place(x=50,y=270)
            if champ_name == 'Malphite':
                Malphite_button.place_forget()
                Malphite_label.place(x=50,y=270)
            if champ_name == 'Maokai':
                Maokai_button.place_forget()
                Maokai_label.place(x=50,y=270)
            if champ_name == 'Nautilus':
                Nautilus_button.place_forget()
                Nautilus_label.place(x=50,y=270)
            if champ_name == 'Yuumi':
                Yuumi_button.place_forget()
                Yuumi_label.place(x=50,y=270)


        if champ_count == 12:
            if champ_name == 'Aatrox':
                Aatrox_button.place_forget()
                Aatrox_label.place(x=1160,y=270)
            if champ_name == 'Alistar':
                Alistar_button.place_forget()
                Alistar_label.place(x=1160,y=270)
            if champ_name == 'Anivia':
                Anivia_button.place_forget()
                Anivia_label.place(x=1160,y=270)
            if champ_name == 'Azir':
                Azir_button.place_forget()
                Azir_label.place(x=1160,y=270)
            if champ_name == 'Caitlyn':
                Caitlyn_button.place_forget()
                Caitlyn_label.place(x=1160,y=270)
            if champ_name == 'Cassiopeia':
                Cassiopeia_button.place_forget()
                Cassiopeia_label.place(x=1160,y=270)
            if champ_name == 'Darius':
                Darius_button.place_forget()
                Darius_label.place(x=1160,y=270)
            if champ_name == 'Ekko':
                Ekko_button.place_forget()
                Ekko_label.place(x=1160,y=270)
            if champ_name == 'Graves':
                Graves_button.place_forget()
                Graves_label.place(x=1160,y=270)
            if champ_name == 'Gwen':
                Gwen_button.place_forget()
                Gwen_label.place(x=1160,y=270)
            if champ_name == 'Irelia':
                Irelia_button.place_forget()
                Irelia_label.place(x=1160,y=270)
            if champ_name == 'Ivern':
                Ivern_button.place_forget()
                Ivern_label.place(x=1160,y=270)
            if champ_name == 'Jayce':
                Jayce_button.place_forget()
                Jayce_label.place(x=1160,y=270)
            if champ_name == 'Jinx':
                Jinx_button.place_forget()
                Jinx_label.place(x=1160,y=270)
            if champ_name == 'Kalista':
                Kalista_button.place_forget()
                Kalista_label.place(x=1160,y=270)
            if champ_name == 'Katarina':
                Katarina_button.place_forget()
                Katarina_label.place(x=1160,y=270)
            if champ_name == 'Malphite':
                Malphite_button.place_forget()
                Malphite_label.place(x=1160,y=270)
            if champ_name == 'Maokai':
                Maokai_button.place_forget()
                Maokai_label.place(x=1160,y=270)
            if champ_name == 'Nautilus':
                Nautilus_button.place_forget()
                Nautilus_label.place(x=1160,y=270)
            if champ_name == 'Yuumi':
                Yuumi_button.place_forget()
                Yuumi_label.place(x=1160,y=270)


        if champ_count == 14:
            if champ_name == 'Aatrox':
                Aatrox_button.place_forget()
                Aatrox_label.place(x=50,y=400)
            if champ_name == 'Alistar':
                Alistar_button.place_forget()
                Alistar_label.place(x=50,y=400)
            if champ_name == 'Anivia':
                Anivia_button.place_forget()
                Anivia_label.place(x=50,y=400)
            if champ_name == 'Azir':
                Azir_button.place_forget()
                Azir_label.place(x=50,y=400)
            if champ_name == 'Caitlyn':
                Caitlyn_button.place_forget()
                Caitlyn_label.place(x=50,y=400)
            if champ_name == 'Cassiopeia':
                Cassiopeia_button.place_forget()
                Cassiopeia_label.place(x=50,y=400)
            if champ_name == 'Darius':
                Darius_button.place_forget()
                Darius_label.place(x=50,y=400)
            if champ_name == 'Ekko':
                Ekko_button.place_forget()
                Ekko_label.place(x=50,y=400)
            if champ_name == 'Graves':
                Graves_button.place_forget()
                Graves_label.place(x=50,y=400)
            if champ_name == 'Gwen':
                Gwen_button.place_forget()
                Gwen_label.place(x=50,y=400)
            if champ_name == 'Irelia':
                Irelia_button.place_forget()
                Irelia_label.place(x=50,y=400)
            if champ_name == 'Ivern':
                Ivern_button.place_forget()
                Ivern_label.place(x=50,y=400)
            if champ_name == 'Jayce':
                Jayce_button.place_forget()
                Jayce_label.place(x=50,y=400)
            if champ_name == 'Jinx':
                Jinx_button.place_forget()
                Jinx_label.place(x=50,y=400)
            if champ_name == 'Kalista':
                Kalista_button.place_forget()
                Kalista_label.place(x=50,y=400)
            if champ_name == 'Katarina':
                Katarina_button.place_forget()
                Katarina_label.place(x=50,y=400)
            if champ_name == 'Malphite':
                Malphite_button.place_forget()
                Malphite_label.place(x=50,y=400)
            if champ_name == 'Maokai':
                Maokai_button.place_forget()
                Maokai_label.place(x=50,y=400)
            if champ_name == 'Nautilus':
                Nautilus_button.place_forget()
                Nautilus_label.place(x=50,y=400)
            if champ_name == 'Yuumi':
                Yuumi_button.place_forget()
                Yuumi_label.place(x=50,y=400)


        if champ_count == 13:
            if champ_name == 'Aatrox':
                Aatrox_button.place_forget()
                Aatrox_label.place(x=1160,y=400)
            if champ_name == 'Alistar':
                Alistar_button.place_forget()
                Alistar_label.place(x=1160,y=400)
            if champ_name == 'Anivia':
                Anivia_button.place_forget()
                Anivia_label.place(x=1160,y=400)
            if champ_name == 'Azir':
                Azir_button.place_forget()
                Azir_label.place(x=1160,y=400)
            if champ_name == 'Caitlyn':
                Caitlyn_button.place_forget()
                Caitlyn_label.place(x=1160,y=400)
            if champ_name == 'Cassiopeia':
                Cassiopeia_button.place_forget()
                Cassiopeia_label.place(x=1160,y=400)
            if champ_name == 'Darius':
                Darius_button.place_forget()
                Darius_label.place(x=1160,y=400)
            if champ_name == 'Ekko':
                Ekko_button.place_forget()
                Ekko_label.place(x=1160,y=400)
            if champ_name == 'Graves':
                Graves_button.place_forget()
                Graves_label.place(x=1160,y=400)
            if champ_name == 'Gwen':
                Gwen_button.place_forget()
                Gwen_label.place(x=1160,y=400)
            if champ_name == 'Irelia':
                Irelia_button.place_forget()
                Irelia_label.place(x=1160,y=400)
            if champ_name == 'Ivern':
                Ivern_button.place_forget()
                Ivern_label.place(x=1160,y=400)
            if champ_name == 'Jayce':
                Jayce_button.place_forget()
                Jayce_label.place(x=1160,y=400)
            if champ_name == 'Jinx':
                Jinx_button.place_forget()
                Jinx_label.place(x=1160,y=400)
            if champ_name == 'Kalista':
                Kalista_button.place_forget()
                Kalista_label.place(x=1160,y=400)
            if champ_name == 'Katarina':
                Katarina_button.place_forget()
                Katarina_label.place(x=1160,y=400)
            if champ_name == 'Malphite':
                Malphite_button.place_forget()
                Malphite_label.place(x=1160,y=400)
            if champ_name == 'Maokai':
                Maokai_button.place_forget()
                Maokai_label.place(x=1160,y=400)
            if champ_name == 'Nautilus':
                Nautilus_button.place_forget()
                Nautilus_label.place(x=1160,y=400)
            if champ_name == 'Yuumi':
                Yuumi_button.place_forget()
                Yuumi_label.place(x=1160,y=400)


        if champ_count == 15:
            if champ_name == 'Aatrox':
                Aatrox_button.place_forget()
                Aatrox_label.place(x=50,y=530)
            if champ_name == 'Alistar':
                Alistar_button.place_forget()
                Alistar_label.place(x=50,y=530)
            if champ_name == 'Anivia':
                Anivia_button.place_forget()
                Anivia_label.place(x=50,y=530)
            if champ_name == 'Azir':
                Azir_button.place_forget()
                Azir_label.place(x=50,y=530)
            if champ_name == 'Caitlyn':
                Caitlyn_button.place_forget()
                Caitlyn_label.place(x=50,y=530)
            if champ_name == 'Cassiopeia':
                Cassiopeia_button.place_forget()
                Cassiopeia_label.place(x=50,y=530)
            if champ_name == 'Darius':
                Darius_button.place_forget()
                Darius_label.place(x=50,y=530)
            if champ_name == 'Ekko':
                Ekko_button.place_forget()
                Ekko_label.place(x=50,y=530)
            if champ_name == 'Graves':
                Graves_button.place_forget()
                Graves_label.place(x=50,y=530)
            if champ_name == 'Gwen':
                Gwen_button.place_forget()
                Gwen_label.place(x=50,y=530)
            if champ_name == 'Irelia':
                Irelia_button.place_forget()
                Irelia_label.place(x=50,y=530)
            if champ_name == 'Ivern':
                Ivern_button.place_forget()
                Ivern_label.place(x=50,y=530)
            if champ_name == 'Jayce':
                Jayce_button.place_forget()
                Jayce_label.place(x=50,y=530)
            if champ_name == 'Jinx':
                Jinx_button.place_forget()
                Jinx_label.place(x=50,y=530)
            if champ_name == 'Kalista':
                Kalista_button.place_forget()
                Kalista_label.place(x=50,y=530)
            if champ_name == 'Katarina':
                Katarina_button.place_forget()
                Katarina_label.place(x=50,y=530)
            if champ_name == 'Malphite':
                Malphite_button.place_forget()
                Malphite_label.place(x=50,y=530)
            if champ_name == 'Maokai':
                Maokai_button.place_forget()
                Maokai_label.place(x=50,y=530)
            if champ_name == 'Nautilus':
                Nautilus_button.place_forget()
                Nautilus_label.place(x=50,y=530)
            if champ_name == 'Yuumi':
                Yuumi_button.place_forget()
                Yuumi_label.place(x=50,y=530)


        if champ_count == 16:
            if champ_name == 'Aatrox':
                Aatrox_button.place_forget()
                Aatrox_label.place(x=1160,y=530)
            if champ_name == 'Alistar':
                Alistar_button.place_forget()
                Alistar_label.place(x=1160,y=530)
            if champ_name == 'Anivia':
                Anivia_button.place_forget()
                Anivia_label.place(x=1160,y=530)
            if champ_name == 'Azir':
                Azir_button.place_forget()
                Azir_label.place(x=1160,y=530)
            if champ_name == 'Caitlyn':
                Caitlyn_button.place_forget()
                Caitlyn_label.place(x=1160,y=530)
            if champ_name == 'Cassiopeia':
                Cassiopeia_button.place_forget()
                Cassiopeia_label.place(x=1160,y=530)
            if champ_name == 'Darius':
                Darius_button.place_forget()
                Darius_label.place(x=1160,y=530)
            if champ_name == 'Ekko':
                Ekko_button.place_forget()
                Ekko_label.place(x=1160,y=530)
            if champ_name == 'Graves':
                Graves_button.place_forget()
                Graves_label.place(x=1160,y=530)
            if champ_name == 'Gwen':
                Gwen_button.place_forget()
                Gwen_label.place(x=1160,y=530)
            if champ_name == 'Irelia':
                Irelia_button.place_forget()
                Irelia_label.place(x=1160,y=530)
            if champ_name == 'Ivern':
                Ivern_button.place_forget()
                Ivern_label.place(x=1160,y=530)
            if champ_name == 'Jayce':
                Jayce_button.place_forget()
                Jayce_label.place(x=1160,y=530)
            if champ_name == 'Jinx':
                Jinx_button.place_forget()
                Jinx_label.place(x=1160,y=530)
            if champ_name == 'Kalista':
                Kalista_button.place_forget()
                Kalista_label.place(x=1160,y=530)
            if champ_name == 'Katarina':
                Katarina_button.place_forget()
                Katarina_label.place(x=1160,y=530)
            if champ_name == 'Malphite':
                Malphite_button.place_forget()
                Malphite_label.place(x=1160,y=530)
            if champ_name == 'Maokai':
                Maokai_button.place_forget()
                Maokai_label.place(x=1160,y=530)
            if champ_name == 'Nautilus':
                Nautilus_button.place_forget()
                Nautilus_label.place(x=1160,y=530)
            if champ_name == 'Yuumi':
                Yuumi_button.place_forget()
                Yuumi_label.place(x=1160,y=530)
    
        if champ_count == 18:
            if champ_name == 'Aatrox':
                Aatrox_button.place_forget()
                Aatrox_label.place(x=50,y=660)
            if champ_name == 'Alistar':
                Alistar_button.place_forget()
                Alistar_label.place(x=50,y=660)
            if champ_name == 'Anivia':
                Anivia_button.place_forget()
                Anivia_label.place(x=50,y=660)
            if champ_name == 'Azir':
                Azir_button.place_forget()
                Azir_label.place(x=50,y=660)
            if champ_name == 'Caitlyn':
                Caitlyn_button.place_forget()
                Caitlyn_label.place(x=50,y=660)
            if champ_name == 'Cassiopeia':
                Cassiopeia_button.place_forget()
                Cassiopeia_label.place(x=50,y=660)
            if champ_name == 'Darius':
                Darius_button.place_forget()
                Darius_label.place(x=50,y=660)
            if champ_name == 'Ekko':
                Ekko_button.place_forget()
                Ekko_label.place(x=50,y=660)
            if champ_name == 'Graves':
                Graves_button.place_forget()
                Graves_label.place(x=50,y=660)
            if champ_name == 'Gwen':
                Gwen_button.place_forget()
                Gwen_label.place(x=50,y=660)
            if champ_name == 'Irelia':
                Irelia_button.place_forget()
                Irelia_label.place(x=50,y=660)
            if champ_name == 'Ivern':
                Ivern_button.place_forget()
                Ivern_label.place(x=50,y=660)
            if champ_name == 'Jayce':
                Jayce_button.place_forget()
                Jayce_label.place(x=50,y=660)
            if champ_name == 'Jinx':
                Jinx_button.place_forget()
                Jinx_label.place(x=50,y=660)
            if champ_name == 'Kalista':
                Kalista_button.place_forget()
                Kalista_label.place(x=50,y=660)
            if champ_name == 'Katarina':
                Katarina_button.place_forget()
                Katarina_label.place(x=50,y=660)
            if champ_name == 'Malphite':
                Malphite_button.place_forget()
                Malphite_label.place(x=50,y=660)
            if champ_name == 'Maokai':
                Maokai_button.place_forget()
                Maokai_label.place(x=50,y=660)
            if champ_name == 'Nautilus':
                Nautilus_button.place_forget()
                Nautilus_label.place(x=50,y=660)
            if champ_name == 'Yuumi':
                Yuumi_button.place_forget()
                Yuumi_label.place(x=50,y=660)

        if champ_count == 17:
            if champ_name == 'Aatrox':
                Aatrox_button.place_forget()
                Aatrox_label.place(x=1160,y=660)
            if champ_name == 'Alistar':
                Alistar_button.place_forget()
                Alistar_label.place(x=1160,y=660)
            if champ_name == 'Anivia':
                Anivia_button.place_forget()
                Anivia_label.place(x=1160,y=660)
            if champ_name == 'Azir':
                Azir_button.place_forget()
                Azir_label.place(x=1160,y=660)
            if champ_name == 'Caitlyn':
                Caitlyn_button.place_forget()
                Caitlyn_label.place(x=1160,y=660)
            if champ_name == 'Cassiopeia':
                Cassiopeia_button.place_forget()
                Cassiopeia_label.place(x=1160,y=660)
            if champ_name == 'Darius':
                Darius_button.place_forget()
                Darius_label.place(x=1160,y=660)
            if champ_name == 'Ekko':
                Ekko_button.place_forget()
                Ekko_label.place(x=1160,y=660)
            if champ_name == 'Graves':
                Graves_button.place_forget()
                Graves_label.place(x=1160,y=660)
            if champ_name == 'Gwen':
                Gwen_button.place_forget()
                Gwen_label.place(x=1160,y=660)
            if champ_name == 'Irelia':
                Irelia_button.place_forget()
                Irelia_label.place(x=1160,y=660)
            if champ_name == 'Ivern':
                Ivern_button.place_forget()
                Ivern_label.place(x=1160,y=660)
            if champ_name == 'Jayce':
                Jayce_button.place_forget()
                Jayce_label.place(x=1160,y=660)
            if champ_name == 'Jinx':
                Jinx_button.place_forget()
                Jinx_label.place(x=1160,y=660)
            if champ_name == 'Kalista':
                Kalista_button.place_forget()
                Kalista_label.place(x=1160,y=660)
            if champ_name == 'Katarina':
                Katarina_button.place_forget()
                Katarina_label.place(x=1160,y=660)
            if champ_name == 'Malphite':
                Malphite_button.place_forget()
                Malphite_label.place(x=1160,y=660)
            if champ_name == 'Maokai':
                Maokai_button.place_forget()
                Maokai_label.place(x=1160,y=660)
            if champ_name == 'Nautilus':
                Nautilus_button.place_forget()
                Nautilus_label.place(x=1160,y=660)
            if champ_name == 'Yuumi':
                Yuumi_button.place_forget()
                Yuumi_label.place(x=1160,y=660)

        if champ_count == 19:
            if champ_name == 'Aatrox':
                Aatrox_button.place_forget()
                Aatrox_label.place(x=50,y=790)
            if champ_name == 'Alistar':
                Alistar_button.place_forget()
                Alistar_label.place(x=50,y=790)
            if champ_name == 'Anivia':
                Anivia_button.place_forget()
                Anivia_label.place(x=50,y=790)
            if champ_name == 'Azir':
                Azir_button.place_forget()
                Azir_label.place(x=50,y=790)
            if champ_name == 'Caitlyn':
                Caitlyn_button.place_forget()
                Caitlyn_label.place(x=50,y=790)
            if champ_name == 'Cassiopeia':
                Cassiopeia_button.place_forget()
                Cassiopeia_label.place(x=50,y=790)
            if champ_name == 'Darius':
                Darius_button.place_forget()
                Darius_label.place(x=50,y=790)
            if champ_name == 'Ekko':
                Ekko_button.place_forget()
                Ekko_label.place(x=50,y=790)
            if champ_name == 'Graves':
                Graves_button.place_forget()
                Graves_label.place(x=50,y=790)
            if champ_name == 'Gwen':
                Gwen_button.place_forget()
                Gwen_label.place(x=50,y=790)
            if champ_name == 'Irelia':
                Irelia_button.place_forget()
                Irelia_label.place(x=50,y=790)
            if champ_name == 'Ivern':
                Ivern_button.place_forget()
                Ivern_label.place(x=50,y=790)
            if champ_name == 'Jayce':
                Jayce_button.place_forget()
                Jayce_label.place(x=50,y=790)
            if champ_name == 'Jinx':
                Jinx_button.place_forget()
                Jinx_label.place(x=50,y=790)
            if champ_name == 'Kalista':
                Kalista_button.place_forget()
                Kalista_label.place(x=50,y=790)
            if champ_name == 'Katarina':
                Katarina_button.place_forget()
                Katarina_label.place(x=50,y=790)
            if champ_name == 'Malphite':
                Malphite_button.place_forget()
                Malphite_label.place(x=50,y=790)
            if champ_name == 'Maokai':
                Maokai_button.place_forget()
                Maokai_label.place(x=50,y=790)
            if champ_name == 'Nautilus':
                Nautilus_button.place_forget()
                Nautilus_label.place(x=50,y=790)
            if champ_name == 'Yuumi':
                Yuumi_button.place_forget()
                Yuumi_label.place(x=50,y=790)

        if champ_count == 20:
            if champ_name == 'Aatrox':
                Aatrox_button.place_forget()
                Aatrox_label.place(x=1160,y=790)
            if champ_name == 'Alistar':
                Alistar_button.place_forget()
                Alistar_label.place(x=1160,y=790)
            if champ_name == 'Anivia':
                Anivia_button.place_forget()
                Anivia_label.place(x=1160,y=790)
            if champ_name == 'Azir':
                Azir_button.place_forget()
                Azir_label.place(x=1160,y=790)
            if champ_name == 'Caitlyn':
                Caitlyn_button.place_forget()
                Caitlyn_label.place(x=1160,y=790)
            if champ_name == 'Cassiopeia':
                Cassiopeia_button.place_forget()
                Cassiopeia_label.place(x=1160,y=790)
            if champ_name == 'Darius':
                Darius_button.place_forget()
                Darius_label.place(x=1160,y=790)
            if champ_name == 'Ekko':
                Ekko_button.place_forget()
                Ekko_label.place(x=1160,y=790)
            if champ_name == 'Graves':
                Graves_button.place_forget()
                Graves_label.place(x=1160,y=790)
            if champ_name == 'Gwen':
                Gwen_button.place_forget()
                Gwen_label.place(x=1160,y=790)
            if champ_name == 'Irelia':
                Irelia_button.place_forget()
                Irelia_label.place(x=1160,y=790)
            if champ_name == 'Ivern':
                Ivern_button.place_forget()
                Ivern_label.place(x=1160,y=790)
            if champ_name == 'Jayce':
                Jayce_button.place_forget()
                Jayce_label.place(x=1160,y=790)
            if champ_name == 'Jinx':
                Jinx_button.place_forget()
                Jinx_label.place(x=1160,y=790)
            if champ_name == 'Kalista':
                Kalista_button.place_forget()
                Kalista_label.place(x=1160,y=790)
            if champ_name == 'Katarina':
                Katarina_button.place_forget()
                Katarina_label.place(x=1160,y=790)
            if champ_name == 'Malphite':
                Malphite_button.place_forget()
                Malphite_label.place(x=1160,y=790)
            if champ_name == 'Maokai':
                Maokai_button.place_forget()
                Maokai_label.place(x=1160,y=790)
            if champ_name == 'Nautilus':
                Nautilus_button.place_forget()
                Nautilus_label.place(x=1160,y=790)
            if champ_name == 'Yuumi':
                Yuumi_button.place_forget()
                Yuumi_label.place(x=1160,y=790)
            t.cancel()
            timer.destroy()
            restart_button.place(x=800, y=830),
        champ_list.remove(champ_name)
        print(champ_name)
        print(champ_list)
        if champ_count > 20:
            return
        play()
        #champ_name = 'None'







    # Timer

    global seconds
    seconds = 30

    def stop():
        global timer
        timer.place_forget()
        global t
        t.cancel()

    def reset():
        global champ_name
        global t
        global seconds
        global timer

        if champ_name == 'None':
            return
        timer.place_forget()
        t.cancel()
        seconds = 30
        mytime()


    def timeout():
        global champ_list
        global timer
        global seconds
        t.cancel
        timer.place_forget()
        seconds = seconds - 1
        if seconds == 5:
            tick()
        if seconds == 0:   
            choice = random.choice(champ_list)
            if choice == 'Aatrox':
                setname1()
                replace_champs()
            if choice == 'Alistar':
                setname2()
                replace_champs()
            if choice == 'Anivia':
                setname3()
                replace_champs()
            if choice == 'Azir':
                setname4()
                replace_champs()
            if choice == 'Caitlyn':
                setname5()
                replace_champs()
            if choice == 'Cassiopeia':
                setname6()
                replace_champs()
            if choice == 'Darius':
                setname7()
                replace_champs()
            if choice == 'Ekko':
                setname8()
                replace_champs()
            if choice == 'Graves':
                setname9()
                replace_champs()
            if choice == 'Gwen':
                setname10()
                replace_champs()
            if choice == 'Irelia':
                setname11()
                replace_champs()
            if choice == 'Ivern':
                setname12()
                replace_champs()
            if choice == 'Jayce':
                setname13()
                replace_champs()
            if choice == 'Jinx':
                setname14()
                replace_champs()
            if choice == 'Kalista':
                setname15()
                replace_champs()
            if choice == 'Katarina':
                setname16()
                replace_champs()
            if choice == 'Malphite':
                setname17()
                replace_champs()
            if choice == 'Maokai':
                setname18()
                replace_champs()
            if choice == 'Nautilus':
                setname19()
                replace_champs()
            if choice == 'Yuumi':
                setname20()
                replace_champs()
            seconds = 30
        mytime()


    my_font=('times',32,'bold')
    global timer
    timer = Label(root,font=my_font,bg='yellow',width=5)
    def mytime():
        global champ_count
        global t
        global timer
        global seconds
        timer.destroy()
        timer = Label(root,font=my_font,bg='yellow',width=5)
        timer.config(text=str(seconds))
        timer.place(x=575,y=35)
        t = Timer(1.0, timeout)
        t.start()



    # Sound

    def play():
        global champ_name
        if champ_name == 'None':
            return
        audio_file = os.path.dirname(__file__) + '\\lock.mp3'
        playsound(audio_file)

    def tick():
        audio = os.path.dirname(__file__) + '\\tick.mp3'
        playsound(audio)







    root.mainloop()

main()