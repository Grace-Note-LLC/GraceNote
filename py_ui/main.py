import flet as ft
import serial
import serialtest
import time
import hand

global ser
global r
global out
global stateArray

total_buttons = 1

def main(page: ft.Page):

    # Setter Methods
    def keyboardTestClear(e):
        print(hand.keyboardTest.value)
        hand.keyboardTest.value = ""
        page.update()
    def keyboardInput():
        hand.keyboardTest.value += str(stateArray[total_buttons - 1])
        page.update()
    def changeTheme(stateArray):
        if stateArray[0] == "0":
            hand.pinky.bgcolor = ft.colors.RED
            hand.pinky.scale = 1
        else:
            hand.pinky.bgcolor = ft.colors.GREEN
            hand.pinky.scale = 0.9


        
        #hand.ring.bgcolor = ft.colors.RED if stateArray[1] == "0" else ft.colors.GREEN
        #hand.middle.bgcolor = ft.colors.RED if stateArray[2] == "0" else ft.colors.GREEN
        #hand.index.bgcolor = ft.colors.RED if stateArray[3] == "0" else ft.colors.GREEN
        #hand.thumb.bgcolor = ft.colors.RED if stateArray[4] == "0" else ft.colors.GREEN

        page.update()
    
    
    # Theme Restraints
    page.title = "cody yelling sim"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window_frameless = True
    page.window_height = 500
    page.window_width = 500

    # Global Serial Variables
    prev = r.readline()
    stateArray = list(str(r.readline()))[12:12 + total_buttons]

    # Page Functionality
    page.add(
        ft.Row(
            [
                # Left Menu Container
                ft.Container(
                    ft.Column(
                        [
                            ft.Card(ft.Text(value = "L1")),
                            ft.Card(ft.Text(value = "L2")),
                            ft.Card(ft.Text(value = "L3"))
                        ]
                    )
                ),

                # Center Container
                ft.Container(
                    ft.Column([
                        # Hand Widgets
                        ft.Row([
                            hand.pinkyBind, hand.ringBind, hand.middleBind, hand.indexBind, hand.thumbBind
                        ]),
                        ft.Row(
                            [hand.pinky, hand.ring, hand.middle, hand.index, hand.thumb],
                            alignment = ft.CrossAxisAlignment.CENTER,
                        ),
                        hand.keyboardTest,
                        ft.ElevatedButton("Clear", on_click = keyboardTestClear)
                    ])
                ),

                # Right Menu Container
                ft.Container()
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

    while True:
        if str(prev) != str(r.readline()):
            stateArray = list(str(r.readline()))[12:12 + total_buttons]
            prev = r.readline()
            # time.sleep(0.1)
            changeTheme(stateArray)
            keyboardInput()


try:
    ser = serial.Serial('COM9', 9600)
    r = serialtest.ReadLine(ser)
    out = r.readline()

except serial.SerialException as e:
    print(f"An error occurred: {e}")
    quit()
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    quit()

ft.app(target=main)