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
port_list = ft.ListView(padding=5, spacing=10, height=200, width=200)
port_menu = ft.Column([port_list_title, port_list],horizontal_alignment=ft.CrossAxisAlignment.CENTER)

def list_ports():
    for port, desc, _ in sorted(ports):
        # print("{}: {}".format(port, desc))
        button = ft.ElevatedButton(
            content=ft.Text("{}".format(port)),
            bgcolor=ft.colors.GREY_900,
            #alignment=ft.alignment.center, # (this gives me wackiest error)
            on_click=lambda _, port=port: assign_port(port),
        )
        port_list.controls.append(button)
    return port_menu

# Assigns the port from a button click
# The port will be passed as a string!!!
def assign_port(port):
    print(port)
    ser = serial.Serial(port, 9600)
    reader = serialtest.ReadLine(ser)
    out = reader.readline()
