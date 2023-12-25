**Altium Subdirectory for Custom ESP32-S3 Board**

- This subdirectory contains all design, schematic, and custom library files used for the GraceNote ESP32-S3 board:

	(i) The 'esp32s3_wroom.PcbLib' custom footprint library containing footprints for the components used in the board (more on this below).

	(ii) The 'esp32s3_wroom.SchLib' custom schematic library containing symbols for the components used in the board (more on this below).

	(iii) The 'gerb.zip' folder containing the gerber files for the board.

	(iv) The 'gracenoteESP_PCB.pdf' PDF file showing the top and bottom signal layers of the board.

	(v) The 'gracenoteESP_schematic.pdf' PDF file showing the schematic for the board.

**Custom Symbol and Footprint Libraries**

- As previously mentioned, some of the components that were ordered for the board did not have readily available schematic symbols or PCB footprints. Using the datasheets of these components, the 'esp32s3_wroom.PcbLib' and 'esp32s3_wroom.SchLib' files collectively provide:

	(i) Schematic symbol and PCB footprint for TRANS NPN 25V 0.8A SOT23-3, Part Number: KSC3265YMTF

 	(ii) Schematic symbol and PCB footprint for LED ORANGE CLEAR SMD, Part Number: LTST-C191KFKT

  	(iii) Schematic symbol and PCB footprint for RF TXRX MOD BLUETOOTH U.FL SMD, Part Number: ESP32-S3-WROOM-1U-N8

	(iv) Schematic symbol and PCB footprint for TVS DIODE 5VWM 18.6VC SOD523, Part Number: ESD5V0D5-TP

	(v) Schematic symvol and PCB footprint for SWITCH TACTILE SPST-NO 0.05A 16V, Part Number: PTS810 SJK 250 SMTR LFS

	(vi) Schematic symbol and PCB footprint for RES 22.1K OHM 1% 1/10W 0603, Part Number: RC0603FR-1022K1L

	(vii) Schematic symbol and PCB footprint for RES 47.5K OHM 1% 1/10W 0603, Part Number: RC0603FR-0747K5L

	(viii) Schematic symbol and PCB footprint for CAP CER 10UF 25V X5R 1206, Part Number: CC1206MKX5R8BB106 
