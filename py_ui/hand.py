# This file contains the Container widgets for the hand.
# From counter.py, only the "bgcolor" gets changed.
#
# pink10000

import flet as ft

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