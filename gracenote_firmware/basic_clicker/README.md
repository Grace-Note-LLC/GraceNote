**Basic Clicker Subdirectory**

- This subdirectory contains all information relating to the basic clicker prototype and sketch for the GraceNote project:

  (i) This README explaining the code and hardware for the basic clicker.

  (ii) The 'basic_clicker.ino' Arduino code running on the device.

**Hardware and Software Explanation**

![IMG_2558](https://github.com/pink10000/qp-fall23/assets/121917210/7003af1e-9032-4ca5-8947-b61cbd8ef5f5)

- This device features an Arduino Nano development board soldered to a piece of perf board, along with a 7-segment display, 7-segment decoder IC and a push button.
- The device increments the 7-segment display each time the button is pressed and writes the current value of the 7-segment display to the host machine over serial.

Device Components:

	- 1x Arduino Nano 33IoT (top right) for reading button input and communicating with the host computer.

	- 1x NE555 timer (top left) for switch debouncing.

	- 1x 7-segment display (left) that increments at the falling edge of the switch signal.

	- 1x Blue LED (middle) that is on while the button is being pushed, off when otherwise.

	- 1x Push button (bottom left) for user input.

	- 1x 74LS47N integrated circuit (bottom middle) for controlling the 7-segment display.
