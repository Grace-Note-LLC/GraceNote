**GraceNote Firmware**

- This subdirectory contains all of the embedded software that was developed for the GraceNote Project:

  (i) The 'basic_clicker' subdirectory containing the very first prototype for GraceNote. This module and accompanying firmware was primarily used by the software team for interfacing the microcontroller and the software application developed for the project.

  (ii) The 'keyboard' subdirectory containing the current firmware running on GraceNote. Using the Arduino Keyboard library, we were able to utilize the native USB interface of the ESP32S3 to allow GraceNote to function as a USB HID device. This greatly reduced button press latency and embedded software implementation.
