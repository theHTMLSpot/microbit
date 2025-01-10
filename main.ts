let amount = 0
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    amount = amount + 1
    basic.showLeds(`
    . . # . .
    . . # . .
    # # # # #
    . . # . .
    . . # . .
    `)
    pause(100)
    basic.clearScreen()
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    basic.showNumber(amount)
    pause(100)
    basic.clearScreen()
})
