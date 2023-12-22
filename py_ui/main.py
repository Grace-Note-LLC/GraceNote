# Main Flet Program
# Author : pink10000

# Main Imports
import flet as ft
import serial
import serial.tools.list_ports
import time
import keyboard

# Helper Imports
import hand
import portdisplays
import global_var

def main(page: ft.Page):
    global_var.page = page
    
    # Setter Methods

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
        num_ports_before = 0
        num_ports_after = 0
        for _, desc, _ in sorted(serial.tools.list_ports.comports()):
            if ("Bluetooth" not in "{}".format(desc)):
                num_ports_after += 1
        if num_ports_after <= num_ports_before and num_ports_after < 1:
            no_ports_dialog()
        lmc.content = portdisplays.list_ports()
        page.update()

    def write_config():
        hand.verify_input()
        payload = "".join([hand.pinkyBind.value, "~", hand.ringBind.value, "~", hand.middleBind.value, "~", hand.indexBind.value])
        try:
            global_var.ser.reset_output_buffer()
            global_var.ser.write(payload.encode('utf-8'))
            time.sleep(0.1)
            global_var.ser.flush()
            print(f"PAYLOAD SENDING: {payload}")
            global_var.port_found = True
        except Exception as e:
            print(f"Sent data to nonexistent port: {e}")
            sent_nothing_dialog()
        
    sent_nothing_dialog_box = ft.AlertDialog(title=ft.Text("\t\t No Port to Send Data to", size=15))
    def sent_nothing_dialog():
        page.dialog = sent_nothing_dialog_box
        sent_nothing_dialog_box.open = True
        page.update()

    def updateButtons(bind_states):
        animationBounceFactor = 0.5
        # -------------------- PINKY --------------------
        if bind_states[0]:
            hand.pinky.bgcolor = ft.colors.RED
            hand.pinky.scale = 1
            page.update()
        else:
            hand.pinky.bgcolor = ft.colors.GREEN
            hand.pinky.scale = 0.9
            hand.pinky.scale = animationBounceFactor
            page.update()
        # -------------------- RING ---------------------
        if bind_states[1]:
            hand.ring.bgcolor = ft.colors.RED
            hand.ring.scale = 1
            page.update()
        else:
            hand.ring.bgcolor = ft.colors.GREEN
            hand.ring.scale = 0.9
            hand.ring.scale = animationBounceFactor
            page.update()
       # -------------------- MIDDLE ---------------------
        if bind_states[2]:
            hand.middle.bgcolor = ft.colors.RED
            hand.middle.scale = 1
            page.update()
        else:
            hand.middle.bgcolor = ft.colors.GREEN
            hand.middle.scale = 0.9
            hand.middle.scale = animationBounceFactor
            page.update()
        # -------------------- INDEX ---------------------
        if bind_states[3]:
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
        on_focus=lambda _: keyboardTestClear(),
    ),width=230)
    def kb_test_change():
        keyboardTest.content.border_color=ft.colors.with_opacity(0.5, ft.colors.GREY_100)
        page.update()
        time.sleep(0.05)
        keyboardTest.content.border_color=ft.colors.with_opacity(0, ft.colors.LIGHT_GREEN_ACCENT_700)
        page.update()
    def keyboardTestClear():
        print(keyboardTest.content.value)
        keyboardTest.content.value = ""
        
        # Update Page Earlier to Reduce Latency
        page.update()
        
        # Automatic Update for Keyboard
        if len(keyboardTest.content.value) > 30:
            keyboardTest.content.value = ""
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

    # Global Serial Variables
    try:
        global_var.ser = serial.Serial('COM9', global_var.baud_rate)
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
                                ft.IconButton(ft.icons.MINIMIZE, on_click=lambda _: minimize()),
                            ),
                            ft.Container(
                                ft.IconButton(ft.icons.DARK_MODE_OUTLINED, on_click=lambda _: theme_changed()),
                            ),
                            ft.Container(
                                ft.IconButton(ft.icons.CLOSE, on_click=lambda _: page.window_close()),
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
                        ft.Column([lmc]),

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
                        ft.PopupMenuButton(
                            items=[button for button in hand.preset_list]
                        ),
                        ft.ElevatedButton(content=ft.Row([ft.Icon(ft.icons.RESTART_ALT_ROUNDED, size=20), ft.Text("Find Ports", size = 12)]), 
                            on_click=lambda _: port_update()
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

    bind_states = [True] * global_var.total_buttons
    while True:
        if (global_var.port_found):
            
            # Needs exception handling when device is pulled
            try:
                all_ports = [tuple(p) for p in list(serial.tools.list_ports.comports())]
                current_port = [port for port in all_ports if global_var.ser.name in port ][0]
                if len(current_port) == 0:
                    global_var.port_found = False
    
            except Exception as e:
                print(f"Device no longer available: {e}")
                global_var.port_found = False
            # The above code is very hack-y and needs new logic to fix it
            # But if it works...it works...

            bind_states[0] = not keyboard.is_pressed(hand.pinkyBind.value) 
            bind_states[1] = not keyboard.is_pressed(hand.ringBind.value) 
            bind_states[2] = not keyboard.is_pressed(hand.middleBind.value)
            bind_states[3] = not keyboard.is_pressed(hand.indexBind.value)

            # time.sleep(0.1)
            updateButtons(bind_states)
            # print(bind_states)

        else:
            bind_states = [True] * global_var.total_buttons
            updateButtons(bind_states)
            print("Not Reading")
            time.sleep(0.5)

# -------------------- Main Program --------------------
ft.app(target=main)