## 8. Implementation Support

## Questions

#### 1. Which of the following are primary roles of a windowing system?  
A) Managing multiple independent user tasks simultaneously  
B) Directly controlling hardware device drivers without abstraction  
C) Handling input focus and window arrangement policies  
D) Enforcing application-specific business logic  

#### 2. Device independence in windowing systems is achieved by:  
A) Using abstract terminal device drivers  
B) Binding applications tightly to specific hardware  
C) Providing image models like PostScript and PHIGS  
D) Allowing applications to manage their own synchronization  

#### 3. Which of the following are true about the client-server architecture in windowing systems?  
A) The server manages display and input devices  
B) Applications act as clients communicating with the server  
C) The window manager is integrated into the kernel  
D) The X protocol defines communication between client and server  

#### 4. In the read-evaluation loop programming model, which of the following are challenges?  
A) Handling multiple simultaneous inputs can complicate the main loop  
B) It naturally supports non-modal dialog boxes without extra complexity  
C) Substantial computation is required per device event  
D) It is inherently notification-based and event-driven  

#### 5. Notification-based programming differs from the read-evaluation loop because:  
A) It uses callbacks or handlers for specific events  
B) It requires explicit polling of events in a loop  
C) It simplifies implementation of non-modal dialogs  
D) It cannot handle modal dialogs effectively  

#### 6. Which statements about modal and non-modal dialog boxes are correct?  
A) Modal dialogs block interaction with other windows until closed  
B) Non-modal dialogs are easier to implement with event-loop programming  
C) Modal dialogs are easier to implement with notification-based programming  
D) Non-modal dialogs require complex mode flags in notification-based systems  

#### 7. Interaction toolkits provide which of the following benefits?  
A) Promote consistency through reusable widgets  
B) Require programmers to handle low-level device input directly  
C) Support object-oriented programming paradigms  
D) Eliminate the need for windowing systems  

#### 8. Regarding Java’s AWT and Swing toolkits, which are true?  
A) AWT 1.0 requires subclassing widgets for event handling  
B) Swing is built on top of AWT and uses MVC architecture  
C) AWT 1.1 introduced callback objects for event handling  
D) Swing does not support higher-level features beyond AWT  

#### 9. User Interface Management Systems (UIMS) primarily aim to:  
A) Combine application semantics and presentation into a single layer  
B) Separate application logic from presentation for portability and reusability  
C) Provide low-level device driver management  
D) Allow multiple interfaces to access the same functionality  

#### 10. The Seeheim model divides the user interface into which components?  
A) Presentation, Dialogue Control, Functionality  
B) Model, View, Controller  
C) Abstraction, Presentation, Control  
D) Lexical, Syntactic, Semantic  

#### 11. In the Seeheim model, the "switch" component is responsible for:  
A) Translating between lexical, syntactic, and semantic levels  
B) Managing hardware device drivers  
C) Rendering graphical output on the screen  
D) Handling application business logic  

#### 12. Which types of feedback correspond to lexical, syntactic, and semantic levels respectively?  
A) Mouse movement, menu highlights, application state changes  
B) Application state changes, mouse movement, menu highlights  
C) Menu highlights, application state changes, mouse movement  
D) Mouse clicks, keyboard input, system errors  

#### 13. The Arch/Slinky model differs from Seeheim by:  
A) Adding more layers and distinguishing lexical from physical levels  
B) Combining presentation and control into a single component  
C) Removing the dialogue control component entirely  
D) Being less flexible in layer thickness depending on system needs  

#### 14. Which of the following best describes the MVC architecture?  
A) Model holds data, View displays data, Controller processes input  
B) Controller holds data, Model displays data, View processes input  
C) View holds data, Controller displays data, Model processes input  
D) Model processes input, Controller displays data, View holds data  

#### 15. A key limitation of MVC in graphical interfaces is:  
A) The controller must communicate with the view to interpret user input context  
B) The model directly handles user input without mediation  
C) The view updates the model without controller involvement  
D) MVC does not support multiple views of the same data  

