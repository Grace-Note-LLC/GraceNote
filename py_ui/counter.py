import flet as ft
import serial
import serialtest
import time

global ser
global r
global out
global pinkyColor
global stateArray

def main(page: ft.Page):
    page.title = "cody yelling sim"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window_frameless = True
    page.window_max_height = 500
    page.window_max_width = 500



    prev = r.readline()
    stateArray = list(str(r.readline()))[12:14]

    # txt_number = ft.Text(value=prev, text_align=ft.TextAlign.RIGHT, width=400)

    # Hand State Values
    pinkyColor = ft.colors.RED if stateArray[0] == "0" else ft.colors.GREEN
    print(pinkyColor)


    page.add(
        ft.Row(
            [
                # Left Menu Container
                ft.Container(
                    ft.Column(
                        [
                            ft.Card(
                                ft.Text(value = "L1")
                            ),
                            ft.Card(
                                ft.Text(value = "L2")
                            ),
                            ft.Card(
                                ft.Text(value = "L3")
                            )
                        ]
                    )
                ),

                # Hand Container
                ft.Container(
                    content = ft.Row(
                        [   
                            ft.Container(
                                width = 50,
                                height = 50,
                                alignment = ft.alignment.center,
                                content = ft.Text("Pinky"),
                                bgcolor = pinkyColor,
                            ),
                            ft.Container(
                                width = 50,
                                height = 50,
                                alignment = ft.alignment.center,
                                content = ft.Text("Ring"),
                                bgcolor = "red",
                            ),
                            ft.Container(
                                width = 50,
                                height = 50,
                                alignment = ft.alignment.center,
                                content = ft.Text("Middle"),
                                bgcolor = ft.colors.AMBER,
                            ),
                            ft.Container(
                                width = 50,
                                height = 50,
                                alignment = ft.alignment.center,
                                content = ft.Text("Index"),
                                bgcolor = ft.colors.AMBER,
                            ),
                            ft.Container(
                                width = 50,
                                height = 50,
                                alignment = ft.alignment.center,
                                content = ft.Text("Thumb"),
                                bgcolor = ft.colors.AMBER,
                            )
                        ],
                        alignment = ft.CrossAxisAlignment.CENTER,

                    )
                ),
                
                # Right Menu Container
                ft.Container(

                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,

        )
    )

    def changeTheme(stateArray):
        pinkyColor = ft.colors.RED if stateArray[0] == "0" else ft.colors.GREEN
        print(pinkyColor)
        page.update()

    while True:
        if str(prev) != str(r.readline()):
            # print("Data Received" + str(r.readline()) + "s")
            stateArray = list(str(r.readline()))[12:14]

            print(stateArray)   
            prev = r.readline()
            #time.sleep(0.1)
            # txt_number.value = str(prev)

            changeTheme(stateArray)

            page.update()



try:
    ser = serial.Serial('COM11', 9600)
    r = serialtest.ReadLine(ser)
    out = r.readline()

except serial.SerialException as e:
    print(f"An error occurred: {e}")
    quit()
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    quit()

ft.app(target=main)