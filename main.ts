input.onLogoEvent(TouchButtonEvent.Pressed, function on_logo_pressed() {
    basic.showLeds(`
        . # . # .
                . . . . .
                # # # # #
                # # # # #
                . # # # .
    `)
})
input.onGesture(Gesture.ScreenDown, function on_gesture_screen_down() {
    basic.showLeds(`
        . # # . .
                . . # # .
                . . # # .
                . . # # .
                . # # . .
    `)
})
input.onLogoEvent(TouchButtonEvent.LongPressed, function on_logo_long_pressed() {
    basic.showLeds(`
        # # # # #
                # . . . .
                # . # . #
                # . . . .
                # # # # #
    `)
    basic.showLeds(`
        # # # # #
                . . . . .
                . # . # .
                . . . . .
                # # # # #
    `)
    basic.showLeds(`
        # # # # #
                . . . . #
                # . # . #
                . . . . #
                # # # # #
    `)
    basic.showString(" micro:bit")
})
basic.showLeds(`
    . . # . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
`)
basic.showLeds(`
    . . # . .
        # . . . .
        . . . . .
        . . . . .
        . . . . .
`)
basic.showLeds(`
    . . # . .
        # . # . .
        . . . . .
        . . . . .
        . . . . .
`)
basic.showLeds(`
    . . # . .
        # . # . #
        . . . . .
        . . . . .
        . . . . .
`)
basic.showLeds(`
    . . # . .
        # . # . #
        # . . . .
        . . . . .
        . . . . .
`)
basic.showLeds(`
    . . # . .
        # . # . #
        # . # . .
        . . . . .
        . . . . .
`)
basic.showLeds(`
    . . # . .
        # . # . #
        # . # . #
        . . . . .
        . . . . .
`)
basic.showLeds(`
    . . # . .
        # . # . #
        # . # . #
        # . . . .
        . . . . .
`)
basic.showLeds(`
    . . # . .
        # . # . #
        # . # . #
        # . . . .
        . . . . .
`)
basic.showLeds(`
    . . # . .
        # . # . #
        # . # . #
        # . . . #
        . . . . .
`)
basic.showLeds(`
    . . # . .
        # . # . #
        # . # . #
        # . . . #
        . # . . .
`)
basic.showLeds(`
    . . # . .
        # . # . #
        # . # . #
        # . . . #
        . # # . .
`)
basic.showLeds(`
    . . # . .
        # . # . #
        # . # . #
        # . . . #
        . # # # .
`)
basic.showLeds(`
    . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
`)
basic.showLeds(`
    . . # . .
        # . # . #
        # . # . #
        # . . . #
        . # # # .
`)
basic.showLeds(`
    . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
`)
basic.showLeds(`
    . . # . .
        # . # . #
        # . # . #
        # . . . #
        . # # # .
`)
basic.showLeds(`
    . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
`)
basic.forever(function on_forever() {
    
})
