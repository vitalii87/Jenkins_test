def test_checkout(app):
    app.click_on_cookie()
    app.click_on_card()
    app.first_step(quan="10")
    app.choose_v_pm_w(message="some_message Cigo")
    app.fill_form(name="Test_first_name", surename="Test_surename", zip="1000AA", house="10", phone="04130",
                  email="vitalii+test@nxte.nl")
    app.choose_bank()
    app.last_step()
    app.select_bank(bank="ABNAMRO Bank")
    app.submit_status()
