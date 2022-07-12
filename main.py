def on_sound_quiet():
    basic.show_icon(IconNames.YES)
    music.play_melody("C5 C5 - - - - - - ", 120)
    music.stop_all_sounds()
input.on_sound(DetectedSound.QUIET, on_sound_quiet)

def on_gesture_tilt_right():
    basic.show_icon(IconNames.DUCK)
input.on_gesture(Gesture.TILT_RIGHT, on_gesture_tilt_right)

def on_button_pressed_a():
    basic.show_icon(IconNames.HAPPY)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_tilt_left():
    basic.show_icon(IconNames.SKULL)
input.on_gesture(Gesture.TILT_LEFT, on_gesture_tilt_left)

def on_sound_loud():
    basic.show_icon(IconNames.ANGRY)
    music.play_melody("C C C C - - - - ", 155)
input.on_sound(DetectedSound.LOUD, on_sound_loud)

def on_gesture_shake():
    basic.show_icon(IconNames.UMBRELLA)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_button_pressed_b():
    basic.show_icon(IconNames.HOUSE)
input.on_button_pressed(Button.B, on_button_pressed_b)

music.play_melody("F G A B C5 C5 C5 - ", 255)
basic.show_string("Hello!")
basic.show_icon(IconNames.HEART)
basic.show_icon(IconNames.YES)