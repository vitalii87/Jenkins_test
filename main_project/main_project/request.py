#!/usr/bin/env python3
import requests

l = (
        "https://www.databoost.nl",
        "http://koffie-cadeau.nl",
        "https://www.nationaledinercadeaukaart.nl",
        "https://saldocheck.cadeauconcepten.nl",
        "https://cdb.cadeauconcepten.nl/",
        "https://www.kunstcultuurcadeaukaart.nl",
        "https://www.horecacadeaukaart.nl",
        "https://www.kunstcultuurbeleving.nl",
        "https://giftbox.cadeauconcepten.nl/",
        "https://www.nationaledinerbon.nl",
        "https://www.cadeaubon.nl",
        "https://www.dagjeuitjaarkaart.nl",
        "https://www.parfumcadeaukaart.nl/",
        "https://www.wijn-cadeaukaart.nl",
        "https://www.kerstkeuzecadeau.nl",
        "https://www.cadeaubonnen.nl/",
        "https://www.dinnercheque.nl",
        "https://www.dinerbon.com/",
        "https://www.jewelcard.nl/",
        "https://www.golfbon.nl/",
        "https://www.diner-cadeau.be",
        "https://www.kook-cadeau.nl",
        "http://www.juwelierscadeaukaart.nl/",
        "https://www.oudgoud.nl",
        "https://www.cadeaukaartbestellen.nl",
        "https://www.weekendontspannen.nl/",
        "https://www.bloemengiftcard.nl",
        "https://www.cadeauservice.nl",
        "https://www.boeken.nl",
        "https://www.dagjeuit-cadeaukaart.nl",
        "https://www.nr1cadeau.nl",
        "https://cigo.diner-cadeau.nl",
        "https://keuze.cadeauservice.nl",
        "https://zakelijk.kerstkeuzecadeau.nl",
        "https://ikea.kerstkeuzecadeau.nl",
        "http://www.dinerkortingskaart.nl",
        "http://www.vipster.nl/",
        "https://www.fashion-giftcard.nl",
        "https://www.diner-cadeau.nl",
        "https://www.goededoelen-cadeaukaart.nl/",
        "https://www.lunchendinerkaart.nl/"
)


def check_all():
        for i in l:
            if requests.get(i).status_code == 500:
                print(i + " ! site is down !")
            elif requests.get(i).status_code == 403:
                print('log-in')
            elif requests.get(i).status_code == 200:
                print('ok')
            else:
                print(i + " check_this_one")
check_all()
