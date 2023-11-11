import flet as ft
import serial
import serialtest

def main(page: ft.Page):
    page.title = "Flet counter example"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window_frameless = True
    page.window_max_height = 500
    page.window_max_width = 500

    prev = r.readline()

    txt_number = ft.Text(value=prev, text_align=ft.TextAlign.RIGHT, width=400)

    page.add(
        ft.Row(
            [
                txt_number,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )
    
    while True:
        if str(prev) != str(r.readline()):
            # print(str(r.readline()) + "s")
            print(str(r.readline())[12:13])   
            prev = r.readline()
            txt_number.value = str(prev)
            page.update()

ser = serial.Serial('COM9', 9600)
r = serialtest.ReadLine(ser)
out = r.readline()


ft.app(target=main)