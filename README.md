# B.U.M.S.


Client
- fragt alle 15 Sekunden ob Update verfügbar ist
	- wenn  Update verfügbar HASHVALUE in Variable speichern
	- wenn nicht nichts tun und alle 15 Sekunden weiter wiederholen

Server
- message publizieren auf Anfrage
- message kommt aus /server/message/message.json


Konstrukt einer Message

1. Titel
2. Inhalt
3. Author (IP Adresse)

Ablauf:

1. Client fragt Update an mit dem Hash der aus dem Inhalt der JSON datei generiert wird
2. Server vergleicht Hash der Anfrage mit Hash der aktuellen JSON datei (gespeichert in Variable)
	1. wenn Hashes sich unterscheiden wird JSON Datei übermittelt
	2. wenn Hashes übereinstimmen gibt er "No updates available" aus
3. Client gibt JSON via simplem GUI aus


Dateistruktur auf Server

/server/working/
 - beinhaltet Code zur Funktion des Servers
	 - networkHandler
		 - kommuniziert mit Client, gleicht angefragten hash mit hash aus hashcalc ab
	 - hashcalc
		 - md5 Hash generierung aus message.json
	 - fileHandler
		 - ==To be refined==

/server/message/
- beinhaltet message.json Datei
---
Dateistruktuf auf Client
/client/working/
- beinhaltet Code zur funktion des Clients
	- networkHandler
		- kommuniziert mit Server, updatet alle 15 Sekunden mit aus hashcalc generiertem Hash
	- hashcalc
		- md5 Hash generierung aus /client/message/message.json
	- fileHandler
		- schreibt von networkHandler erhaltene Datei in /client/message/message.json
	- guiHandler
		- PopUp message wenn networkHandler eine neue Nachricht erhält

- /client/message/
	- beinhaltet message.json
