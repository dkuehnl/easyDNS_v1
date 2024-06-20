#easyDNS Error-Handling-Modul 

error_dict = {
            "Err01": "Fehler in NAPTR-Antwort (Code 121)",
            "Err02": "Fehler in NAPTR-Antwort (Code 122)",
            "Err03": "Eingabefehler - Resolver enthält einen ungültigen Wert (Code 011)",
            "Err04": "Eingabefehler - Domäne enthält einen ungültigen Wert (Code 012)",
            "Err05": "Eingabefehler - Type wird nicht unterstützt (Code 013)",
            "Err06": "Fehler in der Verarbeitung - Type konnte nicht zugeordnet werden (Code 211)",
            "Err07": "Build-Fehler - es konnte kein Query gebaut werden (Code 221)",
            "Err08": "Fehler in der Verarbeitung - Type-Nummer konnte nicht zugeordnet werden (Code 212)",
            "Err10": "Anzeigefehler - Query kann nicht ausgewertet werden (Code 301)",
            "Err11": "Anzeigefehler - Fehler in Auswertung der NAPTR-Antwort (Code 311)",
            "Err12": "Anzeigefehler - Fehler in Auswertung der SRV-Antwort (Code 312)",
            "Err13": "Anzeigefehler - Fehler in Auswertung der A-Record-Antwort (Code 313)",
            "Err14": "Abfragefehler - DNS-Query wurde nicht beantwortet (Code 213)"
        }


def error(message): 
    for code in error_dict: 
        if code == message: 
            return error_dict[code]
    print(message)
    return "Error Unknown"

