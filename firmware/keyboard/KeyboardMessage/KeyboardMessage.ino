/*
  Keyboard Message test

  For the Arduino Leonardo and Micro.

  Sends a text string when a button is pressed.

  The circuit:
  - pushbutton attached from pin 0 to ground
  - 10 kilohm resistor attached from pin 0 to +5V

  created 24 Oct 2011
  modified 27 Mar 2012
  by Tom Igoe
  modified 11 Nov 2013
  by Scott Fitzgerald

  This example code is in the public domain.

  http://www.arduino.cc/en/Tutorial/KeyboardMessage
*/
#ifndef ARDUINO_USB_MODE
#error This ESP32 SoC has no Native USB interface
#elif ARDUINO_USB_MODE == 1
#warning This sketch should be used when USB is in OTG mode
void setup(){}
void loop(){}
#else

#include "USB.h"
#include "USBHIDKeyboard.h"
#include "logo.h"

USBHIDKeyboard Keyboard;

//                 L    ML  MR    R    
char mapping[] = {'A', 'B', 'C', 'D'};

// DEFINE SENSOR GPIO PINS HERE
int leftPin = 4;
int midLeftPin = 3;
int midRightPin = 2;
int rightPin = 1;

void setup() {
  // make the pushButton pin an input:
  pinMode(leftPin, INPUT);
  pinMode(midLeftPin, INPUT);
  pinMode(midRightPin, INPUT);
  pinMode(rightPin, INPUT);

  
  // initialize control over the keyboard:
  Serial.begin(2000000);
  Keyboard.begin();
  USB.begin();
}

//                 R    MR  ML    L
int prevVals[] = {LOW, LOW, LOW, LOW};

bool initialized = false;

/**
 * @brief Read from each pin's sensor. If sensor value is changed from previous and high, Keyboard.press the corresponding char from the mapping array.
 * Likewise if sensor value has changed to low from high, Keyboard.release the corresponding char.
 */
void loop() {
  // Check for config setting in serial port. Each of the 5 characters is separated by a tilde (~) e.g. "A~B~C~D~E"
  while (!initialized) {
    String s = Serial.readString();

    // check that config message has been sent
    if (s.length() > 0) {
      s.trim();
    
      int index = 0;  // Index for the result array
      int start = 0;  // Start index for each substring
    
      for (int i = 0; i < s.length(); i++) {
        if (s.charAt(i) == '~') {
          // Found a delimiter, extract the substring and store it in the result array
          mapping[index] = s.substring(start, i).charAt(0);
          index++;
          start = i + 1;  // Update the start index for the next substring
        }
      }
    
      // Extract the last substring after the last delimiter
      mapping[index] = s.substring(start).charAt(0);

      initialized = true;
    }
  }

  
  // Left-most pin
  int val = digitalRead(leftPin);
  if ((prevVals[0] != val) && (val == HIGH)) {
    Keyboard.press(mapping[0]);
  } else if ((prevVals[0] != val) && (val == LOW)) {
    Keyboard.release(mapping[0]);
  }
  prevVals[0] = val;


  // Middle-left pin
  val = digitalRead(midLeftPin);
  if ((prevVals[1] != val) && (val == HIGH)) {
    Keyboard.press(mapping[1]);
  } else if ((prevVals[1] != val) && (val == LOW)) {
    Keyboard.release(mapping[1]);
  }
  prevVals[1] = val;


  // Middle-right pin
  val = digitalRead(midRightPin);
  if ((prevVals[2] != val) && (val == HIGH)) {
    Keyboard.press(mapping[2]);
  } else if ((prevVals[2] != val) && (val == LOW)) {
    Keyboard.release(mapping[2]);
  }
  prevVals[2] = val;


  // Right-most pin
  val = digitalRead(rightPin);
  if ((prevVals[3] != val) && (val == HIGH)) {
    Keyboard.press(mapping[3]);
  } else if ((prevVals[3] != val) && (val == LOW)) {
    Keyboard.release(mapping[3]);
  }
  prevVals[3] = val;
}
#endif /* ARDUINO_USB_MODE */
