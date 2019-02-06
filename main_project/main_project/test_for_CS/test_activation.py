
def test_activation(app, init_login):
    app.click_on_activation()
    app.setup_cards()
    app.click_to_confirm()
    app.redirection_to_boockaroo()
    app.select_bank()
    app.submit_status()
    # app.alert_accept(message="The information you have entered on this page will be sent over an insecure connection and could be read by a third party.\n\nAre you sure you want to send this information?")
