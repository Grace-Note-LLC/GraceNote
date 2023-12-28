**GraceNote Hardware Subdirectory**

- This subdirectory contains all documentation related to the hardware design, testing, and analysis for the Gracenote project:

  (i) This README explaining the hardware developed for the project along with the evolution of the hardware design for the project.

  (ii) The 'atmega328_board' subdirectory containing documentation for the board developed around the ATMega328p-AU microcontroller for the project.

  (iii) The 'esp32s3_board' subdirectory containing documentation for the board developed around the ESP32S3 microcontroller for the project.

**GraceNote Hardware Evolution**

***Initial Prototype and Hardware Design***

*Picture: Initial Prototype - 5 Capacitive Touch Sensors with Arduino Nano Development Board*

![3a_a](https://github.com/pink10000/GraceNote/assets/121917210/30b4f77e-2f20-4c2a-a0d7-5d577dd7dcce)

- This is the initial prototype for our project.
- At the center of this design is the Arduino Nano development board. In this picture, it is soldered to a perf board with connecting terminals for the 5 capacitive touch sensors.
- The 3D model for the enclosure is designed so the device can be flipped over for use by left or right handed individuals, and intended to be as ergonomic as possible.

*Picture: Initial Hardware Design - Custom PCB with Integrated ATMega328p-AU Microcontroller, AT42QT1010 Touch Sensor ICs, and Capacitive Touch Pads*

![3a_a](https://github.com/pink10000/GraceNote/assets/121917210/2c8ca7ba-1779-4cb4-9e09-138cf1c7df37)

- This is a picture of the top view of the hardware design for the board based on the first prototype.
- The board features an ATMega328p-AU 8-bit microcontroller, the same as the Arduino Nano, as well as the 5 capcitive touch ICs used with the Nano prototype.
- The goal with the hardware design was to merge all of the components from the prototype (microcontroller and touch sensors) onto one board so that we are only using as many components as we need to save space.
- This design was ordered online through a PCB manufacturing company. For this design, we ordered a full assembly service, which ended up being quite costly. There were also some small mistakes that were made within the schematic and PCB design that will be discussed in the section below.
- All documentation for this board is located in the 'atmega328p_board' subdirectory.

**Problems With the Original Prototype and Design**
- The first problem with the design was ergonomics and usability. As mentioned in the home page, our goal with GraceNote was to make a device used for playing rythm games more comfortably and with better control. After testing our first design, the device was difficult to use and was very uncomfortable for the user. This is because the device didn't fit the hand size of some users, and the 3D model itself left much to be desired.
- The second problem was latency. For this first design, we used the pin change interrupt (PCINT) ports on the ATMega328p-AU microcontroller for interfacing with our capacitive touch sensors. When a button was pressed, it would trigger a pin change interrupt and the MCU would write a message over serial to be processed by our software application. We noticed that the latency with this message was rather high (roughly 200ms) which would render the device unusable for the majority of rythm games.
- Thirdly was embedded software implementation. As mentioned previously, we used the PCINT ports on the ATMega processor to interface with the sensors. Implementing this in code was not so simple, as it involved reading from and writing directly to the registers on the MCU, which seemed a bit unneccessary for this application.
- Finally was an issue within the PCB design itself. Unbeknownst to the GraceNote hardware engineering team, ordering a fresh ATMega chip from the factory isn't as simple as plugging it in and flashing code with the Arduino IDE. First, we have to burn a bootloader onto the chip, which requires that the SPI lines be reasonably accessible, and they were not.

***Final Prototype and Hardware Design***

*Final Prototype (Presented at UCSD IEEE Quarter Project Showcase) - 4 Capacitive Touch Sensors with ESP32S2 Development Board*

![3a_a](https://github.com/pink10000/GraceNote/assets/121917210/517f9084-b381-4e42-93b0-438052601c70)

- This prototype features an ESP32S2 development board at the center, again soldered to a piece of perf board with connecting terminals for the touch sensors.
- This design now utilizes 4 touch sensors. This is much more practical since there were many rythm games, both available online and for purchase, requiring either 4 or less buttons to play.
- This design is also much more ergonomic since it closely resembled a keyboard, and the touch sensors for this design are spaced out to make it easier to use.
- The choice for this exact board was because it supports native USB, allowing us to use our device as a USB HID device, simplifying embedded software implementation and greatly reducing latency.
- This design was showcased at the UCSD IEEE Quarterly Project Showcase in early December 2023, where we won the 'Best Demo' title.

*Final Hardware Design - Custom PCB with Integrated ESP32S3 Microcontroller, Breakout for Interfacing with Capacitive Touch Sensors and LEDs* 

![3a_a](https://github.com/pink10000/GraceNote/assets/121917210/f9c2f3a8-0c66-44c9-9e0b-44a50a75554d)

- Similar to the first hardware design, the goal of the hardware design for the second version was to reduce the size of this device by eliminating all unneccessary connections and interfaces.
- This design is centered around the ESP32S3 microcontroller, and features all necessary components to get the board working along with our necessary interfaces (UART, Native USB, Interrupt and Output Pins).
- Unlike the first hardware design that was ordered with full assembly, we cut costs with this design by ordering the parts and the board individually and assembling the board ourselves.
- All documentation for this design is located in the 'esp32s3_board' subdirectory.
