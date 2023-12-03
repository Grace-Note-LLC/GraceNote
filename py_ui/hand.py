# This file contains the Container widgets for the hand.
# pink10000

import flet as ft

fingerWidth = 50
fingerHeight = 50
bindHeight = fingerHeight 

baseColor = ft.colors.RED

# Hand Widgets
pinky = ft.Container(
    width = fingerWidth,
    height = fingerHeight,
    alignment = ft.alignment.center,
    content = ft.Text("Left",text_align=ft.alignment.center),
    bgcolor = ft.colors.RED,
    scale=ft.transform.Scale(scale=1),
    animate_scale=ft.animation.Animation(600, ft.AnimationCurve.BOUNCE_OUT),
)

ring = ft.Container(
    width = fingerWidth,
    height = fingerHeight,
    alignment = ft.alignment.center,
    content = ft.Text("Mid\nLeft",text_align=ft.alignment.center),
    bgcolor = ft.colors.RED,
    scale=ft.transform.Scale(scale=1),
    animate_scale=ft.animation.Animation(600, ft.AnimationCurve.BOUNCE_OUT),
)

middle = ft.Container(
    width = fingerWidth,
    height = fingerHeight,
    alignment = ft.alignment.center,
    content = ft.Text("Mid\nRight",text_align=ft.alignment.center),
    bgcolor = ft.colors.RED,
    scale=ft.transform.Scale(scale=1),
    animate_scale=ft.animation.Animation(600, ft.AnimationCurve.BOUNCE_OUT),
)

index = ft.Container(
    width = fingerWidth,
    height = fingerHeight,
    alignment = ft.alignment.center,
    content = ft.Text("Right",text_align=ft.alignment.center),
    bgcolor = ft.colors.RED,
    scale=ft.transform.Scale(scale=1),
    animate_scale=ft.animation.Animation(600, ft.AnimationCurve.BOUNCE_OUT),
)

# Keybind Input Fields
pinkyBind = ft.TextField(
    width = fingerWidth,
    height = bindHeight,
    text_align = "CENTER",
    value = "a"
)
ringBind = ft.TextField(
    width = fingerWidth,
    height = bindHeight,
    text_align = "CENTER",
    value = "b"
)
middleBind = ft.TextField(
    width = fingerWidth,
    height = bindHeight,
    text_align = "CENTER",
    value = "c"
)
indexBind = ft.TextField(
    width = fingerWidth,
    height = bindHeight,
    text_align = "CENTER",
    value = "d"
)
thumbBind = ft.TextField(
    width = fingerWidth,
    height = bindHeight,
    text_align = "CENTER",
    value = "e"
)
allBinds = [pinkyBind.value, ringBind.value, middleBind.value, indexBind.value, thumbBind.value]