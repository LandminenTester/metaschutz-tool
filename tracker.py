# import urllib library
from urllib.request import urlopen
from datetime import datetime
from multiprocessing import Process
import time
import json
import keyboard
import sys
import os

  #config.json laden lassen
c = open('config.json')
config = json.load(c)


#Variablen aus Config laden
streamer = str(config['streamer'])
sleepdur = config['seconds']

#Keybinds aus Config laden
endProg = str(config['keybind_endProg'])
startRec = str(config['keybind_startRec'])
endRec = str(config['keybind_stopRec'])
endFile = str(config['keybind_endFile'])
startFile = str(config['keybind_startFile'])

#Andere Variablen setzen
isBlacklist = False
isStarted = True
isBreak = False
statusAufnahme = 1
timeCounter = 0

clear = lambda: os.system('cls')

#Abrufen der Viewerliste des Streamers in der Config
url = "https://tmi.twitch.tv/group/user/"+ str(streamer) +"/chatters"

#Abfrage, ob der Name der Ausgabedatei anhand des Datums und dem Config Prefix erstellt werden soll oder ein eigener Eingegeben werden kann
print("Drücke '"+startFile+"' um eine neue Datei anzufagen oder drücke '"+endProg+"' um das Tool zu beenden ")
while True:



  if keyboard.is_pressed(endProg):
    sys.exit()

  if keyboard.is_pressed(startFile):
    if (config['customFilename'] == False): 
      #Automatisch generieren
      filename = str(config['filename'])
      pathFile = str(filename+str(datetime.now())[:-7]).replace(':','-') + "Uhr.txt"
    else: 
      #Selbsteingeben
      print("Bitte gebe einen Namen ein den die Ausgabedatei haben soll:")
      filename = input()
      pathFile = str(filename) + ".txt"

    #Ausgabedatei erstellen mit dem Namen der zuvor generiert wurde
    f = open(pathFile, "w")

    #Header der Ausgabedatei schreiben mit dem Streamernamen
    f.write("Streamer: " + streamer)
    f.write('\n\n')

    print("Drücke '"+startRec+"' um die Aufnahme zu starten - Drücke '"+ endFile+"' um die Datei abzuschließen")
    while True:
      isBreak = False

      if keyboard.is_pressed(endFile):
        f.close()
        clear()
        print("Drücke '"+startFile+"' um eine neue Datei anzufagen oder drücke '"+endProg+"' um das Tool zu beenden ")
        statusAufnahme = 1
        break

      if keyboard.is_pressed(startFile):
        print("Aufnahme gestartet")
        f.write('\n')
        f.write("Aufnahme " + str(statusAufnahme))
        f.write('\n')
        f.write('\n')
        statusAufnahme = statusAufnahme + 1
        while isStarted:
          if (isBreak == True):
            break
          i = 0
          
          currentDateAndTime = datetime.now()
          response = urlopen(url)
          data_json = json.loads(response.read())
          viewerAmount = len(data_json['chatters']['viewers'])
          f.write(str(currentDateAndTime))
          f.write(" : ")
          sizeBlacklist = len(config['names'])

          while i < viewerAmount:
            j = 0
            while j < sizeBlacklist:
              if (config['names'][j] ==  data_json['chatters']['viewers'][i]):
                isBlacklist = True
              j = j + 1
            if (isBlacklist == False):
              f.write(data_json['chatters']['viewers'][i])
              f.write(", ")
            i=i+1
            isBlacklist = False
          f.write('\n')
          clear()
          print("Daten abgerufen und in Datei geschrieben - Um die Aufnahme zu stoppen Halte '"+endRec+"' bis 'Aufnahme gestoppt' erscheint") 
          while timeCounter < sleepdur:
            time.sleep(1)
            timeCounter += 1
            clear()
            print( str(sleepdur- timeCounter)+ " Sekunden bis neue Daten erfasst werden! - Um die Aufnahme zu stoppen Halte '"+endRec+"' bis 'Aufnahme gestoppt' erscheint")
            if keyboard.is_pressed(endRec):
              clear()
              print("Aufnahme gestoppt")
              print("Drücke '"+ startFile +"' um die Aufnahme wieder zu starten - Drücke '"+ endFile +"' um die Datei abzuschließen")
              isBreak=True
              break
          timeCounter = 0
          