## 5. The Computer

## Key Points

#### 1. ⌨️ Keyboard Layouts and Text Entry  
- QWERTY layout was designed to prevent typewriter jams, not for typing speed.  
- Dvorak layout improves typing speed by 10-15% and reduces fatigue by placing common letters under dominant fingers and alternating hands.  
- Alternative keyboard layouts (alphabetic, chord keyboards) exist but face social resistance.  
- T9 predictive text allows typing on numeric phone pads by guessing words from key sequences.  
- Handwriting recognition captures stroke path, pressure, and segments joined letters but struggles with handwriting variability.  
- Speech recognition works best with single users, initial training, and limited vocabularies; noise and pronunciation affect accuracy.

#### 2. 🖱️ Pointing Devices  
- The mouse detects relative movement in the (x, z) plane and moves the cursor in the (x, y) plane.  
- Mechanical mice use a rolling ball and potentiometers; optical mice use LEDs and light reflection.  
- Touchpads are small, touch-sensitive tablets mainly used on laptops, requiring good acceleration settings for speed and accuracy.  
- Trackballs rotate a ball inside a static housing to move the cursor; often used in gaming and portable devices.  
- Joysticks provide velocity-based movement control, commonly used in games and 3D navigation.  
- Touchscreens detect finger or stylus contact by interrupting light beams, capacitance changes, or ultrasonic reflections.  
- Eyegaze systems track eye direction using low-power lasers reflected off the retina for hands-free control.

#### 3. 🖥️ Display Technologies  
- Bitmap screens display images as a grid of pixels; resolution is measured in pixels (width x height) and pixel density in dpi.  
- Aspect ratios are commonly 4:3 or 16:9 (widescreen).  
- Color depth defines the number of colors per pixel, ranging from black/white to millions of colors using 8 bits per RGB channel.  
- CRT monitors use electron beams to excite phosphor-coated screens; LCDs use polarized light passing through liquid crystals controlled by voltage.  
- Digital paper uses electronically updated flexible sheets that retain images without power.  
- VR headsets provide stereoscopic 3D by showing slightly different images to each eye and track head motion for immersion.

#### 4. 💾 Memory and Processing  
- RAM is temporary, fast memory; permanent storage includes hard drives and solid-state drives.  
- Processor speed affects responsiveness; Moore’s Law states processor speed doubles approximately every 18 months, memory capacity every 12 months.  
- Performance bottlenecks include computation bound (slow processing), storage channel bound (slow data transfer), graphics bound (display updates), and network capacity limits.

#### 5. 🖨️ Printing and Scanning  
- Printers create images from dots; resolution measured in dpi, speed in pages per minute.  
- Dot-matrix printers use pins striking an inked ribbon (~80-120 dpi).  
- Inkjet printers spray tiny ink droplets (~300 dpi or better).  
- Laser printers use electrostatic charges and toner powder (~600 dpi or better).  
- Fonts vary by style, size (points), pitch (fixed or variable width), and serif or sans-serif design.  
- Page Description Languages (e.g., PostScript) describe complex pages for printing efficiently.  
- Scanners convert paper to bitmaps; OCR software converts scanned images back to editable text but struggles with complex layouts.  
- Compression can be lossless (ZIP, GIF) or lossy (JPEG, MP3), balancing file size and quality.

#### 6. 🌐 Networks and Interactive Performance  
- Network speed affects interactive performance when computers share resources.  
- Slow networks can cause delays in user interface responsiveness.



<br>

## Study Notes

*Based on Lecture 3: The Computer*


### 1. 🖥️ Introduction to Computer Systems and Interaction

A **computer system** is made up of many different parts, each playing a role in how we interact with it. To understand how humans and computers work together (Human-Computer Interaction or HCI), we need to know what these parts are and how they function.

At its core, a computer system includes:

