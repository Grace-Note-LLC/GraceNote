**ESP32 S3 Board**

- This subdirectory contains all documentation related to the custom ESP32S3 board developed for the GraceNote project:

	(i) This README including an explanation as to why we chose the ESP32S3 MCU and how the board works.
	(ii) The 'altium' subdirectory including all files related to the PCB design (schematic files, pcb files, custom symbol and footprint libraries).

**Why we Chose the ESP32S3 Chip**

- We chose the ESP32S3 chip for the same reason we originally chose the ATMega328P-AU. We wanted a low cost MCU capable of reading from our capactive touch sensors and communicating with a user's host machine running our software application.
- The big difference between the S3 and the ATMega is that the S3 chip supports native USB communication. This allows us to use our product as a USB HID device that a user can easily plug into their machine and play.
- The native USB on the S3 also greatly simplified embedded software implementation and offers reduced button press latency. 

**Board Pictures and Features**

INSERT PICTURE

This is a 3D CAD view of the top of the board taken inside Altium Designer.

Board Features:

	- 1x ESP32-S3-WROOM-1U-N8 Microcontroller (top right) for reading data from external capacitive touch sensors and communicating with host machine running our software application.
	- 1x CP2102N-A02-GQFN28 USB-UART Bridge for converting USB data from the host machine to UART for flashing firmware to the MCU.
	- 1x 3.3V Linear Regulator for stepping down the 5V from the USB connection(s) to the logic level used by the MCU.
	- 2x Micro USB connectors for interfacing with a host machine. One of them is for UART to flash firmware to the chip and monitor serial data, the other is for using the MCU's native USB functionality.
	- Various LEDs and passive components (Power and TX/RX LEDs, decoupling capacitors, voltage dividers, etc).
