## 8. Implementation Support

## Questions

#### 1. Which of the following are primary roles of a windowing system?  
A) Enforcing application-specific business logic  
B) Managing multiple independent user tasks simultaneously  
C) Handling input focus and window arrangement policies  
D) Directly controlling hardware device drivers without abstraction  

#### 2. Device independence in windowing systems is achieved by:  
A) Using abstract terminal device drivers  
B) Allowing applications to manage their own synchronization  
C) Providing image models like PostScript and PHIGS  
D) Binding applications tightly to specific hardware  

#### 3. Which of the following are true about the client-server architecture in windowing systems?  
A) The server manages display and input devices  
B) The window manager is integrated into the kernel  
C) The X protocol defines communication between client and server  
D) Applications act as clients communicating with the server  

#### 4. In the read-evaluation loop programming model, which of the following are challenges?  
A) Substantial computation is required per device event  
B) Handling multiple simultaneous inputs can complicate the main loop  
C) It naturally supports non-modal dialog boxes without extra complexity  
D) It is inherently notification-based and event-driven  

#### 5. Notification-based programming differs from the read-evaluation loop because:  
A) It cannot handle modal dialogs effectively  
B) It uses callbacks or handlers for specific events  
C) It simplifies implementation of non-modal dialogs  
D) It requires explicit polling of events in a loop  

#### 6. Which statements about modal and non-modal dialog boxes are correct?  
A) Non-modal dialogs require complex mode flags in notification-based systems  
B) Non-modal dialogs are easier to implement with event-loop programming  
C) Modal dialogs block interaction with other windows until closed  
D) Modal dialogs are easier to implement with notification-based programming  

#### 7. Interaction toolkits provide which of the following benefits?  
A) Promote consistency through reusable widgets  
B) Support object-oriented programming paradigms  
C) Require programmers to handle low-level device input directly  
D) Eliminate the need for windowing systems  

#### 8. Regarding Java’s AWT and Swing toolkits, which are true?  
A) AWT 1.0 requires subclassing widgets for event handling  
B) Swing is built on top of AWT and uses MVC architecture  
C) AWT 1.1 introduced callback objects for event handling  
D) Swing does not support higher-level features beyond AWT  

#### 9. User Interface Management Systems (UIMS) primarily aim to:  
A) Combine application semantics and presentation into a single layer  
B) Allow multiple interfaces to access the same functionality  
C) Provide low-level device driver management  
D) Separate application logic from presentation for portability and reusability  

#### 10. The Seeheim model divides the user interface into which components?  
A) Model, View, Controller  
B) Lexical, Syntactic, Semantic  
C) Abstraction, Presentation, Control  
D) Presentation, Dialogue Control, Functionality  

#### 11. In the Seeheim model, the "switch" component is responsible for:  
A) Managing hardware device drivers  
B) Rendering graphical output on the screen  
C) Handling application business logic  
D) Translating between lexical, syntactic, and semantic levels  

#### 12. Which types of feedback correspond to lexical, syntactic, and semantic levels respectively?  
A) Application state changes, mouse movement, menu highlights  
B) Mouse movement, menu highlights, application state changes  
C) Mouse clicks, keyboard input, system errors  
D) Menu highlights, application state changes, mouse movement  

#### 13. The Arch/Slinky model differs from Seeheim by:  
A) Removing the dialogue control component entirely  
B) Being less flexible in layer thickness depending on system needs  
C) Adding more layers and distinguishing lexical from physical levels  
D) Combining presentation and control into a single component  

#### 14. Which of the following best describes the MVC architecture?  
A) Controller holds data, Model displays data, View processes input  
B) Model holds data, View displays data, Controller processes input  
C) View holds data, Controller displays data, Model processes input  
D) Model processes input, Controller displays data, View holds data  

#### 15. A key limitation of MVC in graphical interfaces is:  
A) The model directly handles user input without mediation  
B) The controller must communicate with the view to interpret user input context  
C) MVC does not support multiple views of the same data  
D) The view updates the model without controller involvement  

