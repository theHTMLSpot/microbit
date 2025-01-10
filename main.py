amount = 0

def on_button_pressed_a():
    global amount
    amount = amount + 1
    basic.show_leds("""
    . . # . .
    . . # . .
    # # # # #
    . . # . .
    . . # . .
    """)
    pause(100)
    basic.clear_screen()

def on_button_pressed_b():
    basic.show_number(amount)
    pause(100)
    basic.clear_screen()

input.on_button_pressed(Button.A, on_button_pressed_a)
input.on_button_pressed(Button.B, on_button_pressed_b)
