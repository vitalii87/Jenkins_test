
def test_checkout(app):
    app.click_on_cookie()
    # app.check_existing_of_elements()
    app.check_lang()
    app.choose_card()
    app.click_on_order()
    app.choose_price_quan(quan=10)
    app.click_op()
    app.choose_wrapper()
    app.choose_wine(q=8)
    app.choose_message(message=" personal_message CB2 ")  # 😀
    app.step_after_po()
    app.asserts(message="personal_message CB2")
    app.checkout_first()
    app.fill_form_checkout(name="First_Name", prefix="Prefix", last_name="Last_Name", email="vitalii+test@nxte.nl", phone="063",
    sh_nme="ShippingName", sh_prefix="Prefix", sh_lname="LName", postcode="1000AA", housenum="11", suffix="Suffix")
    app.choose_deldate()
    app.choose_payment()
    app.submit()
    app.select()
    app.submit_status()

