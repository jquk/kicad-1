# Elektor Magazine's Article and Project on Regulated Voltage Battery Output: 
`https://www.elektormagazine.com/magazine/elektor-305/62009`

## Bill of Materials
Resistors (0805, 0.125 W):
Use Kicad's standard library.
- R1, R4 = 1 MΩ
- R2 = 604 kΩ, 1%
- R3 = 10 kΩ

Capacitors
Use Kicad's standard library.
- C1 = 4.7 µF, 50 V, X7R (0805)
- C2 = 22 µF, 10 V, X7R (1206)
- C3 = 10 pF, 50 V, X7R (0805)

Inductors
- L1 = 10 µH, 680 mA        --> Snapeda.com: `https://www.snapeda.com/parts/ASPI-0630LR-100M-T15/Abracon/view-part/?ref=search&t=abracon%20ASPI-0630LR-100M-T15&ab_test_case=b`

Semiconductors
- D1, D2 = SS14 (DO-214AC)  --> Snapeda.com: `https://www.snapeda.com/parts/SS14/ON/view-part/?ref=search&t=ss14&ab_test_case=b`
- IC1* = AP3015 or AP3015A  --> Snapeda.com: `https://www.snapeda.com/parts/AP3015AKTR-G1/Diodes%20Inc./view-part/?ref=search&t=AP3015AKTR-G1&ab_test_case=b`
- T1 = 2N7002 (SOT-23)      --> Standard Kicad library

Miscellaneous
- K1, K2, K3 = pin header, 1 row, 2 contacts, 2.54 mm pitch   --> Standard Kicad library
- K4 = pin header, 1 row, 2 contacts, right-angle, 2 mm pitch --> Standard Kicad library



## Description and Project Elements
`https://www.elektormagazine.com/labs/tiny-solar-supply`
Tiny Solar Supply
A tiny solar power supply similar to those found in garden lights, but with a voltage regulator.

Need a regulated voltage out of an AA(A) (rechargeable) battery? Then this tiny boost converter might just be what you are looking for.

We used to have two solar-powered garden light strings from Ikea lighting up our garden at night. They worked very well, but over the years the colorful lights slowly disintegrated until only the solar panels were left over. As these solar panels are well built, waterproof and all that, I decided to keep them to see if I couldn’t do something else with them.

During the day, the solar panel charges a single 1.2 V Ni-MH AA rechargeable battery. When it gets dark, charging stops, and a tiny boost converter switches on to pump up the battery voltage to something suitable for powering a string of white LEDs. This is nice, but unregulated as the output voltage depends on the load.

This little circuit turns the 1.2 V at its input into a regulated 3.3 V suitable for e.g. a microcontroller-based something. The schematic is attached below. The heart of the circuit is IC1, an AP3015 micro power step-up DC/DC converter from Diodes, Inc. Its A-version works with input voltages as low as 1 V (and up to 12 V) and can deliver 100 mA. The non-A version starts at 1.2 V but can supply up to 350 mA. The output voltage is determined by the ratio of R1 and R2:

VOUT = 1.23 × (1 + R1/R2)

With the given values, the output voltage is (almost) 3.3 V. L1, D1, and C1 to C3 are the recommended components needed to make the boost converter work. L1 can be one of those inductors that look like a resistor as long as it can pass at least the maximum load current.

When the solar panel (on K4) is getting light, it charges the battery (connected to K2) through diode D2. At the same time, it pulls the gate of T1 up. This makes T1 conduct, pulling the shutdown pin of IC1 low, turning it off. When the output voltage of the solar panel drops too low, battery charging stops, T1 switches off and IC1 switches on. If you don’t want this automatic switching, then leave T1 out. An On/Off switch or jumper connected to K3 gives you a bit more control over the circuit.

I designed a little PCB for the circuit that fits nicely inside the old Ikea solar panel. Today, this model is obsolete, but I am sure it will fit in other types too.

Design files are attached below.


