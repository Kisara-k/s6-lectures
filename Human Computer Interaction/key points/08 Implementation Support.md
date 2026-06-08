## 8. Implementation Support

## Key Points

#### 1. 🪟 Windowing Systems  
- Windowing systems provide device independence through abstract terminal device drivers.  
- They support resource sharing and simultaneity of user tasks by isolating individual applications.  
- Three main architectures exist:  
  1. Each application manages all processes (low portability).  
  2. Management within OS kernel (apps tied to OS).  
  3. Management as a separate application (maximum portability).  
- X Windows uses a client-server architecture with a pixel imaging model and a separate window manager client.  
- The X protocol defines communication between server and clients.

#### 2. 💻 Programming Paradigms  
- Read-evaluation loop repeatedly reads events and processes them sequentially.  
- Notification-based programming uses event handlers or callbacks triggered by specific events.  
- Modal dialog boxes are easier to implement with event loops; non-modal dialogs are easier with notification-based systems.  
- Implementation should not drive design; system style affects interface behavior.

#### 3. 🧩 Interaction Toolkits  
- Toolkits provide programming with interaction objects (widgets) that link input and output intrinsically.  
- They promote consistency and generalizability through similar look and feel.  
- Java AWT is notification-based; early versions required subclassing widgets, later versions use callback objects.  
- Swing toolkit builds on AWT, offers higher-level features, and uses the MVC architecture.

#### 4. 🧠 User Interface Management Systems (UIMS)  
- UIMS separate application semantics from presentation to improve portability, reusability, multiple interfaces, and customizability.  
- Also known as UI Development Systems (UIDS) or UI Development Environments (UIDE).  
- Visual Basic is an example of a UIMS.

#### 5. 🧩 Seeheim Model  
- Divides UI into Presentation, Dialogue Control, and Functionality components.  
- Uses a switch to translate between lexical (basic input), syntactic (structured interaction), and semantic (meaningful changes) levels.  
- Semantic feedback is slower but essential; lexical and syntactic feedback are faster and more immediate.

#### 6. 🔄 MVC and PAC Models  
- MVC consists of Model (data), View (display), and Controller (input handling).  
- MVC is a pipeline model but requires controller-view communication for graphical interfaces.  
- PAC consists of Presentation (I/O), Abstraction (state), and Control (mediator), managing hierarchy and multiple views.  
- PAC is conceptually cleaner but MVC is more widely used in practice.

#### 7. 🛠️ UIMS Implementation Techniques  
- Dialogue control can be implemented using menu networks, state transition diagrams, grammar notations, event languages, declarative languages, constraints, and graphical specification.  
- Constraints specify what should be true rather than how to do it and are used in both single-user and groupware interfaces.  
- Graphical specification involves visually designing components and linking actions, common in tools like Visual Basic and Dreamweaver.

#### 8. 📋 Summary of Programming Support Levels  
- Windowing systems provide device independence and support multiple tasks.  
- Programming paradigms include read-evaluation loops and notification-based event handling.  
- Toolkits offer reusable interaction objects for easier programming.  
- UIMS provide conceptual architectures and tools to separate application logic from presentation.



<br>

