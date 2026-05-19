## 11. Implementation Support

## Questions

#### 1. What is a primary role of a windowing system in interactive applications?  
A) Managing multiple simultaneous user tasks  
B) Directly handling application-specific logic  
C) Providing device independence for input/output  
D) Enforcing programming language syntax rules  

#### 2. Which of the following are typical architectures for windowing systems?  
A) Each application manages all processes independently  
B) Management embedded within the operating system kernel  
C) Management handled by a separate application (window manager)  
D) Applications communicate directly with hardware devices  

#### 3. In the client-server architecture of windowing systems, what is the role of the server?  
A) Running application-specific event loops  
B) Managing hardware devices and resources  
C) Enforcing input/output policies like window focus  
D) Handling user interface design decisions  

#### 4. Which of the following statements about the X Windows system are true?  
A) It uses a pixel imaging model for output  
B) The X protocol defines communication between client and server  
C) The window manager is part of the kernel  
D) It supports overlapping and tiled windows  

#### 5. In event-driven programming, what is the main difference between a read-evaluation loop and notification-based programming?  
A) Read-evaluation loops require polling for events, notification-based uses callbacks  
B) Notification-based programming cannot handle modal dialogues  
C) Read-evaluation loops are easier to implement non-modal dialogues  
D) Notification-based programming requires explicit mode flags for modal dialogues  

#### 6. Why might modal dialogues be easier to implement with event loops than with notification-based systems?  
A) Event loops can simply add extra read-event loops  
B) Notification systems handle mode flags automatically  
C) Modal dialogues block other interactions, simplifying event flow  
D) Notification systems require complex mode management  

#### 7. Toolkits primarily help programmers by:  
A) Abstracting interaction objects like buttons and menus  
B) Managing hardware device drivers  
C) Promoting consistency and reusability in UI components  
D) Enforcing strict separation between application logic and presentation  

#### 8. Which of the following are characteristics of Java’s AWT toolkit?  
A) It is notification-based  
B) Early versions required subclassing widgets  
C) It uses the MVC architecture from the start  
D) Later versions introduced callback objects  

#### 9. What is a key advantage of User Interface Management Systems (UIMS) over basic toolkits?  
A) They allow non-programmers to develop interfaces more easily  
B) They eliminate the need for any programming knowledge  
C) They separate application semantics from presentation  
D) They guarantee portability across all hardware platforms  

#### 10. The Seeheim model divides the user interface into which main components?  
A) Presentation, Dialogue Control, Application  
B) Model, View, Controller  
C) Lexical, Syntactic, Semantic layers  
D) Input, Processing, Output  

#### 11. Which types of feedback correspond to the lexical, syntactic, and semantic levels respectively?  
A) Mouse movement, menu highlights, application state changes  
B) Application state changes, mouse movement, menu highlights  
C) Menu highlights, application state changes, mouse movement  
D) Keyboard input, screen refresh, error messages  

#### 12. In the Seeheim model, what is the purpose of the "switch" component?  
A) To separate conceptual from implementation concerns  
B) To handle direct communication between presentation and application  
C) To manage user authentication  
D) To control device drivers  

#### 13. How does the PAC (Presentation-Abstraction-Control) model differ from MVC?  
A) PAC includes a control component that manages hierarchy and multiple views  
B) MVC separates input, control, model, and view strictly in a pipeline  
C) PAC does not separate presentation and abstraction  
D) MVC is rarely used in practice compared to PAC  

#### 14. Which of the following are true about MVC architecture in graphical interfaces?  
A) Input only has meaning in relation to output shown in the view  
B) The controller communicates with the view to interpret user actions  
C) The model directly handles user input events  
D) MVC completely separates controller and view with no interaction  

#### 15. Which dialogue control techniques are commonly used in UIMS?  
A) Menu networks and state transition diagrams  
B) Grammar notations and event languages  
C) Declarative languages and constraints  
D) Direct hardware manipulation  

#### 16. What is the main benefit of using constraints in dialogue control?  
A) They specify what should be true rather than what happens  
B) They allow direct manipulation of device drivers  
C) They simplify programming by removing the need for event handling  
D) They are only useful in single-user interfaces  

