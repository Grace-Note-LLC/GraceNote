**ESP32 S3 Board**

- This subdirectory contains all documentation related to the custom ESP32S3 board developed for the GraceNote project:

	(i) This README including an explanation as to why we chose the ESP32S3 MCU and how the board works.

	(ii) The 'altium' subdirectory including all files related to the PCB design (schematic files, pcb files, custom symbol and footprint libraries).

	(iii) The 'GraceNote BOMs - Sheet1.csv' csv file containing the bill of materials for the board.

**Why we Chose the ESP32S3 Chip**

- We chose the ESP32S3 chip for the same reason we originally chose the ATMega328P-AU. We wanted a low cost MCU capable of reading from our capactive touch sensors and communicating with a user's host machine running our software application.
- The big difference between the S3 and the ATMega is that the S3 chip supports native USB communication. This allows us to use our product as a USB HID device that a user can easily plug into their machine and play.
- The native USB on the S3 also greatly simplified embedded software implementation and offers reduced button press latency. 

**Board Pictures and Features**

![3a_a](https://github.com/pink10000/GraceNote/assets/121917210/f9c2f3a8-0c66-44c9-9e0b-44a50a75554d)


Above is a 3D CAD view of the top of the board taken inside Altium Designer.

![aaa](https://github.com/pink10000/GraceNote/assets/121917210/84de3a79-7e34-4a60-8732-f87869e079a2)

Above is a 3D CAD view of the bottom of the board taken inside Altium Designer.


Board Features:

	- 1x ESP32-S3-WROOM-1U-N8 Microcontroller (top right) for reading data from external capacitive touch sensors and communicating with host machine running our software application.
	- 1x CP2102N-A02-GQFN28 USB-UART Bridge (top left) for converting USB data from the host machine to UART for flashing firmware to the MCU.
	- 1x 3.3V Linear Regulator (middle bottom) for stepping down the 5V from the USB connection(s) to the logic level used by the MCU.
	- 2x Micro USB connectors (far left on bottom view) for interfacing with a host machine. One of them is for UART to flash firmware to the chip and monitor serial data, the other is for using the MCU's native USB functionality.
	- Various LEDs and passive components (Power and TX/RX LEDs, decoupling capacitors, voltage dividers, etc).

Many of the components used in the design do not have any symbols, footprints, or 3D models available in Altium, which is why many of the components in the top view picture appear to be missing. We used the datasheets of these components to develop the symbols and footprints to include in the design. All components were hand soldered to the board.
