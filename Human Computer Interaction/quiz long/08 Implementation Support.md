## 8. Implementation Support

## Questions

#### 1. Which of the following are primary roles of a windowing system?  
A) Managing multiple independent user tasks simultaneously  
B) Directly controlling hardware device drivers without abstraction  
C) Enforcing application-specific business logic  
D) Handling input focus and window arrangement policies  

#### 2. Device independence in windowing systems is achieved by:  
A) Using abstract terminal device drivers  
B) Allowing applications to manage their own synchronization  
C) Providing image models like PostScript and PHIGS  
D) Binding applications tightly to specific hardware  

#### 3. Which of the following are true about the client-server architecture in windowing systems?  
A) The window manager is integrated into the kernel  
B) The server manages display and input devices  
C) The X protocol defines communication between client and server  
D) Applications act as clients communicating with the server  

#### 4. In the read-evaluation loop programming model, which of the following are challenges?  
A) It naturally supports non-modal dialog boxes without extra complexity  
B) Handling multiple simultaneous inputs can complicate the main loop  
C) Substantial computation is required per device event  
D) It is inherently notification-based and event-driven  

#### 5. Notification-based programming differs from the read-evaluation loop because:  
A) It uses callbacks or handlers for specific events  
B) It simplifies implementation of non-modal dialogs  
C) It requires explicit polling of events in a loop  
D) It cannot handle modal dialogs effectively  

#### 6. Which statements about modal and non-modal dialog boxes are correct?  
A) Non-modal dialogs are easier to implement with event-loop programming  
B) Non-modal dialogs require complex mode flags in notification-based systems  
C) Modal dialogs are easier to implement with notification-based programming  
D) Modal dialogs block interaction with other windows until closed  

#### 7. Interaction toolkits provide which of the following benefits?  
A) Require programmers to handle low-level device input directly  
B) Support object-oriented programming paradigms  
C) Eliminate the need for windowing systems  
D) Promote consistency through reusable widgets  

#### 8. Regarding Java’s AWT and Swing toolkits, which are true?  
A) AWT 1.0 requires subclassing widgets for event handling  
B) Swing does not support higher-level features beyond AWT  
C) AWT 1.1 introduced callback objects for event handling  
D) Swing is built on top of AWT and uses MVC architecture  

#### 9. User Interface Management Systems (UIMS) primarily aim to:  
A) Provide low-level device driver management  
B) Separate application logic from presentation for portability and reusability  
C) Combine application semantics and presentation into a single layer  
D) Allow multiple interfaces to access the same functionality  

#### 10. The Seeheim model divides the user interface into which components?  
A) Presentation, Dialogue Control, Functionality  
B) Abstraction, Presentation, Control  
C) Lexical, Syntactic, Semantic  
D) Model, View, Controller  

#### 11. In the Seeheim model, the "switch" component is responsible for:  
A) Rendering graphical output on the screen  
B) Translating between lexical, syntactic, and semantic levels  
C) Managing hardware device drivers  
D) Handling application business logic  

#### 12. Which types of feedback correspond to lexical, syntactic, and semantic levels respectively?  
A) Mouse movement, menu highlights, application state changes  
B) Application state changes, mouse movement, menu highlights  
C) Menu highlights, application state changes, mouse movement  
D) Mouse clicks, keyboard input, system errors  

#### 13. The Arch/Slinky model differs from Seeheim by:  
A) Combining presentation and control into a single component  
B) Removing the dialogue control component entirely  
C) Being less flexible in layer thickness depending on system needs  
D) Adding more layers and distinguishing lexical from physical levels  

#### 14. Which of the following best describes the MVC architecture?  
A) Model processes input, Controller displays data, View holds data  
B) Model holds data, View displays data, Controller processes input  
C) Controller holds data, Model displays data, View processes input  
D) View holds data, Controller displays data, Model processes input  

#### 15. A key limitation of MVC in graphical interfaces is:  
A) MVC does not support multiple views of the same data  
B) The controller must communicate with the view to interpret user input context  
C) The model directly handles user input without mediation  
D) The view updates the model without controller involvement  

