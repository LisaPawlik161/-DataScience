Data Science Programmierung mit Python- WiSe 2025/26
Prof. Dr. Selcan Ipek-Ugay/Amy Siu












Die Social-Media-Sucht der Studenten
Dokumentation






	




Lisa-Marie Pawlik	102358	lipa7219@bht-berlin.de
Inhaltsverzeichnis

Inhaltsverzeichnis	
1. Projektinformation	
2. Kernidee und Datenquelle	
3. Datenbereinigung	
4. Datenvisualisierung	
5. ML	
6. Streamlit-Anwendung	
7. Abbildungen	



























1. Projektinformation
Name: Pawlik, Lisa-Marie
Matrikelnummer: 102358
Projekttitel: Die Social-Media-Sucht der Studenten
Link: https://github.com/LisaPawlik161/-DataScience.git
Link zum Download Nextcloud:
https://cloud.bht-berlin.de/index.php/s/qgyoejDCSgqxmBQ

2. Kernidee und Datenquelle
Wir nutzen täglich mehrere Stunden Social-Media. Ob es nur eine Nachricht ist, die wir verschicken oder dem Feed auf Instagram, den wir folgen. Vielleicht nutzen wir auch ein bisschen zu viel Social-Media, vor allem in Situationen wo es nicht passt oder wo wir mehr acht auf andere Dinge geben sollten, wie zum Beispiel in der Universität. Deswegen habe ich mich gefragt: „Haben Studenten eine Social-Media-Sucht?” Dieses Thema betrifft nicht nur mich, sondern auch Millionen Studenten auf dieser Welt, die täglich mehrere Stunden auf Social-Media verbringen. Meine Datenquelle habe ich auf einer Open Data Source Quelle namens Kaggle gefunden.
Dort habe ich nicht nach einer bestimmten Quelle gesucht, sondern erst durchstöbert und bin dann auf diese Datenquelle gestoßen. 
Nach erster Analyse der Datenquelle und Beratung mit der Dozentin stellte sich heraus, dass diese Quelle eine synthetische Quelle ist.
Das hat mich nicht davon abgehalten, diese zu nutzen, sondern hat es für mich noch interessanter gemacht, da ich sehen wollte, ob synthetische Daten wirklich so perfekt sind, wie es vermutet wurde von mir.

3. Datenbereinigung
Der erste Schritt meiner Analyse bestand in der Bereinigung der Datenquelle. Dieser Prozess umfasste die Identifizierung und Behandlung von fehlenden Werten, Duplikaten sowie potenziellen Ausreißern. Da es sich um einen synthetisch generierten Datensatz handelt, fielen diese Probleme erwartungsgemäß geringer aus als bei realen Datensätzen. Als erstes verschaffte ich mir einen Überblick über den Datensatz, der aus 705 Zeilen und 13 Spalten besteht. Die Überprüfung ergab, dass weder Duplikate noch leere Zeilen vorhanden waren. Zudem entsprachen die Datentypen (int64, object und float64) bereits den jeweiligen Kategorien, sodass hier keine Anpassungen erforderlich waren.
Bei der Untersuchung der Spalten, vor allem aber der Spalte Avg_Daily_Usage_Hours traten zwar vereinzelt sehr hohe oder niedrige Werte auf, diese stufe ich aber als plausibel ein und entferne sie nicht als Ausreißer, da sie innerhalb eines realistischen Nutzungsspektrums liegen. Im Kontext der „Generation Z” und der fortschreitenden Digitalisierung im Alltag bei Studenten (Lernen mit YouTube, Kommunikation über WhatsApp/Discord, Entspannung via TikTok) sind solch hohe Werte zwar extrem, aber für mich plausibel. Zum Schluss habe ich die Richtigkeit der Textspalten geprüft (z. B. zur Vermeidung von Duplikaten durch unterschiedliche Groß- und Kleinschreibung oder Tippfehler). Da keine Fehler festgestellt wurden, blieb der Datensatz in seinem ursprünglichen Umfang von 705 Zeilen und 13 Spalten für die weitere Analyse erhalten.

