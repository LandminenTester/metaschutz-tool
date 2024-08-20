DAS METASCHUTZ TOOL IST NICHT MEHR NUTZBAR. TWITCH HAT DIE WEBSCHNITTSTELLE FÜR CHATTER ENTFERNT, DAS REPO BLEIBT FÜR LERN UND INTERESSENZWECKE ONLINE!

# Metaschutz Tool by LandminenTester

Hey! Du spielst auf einem Roleplay Server und bespielst eine Rolle die durch Meta von anderen Spielern beeinflusst werden kann? - Das Tool nimmt alles aktiven Teilnehmer mit einem Twitch Account in deinem Stream und schreibt Sie in eine Textdatei. Diese Namen können im Support genutzt werden, um gegebenenfalls eine Nachweis zu haben, dass eine Person während der aktiven Situation im Stream war.

# Inhaltsverzeichnis

1. F.A.Q.
2. Wie funktioniert das Tool
3. Die Config File

# 1. F.A.Q.
Hier findest du die wichtigsten Fragen die aufkommen können.

## 1.1 Warum ist die .exe in zwei .zip Dateien gelegt?
Dadurch das ein Zertifikat einiges kostet, kann ich meine .exe Datei nicht signieren, dass dazu führt das Chrome diese Datei beim Download sperrt. Dies kann umgangen werden, indem man die Datei in zwei .zip Dateien legt und dadurch wird Chrome dies nicht mehr als Problem erkennen. 

## 1.2 Windows sagt das die Anwendung nicht vertrauenswürdig ist
Wie bereits in Punkt 1. im FAQ geschrieben, ist die Anwendung nicht signiert, dadurch erkennt Windows diese Datei als nicht Vertrauenswürdig an. Drücke hierfür auf den Button "Trotzdem ausführen" nun sollte das Tool starten und beim nächsten mal wirst du nicht erneut aufgefordert.

# 2. Wie funktioniert das Tool?

Hier findest du wichtige Informationen, sodass du das Tool ohne Probleme nutzten kannst. 

# Metaschutz Tool by xBizzlike

Hey! Du spielst auf einem Roleplay Server und bespielst eine Rolle die durch Meta von anderen Spielern beeinflusst werden kann? - Das Tool nimmt alles aktiven Teilnehmer mit einem Twitch Account in deinem Stream und schreibt Sie in eine Textdatei. Diese Namen können im Support genutzt werden, um gegebenenfalls eine Nachweis zu haben, dass eine Person während der aktiven Situation im Stream war.

# Inhaltsverzeichnis

1. F.A.Q.
2. Wie funktioniert das Tool
3. Die Config File

# 1. F.A.Q.
Hier findest du die wichtigsten Fragen die aufkommen können.

## 1.1 Warum ist die .exe in zwei .zip Dateien gelegt?
Dadurch das ein Zertifikat einiges kostet, kann ich meine .exe Datei nicht signieren, dass dazu führt das Chrome diese Datei beim Download sperrt. Dies kann umgangen werden, indem man die Datei in zwei .zip Dateien legt und dadurch wird Chrome dies nicht mehr als Problem erkennen. 

## 1.2 Windows sagt das die Anwendung nicht vertrauenswürdig ist
Wie bereits in Punkt 1. im FAQ geschrieben, ist die Anwendung nicht signiert, dadurch erkennt Windows diese Datei als nicht Vertrauenswürdig an. Drücke hierfür auf den Button "Trotzdem ausführen" nun sollte das Tool starten und beim nächsten mal wirst du nicht erneut aufgefordert.

## 1.3 Die Ausgabedatei ist leer
Dies geschieht meistens wenn du nicht den richtigen Streamer Namen eingeben hast. Überprüfe in der "config.json", ob der Name stimmt, achte dabei vor Allem auf die Groß- und Kleinschreibung.

# 2. Wie funktioniert das Tool?


Das Tool wird über eine Kommandozeile ausgeführt. Sobald es gestartet ist zeigt das Programm dir immer an welche Möglichkeiten du aktuell hast. Dafür werden die verschiedene Short-Cuts angezeigt die du in der Config Datei separat angepasst werden können. Standardgemäß sind die Tastenkombinationen  STRG+F8 bis STRG+F12, um das Tool zu steuern. 

Sobald die Datei beendet wird durch ein Shortcut, wird im Verzeichnis in dem die Anwendung liegt eine Textdatei erstellt. Dort werden die Timestamps mit den Usern abgespeichert und nach den Aufnahmezyklen aufgezeichnet. Die Aufnahme kann gestartet und gestoppt werden, diese werden dann immer als einzelner Aufnahmezyklus in der Textdatei getrennt.

# 3. Die Config Datei
In der "config.json" kannst du verschiedene Einstellungen treffen. Hier findest du eine Erklärung zu der Config Datei. 

        {
    
    "names":  ["01ella","twiscordbot","0ax2","iisabei","notabotdef4","potatomalonettv","floboytwi","cyndyka","aten","larakraf","delotx","kattynah","roxesy","kittenrescue","peculiarasmr","victortomaili","notabotdef9","whypepe","lucentcrown12345678910","thisisunreallol","community_for_streamers","lonely_liza","gamers_and_streamers","notabotdef6","smallstreamers_discord","discordstreamercommunity","squu1zy","streamfahrer","01olivia","einfachuwe42","aliceydra","aliengathering","commanderroot","drapsnatt","kattah","larakraf","rogueg1rl","violets_tv","x_nsa_x","lurxx"],
    
    "streamer":  "ranzratte",
    
    "filename":  "Viewerliste-",
    
    "customFilename":  false,
    
    "seconds":  3,
    
    "keybind_endProg":  "STRG+F12",
    
    "keybind_endFile":  "STRG+F11",
    
    "keybind_startRec":  "STRG+F10",
    
    "keybind_stopRec":  "STRG+F9",
    
    "keybind_startFile":  "STRG+F8"
    
    }
## 3.1 "names"
Hier kannst du Twitchaccount Namen eintragen die bei einer Aufzeichnung nicht gespeichert werden. Dies dient dazu, um Bots auszuschließen und die Ausgabedatei etwas saubere zu halten.

## 3.2 "streamer"
Hier stellst du den Accountnamen von dir oder dem Streamer bei dem du die Zuschauernamen tracken möchtest ein. Bitte achte auf die Groß- und Kleinschreibung. 

 

