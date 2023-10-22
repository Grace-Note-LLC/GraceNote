import 'package:flutter/material.dart';
import 'package:flutter/widgets.dart';
import 'package:flutter_libserialport/flutter_libserialport.dart'; // Serial Port Lib

class ButtonTest extends StatelessWidget {
  int presses = 0;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        body: Column(
      children: [
        Center(
          child: Card(
            child: Padding(
              padding: const EdgeInsets.all(20),
              child: Text(presses.toString()),
            ),
          ),
        ),
      ],
    ));
  }
}