#### 16. The PAC model differs from MVC in that:  
A) It does not separate presentation from abstraction  
B) It is less conceptually clean than MVC  
C) Control mediates between abstraction and presentation and manages hierarchy  
D) It does not support multiple views or components  

#### 17. Which of the following are common techniques used to implement dialogue control in UIMS?  
A) Menu networks and state transition diagrams  
B) Constraints and graphical specification  
C) Event languages and declarative languages  
D) Direct hardware manipulation and device polling  

#### 18. Constraints in UIMS are useful because they:  
A) Replace the need for event-driven programming  
B) Help maintain consistency in groupware environments  
C) Specify what should be true rather than how to achieve it  
D) Are only applicable in single-user interfaces  

#### 19. Graphical specification tools in UIMS typically:  
A) Allow designers to draw interface components and link actions visually  
B) Focus on global system paths rather than local screen elements  
C) Are rarely used in modern UI development environments  
D) Require programmers to write all interface code manually  

#### 20. Which of the following statements about windowing system architectures is correct?  
A) Kernel-based window management ties applications to a specific OS  
B) Device drivers are always integrated into the window manager  
C) Having the window manager as a separate application maximizes portability  
D) Managing all processes within each application improves portability  



<br>

## Answers

#### 1. Which of the following are primary roles of a windowing system?  
A) ✓ Manages multiple independent user tasks simultaneously, core function of windowing systems  
B) ✗ Windowing systems abstract hardware, do not directly control device drivers  
C) ✗ Business logic is application-specific, not a windowing system role  
D) ✓ Handles input focus and window arrangement policies, essential for user interaction  

**Correct:** A, D


#### 2. Device independence in windowing systems is achieved by:  
A) ✓ Abstract terminal device drivers hide hardware specifics  
B) ✗ Synchronization management by apps reduces portability, not device independence  
C) ✓ Image models like PostScript provide hardware-independent graphics output  
D) ✗ Binding apps to hardware contradicts device independence  

**Correct:** A, C


#### 3. Which of the following are true about the client-server architecture in windowing systems?  
A) ✗ Window manager is a separate client, not integrated into kernel  
B) ✓ Server manages display and input devices  
C) ✓ X protocol defines communication between client and server  
D) ✓ Applications act as clients communicating with the server  

**Correct:** B, C, D


#### 4. In the read-evaluation loop programming model, which of the following are challenges?  
A) ✗ Non-modal dialogs are hard to implement with event-loop, not easy  
B) ✓ Handling multiple inputs complicates the main loop  
C) ✓ Substantial computation per device event is required  
D) ✗ Read-evaluation loop is not notification-based; it polls events  

**Correct:** B, C


#### 5. Notification-based programming differs from the read-evaluation loop because:  
A) ✓ Uses callbacks/handlers for events, unlike polling  
B) ✓ Simplifies non-modal dialog implementation  
C) ✗ Polling is characteristic of read-evaluation loop, not notification  
D) ✗ Notification can handle modal dialogs, though with mode flags  

**Correct:** A, B


#### 6. Which statements about modal and non-modal dialog boxes are correct?  
A) ✗ Non-modal dialogs are hard with event-loop, not easy  
B) ✗ Non-modal dialogs are easier with notification, not hard  
C) ✗ Modal dialogs are easier with event-loop, not notification  
D) ✓ Modal dialogs block other interactions until closed  

**Correct:** D


#### 7. Interaction toolkits provide which of the following benefits?  
A) ✗ Toolkits abstract device input, programmers don’t handle low-level input directly  
B) ✓ Support object-oriented programming  
C) ✗ Toolkits rely on windowing systems, do not replace them  
D) ✓ Promote consistency via reusable widgets  

**Correct:** B, D


#### 8. Regarding Java’s AWT and Swing toolkits, which are true?  
A) ✓ AWT 1.0 required subclassing widgets for event handling  
B) ✗ Swing adds higher-level features beyond AWT  
C) ✓ AWT 1.1 introduced callback objects for event handling  
D) ✓ Swing is built on AWT and uses MVC architecture  

