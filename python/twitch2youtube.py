import json
import os
from os import path
import subprocess

PATH='downloaded_vids'
    
class TwitchStream:
    """Twitch steam attribute"""
    # ça c'est le constructeur de ta classe (Objet en gros) ça permet de créer une instance de classe (version de ton objet en gros) comme ça :
    # a = TwitchStream(URL, nom, yt_channel,... )
    # donc si a=  TwitchStream( ('https://twitch.tv/videos/558751806', ...)
    # print(a.url) donne:
    # https://twitch.tv/videos/558751806
    def __init__(self, url, name, yt_channel, splits) :
        self.url = url
        self.name = name
        self.yt_channel = yt_channel
        self.splits = splits
    # La c'est le fonction de ta classe, c'est à dire que tu peut appeler cette fonction sur une instance de ta classe
    # exemple:
    # stream=TwitchStream('https://twitch.tv/videos/558751806', '0303', 'L', ['0-30.30', '30-1.10.30', '1.10.00-1.15.10'])
    # stream.showInfo()
    # Nom : 0303
    # URL : https://twitch.tv/videos/558751806
    # Youtube Channel : L
    # Splits: ['0-30.30', '30-1.10.30', '1.10.00-1.15.10']
    def showInfo(self):
        """Prompt Twitch strem infos"""
        print(f"Nom : {self.name}")
        print(f"URL : {self.url}")
        print(f"Youtube Channel : {self.yt_channel}")
        print(f"Splits: {self.splits}")
    def getInfo(self):
        return dict(name=self.name,url=self.url, yt_channel=self.yt_channel, splits=self.splits)
    def download(self, PATH):
        vid_path=f"{PATH}/{self.name}"
        if path.exists(vid_path):
            print(f"{vid_path} already exists !\nEXITING")
            exit()
        os.mkdir(vid_path)
        subprocess.call(["youtube-dl", "-o", f"{vid_path}/{self.name}.mp4", self.url])

# J'aurai pu mettre ça dans la classe mais bon c'est juste pour le dev donc osef
def test_TwitchStream(stream):
    stream.showInfo() # J'appel la fonction de classe qui print joliement les infos de ma classe
    print("Raw Print: ")
    print(stream.getInfo()) # je Print le resultat de la fonction de classe qui retourne toute les infos dans un dico 

def check_path(PATH):
    if path.exists(PATH):
        pass
    else:
        try :
            os.mkdir(PATH)
        except (Exception) as e:
            print(f"Error creating {PATH} directory",e.args)



if __name__ == '__main__':
    check_path(PATH)
    with open('inputs.json') as f: # On ouvre le JSON dans un with pour bien gerer les erreur
        i=1
        streams_data= json.load(f) # on charge tout le json dans streams_data donc on se retrouve avec une liste de dictionaire (dans ce cas là)
        for stream_raw in streams_data: # pour chanque entré dans la liste qu'on vient de creer
            print(f"\n===================\n Stream n° {i} \n===================") # ça c'est pour faire joli
            stream=TwitchStream(stream_raw['url'], stream_raw['name'], stream_raw['yt_channel'], stream_raw['splits']) # Je creer mon instance de classe
            test_TwitchStream(stream) # J'appel ma fonction de "test"
            stream.download(PATH) 
            i+=1