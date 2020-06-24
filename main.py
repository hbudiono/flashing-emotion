def on_button_pressed_a():
    for index in range(4):
        basic.show_icon(IconNames.HAPPY)
        basic.pause(200)
        basic.clear_screen()
        basic.pause(200)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    for index2 in range(4):
        basic.show_icon(IconNames.SAD)
        basic.pause(200)
        basic.clear_screen()
        basic.pause(200)
input.on_button_pressed(Button.B, on_button_pressed_b)
