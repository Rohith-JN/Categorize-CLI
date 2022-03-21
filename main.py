import time
from creds import *
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
from difflib import SequenceMatcher

folder_to_track = paths.get('folder_to_track')

def moveImages(folder_destination, keyword):
    try:
        for filename in os.listdir(folder_to_track):
            i = 1
            x = [x for x in filename.split()]
            if filename != [folder_name for folder_name in folder_names] and keyword in filename.split():
                new_name = filename
                file_exits = os.path.isfile(folder_destination + '/' + new_name)
                while file_exits:
                    i += 1
                    new_name = os.path.splitext(folder_to_track + '/' + new_name)[0] + str(i) + os.path.splitext(folder_to_track + '/' + new_name)[1]   
                    new_name = new_name.split("/")[4]
                    file_exits = os.path.isfile(folder_destination + "/" + new_name)

                src = folder_to_track + "/" + filename
                new_name = folder_destination + "/" + new_name
                os.rename(src, new_name)
    except Exception as e:
        print(e)

def moveVideos(folder_destination):
    try:
        for filename in os.listdir(folder_to_track):
            i = 1
            if filename != [folder_name for folder_name in folder_names] and filename.endswith('.m4a') or filename.endswith('.mp4') or filename.endswith('.MOV') or filename.endswith('.mkv'):
                new_name = filename
                file_exits = os.path.isfile(folder_destination + '/' + new_name)
                while file_exits:
                    i += 1
                    new_name = os.path.splitext(folder_to_track + '/' + new_name)[0] + str(i) + os.path.splitext(folder_to_track + '/' + new_name)[1]   
                    new_name = new_name.split("/")[4]
                    file_exits = os.path.isfile(folder_destination + "/" + new_name)

                src = folder_to_track + "/" + filename
                new_name = folder_destination + "/" + new_name
                os.rename(src, new_name)
    except Exception as e:
        print(e)

Typeracer = paths.get('Typeracer')
Vscode = paths.get('Vscode')
Monkeytype = paths.get('Monkeytype')
games = paths.get('games')
Entrar = paths.get('Entrar')
Stackoverflow = paths.get('Stackoverflow')
Videos = paths.get('Videos')

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        #moveVideos(Videos)
        #moveImages(Typeracer, 'Typing')
        #moveImages(Vscode, 'Visual')
        #moveImages(Monkeytype, 'Monkeytype')
        #moveImages(games, 'Krunker')
        #moveImages(Entrar, 'EntrarLive')
        #moveImages(Stackoverflow, 'Stack')
        pass

event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()
