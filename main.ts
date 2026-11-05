input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    if (speed == "0") {
        speed = 0
    } else {
        speed += 1
        basic.showNumber(speed)
    }
    
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    speed = 0
})
let speed = 0
speed = 0
basic.forever(function on_forever() {
    if (speed == "0") {
        basic.clearScreen()
    } else {
        basic.showLeds(`
            . . # . .
            . . # . .
            # # # # #
            . . # . .
            . . # . .
            `)
        basic.showLeds(`
            # . . . #
            . # . # .
            . . # . .
            . # . # .
            # . . . #
            `)
    }
    
})