#### 16. The PAC model differs from MVC in that:  
A) Control mediates between abstraction and presentation and manages hierarchy  
B) It does not support multiple views or components  
C) It is less conceptually clean than MVC  
D) It does not separate presentation from abstraction  

#### 17. Which of the following are common techniques used to implement dialogue control in UIMS?  
A) Constraints and graphical specification  
B) Menu networks and state transition diagrams  
C) Event languages and declarative languages  
D) Direct hardware manipulation and device polling  

#### 18. Constraints in UIMS are useful because they:  
A) Specify what should be true rather than how to achieve it  
B) Replace the need for event-driven programming  
C) Are only applicable in single-user interfaces  
D) Help maintain consistency in groupware environments  

#### 19. Graphical specification tools in UIMS typically:  
A) Are rarely used in modern UI development environments  
B) Require programmers to write all interface code manually  
C) Focus on global system paths rather than local screen elements  
D) Allow designers to draw interface components and link actions visually  

#### 20. Which of the following statements about windowing system architectures is correct?  
A) Managing all processes within each application improves portability  
B) Device drivers are always integrated into the window manager  
C) Having the window manager as a separate application maximizes portability  
D) Kernel-based window management ties applications to a specific OS  



<br>

## Answers

#### 1. Which of the following are primary roles of a windowing system?  
A) ✗ Business logic is application-specific, not a windowing system role  
B) ✓ Manages multiple independent user tasks simultaneously, core function of windowing systems  
C) ✓ Handles input focus and window arrangement policies, essential for user interaction  
D) ✗ Windowing systems abstract hardware, do not directly control device drivers  

**Correct:** B, C


#### 2. Device independence in windowing systems is achieved by:  
A) ✓ Abstract terminal device drivers hide hardware specifics  
B) ✗ Synchronization management by apps reduces portability, not device independence  
C) ✓ Image models like PostScript provide hardware-independent graphics output  
D) ✗ Binding apps to hardware contradicts device independence  

**Correct:** A, C


#### 3. Which of the following are true about the client-server architecture in windowing systems?  
A) ✓ Server manages display and input devices  
B) ✗ Window manager is a separate client, not integrated into kernel  
C) ✓ X protocol defines communication between client and server  
D) ✓ Applications act as clients communicating with the server  

**Correct:** A, C, D


#### 4. In the read-evaluation loop programming model, which of the following are challenges?  
A) ✓ Substantial computation per device event is required  
B) ✓ Handling multiple inputs complicates the main loop  
C) ✗ Non-modal dialogs are hard to implement with event-loop, not easy  
D) ✗ Read-evaluation loop is not notification-based; it polls events  

**Correct:** A, B


#### 5. Notification-based programming differs from the read-evaluation loop because:  
A) ✗ Notification can handle modal dialogs, though with mode flags  
B) ✓ Uses callbacks/handlers for events, unlike polling  
C) ✓ Simplifies non-modal dialog implementation  
D) ✗ Polling is characteristic of read-evaluation loop, not notification  

**Correct:** B, C


#### 6. Which statements about modal and non-modal dialog boxes are correct?  
A) ✗ Non-modal dialogs are easier with notification, not hard  
B) ✗ Non-modal dialogs are hard with event-loop, not easy  
C) ✓ Modal dialogs block other interactions until closed  
D) ✗ Modal dialogs are easier with event-loop, not notification  

**Correct:** C


#### 7. Interaction toolkits provide which of the following benefits?  
A) ✓ Promote consistency via reusable widgets  
B) ✓ Support object-oriented programming  
C) ✗ Toolkits abstract device input, programmers don’t handle low-level input directly  
D) ✗ Toolkits rely on windowing systems, do not replace them  

**Correct:** A, B


#### 8. Regarding Java’s AWT and Swing toolkits, which are true?  
A) ✓ AWT 1.0 required subclassing widgets for event handling  
B) ✓ Swing is built on AWT and uses MVC architecture  
C) ✓ AWT 1.1 introduced callback objects for event handling  
D) ✗ Swing adds higher-level features beyond AWT  

