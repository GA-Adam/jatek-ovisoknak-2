darab1 = 0
kitalalando = 0
jatek_megy = False
megjelenitett_kep = 0
darab2 = 0
ido = 0

def on_received_number(receivedNumber):
    global darab1, kitalalando, jatek_megy
    darab1 = 0
    kitalalando = receivedNumber
    if kitalalando == 1:
        images.icon_image(IconNames.HEART).show_image(0, 3000)
    elif kitalalando == 2:
        images.icon_image(IconNames.SQUARE).show_image(0, 3000)
    visszaszamlalas()
    jatek_megy = True
radio.on_received_number(on_received_number)

def on_button_pressed_a():
    global darab1
    if megjelenitett_kep == kitalalando:
        basic.clear_screen()
        basic.show_icon(IconNames.YES)
        darab1 += 1
        radio.send_value("darab2", darab2)
    elif megjelenitett_kep != kitalalando:
        basic.clear_screen()
        basic.show_icon(IconNames.NO)
        radio.send_string("hamis2")
input.on_button_pressed(Button.A, on_button_pressed_a)

def visszaszamlalas():
    global ido
    ido = 3
    for index in range(3):
        basic.show_number(ido)
        basic.pause(1000)
        ido += -1

def on_received_string(receivedString):
    global jatek_megy, darab2
    if receivedString == "db2":
        jatek_megy = False
        images.icon_image(IconNames.HAPPY).show_image(0, 5000)
        basic.clear_screen()
    elif receivedString == "db1":
        jatek_megy = False
        images.icon_image(IconNames.SAD).show_image(0, 5000)
        basic.clear_screen()
    if receivedString == "2esnek pont":
        darab2 += 1
        radio.send_value("darab2", darab2)
    elif receivedString == "1esnek pont":
        darab2 += 0
        radio.send_value("darab2", darab2)
radio.on_received_string(on_received_string)

def on_forever():
    global megjelenitett_kep
    radio.set_group(1)
    if jatek_megy:
        megjelenitett_kep = 1
        images.icon_image(IconNames.HEART).show_image(0, 3000)
        basic.pause(1000)
        if not (jatek_megy):
            return
        megjelenitett_kep = 2
        images.icon_image(IconNames.SQUARE).show_image(0, 3000)
        basic.pause(1000)
        if not (jatek_megy):
            return
        megjelenitett_kep = 3
        images.icon_image(IconNames.EIGHTH_NOTE).show_image(0, 3000)
basic.forever(on_forever)