#### 16. The PAC model differs from MVC in that:  
A) Control mediates between abstraction and presentation and manages hierarchy  
B) It does not separate presentation from abstraction  
C) It does not support multiple views or components  
D) It is less conceptually clean than MVC  

#### 17. Which of the following are common techniques used to implement dialogue control in UIMS?  
A) Menu networks and state transition diagrams  
B) Event languages and declarative languages  
C) Direct hardware manipulation and device polling  
D) Constraints and graphical specification  

#### 18. Constraints in UIMS are useful because they:  
A) Specify what should be true rather than how to achieve it  
B) Are only applicable in single-user interfaces  
C) Help maintain consistency in groupware environments  
D) Replace the need for event-driven programming  

#### 19. Graphical specification tools in UIMS typically:  
A) Allow designers to draw interface components and link actions visually  
B) Require programmers to write all interface code manually  
C) Are rarely used in modern UI development environments  
D) Focus on global system paths rather than local screen elements  

#### 20. Which of the following statements about windowing system architectures is correct?  
A) Having the window manager as a separate application maximizes portability  
B) Managing all processes within each application improves portability  
C) Kernel-based window management ties applications to a specific OS  
D) Device drivers are always integrated into the window manager



<br>

## Answers

#### 1. Which of the following are primary roles of a windowing system?  
A) ✓ Manages multiple independent user tasks simultaneously, core function of windowing systems  
B) ✗ Windowing systems abstract hardware, do not directly control device drivers  
C) ✓ Handles input focus and window arrangement policies, essential for user interaction  
D) ✗ Business logic is application-specific, not a windowing system role  

**Correct:** A, C


#### 2. Device independence in windowing systems is achieved by:  
A) ✓ Abstract terminal device drivers hide hardware specifics  
B) ✗ Binding apps to hardware contradicts device independence  
C) ✓ Image models like PostScript provide hardware-independent graphics output  
D) ✗ Synchronization management by apps reduces portability, not device independence  

**Correct:** A, C


#### 3. Which of the following are true about the client-server architecture in windowing systems?  
A) ✓ Server manages display and input devices  
B) ✓ Applications act as clients communicating with the server  
C) ✗ Window manager is a separate client, not integrated into kernel  
D) ✓ X protocol defines communication between client and server  

**Correct:** A, B, D


#### 4. In the read-evaluation loop programming model, which of the following are challenges?  
A) ✓ Handling multiple inputs complicates the main loop  
B) ✗ Non-modal dialogs are hard to implement with event-loop, not easy  
C) ✓ Substantial computation per device event is required  
D) ✗ Read-evaluation loop is not notification-based; it polls events  

**Correct:** A, C


#### 5. Notification-based programming differs from the read-evaluation loop because:  
A) ✓ Uses callbacks/handlers for events, unlike polling  
B) ✗ Polling is characteristic of read-evaluation loop, not notification  
C) ✓ Simplifies non-modal dialog implementation  
D) ✗ Notification can handle modal dialogs, though with mode flags  

**Correct:** A, C


#### 6. Which statements about modal and non-modal dialog boxes are correct?  
A) ✓ Modal dialogs block other interactions until closed  
B) ✗ Non-modal dialogs are hard with event-loop, not easy  
C) ✗ Modal dialogs are easier with event-loop, not notification  
D) ✗ Non-modal dialogs are easier with notification, not hard  

**Correct:** A


#### 7. Interaction toolkits provide which of the following benefits?  
A) ✓ Promote consistency via reusable widgets  
B) ✗ Toolkits abstract device input, programmers don’t handle low-level input directly  
C) ✓ Support object-oriented programming  
D) ✗ Toolkits rely on windowing systems, do not replace them  

**Correct:** A, C


#### 8. Regarding Java’s AWT and Swing toolkits, which are true?  
A) ✓ AWT 1.0 required subclassing widgets for event handling  
B) ✓ Swing is built on AWT and uses MVC architecture  
C) ✓ AWT 1.1 introduced callback objects for event handling  
D) ✗ Swing adds higher-level features beyond AWT  

