def on_button_pressed_a():
    global speed
    if speed == "0"
        speed = 0
    else:
        speed += 1
        basic.show_number(speed)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global speed
    speed = 0
input.on_button_pressed(Button.B, on_button_pressed_b)

speed = 0
speed = 0

def on_forever():
    if speed == "0":
        basic.clear_screen()
    else:
        basic.show_leds("""
            . . # . .
            . . # . .
            # # # # #
            . . # . .
            . . # . .
            """)
        basic.show_leds("""
            # . . . #
            . # . # .
            . . # . .
            . # . # .
            # . . . #
            """)
basic.forever(on_forever)
