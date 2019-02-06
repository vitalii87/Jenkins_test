
def test_reorder(app, init_login):
    app.click_on_reorder()
    app.addition_cards()
    app.fake_next_step()
    app.addition_wrappers()
    app.fake_next_step()
    app.click_to_confirm()
    app.redirection_to_boockaroo()
    app.select_bank()
    app.submit_status()
    # app.alert_accept(message="The information you have entered on this page will be sent over an insecure connection and could be read by a third party.\n\nAre you sure you want to send this information?")