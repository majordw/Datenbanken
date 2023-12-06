# übernommen und angepasst von https://www.sqlitetutorial.net/sqlite-python/
# Die Website enthält Fehler!
import sqlite3
from sqlite3 import Error


# Klasse für Tabellen erstellen
# Datenbankverbindung erstellen
# DB erstellen, wenn noch nicht erstellen
# Funktion für das Einfüllen der Daten
# Aktualisieren der Daten mit Funktionen
# Löschen von Daten
# Anzeigen der Daten


class Datenbank:
    def __init__(self, db_file):
        self.db_file = db_file

    # Erstellen einer Datenbankverbindung
    def createConnection(self, db_file):
        global connection
        connection = None
        try:
            connection = sqlite3.connect(db_file)  # hier wird der Filename festgelegt.
            return connection
        except Error as e:  # Fehlermeldung, damit man Fehlerhandling betreiben kann.
            print(e)

        return connection

    # Erstellen der Datenbank
    # zuerst wird die Verbindung erstellt, dann wird überprüft, ob eine Tabelle vorliegt. Sollte keine Tabelle
    # vorliegen, wird eine mit SQL-Befehlen erstellt.
    def createTable(self, connection, table):
        try:
            c = connection.cursor()
            c.execute(table)
        except Error as e:
            print(e)

    def ctMain(self):
        database = self.db_file

        table = """ CREATE TABLE IF NOT EXISTS datenbank (
                                            id integer PRIMARY KEY,
                                            aufgabe text NOT NULL,
                                            antwort1 text,
                                            antwort2 text,
                                            antwort3 text,
                                            antwort4 text
                                        ); """

        connection = self.createConnection(database)

        # Fehlerhandling
        if connection is not None:
            self.createTable(connection, table)
        else:
            print("Error! cannot create the database connection.")

    # Einfüllen der Daten
    # es wird in insert abstrakt der SQL-Befehl erstellt, und in inMain wird die Eingaben genommen, dann in den
    # SQL-Befehl eingetragen und übertragen.
    def insert(self, connection, eingabe):
        sql = """INSERT INTO datenbank(aufgabe, antwort1, antwort2,antwort3,antwort4)
                  VALUES(?,?,?,?,?)"""
        cursor = connection.cursor()
        cursor.execute(sql, eingabe)
        connection.commit()
        return cursor.lastrowid  # Letzte Reihennummer wird zurückgegeben.

    # Eingabe erfassen und Verbindung erstellen, Eingaben in den abstrakten SQL-Befehl einfügen
    def inMain(self, aufgabe, antwort1, antwort2, antwort3, antwort4):
        database = self.db_file

        connection = self.createConnection(database)
        with connection:
            insert = (aufgabe, antwort1, antwort2, antwort3, antwort4)
            self.insert(connection, insert)

    # Aktualisieren der Daten
    # abstrakter SQL-Befehl erstellen
    def update(self, connection, update_eingabe):

        sql = """ UPDATE datenbank
                   SET
                         aufgabe = ?,
                         antwort1 = ?,
                         antwort2 = ?,
                         antwort3 = ?,
                         antwort4 = ?
                   WHERE id = ?"""
        cur = connection.cursor()
        cur.execute(sql, update_eingabe)
        connection.commit()

    # Einfügen der Eingaben in den abstrakten SQL-Befehl und ausführen des Befehls
    def upMain(self, aufgabe, antwort1, antwort2, antwort3, antwort4, id_nummer):
        database = self.db_file
        connection = self.createConnection(database)
        with connection:
            up = (aufgabe, antwort1, antwort2, antwort3, antwort4, id_nummer)
            self.update(connection, up)

    # Löschen des Eintrages
    # abstrakter SQL-Befehl für die Löschung und Ausführen des Befehls und Verbindung mit der Datenbank erstellen, sowie
    # übertragen der Daten
    def delete(self, conncetion, nummer):
        sql = "DELETE FROM datenbank WHERE id=?"
        cursor = conncetion.cursor()
        cursor.execute(sql, (nummer,))
        conncetion.commit()

    # Einfügen der Daten in den SQL-Befehl und erstellen der Verbindung zur Datenbank.
    def delMain(self, nummer):
        database = self.db_file
        connection = self.createConnection(database)
        with connection:
            self.delete(connection, nummer)

    # Anzeigen der Daten
    # abstrakter SQL-Befehl und Ausführung des Befehls
    def showData(self, connection):
        cur = connection.cursor()
        cur.execute("SELECT * FROM datenbank")
        rows = cur.fetchall()  # Befehl alles Daten zu nehmen
        return rows

    # Aufrufen der Daten in der Datenbank und Verbindung erstellen zur Datenbank
    def showMain(self):
        database = self.db_file
        connection = self.createConnection(database)
        with connection:
            return self.showData(connection)


if __name__ == '__main__':
    # pass
    Chemie = Datenbank("Chemie.db")
    # Chemie.ctMain()
    # Chemie.in_main("aufgabe", "antwort1", "antwort2", "antwort3", "antwort4")
    # Chemie.up_main("aufgabe", "a", "b", "c", "d", 2)
    Chemie.delMain("11")
    # Chemie.show_main()
    # table = Chemie.showMain()
    # for row in table:
    # for data in row:
    # print(data)
