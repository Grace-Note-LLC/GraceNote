# Grace Note - QP Fall 2023 Team 6 Spec Sheet

## High-level Explanation
Grace Note is a USB serial device that is intended for use in musical applications, built off of the ESP32-S2 microprocessor. Similar to a Guitar Hero guitar, or an Osu tablet/pen, we are hoping to make a device that can bring a fun, handy new tool to the genre of rhythm games. The physical device has 4 independent "pads", each intended for use with 1 finger. When the user touches one of their fingers to a pad, it will send a key press (like from a keyboard) to the computer. The exact key that is sent can be configured by the user with our multi-platform companion app (created using Flet) on the device of their choosing. This could be applied directly to rhythm games such as _Osu! Mania_ or _Guitar Hero_, or it could be treated as if it were its own instrument - the choice is up to the user!

## Technical Details

### Hardware:
The primary interaction between the user and the device will be via individual capacitive touch sensors. When the user makes contact with one of the sensors, the signal will be picked up by an ESP32-S2 which will then encode the signal into some number to be passed over the serial connection and then interpreted by the software.

### Software:

In addition to the physical device, we made a companion app that allows users to connect it to their computer and configure which keys the touch sensors correspond to when pressed. This was accomplished using Flet, a Python wrapper for Flutter. This app is comparable to something like Razer Synapse, which allows Razer product users to configure their hardware devices and test them out.

Expected User Workflow:
1. User plugs in device
2. User opens rhythm game (e.g. Osu! mania)
3. User selects some setting in the game to replace the default input with our device
4. User is able to play the game normally, using the device as input instead of the default/intended instrument.
5. Optionally, the user can open the interface app, which will show which pads are being pressed and potentially allow for configuration settings.

Compatibility:
1. Windows
2. Linux
3. Android Devices 4.4+
4. macOS
5. Smart TVs
6. Android Watches
7. Refrigerators (YES REALLY!)

## Ideas for future implementation:
- Make our own rhythm game built around the device
  - This would take a lot of effort, and should only be done if we are confident that we can make something polished.
  - A very simple alternative to this would be to have a reaction time game that, after a random amount of time, will display a pad number to press. When the user presses the correct pad, it will show the amount of time that it took for them to press the button.
- In the interface app, we could have a button to "Test Connection", which would prompt the user to press each button and check internally if the corresponding signal was received properly.
- Make our own board that integrates an MCU (as opposed to buying an off the shelf development board like an Arduino Uno)
  - We need to account for the factory's shipping and production time (given that our budget is around $50 max)
- Make the device work wirelessly
  - This would likely introduce significant latency issues, especially because the intended application is for rhythm games. Therefore, if we were to do this we would not use Bluetooth but instead send an analog signal via a wireless transmitter/receiver pair (like what real wireless guitars use).
