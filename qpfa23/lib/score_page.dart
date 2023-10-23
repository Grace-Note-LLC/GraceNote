import 'package:flutter/foundation.dart';
import 'package:flutter/material.dart';
import 'package:flutter_libserialport/flutter_libserialport.dart';

class ScorePage extends StatefulWidget {
  int presses = 0;

  @override
  State<ScorePage> createState() => _ScorePageState();
}

class _ScorePageState extends State<ScorePage> {
  SerialPort port = SerialPort('COM9');
  late SerialPortReader reader;

  @override
  void initState() {
    super.initState();
    var res = port.openRead();

    if (!res) {
      print('Error opening port:${port.name}');
      // handle to close reconnet
    }
    var portConfig = SerialPortConfig()
      ..baudRate = 9600
      ..bits = 8
      ..stopBits = 1;
    port.config = portConfig;

    reader = SerialPortReader(port);
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Center(
        child: StreamBuilder<Uint8List>(
          stream: reader.stream,
          builder: (context, snapshot) {
            if (snapshot.hasError) {
              return Text('Error: ${snapshot.error}');
            }
            if (snapshot.connectionState == ConnectionState.waiting) {
              return const Text('Awaiting result...');
            }

            var decodedString = String.fromCharCodes(snapshot.data!);
            print(decodedString);
            widget.presses++;
            return Column(
              mainAxisAlignment: MainAxisAlignment.center,
              children: <Widget>[
                const Text(
                  'Counter from Arduino:',
                ),
                Text(
                  widget.presses.toString(),
                  style: Theme.of(context).textTheme.headline1,
                ),
              ],
            );
          },
        ),
      ),
    );
  }

  @override
  void dispose() {
    port.close();
    super.dispose();
  }
}
