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

total_buttons = 5

def main(page: ft.Page):
    
    # Setter Methods
    def keyboardTestClear():
        print(hand.keyboardTest.value)
        hand.keyboardTest.value = ""
        
        # Update Page Earlier to Reduce Latency
        page.update()
        
        # Automatic Update for Keyboard
        if len(hand.keyboardTest.value) > 30:
            hand.keyboardTest.value = ""
        page.update()
    
    def port_update():

        print("Updating Ports")
        num_ports_before = serial.tools.list_ports.comports()
        lmc.content = portdisplays.list_ports()
        num_ports_after = serial.tools.list_ports.comports()
        if num_ports_after > num_ports_before:
            portdisplays.display_box.content = "Port Found"
            portdisplays.display_box.bgcolor = ft.colors.GREEN
            global_var.port_found = True
        page.update()


    # def port_connected_update():


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
            hand.ring.scale = 0.9

            hand.ring.scale = animationBounceFactor
        # -------------------- MIDDLE ---------------------
        if stateArray[2] == "0":
            hand.middle.bgcolor = ft.colors.RED
            hand.middle.scale = 1
        else:
            kb.write(hand.middleBind.value)
            hand.middle.bgcolor = ft.colors.GREEN
            hand.middle.scale = 0.9

            hand.middle.scale = animationBounceFactor
        # -------------------- INDEX ---------------------
        if stateArray[3] == "0":
            hand.index.bgcolor = ft.colors.RED
            hand.index.scale = 1
        else:
            kb.write(hand.indexBind.value)
            hand.index.bgcolor = ft.colors.GREEN
            hand.index.scale = 0.9

            hand.index.scale = animationBounceFactor
        # -------------------- THUMB ---------------------
        if stateArray[4] == "0":
            hand.thumb.bgcolor = ft.colors.RED
            hand.thumb.scale = 1
        else:
            kb.write(hand.thumbBind.value)
            hand.thumb.bgcolor = ft.colors.GREEN
            hand.thumb.scale = 0.9

            hand.thumb.scale = animationBounceFactor
        # -------
        page.update()

    # Theme Restraints
    page.title = "GraceNote Interface Companion"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # page.window_frameless = False
    #page.window_min_height = 350
    page.window_max_height = 300
    #page.window_min_width = 500
    page.window_max_width = 550
    page.window_width = 550
    page.window_maximizable = False
    page.window_center()
    page.padding = 0
    page.spacing = 0

    page.theme = ft.Theme(font_family="Consolas")

    # page.window_always_on_top = True
    # page.show_semantics_debugger = True 

    page.window_opacity = 0.95
    page.window_title_bar_hidden = True

    # Try Catch-Setup
    prev = None

    # Global Serial Variables
    try:
        global_var.ser = serial.Serial('COM9', 9600)
        global_var.reader = serialtest.ReadLine(global_var.ser)
        prev = global_var.reader.readline()

        stateArray = list(str(global_var.reader.readline()))[12:12 + total_buttons]
        global_var.port_found = True
        print("Port Found Again")

    except Exception as e:
        print(f"Error in Global Serial Variables: {e}")
        global_var.port_found = False
    
    # Page Functionality
    page.add(
        ft.ResponsiveRow([
            ft.WindowDragArea(
                ft.Container(
                    width=page.window_width,
                    #bgcolor="Brown",
                    content=ft.Row([
                        ft.Text("\t\tGraceNote Interface Companion", size=15, text_align="center"),
                        ft.Container(
                            ft.IconButton(ft.icons.CLOSE, icon_color="white", on_click=lambda _: page.window_close()),
                        )
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                    )
                ),
            )
        ]),
    )


    lmc = ft.Container(portdisplays.list_ports())
    page.add(
        ft.Column(
            [
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
                                ft.Row(
                                    [
                                        ft.ElevatedButton("Clear", on_click = keyboardTestClear),
                                        ft.ElevatedButton("Retry Finding Ports", on_click=lambda _: port_update())   
                                    ],
                                    alignment=ft.MainAxisAlignment.CENTER
                                )
                                
                            ])
                        ),

                        # Right Menu Container / Unused 
                        ft.Container()
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                )
            ],
            ft.MainAxisAlignment.START
        )
    )
    
    while True:
        if (global_var.port_found):
            print("Reading")
            # time.sleep(0.1)
             
            # Needs exception handling when device is pulled
            line = None
            try:
                line = str(global_var.reader.readline())
            except Exception as e:
                print(f"Device no longer available: {e}")
                global_var.port_found = False
                continue

            if str(prev) != line:
                stateArray = list(str(global_var.reader.readline()))[12:12 + total_buttons]
                prev = global_var.reader.readline()
                time.sleep(0.1)
                updateButtons(stateArray)
                print(stateArray)
        else:
            stateArray = ["0"] * total_buttons
            updateButtons(stateArray)
            print("Not Reading")
            time.sleep(0.5)

# -------------------- Main Program --------------------
ft.app(target=main)