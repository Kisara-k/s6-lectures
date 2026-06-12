## 8. Implementation Support

## Questions

#### 1. Which of the following are primary roles of a windowing system in managing user interaction?  
A) Managing simultaneous execution and isolation of multiple applications  
B) Enforcing application-specific business logic  
C) Handling input focus and window arrangement policies  
D) Providing device independence by abstracting hardware details  

#### 2. In the client-server architecture of windowing systems like X Windows, which statements are true?  
A) The window manager enforces policies such as tiled vs. overlapping windows  
B) The X server manages display and input devices  
C) The window manager is integrated into the kernel for maximum performance  
D) Applications act as clients communicating with the server via a defined protocol  

#### 3. Regarding programming paradigms for handling user input, which of the following correctly describe differences between read-evaluation loops and notification-based programming?  
A) Notification-based programming uses callbacks triggered by specific events  
B) Notification-based programming requires extensive mode flags to handle modal dialogs  
C) Read-evaluation loops continuously poll for events and process them sequentially  
D) Read-evaluation loops naturally simplify handling non-modal dialogs  

#### 4. Interaction toolkits provide several benefits for interface programming. Which of the following are accurate?  
A) They guarantee portability across all operating systems without modification  
B) They eliminate the need for event handling in applications  
C) They support object-oriented programming by encapsulating interaction objects  
D) They promote consistency by standardizing widget appearance and behavior  

#### 5. Which of the following statements about User Interface Management Systems (UIMS) are correct?  
A) UIMS facilitate reusability of interface components across different applications  
B) UIMS separate application semantics from presentation to improve portability  
C) UIMS make it impossible for users to customize interfaces  
D) UIMS are primarily designed to replace windowing systems  

#### 6. In the Seeheim model of interface architecture, what is the role of the "switch" component?  
A) To mediate communication between presentation and functionality layers  
B) To implement the graphical rendering of interface elements  
C) To translate between lexical, syntactic, and semantic levels of interaction  
D) To directly manage hardware device drivers  

#### 7. Which of the following best describe the differences between MVC and PAC architectural patterns?  
A) PAC includes a control component that manages hierarchy and multiple views within components  
B) PAC is conceptually closer to the Seeheim model than MVC  
C) MVC separates model, view, and controller, with the controller mediating input and updating the model and view  
D) MVC inherently supports multiple views of the same data without additional control logic  

#### 8. When implementing dialogue control in UIMS, which techniques can be used to specify interaction behavior?  
A) Direct manipulation of device drivers  
B) Graphical specification tools like Visual Basic and Dreamweaver  
C) Declarative languages and constraints  
D) State transition diagrams and menu networks  

#### 9. Consider the following statements about feedback types in user interfaces. Which are true?  
A) Syntactic feedback includes interface-level cues such as menu highlighting  
B) Rapid semantic feedback is unnecessary in freehand drawing applications  
C) Semantic feedback is always faster than syntactic feedback  
D) Lexical feedback involves low-level events like mouse movement and is typically very fast  

#### 10. Which of the following statements about windowing system architectures are correct?  
A) Managing windowing within the OS kernel ties applications to that operating system  
B) A separate window manager application maximizes portability across systems  
C) Having each application manage all processes reduces portability of applications  
D) Device drivers are typically integrated into the window manager application  



<br>

## Answers

#### 1. Which of the following are primary roles of a windowing system in managing user interaction?  
A) ✓ Manages simultaneous execution and isolation of multiple applications, enabling multitasking and preventing interference.  
B) ✗ Enforcing application-specific business logic is the responsibility of the application, not the windowing system.  
C) ✓ Handles input focus and window arrangement policies, deciding which window receives input and how windows are displayed.  
D) ✓ Provides device independence by abstracting hardware details, allowing programs to run on different devices without modification.  

**Correct:** A, C, D


#### 2. In the client-server architecture of windowing systems like X Windows, which statements are true?  
A) ✓ The window manager enforces policies such as tiled vs. overlapping windows and input focus.  
B) ✓ The X server manages display and input devices, acting as the central controller of hardware resources.  
C) ✗ The window manager is a separate client application, not integrated into the kernel.  
D) ✓ Applications act as clients communicating with the server via a defined protocol (X protocol).  

