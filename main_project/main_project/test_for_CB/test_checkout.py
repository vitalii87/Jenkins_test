def test_checkout(app):
    app.click_on_cookie()
    app.click_on_keuze()
    app.first_step(quan="10")
    app.choose_v_pm_w(message="message on CB___---000")
    app.fill_form(name="Test_first_name", surename="Test_surename", zip="1000AA", house="10", phone="04130",
                  email="vitalii+test@nxte.nl")
    app.choose_bank()
    app.last_step()
    app.select_bank(bank="ABNAMRO Bank")
    app.submit_status()
    # app.alert_accept()
#
# d = 'http://development.nxte.nl/Cadeau_Concepten/CACO1607-Cadeaubonnen/',
# s = 'https://cadeaubon.testconcepten.nl/',
# l = 'https://www.cadeaubon.nl/'

