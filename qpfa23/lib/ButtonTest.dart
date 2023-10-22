import 'dart:typed_data';

import 'package:flutter/material.dart';
import 'package:flutter_libserialport/flutter_libserialport.dart'; // Serial Port Lib

class ButtonTest extends StatefulWidget {
  int presses = 0;

  @override
  State<ButtonTest> createState() => _ButtonTestState();
}

class _ButtonTestState extends State<ButtonTest> {
  List<String> availablePorts = SerialPort.availablePorts;
  SerialPort mainPort = SerialPort("COM9");

  Future<void> readTest() async {
    for (var p in availablePorts) {
      if (p == "COM9") {
        print(p);
        List<int> d = [65, 84, 13];
        Uint8List bytes = Uint8List.fromList(d);
        SerialPort port = SerialPort(p);
        SerialPortReader reader = SerialPortReader(port, timeout: 10000);
        try {
          port.openReadWrite();
          print(port.write(bytes));
          await reader.stream.listen((data) {
            widget.presses++;
            print('received : $data');
          });
        } on SerialPortError catch (_, err) {
          if (port.isOpen) {
            port.close();
            print('serial port error');
          }
        }
      }
    }
  }

  @override
  Widget build(BuildContext context) {
    print(availablePorts);

    mainPort.openReadWrite();
    SerialPortReader reader = SerialPortReader(mainPort);
    try {
      print(mainPort);
    } on SerialPortError catch (err, _) {
      print(SerialPort.lastError);
    }

    reader.stream.listen(
      (data) {
        print(data);
        print(String.fromCharCodes(data));
        widget.presses++;
      },
    );

    return Scaffold(
      body: Center(
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.center,
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            Card(
              child: Padding(
                padding: const EdgeInsets.all(200),
                child: Text(
                  widget.presses.toString(),
                  style: const TextStyle(fontSize: 40),
                ),
              ),
            ),
            Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                FloatingActionButton(
                  onPressed: readTest,
                  child: const Icon(Icons.refresh),
                ),
                FloatingActionButton(
                  onPressed: () {
                    setState(() {
                      print("manual press");
                      widget.presses++;
                      print(widget.presses.toString());
                    });
                  },
                  child: const Icon(Icons.ac_unit),
                ),
                FloatingActionButton(
                  onPressed: () {
                    setState(() {
                      widget.presses = 0;
                    });
                  },
                  child: const Icon(Icons.adobe_rounded),
                )
              ],
            )
          ],
        ),
      ),
    );
  }
}
