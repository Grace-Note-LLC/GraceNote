# This file contains the Container widgets for the hand.
# pink10000

import flet as ft
import global_var

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
    value = "d",
    on_focus = lambda _: verify_input(),
)
ringBind = ft.TextField(
    width = fingerWidth,
    height = bindHeight,
    text_align = "CENTER",
    value = "f",
    on_focus = lambda _: verify_input(),
)
middleBind = ft.TextField(
    width = fingerWidth,
    height = bindHeight,
    text_align = "CENTER",
    value = "j",
    on_focus = lambda _: verify_input(),
)
indexBind = ft.TextField(
    width = fingerWidth,
    height = bindHeight,
    text_align = "CENTER",
    value = "k",
    on_focus = lambda _: verify_input(),
)

allBinds = [pinkyBind.value, ringBind.value, middleBind.value, indexBind.value]

def verify_input():
    pinkyBind.value = pinkyBind.value[-1] if len(pinkyBind.value) > 0 else ""
    ringBind.value = ringBind.value[-1] if len(ringBind.value) > 0 else ""
    middleBind.value = middleBind.value[-1] if len(middleBind.value) > 0 else ""
    indexBind.value = indexBind.value[-1] if len(indexBind.value) > 0 else ""
    global_var.page.update()

def preset1():
    pinkyBind.value = "z"
    ringBind.value = "x"
    middleBind.value = ""
    indexBind.value = ""
    global_var.page.update()