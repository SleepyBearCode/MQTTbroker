# Analyseverslag - Proof of concept 
Naam: Wurud Salih

Klas: 3ITIOT1

## Inleiding:

Dit analyseverslag belicht de essentiële aspecten van de beveiliging van een innovatief energiesysteem, waarbij windmolens en zonnepanelen zijn gekoppeld aan een Mosquitto MQTT-broker. De architectuur, communicatiebeveiliging en afhankelijkheden van het systeem worden grondig besproken. Daarnaast biedt het verslag inzicht in de uitgevoerde tests en de resultaten daarvan, inclusief de ontdekkingen en uitdagingen op het gebied van netwerkbeveiliging.

## Architectuur van het Systeem:
![werking van systeem](Verslagen/systeem.png)

Het systeem is al opgebouwd volgens het volgende principe: de windmolens en zonnepanelen zijn verbonden met de Mosquitto broker via twee clients, één voor het publiceren en de andere voor het abonneren. Bijvoorbeeld, op het topic 'windmolen/data' wordt informatie elke 5 minuten verzonden vanuit één van de 4 windmolens. Daarnaast kan via het topic 'windmolen/request' op elk moment specifieke informatie worden opgevraagd over een van de windmolens, zonder te hoeven wachten op het periodieke verzenden van gegevens. Voor de zonnepanelen geldt hetzelfde principe.

De sensoren verschillen van elkaar; er is er één specifiek voor de zonnepanelen en een andere voor de windmolens. De ene sensor verstuurt elke 5 minuten gegevens, terwijl de andere dit om de 10 minuten doet.

De gebruikte libraries zijn:

- Paho MQTT client
- Time
- Schedule

Voor de windmolens draait het script als volgt:

Python script genaamd "Windmill\_send\_and\_receive"

JSON-formaat voor de data

Voor de zonnepanelen draait het script als volgt:

Python script genaamd "Zonnepaneel\_send\_and\_receive"

JSON-formaat voor de data

Communicatiebeveiliging:

De MQTT-broker wordt beveiligd door het gebruik van een gebruikersnaam en wachtwoord. De wachtwoorden worden versleuteld opgeslagen in het wachtwoordbestand. Om de integriteit van het systeem te waarborgen, hebben de clients beperkte toegang tot specifieke MQTT-topics via Access Control Lists (ACL). Zelfs als een client probeert gebruik te maken van een niet-toegewezen topic, wordt dit geblokkeerd door de ACL-configuratie.

Wanneer een client toch probeert toegang te krijgen tot een niet-toegewezen topic, genereert de broker een waarschuwing. Deze waarschuwing geeft aan dat de poging is geblokkeerd vanwege de strikte ACL-beperkingen. Het systeem is ontworpen om ongeoorloofde toegang tot specifieke MQTT-topics te voorkomen en de integriteit van de communicatie te handhaven.

Het gebruik van gebruikersnamen en wachtwoorden, hoewel versleuteld, introduceert een potentieel zwak punt. In theorie zou een aanvaller de versleutelingsmethode kunnen achterhalen. Het is van cruciaal belang om regelmatig de beveiligingsprotocollen te evalueren en, indien mogelijk, te upgraden om deze zwakheden te verminderen. Niettemin, zelfs als de versleutelingsmethode zou worden achterhaald, blijft de toegang beperkt door de ACL-configuratie. Het handhaven van de beveiligingsprotocollen en het regelmatig bijwerken ervan zijn essentiële aspecten om de integriteit van het systeem te waarborgen.
## Afhankelijkheden en Third-Party Libraries:
**Paho MQTT Client:**

Deze library is veelgebruikt en goed onderhouden. Het is echter belangrijk om altijd de laatste versie te gebruiken; momenteel is dat versie 1.6.1 uitgebracht op 21 oktober 2021.

**Time:**

Dit is een kernbibliotheek die geen specifieke beveiligingskwesties heeft. Het wordt vaak gebruikt voor het manipuleren van tijd in Python-scripts.

**Schedule:**

De 'schedule' library is een externe library die wordt gebruikt voor het plannen van taken in Python. Het is belangrijk om te controleren of er recente beveiligingsupdates zijn voor deze bibliotheek.

Cryptografie:

Na het zoeken naar encryptie-methodes en het gebruik van Fernet-encryptie, bleek het opslaan van de sleutel in een bestand voor mijn systeem een uitdaging. Om het bericht te laten versleutelen, heb ik ook gekeken naar TLS-beveiliging. Hiervoor zijn er twee opties: 

- Zelf een certificaat genereren en dit gebruiken voor de versleuteling.
- Een certificaat aanschaffen bij een provider. Houd er rekening mee dat de kosten hiervoor niet specifiek vermeld worden.

Hoewel de eerste optie niet erg handig lijkt voor mijn systeem, is het ook belangrijk op te merken dat het aanschaffen van een certificaat prijzig kan zijn, vooral als de kosten niet specifiek worden vermeld.
## Netwerkbeveiliging:
Zelf heeft mijn computer, waarop de MQTT-broker draait, een firewall en een antivirus scanner. Momenteel staat de MQTT-broker niet altijd aan. Mijn wifi-router draait zelf op WPA2, maar ik heb geprobeerd dit te wijzigen naar de nieuwere versie. Helaas ondersteunt mijn wifi-provider geen WPA op de modems die zij maken.
## Testjes op systeem 
Bij het uitvoeren van een analyse op het testen van de beveiliging van het systeem, zullen we dit benaderen vanuit het perspectief van een hacker. Het eerste wat ze zullen proberen, is het onderzoeken van open poorten op verschillende apparaten. Hieruit kunnen we concluderen welke apparaten interessant zijn. Eenmaal interessante apparaten zijn gevonden, zal er packet sniffing worden uitgevoerd. Door een script te draaien met Scapy, kunnen de pakketten worden opgenomen in een bestand en geanalyseerd worden met Wireshark. Hiermee wordt ervoor gezorgd dat je als het ware een soort tussenpersoon wordt met de verkregen pakketten
### Resultaat van het testen:
#### *Resultaat van network mapping*
![](result.png)

Bij het uitvoeren van het script kon het niets vinden, wat naar mijn mening positief is. Packet sniffing was de tweede optie, maar helaas werkt dit niet met mijn script omdat mijn netwerkbeveiliging goed is ingesteld om dit te voorkomen

Conclusie:

Als conclusie op mijn analyse lijkt het systeem een robuuste beveiligingsaanpak te hebben, met specifieke aandacht voor zowel communicatie- als netwerkbeveiliging. Het is echter teleurstellend dat de beveiliging op het netwerk beperkt was door de wifi-provider. Desondanks bleek uit de uitgevoerde tests dat het systematisch scannen geen interessante apparaten opleverde, wat positief is. Helaas bleek packet sniffing geen haalbare optie door de strakke netwerkbeveiligingsinstellingen.

Daarnaast viel op dat het systeem slechts beperkt gebruikmaakt van third-party libraries, maar de gebruikte libraries worden wel goed onderhouden. Met betrekking tot de communicatiebeveiliging hebben we vastgesteld dat, hoewel de versleutelingsmethode theoretisch kwetsbaar zou kunnen zijn, de toegang strikt beperkt blijft door de ACL-configuratie. Het wordt aanbevolen om de beveiligingsprotocollen regelmatig te evalueren en indien nodig te upgraden.

**Bronnen**:

<https://www.emqx.com/en/blog/how-to-use-mqtt-in-django>

<http://www.steves-internet-guide.com/>