- **Input devices**: Tools we use to send information into the computer (e.g., keyboards, mice, scanners).
- **Output devices**: Ways the computer shows us information (e.g., screens, printers, speakers).
- **Memory**: Where the computer stores data temporarily (RAM) or permanently (hard drives).
- **Processing**: The computer’s ability to perform calculations and run programs.
- **Networks**: Connections between computers that allow sharing of data and resources.

Understanding these elements helps us design better ways for people to interact with computers, making the experience smoother, faster, and more natural.


### 2. ⌨️ Input Devices: How We Tell Computers What to Do

Input devices are the tools we use to communicate with computers. They convert our actions—typing, pointing, speaking—into signals the computer can understand.

#### Text Entry Devices

- **Keyboards** are the most common text input devices. They send a character code every time a key is pressed.
- The **QWERTY layout** is the standard keyboard design, originally created to prevent typewriter jams, not for typing speed. Despite this, it remains dominant because so many people are used to it.
- Alternative layouts like **Dvorak** aim to increase typing speed and reduce fatigue by placing common letters under the strongest fingers and alternating hands. However, social resistance keeps QWERTY dominant.
- Special keyboards exist for specific needs, such as ergonomic designs to reduce repetitive strain injury (RSI) or one-handed keyboards like the Maltron.

#### Other Text Input Methods

- **Chord keyboards** use combinations of a few keys pressed simultaneously to represent letters. They are compact and fast once learned but have a steep learning curve and limited adoption.
- **Phone pads and T9 predictive text** allow typing on numeric keypads by pressing keys multiple times or using a dictionary to guess words, making texting faster on phones.
- **Handwriting recognition** lets users write naturally with a pen or stylus on tablets. The computer must interpret strokes, segment joined letters, and handle different handwriting styles, which is technically challenging.
- **Speech recognition** is improving, especially for single users with limited vocabularies and initial training. Challenges include background noise, pronunciation differences, and large vocabularies.

#### Pointing and Positioning Devices

- The **mouse** is a handheld device that moves a cursor on the screen. It detects relative movement (how far it moves) rather than absolute position. It usually has 1-3 buttons for selecting or interacting with objects.
- **Mechanical mice** use a rolling ball to detect movement, while **optical mice** use light sensors, which are cleaner and more reliable.
- **Touchpads** are small, flat surfaces (common on laptops) where finger movement controls the cursor. They require good sensitivity settings to balance speed and accuracy.
- **Trackballs** are like upside-down mice with a ball you roll with your fingers. They are precise and often used in gaming or portable devices.
- **Joysticks** and **keyboard nipples** (miniature joysticks on keyboards) provide directional control, often used in gaming or 3D navigation.
- **Touchscreens** detect finger or stylus contact directly on the display, allowing fast and intuitive interaction but can be imprecise for small targets.
- **Stylus and light pens** allow direct drawing or pointing on screens but can obscure the view.
- **Eyegaze systems** track where you look to control the computer, useful for hands-free control but require specialized hardware.


### 3. 🖥️ Output Devices: How Computers Show Us Information

Output devices display or present information from the computer to the user.

#### Screens and Displays

- **Bitmap screens** (like CRT and LCD monitors) display images as a grid of tiny dots called pixels.
- **Resolution** refers to the number of pixels on the screen (e.g., 1024x768). Higher resolution means more detail.
- **Pixel density** (dots per inch, dpi) affects how sharp the image looks.
- **Aspect ratio** is the width-to-height ratio of the screen, commonly 4:3 or widescreen 16:9.
- **Color depth** indicates how many colors each pixel can show, from simple black and white to millions of colors using red, green, and blue channels.
- **Anti-aliasing** smooths jagged edges on diagonal lines by blending colors, improving visual quality.

#### Types of Screens

- **Cathode Ray Tube (CRT)** monitors use electron beams to light up phosphor dots on the screen. They are bulky and produce some radiation.
- **Liquid Crystal Displays (LCDs)** are thinner, lighter, and safer. They work by controlling light passing through crystals that change color with voltage.
- **Digital paper** is a flexible, electronic display that retains an image without power, similar to e-ink technology used in e-readers.