**Correct:** A, B, D


#### 3. Regarding programming paradigms for handling user input, which of the following correctly describe differences between read-evaluation loops and notification-based programming?  
A) ✓ Notification-based programming uses callbacks or handlers triggered by specific events.  
B) ✗ Notification-based programming handles modal dialogs more easily without needing many mode flags.  
C) ✓ Read-evaluation loops continuously poll for events and process them sequentially in a loop.  
D) ✗ Read-evaluation loops make non-modal dialogs complicated to implement due to complex main loops.  

**Correct:** A, C


#### 4. Interaction toolkits provide several benefits for interface programming. Which of the following are accurate?  
A) ✗ Toolkits improve portability but do not guarantee it across all operating systems without modification.  
B) ✗ They do not eliminate the need for event handling; event handling is still required but simplified.  
C) ✓ They support object-oriented programming by encapsulating interaction objects as reusable components.  
D) ✓ They promote consistency by standardizing widget appearance and behavior across applications.  

**Correct:** C, D


#### 5. Which of the following statements about User Interface Management Systems (UIMS) are correct?  
A) ✓ UIMS facilitate reusability of interface components, reducing development costs.  
B) ✓ UIMS separate application semantics from presentation, improving portability and flexibility.  
C) ✗ UIMS allow customization by designers and users; they do not prevent it.  
D) ✗ UIMS do not replace windowing systems; they build on top of them to provide higher-level support.  

**Correct:** A, B


#### 6. In the Seeheim model of interface architecture, what is the role of the "switch" component?  
A) ✓ It mediates communication between presentation and functionality layers, coordinating interaction flow.  
B) ✗ It does not implement graphical rendering; that is the role of the presentation component.  
C) ✓ It translates between lexical, syntactic, and semantic levels of interaction, enabling communication between layers.  
D) ✗ It does not manage hardware device drivers; that is handled by lower-level system components.  

**Correct:** A, C


#### 7. Which of the following best describe the differences between MVC and PAC architectural patterns?  
A) ✓ PAC includes a control component that manages hierarchy and multiple views within components.  
B) ✓ PAC is conceptually closer to the Seeheim model, emphasizing separation and control mediation.  
C) ✓ MVC separates model, view, and controller, with the controller mediating input and updating model and view.  
D) ✗ MVC does not inherently support multiple views without additional control logic; the controller must coordinate.  

**Correct:** A, B, C


#### 8. When implementing dialogue control in UIMS, which techniques can be used to specify interaction behavior?  
A) ✗ Direct manipulation of device drivers is low-level and outside the scope of dialogue control in UIMS.  
B) ✓ Graphical specification tools allow visual design of interfaces and linking actions, widely used in UIMS.  
C) ✓ Declarative languages and constraints specify what should be true rather than how to do it, useful in UIMS.  
D) ✓ State transition diagrams and menu networks are common techniques for modeling dialogue flow.  

**Correct:** B, C, D


#### 9. Consider the following statements about feedback types in user interfaces. Which are true?  
A) ✓ Syntactic feedback includes interface-level cues such as menu highlighting to guide user interaction.  
B) ✗ Rapid semantic feedback is necessary in applications like freehand drawing to provide immediate meaningful response.  
C) ✗ Semantic feedback is often slower than syntactic feedback because it involves meaningful changes in application state.  
D) ✓ Lexical feedback involves low-level events like mouse movement and is typically very fast and immediate.  

**Correct:** A, B, D


#### 10. Which of the following statements about windowing system architectures are correct?  
A) ✓ Managing windowing within the OS kernel ties applications to that operating system, reducing portability.  
B) ✓ A separate window manager application maximizes portability by decoupling window management from OS kernel.  
C) ✓ Having each application manage all processes reduces portability because synchronization must be handled individually.  
D) ✗ Device drivers are typically separate from the window manager application, handled at a lower system level.  

**Correct:** A, B, C