**Correct:** A, C, D


#### 9. User Interface Management Systems (UIMS) primarily aim to:  
A) ✗ UIMS do not manage low-level device drivers  
B) ✓ Separation improves portability and reusability  
C) ✗ They separate semantics and presentation, not combine them  
D) ✓ Support multiple interfaces accessing same functionality  

**Correct:** B, D


#### 10. The Seeheim model divides the user interface into which components?  
A) ✓ Presentation, Dialogue Control, Functionality is correct Seeheim division  
B) ✗ PAC components, not Seeheim  
C) ✗ Lexical/syntactic/semantic are language levels, not components  
D) ✗ MVC components, not Seeheim  

**Correct:** A


#### 11. In the Seeheim model, the "switch" component is responsible for:  
A) ✗ Rendering is part of Presentation, not switch  
B) ✓ Translating between lexical, syntactic, and semantic levels  
C) ✗ Device drivers are outside Seeheim model  
D) ✗ Application logic is Functionality, not switch  

**Correct:** B


#### 12. Which types of feedback correspond to lexical, syntactic, and semantic levels respectively?  
A) ✓ Mouse movement (lexical), menu highlights (syntactic), app state changes (semantic)  
B) ✗ Incorrect order of feedback types  
C) ✗ Incorrect order of feedback types  
D) ✗ Mouse clicks and keyboard input are lexical, but system errors don’t fit here  

**Correct:** A


#### 13. The Arch/Slinky model differs from Seeheim by:  
A) ✗ Does not combine presentation and control  
B) ✗ Dialogue control remains essential  
C) ✗ Layer thickness varies, so it is flexible, not less so  
D) ✓ Adds more layers and distinguishes lexical from physical levels  

**Correct:** D


#### 14. Which of the following best describes the MVC architecture?  
A) ✗ Incorrect roles assigned  
B) ✓ Model holds data, View displays data, Controller processes input  
C) ✗ Incorrect roles assigned  
D) ✗ Incorrect roles assigned  

**Correct:** B


#### 15. A key limitation of MVC in graphical interfaces is:  
A) ✗ MVC supports multiple views of same data  
B) ✓ Controller must communicate with view to interpret input context  
C) ✗ Model does not handle input directly  
D) ✗ View does not update model without controller  

**Correct:** B


#### 16. The PAC model differs from MVC in that:  
A) ✗ PAC separates presentation and abstraction  
B) ✗ PAC is conceptually cleaner than MVC  
C) ✓ Control mediates between abstraction and presentation and manages hierarchy  
D) ✗ PAC supports multiple views and components  

**Correct:** C


#### 17. Which of the following are common techniques used to implement dialogue control in UIMS?  
A) ✓ Menu networks and state transition diagrams are common  
B) ✓ Constraints and graphical specification are used  
C) ✓ Event languages and declarative languages are used  
D) ✗ Direct hardware manipulation is not typical in UIMS  

**Correct:** A, B, C


#### 18. Constraints in UIMS are useful because they:  
A) ✗ Do not replace event-driven programming, complement it  
B) ✓ Help maintain consistency in groupware environments  
C) ✓ Specify what should be true, not how to do it  
D) ✗ Applicable in both single-user and groupware interfaces  

**Correct:** B, C


#### 19. Graphical specification tools in UIMS typically:  
A) ✓ Allow designers to visually draw components and link actions  
B) ✗ Focus on local screen elements, not just global paths  
C) ✗ Are widely used in modern UI development  
D) ✗ Do not require all manual coding  

**Correct:** A, B, C


#### 20. Which of the following statements about windowing system architectures is correct?  
A) ✓ Kernel-based management ties apps to specific OS  
B) ✗ Device drivers are separate from window manager  
C) ✓ Separate window manager maximizes portability  
D) ✗ Managing all processes in each app reduces portability  

**Correct:** A, C