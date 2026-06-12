## 8. Implementation Support

## Questions

#### 1. Which of the following are primary roles of a windowing system?  
A) Enforcing application-specific business logic  
B) Managing multiple independent user tasks simultaneously  
C) Directly controlling hardware device drivers without abstraction  
D) Handling input focus and window arrangement policies  

#### 2. Device independence in windowing systems is achieved by:  
A) Binding applications tightly to specific hardware  
B) Allowing applications to manage their own synchronization  
C) Providing image models like PostScript and PHIGS  
D) Using abstract terminal device drivers  

#### 3. Which of the following are true about the client-server architecture in windowing systems?  
A) The window manager is integrated into the kernel  
B) Applications act as clients communicating with the server  
C) The server manages display and input devices  
D) The X protocol defines communication between client and server  

#### 4. In the read-evaluation loop programming model, which of the following are challenges?  
A) It naturally supports non-modal dialog boxes without extra complexity  
B) Handling multiple simultaneous inputs can complicate the main loop  
C) Substantial computation is required per device event  
D) It is inherently notification-based and event-driven  

#### 5. Notification-based programming differs from the read-evaluation loop because:  
A) It uses callbacks or handlers for specific events  
B) It cannot handle modal dialogs effectively  
C) It requires explicit polling of events in a loop  
D) It simplifies implementation of non-modal dialogs  

#### 6. Which statements about modal and non-modal dialog boxes are correct?  
A) Modal dialogs are easier to implement with notification-based programming  
B) Modal dialogs block interaction with other windows until closed  
C) Non-modal dialogs require complex mode flags in notification-based systems  
D) Non-modal dialogs are easier to implement with event-loop programming  

#### 7. Interaction toolkits provide which of the following benefits?  
A) Require programmers to handle low-level device input directly  
B) Promote consistency through reusable widgets  
C) Eliminate the need for windowing systems  
D) Support object-oriented programming paradigms  

#### 8. Regarding Java’s AWT and Swing toolkits, which are true?  
A) AWT 1.0 requires subclassing widgets for event handling  
B) Swing does not support higher-level features beyond AWT  
C) AWT 1.1 introduced callback objects for event handling  
D) Swing is built on top of AWT and uses MVC architecture  

#### 9. User Interface Management Systems (UIMS) primarily aim to:  
A) Provide low-level device driver management  
B) Separate application logic from presentation for portability and reusability  
C) Allow multiple interfaces to access the same functionality  
D) Combine application semantics and presentation into a single layer  

#### 10. The Seeheim model divides the user interface into which components?  
A) Lexical, Syntactic, Semantic  
B) Abstraction, Presentation, Control  
C) Model, View, Controller  
D) Presentation, Dialogue Control, Functionality  

#### 11. In the Seeheim model, the "switch" component is responsible for:  
A) Rendering graphical output on the screen  
B) Handling application business logic  
C) Managing hardware device drivers  
D) Translating between lexical, syntactic, and semantic levels  

#### 12. Which types of feedback correspond to lexical, syntactic, and semantic levels respectively?  
A) Menu highlights, application state changes, mouse movement  
B) Application state changes, mouse movement, menu highlights  
C) Mouse clicks, keyboard input, system errors  
D) Mouse movement, menu highlights, application state changes  

#### 13. The Arch/Slinky model differs from Seeheim by:  
A) Combining presentation and control into a single component  
B) Adding more layers and distinguishing lexical from physical levels  
C) Removing the dialogue control component entirely  
D) Being less flexible in layer thickness depending on system needs  

#### 14. Which of the following best describes the MVC architecture?  
A) View holds data, Controller displays data, Model processes input  
B) Model holds data, View displays data, Controller processes input  
C) Model processes input, Controller displays data, View holds data  
D) Controller holds data, Model displays data, View processes input  

#### 15. A key limitation of MVC in graphical interfaces is:  
A) MVC does not support multiple views of the same data  
B) The view updates the model without controller involvement  
C) The model directly handles user input without mediation  
D) The controller must communicate with the view to interpret user input context  

#### 16. The PAC model differs from MVC in that:  
A) It is less conceptually clean than MVC  
B) It does not separate presentation from abstraction  
C) It does not support multiple views or components  
D) Control mediates between abstraction and presentation and manages hierarchy  

#### 17. Which of the following are common techniques used to implement dialogue control in UIMS?  
A) Menu networks and state transition diagrams  
B) Direct hardware manipulation and device polling  
C) Event languages and declarative languages  
D) Constraints and graphical specification  

#### 18. Constraints in UIMS are useful because they:  
A) Replace the need for event-driven programming  
B) Are only applicable in single-user interfaces  
C) Help maintain consistency in groupware environments  
D) Specify what should be true rather than how to achieve it  

#### 19. Graphical specification tools in UIMS typically:  
A) Are rarely used in modern UI development environments  
B) Allow designers to draw interface components and link actions visually  
C) Focus on global system paths rather than local screen elements  
D) Require programmers to write all interface code manually  

#### 20. Which of the following statements about windowing system architectures is correct?  
A) Having the window manager as a separate application maximizes portability  
B) Managing all processes within each application improves portability  
C) Device drivers are always integrated into the window manager
D) Kernel-based window management ties applications to a specific OS  



<br>

## Answers

#### 1. Which of the following are primary roles of a windowing system?  
A) ✗ Business logic is application-specific, not a windowing system role  
B) ✓ Manages multiple independent user tasks simultaneously, core function of windowing systems  
C) ✗ Windowing systems abstract hardware, do not directly control device drivers  
D) ✓ Handles input focus and window arrangement policies, essential for user interaction  

**Correct:** B, D


