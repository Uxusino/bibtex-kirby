"""
Tämä moduuli käynnistää Flask-sovelluksen.

Moduuli tuo sovelluksen app-muuttujan app-moduulista ja käynnistää sen, 
kun tiedosto suoritetaan pääohjelmana. Sovellus ajetaan portissa 5001 
ja se on saatavilla kaikista verkko-osoitteista (host="0.0.0.0"). 
Debug-tila on päällä, mikä mahdollistaa virheiden ja muutosten 
seurannan kehitysvaiheessa.
"""
# random comment to test commits

from app import app

if __name__ == "__main__":
    app.run(port=5001, host="0.0.0.0", debug=True)