#### Virtual Reality (VR) and 3D Displays

- VR systems use special helmets or rooms ("caves") to immerse users in 3D environments.
- Devices track head and body movement, allowing interaction with virtual objects.
- VR headsets show slightly different images to each eye to create depth perception.
- Motion sickness can occur due to delays or conflicting sensory information.

#### Special Displays and Physical Output

- **Dedicated displays** like dials, gauges, and LED lights provide quick, analog or digital feedback.
- **Head-up displays** in aircraft project important information onto the windshield.
- **Sound output** includes beeps and alerts to confirm actions or warn of errors.
- **Haptic devices** provide touch feedback, such as vibrations or force, enhancing realism in games or simulations.
- **Environmental and bio-sensing outputs** can include sensors that detect temperature, heart rate, or other bodily signals.


### 4. 💾 Memory, Storage, and Processing

#### Memory

- **RAM (Random Access Memory)** is fast, temporary storage used while programs run.
- **Permanent storage** includes hard drives and solid-state drives, which keep data even when the computer is off.
- Memory capacity and speed affect how much data can be handled and how quickly.

#### Processing

- The **processor (CPU)** executes instructions and performs calculations.
- Processing speed impacts how fast the computer responds to user input and runs programs.
- Designers often assume processors are fast, but limitations can cause delays, such as cursor lag or slow interface responses.
- **Moore’s Law** observes that processor speed roughly doubles every 18 months, and memory capacity doubles every 12 months, leading to rapid technological improvements.

#### Limitations on Performance

- **Computation bound**: When calculations take too long, users get frustrated.
- **Storage channel bound**: Slow data transfer between disk and memory can bottleneck performance.
- **Graphics bound**: Updating complex displays requires significant processing power; graphics co-processors help.
- **Network capacity**: Slow network speeds can reduce interactive performance when computers share resources.


### 5. 🖨️ Paper, Printing, and Scanning

Even in a digital world, paper remains important for input and output.

#### Printing

- Printers create images from tiny dots, allowing any text or graphic to be printed.
- Key features include **resolution** (dots per inch), **speed** (pages per minute), and **cost**.
- Types of printers:
  - **Dot-matrix**: Use pins to strike an inked ribbon, low resolution.
  - **Inkjet**: Spray tiny ink droplets, better resolution.
  - **Laser**: Use electrostatic charges and toner powder, high resolution and speed.

#### Fonts and Text

- Fonts define the style of text (e.g., Times Roman, Helvetica).
- Font size is measured in points (pt), roughly 1/72 inch per point.
- Fonts can be **fixed-pitch** (all characters same width) or **variable-pitch** (characters have different widths).
- **Serif fonts** have small decorative strokes; **sans-serif** fonts do not.

#### Page Description Languages

- Complex pages with text, images, and graphics are described using languages like **PostScript**, which instruct printers how to render the page efficiently.

#### Scanning and OCR

- **Scanners** convert paper documents into digital images.
- **Optical Character Recognition (OCR)** software converts scanned images back into editable text, though it struggles with complex layouts and handwriting.

#### Compression and Storage Formats

- Compression reduces file size:
  - **Lossless** compression (e.g., ZIP) preserves exact data.
  - **Lossy** compression (e.g., JPEG, MP3) sacrifices some detail for smaller files.
- Text storage formats include ASCII, UTF-8, and markup languages like XML.
- Images and audio/video have many formats optimized for quality and size.


### 6. 🌐 Networks and Interactive Performance

Many computers are connected in networks, sharing files, printers, and other resources. However, network speed can affect how quickly a computer responds to user actions, especially in interactive applications.


### Summary

Understanding the computer’s components—input devices, output devices, memory, processing, and networks—is essential for designing effective human-computer interactions. Each element influences how users communicate with computers and how computers respond. From keyboards and mice to VR headsets and digital paper, the variety of devices reflects the many ways humans can interact with technology. Meanwhile, processing speed, memory capacity, and network performance set practical limits on what is possible, shaping the user experience.