#### 2. Device independence in windowing systems is achieved by:  
A) ✗ Binding apps to hardware contradicts device independence  
B) ✗ Synchronization management by apps reduces portability, not device independence  
C) ✓ Image models like PostScript provide hardware-independent graphics output  
D) ✓ Abstract terminal device drivers hide hardware specifics  

**Correct:** C, D


#### 3. Which of the following are true about the client-server architecture in windowing systems?  
A) ✗ Window manager is a separate client, not integrated into kernel  
B) ✓ Applications act as clients communicating with the server  
C) ✓ Server manages display and input devices  
D) ✓ X protocol defines communication between client and server  

**Correct:** B, C, D


#### 4. In the read-evaluation loop programming model, which of the following are challenges?  
A) ✗ Non-modal dialogs are hard to implement with event-loop, not easy  
B) ✓ Handling multiple inputs complicates the main loop  
C) ✓ Substantial computation per device event is required  
D) ✗ Read-evaluation loop is not notification-based; it polls events  

**Correct:** B, C


#### 5. Notification-based programming differs from the read-evaluation loop because:  
A) ✓ Uses callbacks/handlers for events, unlike polling  
B) ✗ Notification can handle modal dialogs, though with mode flags  
C) ✗ Polling is characteristic of read-evaluation loop, not notification  
D) ✓ Simplifies non-modal dialog implementation  

**Correct:** A, D


#### 6. Which statements about modal and non-modal dialog boxes are correct?  
A) ✗ Modal dialogs are easier with event-loop, not notification  
B) ✓ Modal dialogs block other interactions until closed  
C) ✗ Non-modal dialogs are easier with notification, not hard  
D) ✗ Non-modal dialogs are hard with event-loop, not easy  

**Correct:** B


#### 7. Interaction toolkits provide which of the following benefits?  
A) ✗ Toolkits abstract device input, programmers don’t handle low-level input directly  
B) ✓ Promote consistency via reusable widgets  
C) ✗ Toolkits rely on windowing systems, do not replace them  
D) ✓ Support object-oriented programming  

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
C) ✓ Support multiple interfaces accessing same functionality  
D) ✗ They separate semantics and presentation, not combine them  

**Correct:** B, C


#### 10. The Seeheim model divides the user interface into which components?  
A) ✗ Lexical/syntactic/semantic are language levels, not components  
B) ✗ PAC components, not Seeheim  
C) ✗ MVC components, not Seeheim  
D) ✓ Presentation, Dialogue Control, Functionality is correct Seeheim division  

**Correct:** D


#### 11. In the Seeheim model, the "switch" component is responsible for:  
A) ✗ Rendering is part of Presentation, not switch  
B) ✗ Application logic is Functionality, not switch  
C) ✗ Device drivers are outside Seeheim model  
D) ✓ Translating between lexical, syntactic, and semantic levels  

**Correct:** D


#### 12. Which types of feedback correspond to lexical, syntactic, and semantic levels respectively?  
A) ✗ Incorrect order of feedback types  
B) ✗ Incorrect order of feedback types  
C) ✗ Mouse clicks and keyboard input are lexical, but system errors don’t fit here  
D) ✓ Mouse movement (lexical), menu highlights (syntactic), app state changes (semantic)  

**Correct:** D


#### 13. The Arch/Slinky model differs from Seeheim by:  
A) ✗ Does not combine presentation and control  
B) ✓ Adds more layers and distinguishes lexical from physical levels  
C) ✗ Dialogue control remains essential  
D) ✗ Layer thickness varies, so it is flexible, not less so  

**Correct:** B


#### 14. Which of the following best describes the MVC architecture?  
A) ✗ Incorrect roles assigned  
B) ✓ Model holds data, View displays data, Controller processes input  
C) ✗ Incorrect roles assigned  
D) ✗ Incorrect roles assigned  

**Correct:** B


#### 15. A key limitation of MVC in graphical interfaces is:  
A) ✗ MVC supports multiple views of same data  
B) ✗ View does not update model without controller  
C) ✗ Model does not handle input directly  
D) ✓ Controller must communicate with view to interpret input context  

**Correct:** D


#### 16. The PAC model differs from MVC in that:  
A) ✗ PAC is conceptually cleaner than MVC  
B) ✗ PAC separates presentation and abstraction  
C) ✗ PAC supports multiple views and components  
D) ✓ Control mediates between abstraction and presentation and manages hierarchy  

**Correct:** D


#### 17. Which of the following are common techniques used to implement dialogue control in UIMS?  
A) ✓ Menu networks and state transition diagrams are common  
B) ✗ Direct hardware manipulation is not typical in UIMS  
C) ✓ Event languages and declarative languages are used  
D) ✓ Constraints and graphical specification are used  

**Correct:** A, C, D


#### 18. Constraints in UIMS are useful because they:  
A) ✗ Do not replace event-driven programming, complement it  
B) ✗ Applicable in both single-user and groupware interfaces  
C) ✓ Help maintain consistency in groupware environments  
D) ✓ Specify what should be true, not how to do it  

**Correct:** C, D


#### 19. Graphical specification tools in UIMS typically:  
A) ✗ Are widely used in modern UI development  
B) ✓ Allow designers to visually draw components and link actions  
C) ✗ Focus on local screen elements, not just global paths  
D) ✗ Do not require all manual coding  

**Correct:** A, B, C


#### 20. Which of the following statements about windowing system architectures is correct?  
A) ✓ Separate window manager maximizes portability  
B) ✗ Managing all processes in each app reduces portability  
C) ✗ Device drivers are separate from window manager  
D) ✓ Kernel-based management ties apps to specific OS  

**Correct:** A, D