#### 17. Which of the following statements about graphical specification in UIMS is correct?  
A) It allows designers to visually place components and link actions  
B) It eliminates the need for any programming or scripting  
C) It is rarely used in popular UI development tools  
D) It focuses on global system paths rather than local screen views  

#### 18. What does "device independence" mean in the context of windowing systems?  
A) Applications can run without any input devices  
B) Programmers write code without needing to know specific hardware details  
C) The system automatically detects and installs new hardware drivers  
D) Input and output devices are physically separated from the computer  

#### 19. Why is it important that implementation should not drive design in UI development?  
A) Because implementation constraints can limit usability and user experience  
B) Because design decisions should always be made by programmers  
C) Because implementation is always more important than design  
D) Because users prefer interfaces designed solely by developers  

#### 20. Which of the following best describes the "drift of dialogue control"?  
A) The shift from internal control (application-driven) to external or presentation control  
B) The gradual loss of user input events over time  
C) The increasing complexity of device drivers in windowing systems  
D) The transition from graphical to text-based interfaces



<br>

## Answers

#### 1. What is a primary role of a windowing system in interactive applications?  
A) ✓ Manages multiple simultaneous user tasks by supporting multiple windows and processes  
B) ✗ Application-specific logic is handled by the application, not the windowing system  
C) ✓ Provides device independence by abstracting hardware input/output devices  
D) ✗ Programming language syntax rules are unrelated to windowing systems  

**Correct:** A, C


#### 2. Which of the following are typical architectures for windowing systems?  
A) ✓ Each application managing all processes is one architecture but reduces portability  
B) ✓ Kernel-based management ties applications to the OS  
C) ✓ Separate application (window manager) maximizes portability  
D) ✗ Applications do not communicate directly with hardware; device drivers handle that  

**Correct:** A, B, C


#### 3. In the client-server architecture of windowing systems, what is the role of the server?  
A) ✗ Running application event loops is done by clients (applications)  
B) ✓ Server manages hardware devices and resources like keyboard, mouse, display  
C) ✓ Window manager (a client) enforces input/output policies, often considered part of server-side management  
D) ✗ UI design decisions are made by application developers, not the server  

**Correct:** B, C


#### 4. Which of the following statements about the X Windows system are true?  
A) ✓ Uses pixel imaging model for graphics output  
B) ✓ X protocol defines communication between client and server  
C) ✗ Window manager is a separate client, not part of the kernel  
D) ✓ Supports both tiled and overlapping windows  

**Correct:** A, B, D


#### 5. In event-driven programming, what is the main difference between a read-evaluation loop and notification-based programming?  
A) ✓ Read-evaluation loops poll for events; notification-based uses callbacks  
B) ✗ Notification-based can handle modal dialogues but requires mode flags  
C) ✗ Event loops find non-modal dialogues complicated, not easier  
D) ✓ Notification-based programming needs mode flags to manage modal dialogues  

**Correct:** A, D


#### 6. Why might modal dialogues be easier to implement with event loops than with notification-based systems?  
A) ✓ Event loops can add extra read-event loops to block other input easily  
B) ✗ Notification systems do not handle mode flags automatically; they require explicit management  
C) ✓ Modal dialogues block other interactions, simplifying event flow in event loops  
D) ✓ Notification systems require complex mode management to simulate modality  

**Correct:** A, C, D


#### 7. Toolkits primarily help programmers by:  
A) ✓ Abstracting interaction objects like buttons and menus  
B) ✗ Device drivers are managed by the OS or windowing system, not toolkits  
C) ✓ Promoting consistency and reusability in UI components  
D) ✗ Strict separation of application logic and presentation is a UIMS feature, not basic toolkits  

**Correct:** A, C


#### 8. Which of the following are characteristics of Java’s AWT toolkit?  
A) ✓ AWT is notification-based  
B) ✓ Early versions required subclassing widgets to customize behavior  
C) ✗ MVC architecture was introduced later in Swing, not in early AWT  
D) ✓ Later versions introduced callback objects for event handling  

**Correct:** A, B, D


#### 9. What is a key advantage of User Interface Management Systems (UIMS) over basic toolkits?  
A) ✓ UIMS make interface development easier for non-programmers  
B) ✗ Programming knowledge is still needed, though reduced  
C) ✓ UIMS separate application semantics from presentation, improving portability and reusability  
D) ✗ Portability depends on implementation; UIMS improve it but do not guarantee it universally  

