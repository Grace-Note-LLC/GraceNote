**ATMega328P-AU Board**

- This subdirectory contains all documentation related to the custom ATMega328p-AU board developed for the GraceNote project:

  (i) This README explaining why we chose the ATMega328p-AU MCU and how the board works.

  (ii) The 'altium' subdirectory containing all files related to the PCB design (schematic sheets, pcb sheet, etc.)

  (iii) The 'GraceNote BOMs - Sheet1.csv' csv file containing the bill of materials for the board.

**Why we Chose the ATMega328p-AU Chip**

- We chose the ATMega328p-AU chip because it is cheap, has enough ports and peripherals to support our project, and it is the same chip used by the module that we used for prototyping: the Arduino Nano development board.
- Prior to us using the native USB interface with the ESP32S3 chip for our final product, we utilized the pin change interrupt (PCINT) ports on the ATMega328p-AU since it has many pins that support this.

**Board Pictures and Features**

![3a_a](https://github.com/pink10000/GraceNote/assets/121917210/2c8ca7ba-1779-4cb4-9e09-138cf1c7df37)

Above is a 3D CAD view of the top of the board taken inside Altium Designer.

![aaa](https://github.com/pink10000/GraceNote/assets/121917210/ad981fe8-b180-457c-b34a-c63377d50234)

Above is a 3D CAD view of the bottom of the board taken inside Altium Designer.

Board features:

  - ATMega328p-AU microcontroller for reading sensor data and communicating with the host machine.
  - FTDI chip allowing for flashing firmware to the board and monitoring serial data.
  - 5x AT42QT1010 capacitive touch sensor ICs for registering touches. One for each of the large solder pads at the edges of the board.
  - Various LEDs, capactive components, and a crystal oscillator for the chip.
