---
layout: article
title:  "Audio Electronics Gallery"
date:   2019-06-01 08:59:25 +0000
categories: music
comments: True
image:
  teaser: music/FromWithinSpec_teaser.png
  feature: music/Spectrogram_310319.png
---

#### Valve Amplifiers

###### Chasm #1

A high gain, ~20 W guitar amplifier head designed for versatility and excellent tone. Built in 2009, still in occasional use.

![Chasm #1](/images/music/Chasm1_EDITED.png)
*Chasm #1*

As a teenager with a need for tone but no budget, I treated my A Level design project as an excuse to build this machine. While my teacher was more interested in the funny-shaped, laminated plywood box, I spent months tinkering and tweaking the circuit, honing the sounds it could produce. At university, this was my primary amp: light enough to carry, loud enough to play with a drummer, and tonally rich and diverse, this project was a huge success, and I learn a massive amount from the build.

![Chasm #1](/images/music/Chasm1_chassis.JPG)
*Chasm #1 Chassis*

The chassis was bent from aluminium. Atop sit three 12ax7 and two el84 valves, and two very nice purpose-made transformers. On the front panel are the power switches; guitar input; volume, gain, and tone controls; a 'clean' switch to bypass part of the preamp circuitry; and preamp-out and power-amp-in jacks. These were added later for silent recording, very useful as a student in a shared house. I often recorded using the preamp out, directly into a DAW using convolution cabinet modelling.

![Chasm #1](/images/music/Chasm1_gutshot.JPG)
*Chasm #1 Gutshot*

The guts of the machine. The power supply board (acid etched 'PCB') is on the right, amplifier board (turret construction) on the left. The tone stack is built point-to-point onto the tone controls, lower edge of the picture. The circuit saw drastic modifications after the initial construction, hence the layout is not ideal.

![Chasm #1](/images/music/SCAN0002.JPG)
*Chasm #1 Power Amp Schematic (Preamp/power supply schematics not shown.)*

The circuit was based on a number of existing amplifiers and elements were borrowed from many sources. Particular inspiration came from Marshall, Soldano, and Mesa Boogie amplifiers, and I learned and borrowed a huge amount from the online DIY community. (Preamp/power supply schematics not shown.)

The signal path consists of:
- Four cascaded triode gain stages, gain control after the first. The 'clean' switch bypasses the latter two stages. I carefully balanced the circuit gain between successive stages, to give a smooth and relatively symmetrical overdriven sound.
- A conventional treble/middle/bass tone stack (filter section) followed by a master volume control. I have omitted the buffer stage usually found before the tone stacks of similar amplifiers, as my experiments suggested it was not necessary. This freed up a triode, allowing the fourth gain stage.
- A 'long tailed pair' phase inverter driving the output valves in push-pull, class AB configuration for about 20 Watts.


###### Chasm #2

Chasm #2 is a full valve guitar preamplifier built into a highly portable 1U rack case. It has a flexible gain architecture, and switchable twin tone stacks, making it extremely versatile.

![Chasm #2](/images/music/Chasm2_EDITED.png)
*Chasm #2*

I generally use this preamp either directly into a DAW with convolution cabinet simulation, for silent practice and recording, or plugged into the power section of another guitar amp, most often my Marshall JCM900 combo. It has a smooth and saturated sound, with a lot of character and good response to playing dynamics.

![Chasm #2](/images/music/SCAN0001.JPG)
*Chasm #2 Schematic*

While Chasm #1 took hours of tweaking before it started to even sound like a guitar amplifier, Chasm #2 worked the very first time I plugged it in, and sounded more or less exactly as i'd intended. With the benefit of all that i'd learnt previously, I was able to get the design of Chasm #2 pretty spot-on. I took some inspiration from Sunn and Orange amplifiers in search of bigger, thicker tones, but the design was largely based off my experience with Chasm #1.

The circuit is built into an old 1U rack case, and uses turret board construction, with point-to-point tone stacks built onto the tone controls, like Chasm #1. It uses three 12ax7 valves. After some experimentation, I settled on a beautiful vintage Sylvania valve for the first stages.

Controls include two gain controls, at two stages through the preamp, to give some control over the character of overdriven sound; and two switchable tone stacks: a conventional treble/middle/bass circuit, and a much more flexible passive James tone circuit, more commonly found in hifi amplifiers.

The signal path consists of four cascaded stages, the first of which is a parallel pair, followed by a cathode follower stage driving the tone stacks.

#### Effects Pedals

Over the years I have built many effects pedals. Some for me, some for friends. Some clones of existing circuits, some my own designs, many somewhere in between. Some on homemade PCBs, many on veroboard or perfboard. Mostly fuzzes, overdrives, buffers, and filters. Many have been gigged. Most have been reliable. Some worked first time, some didn't.

![GeFuzz](/images/music/IMG_5441.JPG)
*A simple Germanium fuzz (built 2019 for a friend)*

![VMT](/images/music/IMG-20170529-WA0000.jpg)
*A complex overdrive, inside-out on the debugging bench (built 2017)*


![Collection](/images/music/IMG_3020.JPG)
*A few old builds. Pity I never got into painting the boxes.*

The image above shows, clockwise from top-left:
- Modified Ibanez Tubescreamer overdrive, built ~2008. My first acid-etched PCB. It's still being gigged by another member of the band.
- Simple buffer pedal, built into a tupperware tin. My first pedal build.
- fOXX Tone Machine clone, a gorgeous-sounding octave fuzz circuit from the early '70s.
- A buffered, transformer isolated A/B/Y box of my own design.

![TM_TS_gutshots](/images/music/IMG_3023.JPG)
*The guts of my Tubescreamer and Tone Machine*

My current pedalboard, as of mid-2019, has three of my own builds: a bass overdrive clone, a Tone Machine octave fuzz clone, and a modified super heavy doom fuzz. I also have a tuner and a delay on the board.

#### Other
