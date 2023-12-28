Basic Clicker 

Use this device by pushing the button located in the bottom left. Pushing this button will cause the Arduino Nano 33IoT to write a '1' over the serial communication port with the host computer. 

![IMG_2558](https://github.com/pink10000/qp-fall23/assets/121917210/7003af1e-9032-4ca5-8947-b61cbd8ef5f5)


Device Components:

	- 1x Arduino Nano 33IoT (top right) for reading button input and communicating with the host computer.

	- 1x NE555 timer (top left) for switch debouncing.

	- 1x 7-segment display (left) that increments at the falling edge of the switch signal.

	- 1x Blue LED (middle) that is on while the button is being pushed, off when otherwise.

	- 1x Push button (bottom left) for user input.

	- 1x 74LS47N integrated circuit (bottom middle) for controlling the 7-segment display.