4. Datenvisualisierung 
Bei der Auswahl der Visualisierungen lag mein Fokus darauf, die zentrale Fragestellung, ob Studierende Social-Media-Süchtig sind, zu untersuchen. 
Ich habe mich primär für Scatterplots mit Farb- oder Größencodierung entschieden, da diese für mich am aussagekräftigsten erscheinen.
Mit diesen habe ich versucht zu visualisieren, welches Geschlecht welche Plattform am meisten nutzt und wie sich dies auf den Schlaf auswirkt.
Besonders auffällig war, dass Nutzer der Plattform Tiktok und Instagram im Durchschnitt die geringste Schlafdauer aufwiesen. 
Ebenso habe ich durch einen anderen Scatterplot herausgefunden, dass je weniger die Menschen schlafen, desto abhängiger diese sind. 
Welches für mich logisch erscheint nicht nur aus dem Aspekt, dass viele Social Media zu späterer Stunde nutzen, sondern auch dadurch, dass der Datensatz synthetisch ist.
Ich glaube, dass die Spalte der Abhängigkeit auf Grundlage der Schlafstunden erstellt wurde.
In meiner App habe ich ein Tool zur Verteilungsanalyse eingebaut. Nutzer können über ein Dropdown-Menü verschiedene Werte auswählen und sich diese als Histogramm anzeigen lassen. Besonders hilfreich ist die Funktion, die Daten per Checkbox nach Geschlecht aufzuteilen.
Durch transparente Balken sieht man sofort, ob es Unterschiede zwischen Studenten und Studentinnen gibt. Ich habe aber auch nicht-relevante Daten wie die Student_ID automatisch aus der Auswahl entfernt, da diese für mich nicht relevant erscheinen.



5. ML
In diesem Teil des Projekts wollte ich herausfinden, ob man die Social-Media-Sucht (den Addicted_Score) mathematisch vorhersagen kann. Ich habe also eine Regressionsanalyse durchgeführt. Dafür habe ich ein Modell gebaut, das aus verschiedenen Daten lernt. Als „Lehrer“ dienten Informationen wie das Alter, die täglichen Handy-Stunden, die Schlafdauer und die psychische Gesundheit. Damit die Analyse spannend bleibt, habe ich nicht nur ein Modell genutzt, sondern drei verschiedene eingebaut: die Lineare Regression, den Decision Tree und den Random Forest. Um zu testen, wie gut die ML wirklich ist, habe ich den Datensatz aufgeteilt: Ein Teil der Daten wurde zum Lernen genutzt, und mit dem anderen Teil musste die ML beweisen, ob ihre Vorhersagen stimmen. Dabei gab es eine interessante Erkenntnis: Besonders der Random Forest zeigt sehr genau, welche Faktoren am wichtigsten sind. Es stellte sich heraus, dass Schlafmangel und eine hohe tägliche Nutzungsdauer die sichersten Anzeichen für einen hohen Sucht-Score sind. Da mein Datensatz synthetisch ist, waren die Vorhersagen fast schon „zu perfekt“. Das zeigt deutlich, dass die Daten nach logischen Regeln erstellt wurden.

6. Streamlit-Anwendung
In meiner Anwendung gibt es vier Seiten namens app, Daten Exploration, Visualisierung und Machine Learning Prediction die über die Sidebar auszuwählen sind. Auf der app Seite gibt es einen kleinen Einblick in den Datensatz.
Auf der Daten Exploration Seite gibt es die Tabs Übersicht, Datenqualität und Variablenbeschreibung. Bei der Übersicht gibt es wieder einen kleinen Überblick über den Datensatz, wobei aber der Nutzer durch den integrierten Slider selber entscheiden kann, wie viele Zeilen angezeigt werden (zwischen 5 und 50). Auch die Anzahl und welche Datentypen vertreten sind, werden durch ein Drop-down-Menü abgedeckt. In dem Datenqualität Tab kann der Nutzer sehen, welche Werte fehlen. In dem letzten Tab der Seite werden manche Spalten nochmal tabellarisch erklärt und die Spalte Addicted Score wird nochmal in Gering, Moderat und Hoch kategorisiert.
Auf der Seite Visualisierungen gibt es wieder drei Tabs, welche für die drei Visualisierungen stehen, die ich oben im Part Datenvisualisierung beschrieben habe.
Dort habe ich dann die Filterauswahl implementiert für die Verteilungsanalyse nach Geschlecht. 
Auf der Seite der ML habe ich Tabs, Training und Vorhersage.
Bei dem Training habe ich ebenso einen Slider und ein Drop-down-Menü eingebaut und bei der Vorhersage ebenso Slider verwendet.


