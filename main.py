def on_logo_pressed():
    basic.show_leds("""
        . # . # .
                . . . . .
                # # # # #
                # # # # #
                . # # # .
    """)
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

def on_gesture_screen_down():
    basic.show_leds("""
        . # # . .
                . . # # .
                . . # # .
                . . # # .
                . # # . .
    """)
input.on_gesture(Gesture.SCREEN_DOWN, on_gesture_screen_down)

def on_logo_long_pressed():
    basic.show_leds("""
        # # # # #
                # . . . .
                # . # . #
                # . . . .
                # # # # #
    """)
    basic.show_leds("""
        # # # # #
                . . . . .
                . # . # .
                . . . . .
                # # # # #
    """)
    basic.show_leds("""
        # # # # #
                . . . . #
                # . # . #
                . . . . #
                # # # # #
    """)
    basic.show_string(" micro:bit")
input.on_logo_event(TouchButtonEvent.LONG_PRESSED, on_logo_long_pressed)

basic.show_leds("""
    . . # . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
""")
basic.show_leds("""
    . . # . .
        # . . . .
        . . . . .
        . . . . .
        . . . . .
""")
basic.show_leds("""
    . . # . .
        # . # . .
        . . . . .
        . . . . .
        . . . . .
""")
basic.show_leds("""
    . . # . .
        # . # . #
        . . . . .
        . . . . .
        . . . . .
""")
basic.show_leds("""
    . . # . .
        # . # . #
        # . . . .
        . . . . .
        . . . . .
""")
basic.show_leds("""
    . . # . .
        # . # . #
        # . # . .
        . . . . .
        . . . . .
""")
basic.show_leds("""
    . . # . .
        # . # . #
        # . # . #
        . . . . .
        . . . . .
""")
basic.show_leds("""
    . . # . .
        # . # . #
        # . # . #
        # . . . .
        . . . . .
""")
basic.show_leds("""
    . . # . .
        # . # . #
        # . # . #
        # . . . .
        . . . . .
""")
basic.show_leds("""
    . . # . .
        # . # . #
        # . # . #
        # . . . #
        . . . . .
""")
basic.show_leds("""
    . . # . .
        # . # . #
        # . # . #
        # . . . #
        . # . . .
""")
basic.show_leds("""
    . . # . .
        # . # . #
        # . # . #
        # . . . #
        . # # . .
""")
basic.show_leds("""
    . . # . .
        # . # . #
        # . # . #
        # . . . #
        . # # # .
""")
basic.show_leds("""
    . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
""")
basic.show_leds("""
    . . # . .
        # . # . #
        # . # . #
        # . . . #
        . # # # .
""")
basic.show_leds("""
    . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
""")
basic.show_leds("""
    . . # . .
        # . # . #
        # . # . #
        # . . . #
        . # # # .
""")
basic.show_leds("""
    . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
""")

def on_forever():
    pass
basic.forever(on_forever)
