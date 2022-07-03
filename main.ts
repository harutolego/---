input.onSound(DetectedSound.Quiet, function () {
    basic.showIcon(IconNames.Yes)
    music.playMelody("C5 C5 - - - - - - ", 120)
    music.stopAllSounds()
})
input.onGesture(Gesture.TiltRight, function () {
    basic.showIcon(IconNames.Duck)
})
input.onButtonPressed(Button.A, function () {
    basic.showIcon(IconNames.Happy)
})
input.onGesture(Gesture.TiltLeft, function () {
    basic.showIcon(IconNames.Skull)
})
input.onSound(DetectedSound.Loud, function () {
    basic.showIcon(IconNames.Angry)
    music.playMelody("C C C C - - - - ", 155)
})
input.onGesture(Gesture.Shake, function () {
    basic.showIcon(IconNames.Umbrella)
})
input.onButtonPressed(Button.B, function () {
    basic.showIcon(IconNames.House)
})
music.playMelody("F G A B C5 C5 C5 - ", 255)
basic.showString("Hello!")
basic.showIcon(IconNames.Heart)
basic.showIcon(IconNames.Yes)
