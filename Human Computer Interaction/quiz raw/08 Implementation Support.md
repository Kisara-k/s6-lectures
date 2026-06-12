## 8. Implementation Support

## Questions

#### 1. Which of the following are primary roles of a windowing system?  
A) Managing simultaneous user tasks and resource sharing  
B) Enforcing application-specific business logic  
C) Achieving device independence through abstract terminal device drivers  
D) Isolating individual applications to prevent interference  

#### 2. In the context of windowing system architectures, which statements about the three main approaches are true?  
A) A separate management application maximizes portability across systems  
B) Device drivers are integrated within each application for better performance  
C) Having each application manage all processes reduces portability due to synchronization complexity  
D) Placing management within the OS kernel ties applications to that operating system  

#### 3. Regarding the X Windows architecture, which of the following are correct?  
A) The X protocol defines communication between server and client  
B) Pixel imaging models are not supported in X Windows  
C) The window manager client enforces policies such as input focus and window tiling  
D) Input/output policies are managed exclusively by the operating system kernel  

#### 4. Comparing read-evaluation loops and notification-based programming paradigms, which statements are accurate?  
A) Read-evaluation loops inherently simplify handling multiple simultaneous dialogues  
B) Read-evaluation loops use substantial computation power per device and are event-driven  
C) Notification-based programming requires extensive mode flags to handle modal dialogues  
D) Non-modal dialogues are easier to implement with notification-based programming than with event loops  

#### 5. Interaction toolkits provide which of the following benefits?  
A) Promoting consistency and generalizability through similar look and feel  
B) Bringing programming closer to the level of user perception  
C) Programming with interaction objects that link input and output intrinsically  
D) Eliminating the need for object-oriented programming techniques  

#### 6. Which statements about User Interface Management Systems (UIMS) are true?  
A) UIMS are primarily designed to make programming easier for expert programmers only  
B) UIMS support multiple interfaces accessing the same functionality and allow customization  
C) Visual Basic is an example of a UI development environment that functions as a UIMS  
D) UIMS separate application semantics from presentation to improve portability and reusability  

#### 7. In the Seeheim model of UI architecture, what are the roles of the components?  
A) The switch component is purely conceptual and not needed for implementation  
B) Functionality corresponds to the application interface and logic  
C) Dialogue controls the relationship between presentation and functionality  
D) Presentation handles the user interface rendering and interaction  

#### 8. Which of the following correctly describe the differences between MVC and PAC models?  
A) MVC is conceptually closer to Seeheim than PAC  
B) PAC model’s control component manages communication between abstraction and presentation  
C) MVC separates model, view, and controller but input meaning depends on output context  
D) PAC integrates control as a mediator managing hierarchy and multiple views  

#### 9. Which techniques are commonly used for implementing dialogue controllers in UIMS?  
A) Direct manipulation of device drivers  
B) Menu networks and state transition diagrams  
C) Declarative languages and constraints  
D) Grammar notations and event languages  

#### 10. Regarding graphical specification in UI development, which statements are correct?  
A) It eliminates the need for any programming knowledge in UI design  
B) It is the least popular technique compared to raw programming methods  
C) It involves drawing components on screen and linking actions via scripts or program code  
D) It tends to focus on local screen views rather than global system paths  



<br>

## Answers

#### 1. Which of the following are primary roles of a windowing system?  
A) ✓ Managing simultaneous user tasks and resource sharing is essential for supporting multiple processes.  
B) ✗ Enforcing application-specific business logic is outside the scope of windowing systems.  
C) ✓ Achieving device independence through abstract terminal device drivers is a core element of windowing systems.  
D) ✓ Isolating individual applications to prevent interference is a key role of windowing systems.  

**Correct:** A, C, D


#### 2. In the context of windowing system architectures, which statements about the three main approaches are true?  
A) ✓ Having management as a separate application maximizes portability across systems.  
B) ✗ Device drivers are separate from applications, not integrated within each application.  
C) ✓ When each application manages all processes, synchronization complexity reduces portability.  
D) ✓ Management within the OS kernel ties applications to that specific operating system.  

**Correct:** A, C, D


#### 3. Regarding the X Windows architecture, which of the following are correct?  
A) ✓ The X protocol defines communication between server and client.  
B) ✗ Pixel imaging models are supported in X Windows; it uses pixel-based rendering.  
C) ✓ The window manager client enforces policies like input focus and window tiling.  
D) ✗ Input/output policies are managed by the window manager client, not exclusively by the OS kernel.  

**Correct:** A, C


#### 4. Comparing read-evaluation loops and notification-based programming paradigms, which statements are accurate?  
A) ✗ Read-evaluation loops make handling multiple simultaneous dialogues complicated, not simpler.  
B) ✓ Read-evaluation loops use substantial computation per device and are event-driven.  
C) ✓ Notification-based programming requires many mode flags to handle modal dialogues.  
D) ✓ Non-modal dialogues are easier to implement with notification-based programming than with event loops.  

**Correct:** B, C, D


#### 5. Interaction toolkits provide which of the following benefits?  
A) ✓ They promote consistency and generalizability through similar look and feel.  
B) ✓ They bring programming closer to the level of user perception by abstracting interaction.  
C) ✓ They program with interaction objects linking input and output intrinsically.  
D) ✗ They do not eliminate object-oriented programming; they often rely on it.  

**Correct:** A, B, C


#### 6. Which statements about User Interface Management Systems (UIMS) are true?  
A) ✗ UIMS are designed to help non-programmers as well, not just expert programmers.  
B) ✓ UIMS support multiple interfaces for the same functionality and allow customization.  
C) ✓ Visual Basic is an example of a UI development environment functioning as a UIMS.  
D) ✓ UIMS separate application semantics from presentation, improving portability and reusability.  

**Correct:** B, C, D


#### 7. In the Seeheim model of UI architecture, what are the roles of the components?  
A) ✗ The switch component is needed for implementation, not just conceptual.  
B) ✓ Functionality corresponds to the application interface and logic.  
C) ✓ Dialogue controls the relationship between presentation and functionality.  
D) ✓ Presentation handles rendering and user interaction.  

**Correct:** B, C, D


#### 8. Which of the following correctly describe the differences between MVC and PAC models?  
A) ✗ PAC is conceptually closer to Seeheim than MVC, not the other way around.  
B) ✓ PAC’s control component manages communication between abstraction and presentation.  
C) ✓ MVC separates model, view, and controller, but input meaning depends on output context.  
D) ✓ PAC integrates control as a mediator managing hierarchy and multiple views.  

**Correct:** B, C, D


#### 9. Which techniques are commonly used for implementing dialogue controllers in UIMS?  
A) ✗ Direct manipulation of device drivers is not a dialogue controller technique.  
B) ✓ Menu networks and state transition diagrams are common techniques.  
C) ✓ Declarative languages and constraints are techniques for dialogue control.  
D) ✓ Grammar notations and event languages are also used.  

**Correct:** B, C, D


#### 10. Regarding graphical specification in UI development, which statements are correct?  
A) ✗ It does not eliminate the need for programming knowledge; scripting or linking is still required.  
B) ✗ It is one of the most popular techniques, not the least popular.  
C) ✓ It involves drawing components and linking actions via scripts or program code.  
D) ✓ It tends to focus on local screen views rather than global system paths.  

**Correct:** C, D