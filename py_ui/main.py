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
import global_var

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
        
        # Update Page Earlier to Reduce Latency
        page.update()
        
        # Automatic Update for Keyboard
        if len(hand.keyboardTest.value) > 30:
            hand.keyboardTest.value = ""
        page.update()
    
    def port_update():
        global port_found

        print("Updating Ports")
        num_ports_before = serial.tools.list_ports.comports()
        lmc.content = portdisplays.list_ports(page)
        num_ports_after = serial.tools.list_ports.comports()
        if num_ports_after > num_ports_before:
            portdisplays.display_box.content = "Port Found"
            portdisplays.display_box.bgcolor = ft.colors.GREEN
            port_found = True
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
        global_var.ser = serial.Serial('COM9', 9600)
        print("ser found")
        global_var.reader = serialtest.ReadLine(global_var.ser)
        print("reader found")

        prev = global_var.reader.readline()
        stateArray = list(str(global_var.reader.readline()))[12:12 + total_buttons]
        port_found = True
        print("Port Found Again")
    except Exception as e:
        print(f"Error in Global Serial Variables: {e}")
        port_found = False
    
    # Page Functionality
    lmc = ft.Container(portdisplays.list_ports())

    page.add(
        ft.Row(
            [
                # Left Menu Container
                lmc,

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
                        ft.Row([
                            ft.ElevatedButton("Clear", on_click = keyboardTestClear),
                            ft.ElevatedButton("Retry Finding Ports", on_click=lambda _: port_update())   
                        ])
                        
                    ])
                ),

                # Right Menu Container
                ft.Container()
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )
    
    while True:
        if (port_found):
            print("Reading")
            # time.sleep(0.1)
             
            # Needs exception handling when device is pulled

            if str(prev) != str(global_var.reader.readline()):
                stateArray = list(str(global_var.reader.readline()))[12:12 + total_buttons]
                prev = global_var.reader.readline()
                time.sleep(0.1)
                updateButtons(stateArray)
                print(stateArray)
            # updateButtons(stateArray) # DO NOT REMOVE
        else:
            print("Not Reading")
            time.sleep(0.5)

# -------------------- Main Program --------------------
ft.app(target=main)