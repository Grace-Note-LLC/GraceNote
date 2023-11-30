# Main Flet Program
# Author : pink10000

# Main Imports
import flet as ft
import serial
import serialtest

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

    # Theme Restraints
    page.title = "GraceNote Interface Companion"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window_frameless = True
    page.window_height = 450
    page.window_width = 600

    # Try Catch-Setup
    prev = None
    reader = None
    port_found = False

    # Global Serial Variables
    try:
        prev = reader.readline()
        stateArray = list(str(reader.readline()))[12:12 + total_buttons]
        port_found = True
    except Exception as e:
        print(f"Error: {e}")
    
    # Page Functionality
    page.add(
        ft.Row(
            [
                # Left Menu Container
                ft.Container(portdisplays.list_ports()),

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
                # time.sleep(0.1)
                hand.updateButtons(stateArray)
    else:
        page.add(
            ft.Column(
                [
                    portdisplays.display_box,
                    ft.ElevatedButton(
                        "Retry Finding Ports",
                        on_click=page.update
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
except serial.SerialException as e:
    print(f"Error: {e}")
    #quit()
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    #quit()

ft.app(target=main)