**Correct:** A, B, C


#### 9. User Interface Management Systems (UIMS) primarily aim to:  
A) ✗ They separate semantics and presentation, not combine them  
B) ✓ Support multiple interfaces accessing same functionality  
C) ✗ UIMS do not manage low-level device drivers  
D) ✓ Separation improves portability and reusability  

**Correct:** B, D


#### 10. The Seeheim model divides the user interface into which components?  
A) ✗ MVC components, not Seeheim  
B) ✗ Lexical/syntactic/semantic are language levels, not components  
C) ✗ PAC components, not Seeheim  
D) ✓ Presentation, Dialogue Control, Functionality is correct Seeheim division  

**Correct:** D


#### 11. In the Seeheim model, the "switch" component is responsible for:  
A) ✗ Device drivers are outside Seeheim model  
B) ✗ Rendering is part of Presentation, not switch  
C) ✗ Application logic is Functionality, not switch  
D) ✓ Translating between lexical, syntactic, and semantic levels  

**Correct:** D


#### 12. Which types of feedback correspond to lexical, syntactic, and semantic levels respectively?  
A) ✗ Incorrect order of feedback types  
B) ✓ Mouse movement (lexical), menu highlights (syntactic), app state changes (semantic)  
C) ✗ Mouse clicks and keyboard input are lexical, but system errors don’t fit here  
D) ✗ Incorrect order of feedback types  

**Correct:** B


#### 13. The Arch/Slinky model differs from Seeheim by:  
A) ✗ Dialogue control remains essential  
B) ✗ Layer thickness varies, so it is flexible, not less so  
C) ✓ Adds more layers and distinguishes lexical from physical levels  
D) ✗ Does not combine presentation and control  

**Correct:** C


#### 14. Which of the following best describes the MVC architecture?  
A) ✗ Incorrect roles assigned  
B) ✓ Model holds data, View displays data, Controller processes input  
C) ✗ Incorrect roles assigned  
D) ✗ Incorrect roles assigned  

**Correct:** B


#### 15. A key limitation of MVC in graphical interfaces is:  
A) ✗ Model does not handle input directly  
B) ✓ Controller must communicate with view to interpret input context  
C) ✗ MVC supports multiple views of same data  
D) ✗ View does not update model without controller  

**Correct:** B


#### 16. The PAC model differs from MVC in that:  
A) ✓ Control mediates between abstraction and presentation and manages hierarchy  
B) ✗ PAC supports multiple views and components  
C) ✗ PAC is conceptually cleaner than MVC  
D) ✗ PAC separates presentation and abstraction  

**Correct:** A


#### 17. Which of the following are common techniques used to implement dialogue control in UIMS?  
A) ✓ Constraints and graphical specification are used  
B) ✓ Menu networks and state transition diagrams are common  
C) ✓ Event languages and declarative languages are used  
D) ✗ Direct hardware manipulation is not typical in UIMS  

**Correct:** A, B, C


#### 18. Constraints in UIMS are useful because they:  
A) ✓ Specify what should be true, not how to do it  
B) ✗ Do not replace event-driven programming, complement it  
C) ✗ Applicable in both single-user and groupware interfaces  
D) ✓ Help maintain consistency in groupware environments  

**Correct:** A, D


#### 19. Graphical specification tools in UIMS typically:  
A) ✗ Are widely used in modern UI development  
B) ✗ Do not require all manual coding  
C) ✗ Focus on local screen elements, not just global paths  
D) ✓ Allow designers to visually draw components and link actions  

**Correct:** A, C, D


#### 20. Which of the following statements about windowing system architectures is correct?  
A) ✗ Managing all processes in each app reduces portability  
B) ✗ Device drivers are separate from window manager  
C) ✓ Separate window manager maximizes portability  
D) ✓ Kernel-based management ties apps to specific OS  

**Correct:** C, D