**Correct:** A, C


#### 10. The Seeheim model divides the user interface into which main components?  
A) ✓ Presentation, Dialogue Control, Application are the three main parts  
B) ✗ Model, View, Controller is MVC, not Seeheim  
C) ✗ Lexical, Syntactic, Semantic are language layers, not main components  
D) ✗ Input, Processing, Output is a general model, not Seeheim-specific  

**Correct:** A


#### 11. Which types of feedback correspond to the lexical, syntactic, and semantic levels respectively?  
A) ✓ Mouse movement (lexical), menu highlights (syntactic), application state changes (semantic)  
B) ✗ Incorrect order of feedback types  
C) ✗ Incorrect order of feedback types  
D) ✗ Keyboard input and error messages do not map cleanly to these categories  

**Correct:** A


#### 12. In the Seeheim model, what is the purpose of the "switch" component?  
A) ✓ Separates conceptual from implementation concerns, managing communication between layers  
B) ✓ Handles regulated communication between presentation and application  
C) ✗ User authentication is unrelated  
D) ✗ Device drivers are outside the scope of Seeheim’s switch  

**Correct:** A, B


#### 13. How does the PAC (Presentation-Abstraction-Control) model differ from MVC?  
A) ✓ PAC’s control manages hierarchy and multiple views, unlike MVC’s simpler control  
B) ✓ MVC is often described as a pipeline model with strict input-control-model-view-output flow  
C) ✗ PAC does separate presentation and abstraction clearly  
D) ✗ MVC is more widely used in practice, especially in Java Swing  

**Correct:** A, B, D


#### 14. Which of the following are true about MVC architecture in graphical interfaces?  
A) ✓ Input only makes sense relative to what is shown in the view  
B) ✓ Controller communicates with the view to interpret user actions  
C) ✗ Model does not handle user input directly; controller does  
D) ✗ Controller and view interact closely; separation is not absolute  

**Correct:** A, B


#### 15. Which dialogue control techniques are commonly used in UIMS?  
A) ✓ Menu networks and state transition diagrams model interaction flow  
B) ✓ Grammar notations and event languages specify valid sequences and events  
C) ✓ Declarative languages and constraints define interface behavior and conditions  
D) ✗ Direct hardware manipulation is not a dialogue control technique  

**Correct:** A, B, C


#### 16. What is the main benefit of using constraints in dialogue control?  
A) ✓ Constraints specify what should be true, not just what happens, improving consistency  
B) ✗ Constraints do not manage hardware drivers  
C) ✗ Constraints complement event handling, not replace it  
D) ✗ Constraints are useful in both single-user and groupware interfaces  

**Correct:** A


#### 17. Which of the following statements about graphical specification in UIMS is correct?  
A) ✓ Designers visually place components and link actions via scripts or code  
B) ✗ Programming or scripting is usually still required for complex behavior  
C) ✗ Graphical specification is widely used in popular UI tools like Visual Basic  
D) ✗ Focus is often on local screen views, not global system paths  

**Correct:** A, C, D


#### 18. What does "device independence" mean in the context of windowing systems?  
A) ✗ Applications still require input devices; device independence means abstraction, not absence  
B) ✓ Programmers write code without needing to know specific hardware details  
C) ✗ Automatic driver detection is a separate OS function, not device independence per se  
D) ✗ Devices are physically connected; independence refers to software abstraction  

**Correct:** B


#### 19. Why is it important that implementation should not drive design in UI development?  
A) ✓ Implementation constraints can limit usability and user experience if design is not prioritized  
B) ✗ Design decisions should involve users and designers, not only programmers  
C) ✗ Implementation is important but should support, not dictate, design  
D) ✗ Users prefer interfaces designed with their needs, not solely by developers  

**Correct:** A


#### 20. Which of the following best describes the "drift of dialogue control"?  
A) ✓ Shift from internal (application-driven) control to external or presentation control methods  
B) ✗ Loss of user input events is unrelated  
C) ✗ Device driver complexity is unrelated  
D) ✗ Transition from graphical to text-based interfaces is unrelated  

**Correct:** A