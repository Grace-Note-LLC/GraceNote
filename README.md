# \<insert project name> - QP Fall 2023 Team 6

## High-level Concept
We will be making a serial device that is intended for use in musical applications. Similar to a Guitar Hero guitar, or an Osu tablet/pen, we are hoping to make a device that can bring a fun, handy new tool to the genre of rhythm games. The device will have 5 independent "pads", with one for each finger. When the user touches one of their fingers to a pad, it will send some serial message to the computer which can be interpreted as a button press. This could be applied directly to rhythm games such as _Osu! Mania_ or _Guitar Hero_, or it could be treated as if it were its own instrument - the choice is up to the user!

## Technical Details

### Hardware:
The primary interaction between the user and the device will be via individual capacitive touch sensors (or soft potentiometers, we haven't entirely decided yet). When the user makes contact with one of the sensors, the signal will be picked up by an Arduino (or other MCU, we haven't decided yet) which will then encode the signal into some number to be passed over the serial connection and then interpreted by the software.

#### Other ideas that we could choose to implement:
- Make our own board that integrates an MCU (as opposed to buying an off the shelf development board like an Arduino Uno)
  - We need to account for the factory's shipping and production time (given that our budget is around $50 max)
- Make the device work wirelessly
  - This would likely introduce significant latency issues, especially because the intended application is for rhythm games. Therefore, if we were to do this we would not use Bluetooth but instead send an analog signal via a wireless transmitter/receiver pair (like what real wireless guitars use).

### Software:

At the very least, we would like to make our device work as an "instrument" in multiple rhythm games (e.g. Osu! mania and Guitar Hero). Since this is a relatively small scope, it would also be great to have an app that works as an interface for the device, allowing the user to visualize all the connections and ensure everything is working as expected. Perhaps we could add customization/configuration settings, so that the app would function similar to something like Razer Synapse. This will done in a Flutter app, so that it can work on both mobile and PC devices.

If possible, the software should make it so that the user workflow is as simple as the following:

1. User plugs in device
2. User opens rhythm game (e.g. Osu! mania)
3. User selects some setting in the game to replace the default input with our device
4. User is able to play the game normally, using the device as input instead of the default/intended instrument.
5. Optionally, the user can open the interface app, which will show which pads are being pressed and potentially allow for configuration settings.

#### Other implementation ideas:
- Make our own rhythm game built around the device
  - This would take a lot of effort, and should only be done if we are confident that we can make something polished.
  - A very simple alternative to this would be to have a reaction time game that, after a random amount of time, will display a pad number to press. When the user presses the correct pad, it will show the amount of time that it took for them to press the button.
- In the interface app, we could have a button to "Test Connection", which would prompt the user to press each button and check internally if the corresponding signal was received properly.