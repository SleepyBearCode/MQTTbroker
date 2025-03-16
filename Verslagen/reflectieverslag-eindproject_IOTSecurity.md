# Reflectieverslag - Proof of concept 
Naam: Wurud Salih

Klas: 3ITIOT1

## Doel van het POC:
Het hoofddoel van de POC was om te demonstreren hoe cruciaal het is om de communicatie tussen de sensor en de windmolen/zonnepaneel te beveiligen. Dit is met name van belang om mogelijke aanvallen door een middle-man attack te voorkomen. Dit is belangrijk, vooral wanneer deze systemen de basis energie leveren aan woningen, bedrijven op locaties in het land of ergens anders in de wereld.
## Duurzame Energieconcept:
Het concept maakt gebruik van duurzame energie, waarbij een mix van windmolens en zonnepanelen wordt ingezet voor de productie. Op dit moment worden er 4 getoond in de applicatie, bestaande uit windmolens , zonnepanelen en twee sensors,
## Verloop van de Communicatie met Windmolen:
De windmolens hebben verbinding met een MQTT-server. Deze server stuurt gegevens naar het topic 'Windmolen/data'. De windmolens luisteren ook naar het topic 'windmolen/request'. Op dit onderwerp kan bijvoorbeeld data binnenkomen over de windkracht of het ophalen van de gebruikte capaciteit van een bedrijf, afkomstig van een sensor. Hierdoor kan de windmolen worden in- of uitgeschakeld op basis van de ontvangen gegevens. In het geval van een ramp, waarbij geen informatie kan worden verzonden over windkracht of capaciteit, kan via het op Django gebaseerde dashboard een besturing worden verzonden om handmatig de windmolen in of uit te schakelen.
## Verloop van de Communicatie met Zonnepanelen:
Zoals bij de winmolens geldt hetzelfde ook voor de zonnepanelen; deze luisteren naar het MQTT-onderwerp 'zonnepaneel/request'. De zonnepanelen worden aangestuurd door een powermanager sensor. Ze worden ingeschakeld afhankelijk van de zonnestraling en of de capaciteit niet te laag of te hoog is om de zonnepanelen in of uit te schakelen. De powermanager sensor neemt beslissingen op basis van deze factoren, wat bijdraagt aan een efficiënte werking van de zonnepanelen.
## Keuze voor MQTT:
Mijn keuze voor het MQTT-protocol in dit duurzame energieproject is gebaseerd op de eenvoudige implementatie met IoT-data, de gemakkelijke apparaatkoppeling via publish-subscribe, de efficiënte verspreiding van gegevens tussen windmolens, zonnepanelen en het dashboard, en de integratie in de TCP/IP-applicatielaag.
## Dashboard Functionaliteiten:
![dashboard](dashboard.png)

Het dashboard is eenvoudig omgebouwd. Bij Windmill komen alle gegevens binnen van de windmolens, inclusief bijbehorende data. De sensorinformatie is afkomstig van twee gekoppelde sensoren. Bovenaan het tabblad kun je schakelen tussen de windmolens en zonnepanelen. Het wijzigen van de status is alleen mogelijk voor windmolens, waarbij je per windmolen de status en de richting kunt aanpassen.
**Let wel op**: bij het opstarten van de Django-webserver zullen er automatisch terminals worden gestart voor de zonnepanelen, windmolens en sensoren voor de MQTT-communicatie.

## Beveiligingsaspecten:
In mijn systeem zijn diverse beveiligingsmaatregelen genomen voor de MQTT-communicatie en de algehele beveiliging. Gebruikersnamen en wachtwoorden zijn ingesteld in de Mosquitto-configuratie om alleen geautoriseerde toegang toe te staan. Access Control Lists (ACL) bieden gedetailleerde controle over de toegang tot MQTT-topics. Voor extra privacy en integriteit is TLS/SSL-encryptie geïmplementeerd om de communicatie tussen de MQTT-broker en clients te versleutelen. Deze gelaagde beveiligingsaanpak minimaliseert risico's op ongeautoriseerde toegang en waarborgt de beveiliging van het systeem.
## Impact van Beveiligingsmaatregelen:
Door de implementatie van gebruikersnamen en wachtwoorden is ongeautoriseerde toegang tot de broker voorkomen. Daarnaast zorgt het gebruik van Access Control Lists ervoor dat gebruikers alleen toegang hebben tot specifieke MQTT-topics volgens de gedefinieerde regels. Hierdoor kan bijvoorbeeld de gebruiker 'solar' alleen publiceren op het 'zonnepaneel/data'-topic en niet op het 'windmolen/data'-topic, dat voorbehouden is aan de gebruiker 'wind'. Dit biedt een gerichte en doeltreffende beveiliging van de MQTT-communicatie binnen het systeem.
## Toekomstige Ontwikkelingen:
Er zijn nog vele opties toe te voegen aan de Mosquitto broker. In toekomstige aanpassingen zou ook het IP-adresbereik een mogelijkheid moeten zijn. Zelf zouden de gebruikersnaam en het wachtwoord per maand moeten worden aangepast om de veiligheid te waarborgen. Ook het controleren van de logs op verdacht gedrag is een optie, om direct actie te ondernemen bij het identificeren van verdachte activiteiten.
## Reflectie op POC: 
De uitdagingen waar ik tegenaan ben gelopen en van heb geleerd, was het maken van verbinding met één hoofdonderwerp en één abonnement ('subscribe') in 'zonnenpaneel'. Hierbij heb ik ontdekt dat er twee clients gecreëerd moeten worden om deze functionaliteit te laten werken. Ook was het lastig om het dashboard te actualiseren en real-time gegevens toe te voegen. Uiteindelijk heb ik een knop toegevoegd die ervoor zorgt dat de pagina wordt vernieuwd.

Het instellen van de Mosquitto-configuratie om te werken met gebruikersnaam en wachtwoord bleek ook een uitdaging te zijn. Ondanks dat ik wijzigingen had aangebracht in het configuratiebestand, werden deze niet toegepast bij de verbinding met een client. Hier kwam ik achter dat je bij het opstarten van de MQTT-broker het configuratiebestand moet meenemen in de command line om het te laten werken.

**Bronnen**: 

<http://www.steves-internet-guide.com/mosquitto-broker/>

<https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7561515/#:~:text=MQTT%20protocol%20is%20used%20in,is%20mainly%20commands%20or%20data>.

