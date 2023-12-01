# Main Flet Program
# Author : pink10000

# Main Imports
import flet as ft
import serial
import serialtest
import pyautogui as kb
import time

# Helper Imports
import hand
import portdisplays

global ser
global reader
global out
global stateArray

total_buttons = 5



def main(page: ft.Page):

    # Setter Methods
    def keyboardTestClear(e):
        print(hand.keyboardTest.value)
        hand.keyboardTest.value = ""
        page.update()
        
        # Update Page Earlier to Reduce Latency
        page.update()
        
        # Automatic Update for Keyboard
        if len(hand.keyboardTest.value) > 30:
            hand.keyboardTest.value = ""
        page.update()

    def port_update():
        portdisplays.list_ports(page)
        page.update()

    def updateButtons(stateArray):
        animationBounceFactor = 0.5
        # -------------------- PINKY --------------------
        if stateArray[0] == "0":
            hand.pinky.bgcolor = ft.colors.RED
            hand.pinky.scale = 1
        else:
            kb.write(hand.pinkyBind.value)
            hand.pinky.bgcolor = ft.colors.GREEN
            hand.pinky.scale = 0.9

            hand.pinky.scale = animationBounceFactor
        # -------------------- RING ---------------------
        if stateArray[1] == "0":
            hand.ring.bgcolor = ft.colors.RED
            hand.ring.scale = 1
        else:
            kb.write(hand.ringBind.value)
            hand.ring.bgcolor = ft.colors.GREEN
            hand.ring.scale = animationBounceFactor
        # -------------------- MIDDLE ---------------------
        if stateArray[2] == "0":
            hand.middle.bgcolor = ft.colors.RED
            hand.middle.scale = 1
        else:
            kb.write(hand.middleBind.value)
            hand.middle.bgcolor = ft.colors.GREEN
            hand.middle.scale = animationBounceFactor
        # -------------------- INDEX ---------------------
        if stateArray[3] == "0":
            hand.index.bgcolor = ft.colors.RED
            hand.index.scale = 1
        else:
            kb.write(hand.indexBind.value)
            hand.index.bgcolor = ft.colors.GREEN
            hand.index.scale = animationBounceFactor
        # -------------------- THUMB ---------------------
        if stateArray[4] == "0":
            hand.thumb.bgcolor = ft.colors.RED
            hand.thumb.scale = 1
        else:
            kb.write(hand.thumbBind.value)
            hand.thumb.bgcolor = ft.colors.GREEN
            hand.thumb.scale = animationBounceFactor
        # -------
        page.update()


    # Theme Restraints
    page.title = "GraceNote Interface Companion"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window_frameless = True
    page.window_height = 450
    page.window_width = 600

    # Try Catch-Setup
    prev = None
    # reader = None
    port_found = False

    # Global Serial Variables
    try:
        prev = reader.readline()
        stateArray = list(str(reader.readline()))[12:12 + total_buttons]
        port_found = True
        print("Port Found Again")
    except Exception as e:
        print(f"Error: {e}")
    
    # Page Functionality
    page.add(
        ft.Row(
            [
                # Left Menu Container
                ft.Container(portdisplays.list_ports(page)),

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
    
    if (port_found):
        while True:
            if str(prev) != str(reader.readline()):
                stateArray = list(str(reader.readline()))[12:12 + total_buttons]
                prev = reader.readline()
                time.sleep(0.1)
                updateButtons(stateArray)
            # updateButtons(stateArray) # DO NOT REMOVE
    else:
        page.add(
            ft.Column(
                [
                    portdisplays.display_box,
                    ft.ElevatedButton(
                        "Retry Finding Ports",
                        on_click=lambda _: port_update()
                    )
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        )

# -------------------- Main Program --------------------
try:
    ser = serial.Serial('COM9', 9600)
    reader = serialtest.ReadLine(ser)
    out = reader.readline()
    print("Port Located")
except serial.SerialException as e:
    print(f"Error: {e}")
    #quit()
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    #quit()

ft.app(target=main)