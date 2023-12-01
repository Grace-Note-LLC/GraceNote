import flet as ft

import serialtest

import serial.tools.list_ports
ports = serial.tools.list_ports.comports()

display_box = ft.Container(
    content=ft.Text("No Device Found"), 
    padding=5,
    bgcolor=ft.colors.RED,
    border_radius=3
)
port_list_title = ft.Container(
    content=ft.Text("List of Available Ports"),
    padding=5,
    bgcolor=ft.colors.BLUE,
    border_radius=3
)
no_ports = ft.Container(
    content=ft.Text("No Device Found"), 
    padding=5,
    bgcolor=ft.colors.RED,
    border_radius=3,
    alignment=ft.alignment.center
)

port_list = ft.ListView(padding=5, spacing=10, height=200, width=200)
port_menu = ft.Column([port_list_title, port_list],horizontal_alignment=ft.CrossAxisAlignment.CENTER)

# Loop for all available ports to find the button
def list_ports(page):
    for port, desc, _ in sorted(ports):
        if ("Bluetooth" not in "{}".format(desc)):
            print("{}".format(desc))
            button = ft.ElevatedButton(
                content=ft.Text("{}: {}".format(port, desc)),
                bgcolor=ft.colors.GREY_900,
                on_click=lambda _, port=port: assign_port(page, port),
            )
            port_list.controls.append(button)
    if len(port_list.controls) == 0:
        port_list.controls.append(no_ports)

    return port_menu

# Assigns the port from a button click
# The port will be passed as a string!!!
def assign_port(page, port):
    print(port)
    page.ser = serial.Serial(port, 9600)
    page.reader = serialtest.ReadLine(page.ser)
    page.out = page.reader.readline()
