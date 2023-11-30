# This file contains the Container widgets for the hand.
# From counter.py, only the "bgcolor" gets changed.
#
# pink10000

import flet as ft
import pyautogui as kb

fingerWidth = 50
fingerHeight = 50
baseColor = ft.colors.RED

# Hand Widgets
pinky = ft.Container(
    width = fingerWidth,
    height = fingerHeight,
    alignment = ft.alignment.center,
    content = ft.Text("Pinky"),
    bgcolor = ft.colors.RED,
    scale=ft.transform.Scale(scale=1),
    animate_scale=ft.animation.Animation(600, ft.AnimationCurve.BOUNCE_OUT),
)

ring = ft.Container(
    width = fingerWidth,
    height = fingerHeight,
    alignment = ft.alignment.center,
    content = ft.Text("Ring"),
    bgcolor = baseColor,
)

middle = ft.Container(
    width = fingerWidth,
    height = fingerHeight,
    alignment = ft.alignment.center,
    content = ft.Text("Middle"),
    bgcolor = baseColor,
)

index = ft.Container(
    width = fingerWidth,
    height = fingerHeight,
    alignment = ft.alignment.center,
    content = ft.Text("Index"),
    bgcolor = baseColor,
)

thumb = ft.Container(
    width = fingerWidth,
    height = fingerHeight,
    alignment = ft.alignment.center,
    content = ft.Text("Thumb"),
    bgcolor = baseColor,
)

# Clear Button Widget
keyboardTest = ft.TextField(
    label = "Keyboard Test Field",
    value = ""
)

# Keybind Input Fields
pinkyBind = ft.TextField(
    width = fingerWidth,
    text_align = "CENTER",
    value = "a"
)
ringBind = ft.TextField(
    width = fingerWidth,
    text_align = "CENTER",
    value = "b"
)
middleBind = ft.TextField(
    width = fingerWidth,
    text_align = "CENTER",
    value = "c"
)
indexBind = ft.TextField(
    width = fingerWidth,
    text_align = "CENTER",
    value = "d"
)
thumbBind = ft.TextField(
    width = fingerWidth,
    text_align = "CENTER",
    value = "e"
)
allBinds = [pinkyBind.value, ringBind.value, middleBind.value, indexBind.value, thumbBind.value]

def updateButtons(stateArray):
        animationBounceFactor = 0.5
        # -------------------- PINKY --------------------
        if stateArray[0] == "0":
            pinky.bgcolor = ft.colors.RED
            pinky.scale = 1
        else:
            kb.write(pinkyBind.value)
            pinky.bgcolor = ft.colors.GREEN
            pinky.scale = animationBounceFactor

        # -------------------- RING ---------------------
        if stateArray[1] == "0":
            ring.bgcolor = ft.colors.RED
            ring.scale = 1
        else:
            kb.write(ringBind.value)
            ring.bgcolor = ft.colors.GREEN
            ring.scale = animationBounceFactor
        # -------------------- MIDDLE ---------------------
        if stateArray[2] == "0":
            middle.bgcolor = ft.colors.RED
            middle.scale = 1
        else:
            kb.write(middleBind.value)
            middle.bgcolor = ft.colors.GREEN
            middle.scale = animationBounceFactor
        # -------------------- INDEX ---------------------
        if stateArray[3] == "0":
            index.bgcolor = ft.colors.RED
            index.scale = 1
        else:
            kb.write(indexBind.value)
            index.bgcolor = ft.colors.GREEN
            index.scale = animationBounceFactor
        # -------------------- THUMB ---------------------
        if stateArray[4] == "0":
            thumb.bgcolor = ft.colors.RED
            thumb.scale = 1
        else:
            kb.write(thumbBind.value)
            thumb.bgcolor = ft.colors.GREEN
            thumb.scale = animationBounceFactor