radio.setGroup(1)
let megjelenitett_kep = 0
let kitalalando2 = 0
let darab2 = 0
let ido = 0
let jatek_megy = false
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    if (megjelenitett_kep == kitalalando2) {
        basic.clearScreen()
        basic.showIcon(IconNames.Yes)
        darab2 += 1
        radio.sendValue("darab2", darab2)
    } else if (megjelenitett_kep != kitalalando2) {
        basic.clearScreen()
        basic.showIcon(IconNames.No)
        darab2 += 0
        radio.sendValue("darab2", darab2)
    }
    
})
function visszaszamlalas() {
    
    ido = 3
    for (let index = 0; index < 3; index++) {
        basic.showNumber(ido)
        basic.pause(1000)
        ido += -1
    }
}

radio.onReceivedString(function on_received_string(receivedString: string) {
    
    if (receivedString == "db2") {
        jatek_megy = false
        images.iconImage(IconNames.Happy).showImage(0, 5000)
        basic.clearScreen()
    } else if (receivedString == "db1") {
        jatek_megy = false
        images.iconImage(IconNames.Sad).showImage(0, 5000)
        basic.clearScreen()
    }
    
})
radio.onReceivedValue(function on_received_value(name: string, value: number) {
    
    if (name == "kitalalando2") {
        kitalalando2 = value
        darab2 = 0
        if (kitalalando2 == 1) {
            images.iconImage(IconNames.Heart).showImage(0, 3000)
        } else if (kitalalando2 == 2) {
            images.iconImage(IconNames.Square).showImage(0, 3000)
        }
        
        visszaszamlalas()
        jatek_megy = true
    }
    
})
basic.forever(function on_forever() {
    
    if (jatek_megy) {
        megjelenitett_kep = 1
        images.iconImage(IconNames.Heart).showImage(0, 3000)
        basic.pause(1000)
        if (!jatek_megy) {
            return
        }
        
        megjelenitett_kep = 2
        images.iconImage(IconNames.Square).showImage(0, 3000)
        basic.pause(1000)
        if (!jatek_megy) {
            return
        }
        
        megjelenitett_kep = 3
        images.iconImage(IconNames.EighthNote).showImage(0, 3000)
    }
    
})
