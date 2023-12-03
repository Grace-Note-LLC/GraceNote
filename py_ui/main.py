# Main Flet Program
# Author : pink10000

# Main Imports
import flet as ft
import serial
import time

# Helper Imports
import hand
import portdisplays
import global_var

def main(page: ft.Page):
    
    # Setter Methods

    # (e) required!!
    def keyboardTestClear():
        print(keyboardTest.content.value)
        keyboardTest.value = ""
        
        # Update Page Earlier to Reduce Latency
        page.update()
        
        # Automatic Update for Keyboard
        if len(keyboardTest.content.value) > 30:
            keyboardTest.content.value = ""
        page.update()
    
    no_ports_dialog_box = ft.AlertDialog(
        content=ft.Text("\t\t\t\t\tNo Ports Available", size=15, text_align=ft.MainAxisAlignment.CENTER),
        actions_alignment=ft.alignment.center,
        content_padding=20,
        inset_padding=ft.padding.symmetric(vertical=0, horizontal=0),
    )
    def no_ports_dialog():
        page.dialog = no_ports_dialog_box
        no_ports_dialog_box.open = True
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
        elif num_ports_after == num_ports_before:
            no_ports_dialog()
        page.update()

    def write_config():
        payload = "".join([hand.pinkyBind.value, hand.ringBind.value, hand.middleBind.value, hand.indexBind.value])

        try:
            global_var.ser.reset_output_buffer()
        except Exception as e:
            print(f"Sent data to nonexistent port: {e}")
            sent_nothing_dialog()
        print(f"PAYLOAD SENDING: {payload}")
        global_var.ser.write(payload.encode('utf-8'))
        time.sleep(0.1)
        global_var.ser.flush()

    sent_nothing_dialog_box = ft.AlertDialog(title=ft.Text("\t\t No Port to Send Data to", size=15))
    def sent_nothing_dialog():
        page.dialog = sent_nothing_dialog_box
        sent_nothing_dialog_box.open = True
        page.update()

    def updateButtons(stateArray):
        animationBounceFactor = 0.5
        # -------------------- PINKY --------------------
        if stateArray[0] == "0":
            hand.pinky.bgcolor = ft.colors.RED
            hand.pinky.scale = 1
            page.update()
        else:
            hand.pinky.bgcolor = ft.colors.GREEN
            hand.pinky.scale = 0.9
            hand.pinky.scale = animationBounceFactor
            page.update()
        # -------------------- RING ---------------------
        if stateArray[1] == "0":
            hand.ring.bgcolor = ft.colors.RED
            hand.ring.scale = 1
            page.update()
        else:
            hand.ring.bgcolor = ft.colors.GREEN
            hand.ring.scale = 0.9
            hand.ring.scale = animationBounceFactor
            page.update()
       # -------------------- MIDDLE ---------------------
        if stateArray[2] == "0":
            hand.middle.bgcolor = ft.colors.RED
            hand.middle.scale = 1
            page.update()
        else:
            hand.middle.bgcolor = ft.colors.GREEN
            hand.middle.scale = 0.9
            hand.middle.scale = animationBounceFactor
            page.update()
        # -------------------- INDEX ---------------------
        if stateArray[3] == "0":
            hand.index.bgcolor = ft.colors.RED
            hand.index.scale = 1
            page.update()
        else:
            hand.index.bgcolor = ft.colors.GREEN
            hand.index.scale = 0.9
            hand.index.scale = animationBounceFactor
            page.update()

    keyboardTest = ft.Container(content=ft.TextField(
        label = "Keyboard Test Field",
        value = "",
        border_color = "transparent",
        content_padding= 5,
        on_change=lambda _: kb_test_change(),
    ),width=230)
    def kb_test_change():
        keyboardTest.content.border_color=ft.colors.with_opacity(0.5, ft.colors.GREY_100)
        page.update()
        time.sleep(0.05)
        keyboardTest.content.border_color=ft.colors.with_opacity(0, ft.colors.LIGHT_GREEN_ACCENT_700)
        page.update()

    theme_switch = ft.Switch(label="Light theme", on_change=lambda _: theme_changed())
    def theme_changed():
        page.theme_mode = (
            ft.ThemeMode.DARK
            if page.theme_mode == ft.ThemeMode.LIGHT
            else ft.ThemeMode.LIGHT
        )
        theme_switch.label = (
            "Light theme" if page.theme_mode == ft.ThemeMode.LIGHT else "Dark theme"
        )
        page.update()

    def minimize():
        page.window_minimized = True
        page.update()

    # Theme Restraints
    page.title = "GraceNote Interface Companion"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.window_frameless = False
    #page.window_min_height = 350
    page.window_max_height = 300
    #page.window_min_width = 500
    page.window_max_width = 500
    page.window_width = 500
    page.window_maximizable = False
    page.window_center()
    page.padding = 0
    page.spacing = 0

    page.theme = ft.Theme(font_family="Consolas")

    # page.window_always_on_top = True
    # page.show_semantics_debugger = True 

    page.window_opacity = 0.90
    page.window_title_bar_hidden = True

    # Try Catch-Setup
    prev = None

    # Global Serial Variables
    try:
        global_var.ser = serial.Serial('COM9', global_var.baud_rate)
        # global_var.reader = serialtest.ReadLine(global_var.ser)
        prev = global_var.reader.readline()

        stateArray = list(str(global_var.reader.readline()))[12:12 + global_var.total_buttons]
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
                        ft.Text("\t\tGraceNote Interface Companion", size=15, text_align=ft.alignment.center),
                        ft.Row([
                            ft.Container(
                                ft.IconButton(ft.icons.MINIMIZE, icon_color="white", on_click=lambda _: minimize()),
                            ),
                            ft.Container(
                                ft.IconButton(ft.icons.CLOSE, icon_color="white", on_click=lambda _: page.window_close()),
                            )
                        ])
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
                                ft.Row(
                                    [hand.pinkyBind, hand.ringBind, hand.middleBind, hand.indexBind], 
                                    alignment=ft.MainAxisAlignment.CENTER,
                                ),
                                ft.Row(
                                    [hand.pinky, hand.ring, hand.middle, hand.index,],
                                    alignment=ft.MainAxisAlignment.CENTER,
                                ),
                                keyboardTest,
                            ])
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.Row(
                    [
                        ft.ElevatedButton(content=ft.Row([ft.Icon(ft.icons.RESTART_ALT_ROUNDED, size=20), ft.Text("Find Ports", size = 12)]), 
                            on_click=lambda _: port_update()
                        ),
                        ft.ElevatedButton(content=ft.Row([ft.Icon(ft.icons.DELETE_OUTLINE,size=20), ft.Text("Clear", size = 12)]), 
                            on_click=lambda _: keyboardTestClear()
                        ),
                        ft.ElevatedButton(content=ft.Row([ft.Icon(ft.icons.UPLOAD_ROUNDED, size=20), ft.Text("Send Input", size=12),]),    
                            on_click=lambda _: write_config() )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
            ],
            ft.MainAxisAlignment.START
        )
    )
    
    while True:
        if (global_var.port_found):
            
            # Needs exception handling when device is pulled
            line = None
            try:
                line = str(global_var.reader.readline())
            except Exception as e:
                print(f"Device no longer available: {e}")
                global_var.port_found = False
                continue

            if str(prev) != line:
                stateArray = list(str(global_var.reader.readline()))[12:12 + global_var.total_buttons]
                prev = global_var.reader.readline()
                # time.sleep(0.1)
                updateButtons(stateArray)
                print(stateArray)

        else:
            stateArray = ["0"] * global_var.total_buttons
            updateButtons(stateArray)
            # print("Not Reading")
            time.sleep(0.5)

# -------------------- Main Program --------------------
ft.app(target=main)