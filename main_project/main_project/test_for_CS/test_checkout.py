
def test_checkout(app, init_login):
    # assert "Cadeau Concepten Giftbox" in app.driver.title  # check title
    app.click_on_order()
    app.first_card("3", '100')
    app.second_card("2", '50')
    app.next()
    app.choosing_to_first()
    app.pers_message("give_some_text_to_textfield")
    app.fake_next_step()
    app.to_one_adress()
    app.click_to_confirm()
    app.redirection_to_boockaroo()
    app.select_bank()
    app.submit_status()
    # app.alert_accept(message="The information you have entered on this page will be sent over an insecure connection and could be read by a third party.\n\nAre you sure you want to send this information?")