**Correct:** A, B, C


#### 9. User Interface Management Systems (UIMS) primarily aim to:  
A) ✗ They separate semantics and presentation, not combine them  
B) ✓ Separation improves portability and reusability  
C) ✗ UIMS do not manage low-level device drivers  
D) ✓ Support multiple interfaces accessing same functionality  

**Correct:** B, D


#### 10. The Seeheim model divides the user interface into which components?  
A) ✓ Presentation, Dialogue Control, Functionality is correct Seeheim division  
B) ✗ MVC components, not Seeheim  
C) ✗ PAC components, not Seeheim  
D) ✗ Lexical/syntactic/semantic are language levels, not components  

**Correct:** A


#### 11. In the Seeheim model, the "switch" component is responsible for:  
A) ✓ Translating between lexical, syntactic, and semantic levels  
B) ✗ Device drivers are outside Seeheim model  
C) ✗ Rendering is part of Presentation, not switch  
D) ✗ Application logic is Functionality, not switch  

**Correct:** A


#### 12. Which types of feedback correspond to lexical, syntactic, and semantic levels respectively?  
A) ✓ Mouse movement (lexical), menu highlights (syntactic), app state changes (semantic)  
B) ✗ Incorrect order of feedback types  
C) ✗ Incorrect order of feedback types  
D) ✗ Mouse clicks and keyboard input are lexical, but system errors don’t fit here  

**Correct:** A


#### 13. The Arch/Slinky model differs from Seeheim by:  
A) ✓ Adds more layers and distinguishes lexical from physical levels  
B) ✗ Does not combine presentation and control  
C) ✗ Dialogue control remains essential  
D) ✗ Layer thickness varies, so it is flexible, not less so  

**Correct:** A


#### 14. Which of the following best describes the MVC architecture?  
A) ✓ Model holds data, View displays data, Controller processes input  
B) ✗ Incorrect roles assigned  
C) ✗ Incorrect roles assigned  
D) ✗ Incorrect roles assigned  

**Correct:** A


#### 15. A key limitation of MVC in graphical interfaces is:  
A) ✓ Controller must communicate with view to interpret input context  
B) ✗ Model does not handle input directly  
C) ✗ View does not update model without controller  
D) ✗ MVC supports multiple views of same data  

**Correct:** A


#### 16. The PAC model differs from MVC in that:  
A) ✓ Control mediates between abstraction and presentation and manages hierarchy  
B) ✗ PAC separates presentation and abstraction  
C) ✗ PAC supports multiple views and components  
D) ✗ PAC is conceptually cleaner than MVC  

**Correct:** A


#### 17. Which of the following are common techniques used to implement dialogue control in UIMS?  
A) ✓ Menu networks and state transition diagrams are common  
B) ✓ Event languages and declarative languages are used  
C) ✗ Direct hardware manipulation is not typical in UIMS  
D) ✓ Constraints and graphical specification are used  

**Correct:** A, B, D


#### 18. Constraints in UIMS are useful because they:  
A) ✓ Specify what should be true, not how to do it  
B) ✗ Applicable in both single-user and groupware interfaces  
C) ✓ Help maintain consistency in groupware environments  
D) ✗ Do not replace event-driven programming, complement it  

**Correct:** A, C


#### 19. Graphical specification tools in UIMS typically:  
A) ✓ Allow designers to visually draw components and link actions  
B) ✗ Do not require all manual coding  
C) ✗ Are widely used in modern UI development  
D) ✗ Focus on local screen elements, not just global paths  

**Correct:** A, C, D


#### 20. Which of the following statements about windowing system architectures is correct?  
A) ✓ Separate window manager maximizes portability  
B) ✗ Managing all processes in each app reduces portability  
C) ✓ Kernel-based management ties apps to specific OS  
D) ✗ Device drivers are separate from window manager  

**Correct:** A, C