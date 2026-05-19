## 11. Implementation Support

## Key Points

#### 1. 🪟 Windowing Systems  
- Windowing systems provide core support for separate and simultaneous user-system activity.  
- They enable device independence by abstracting hardware devices like keyboards and mice.  
- Windowing systems support resource sharing and isolation of individual applications.  
- Three architectures exist:  
  1. Each application manages all processes (low portability).  
  2. Management within OS kernel (applications tied to OS).  
  3. Management as a separate application (maximum portability).  
- The client-server architecture separates applications (clients) from device/resource management (server).  
- X Windows uses a pixel imaging model and a protocol for client-server communication, with a separate window manager client.

#### 2. 💻 Programming Models in Windowing Systems  
- Event-driven programming uses a read-evaluation loop to process events continuously.  
- Notification-based programming registers callbacks that are triggered by specific events.  
- Modal dialog boxes are easier to implement with event loops but harder with notification systems.  
- Non-modal dialog boxes are easier with notification systems but complicated with event loops.

#### 3. 🧩 Toolkits  
- Toolkits provide abstraction by allowing programming with interaction objects (widgets).  
- They promote consistency and generalizability through similar look and feel.  
- Toolkits are amenable to object-oriented programming.  
- Java AWT is notification-based; early versions required subclassing, later versions use callbacks.  
- Swing toolkit is built on AWT, offers higher-level features, and uses MVC architecture.

#### 4. 🛠️ User Interface Management Systems (UIMS)  
- UIMS add a level above toolkits to simplify UI development, especially for non-programmers.  
- UIMS separate application semantics from presentation, improving portability, reusability, and customizability.  
- UIMS are also called UI Development Systems (UIDS) or UI Development Environments (UIDE).  
- Visual Basic is an example of a UIMS.

#### 5. 🧠 Seeheim Model (Conceptual Architecture)  
- Divides UI into Presentation, Dialogue Control, and Application components.  
- Distinguishes lexical (basic input), syntactic (interaction structure), and semantic (meaningful feedback) levels.  
- Semantic feedback is often slower but necessary for meaningful updates; lexical and syntactic feedback are faster.

#### 6. 🔄 MVC and PAC Models  
- MVC divides UI into Model (data), View (presentation), and Controller (input handling).  
- MVC is a pipeline model but requires close communication between controller and view.  
- PAC divides UI into Presentation (I/O management), Abstraction (logical state), and Control (mediates and manages hierarchy).  
- PAC is conceptually cleaner but MVC is more widely used in practice (e.g., Java Swing).

#### 7. ⚙️ UIMS Implementation Techniques  
- Dialogue control techniques include menu networks, state transition diagrams, grammar notations, event languages, declarative languages, and constraints.  
- Constraints specify conditions that must always be true and are used in both single-user and groupware interfaces.  
- Graphical specification allows visual UI design with components placed on screen and linked to actions.  
- Control in dialogue can be internal (application-driven), external (independent), or presentation-based (graphical specification).



<br>

## Study Notes

### 1. 🖥️ Introduction to Implementation Support in HCI

When we talk about **Implementation Support** in Human-Computer Interaction (HCI), we are focusing on the tools and systems that help programmers create interactive applications. These tools bridge the gap between the user’s experience and the underlying software that makes it all work. Implementation support includes programming tools, windowing systems, toolkits, and user interface management systems (UIMS). Each of these plays a role in making programming easier, more efficient, and more aligned with how users perceive and interact with software.

The goal is to support programmers in managing complex interactions, multiple simultaneous tasks, and device independence, while also promoting consistency and reusability in user interfaces.


### 2. 🪟 Windowing Systems: Core Support for Multiple Users and Applications

#### What is a Windowing System?

A **windowing system** is a fundamental layer of software that allows multiple applications to run simultaneously on a computer screen, each within its own "window." It manages how these windows are displayed, how users interact with them, and how resources like the keyboard and mouse are shared.

#### Key Features of Windowing Systems

- **Device Independence:** Programmers write code without worrying about the specific hardware (like different types of keyboards or mice). The windowing system abstracts these devices into a common interface.
- **Resource Sharing:** Multiple applications can run at the same time, sharing input devices and screen space without interfering with each other.
- **Isolation:** Each application runs independently, so if one crashes, it doesn’t bring down the whole system.

#### Architectures of Windowing Systems

There are three main software architectures for windowing systems, differing in how they manage multiple applications:

1. **Each Application Manages Its Own Processes:** Every program handles synchronization and resource management itself. This reduces portability because each app must be tailored to the system.
2. **Management Within the Operating System Kernel:** The OS kernel controls application management, which ties applications closely to the OS.
3. **Management as a Separate Application:** A dedicated window manager handles multiple applications, maximizing portability since the OS and applications are loosely coupled.

#### Client-Server Architecture

Modern windowing systems often use a **client-server model**:

- The **server** manages hardware devices and resources.
- The **client** is the application requesting services (like drawing a window or receiving input).
- Communication between client and server happens through a protocol.

#### Example: X Windows System

- Uses a **pixel imaging model** for graphics.
- Supports pointing devices like mice.
- Defines a protocol for client-server communication.
- Has a separate **window manager** client that controls window behavior (e.g., overlapping windows, input focus).


### 3. 💻 Programming Applications in Windowing Systems

#### Event-Driven Programming

Applications in windowing systems often use an **event-driven** model, where the program waits for user actions (events) like mouse clicks or key presses and responds accordingly.

- **Read-Evaluation Loop:** The program continuously reads events, evaluates their type, and processes them.
- **Notification-Based Programming:** Instead of polling for events, the program registers **callbacks** (functions) that get called automatically when specific events occur.

#### Example of Notification-Based Programming

- Create a menu with options like "Save" and "Quit."
- Register callback functions for these options.
- When the user selects "Save," the `mySave` function is called.
- When the user selects "Quit," the `myQuit` function is called.

This approach simplifies programming by letting the system handle event detection and dispatch.

#### Modal vs. Non-Modal Dialogues

- **Modal Dialogues:** Block interaction with other windows until closed. Easier to implement with event loops but harder with notification systems.
- **Non-Modal Dialogues:** Allow interaction with other windows simultaneously. Easier with notification systems but more complex with event loops.

Programmers must design interfaces carefully to avoid letting implementation constraints dictate design choices.


### 4. 🧩 Toolkits: Programming with Interaction Objects

#### What Are Toolkits?

Toolkits provide a higher level of abstraction for programming user interfaces. Instead of dealing with low-level events and drawing commands, programmers work with **interaction objects** (also called widgets or gadgets) like buttons, menus, sliders, etc.

#### Benefits of Toolkits

- **Consistency:** All widgets follow a similar look and feel, making interfaces more predictable for users.
- **Reusability:** Widgets can be reused across different applications.
- **Object-Oriented Programming Friendly:** Toolkits often use object-oriented principles, making it easier to extend and customize components.

#### Example: Java Toolkits

- **AWT (Abstract Windowing Toolkit):** Provides basic UI components. Early versions required subclassing widgets; later versions introduced callback objects.
- **Swing:** Built on top of AWT, offers more advanced features and uses the **Model-View-Controller (MVC)** architecture for better separation of concerns.


### 5. 🛠️ User Interface Management Systems (UIMS)

#### What is a UIMS?

A **User Interface Management System** is a software layer above toolkits designed to make UI development easier, especially for non-programmers or those who want to focus on design rather than coding.

#### Why Use UIMS?

- **Separation of Concerns:** UIMS separates the **application logic** (what the program does) from the **presentation** (how it looks and interacts).
- **Portability:** Interfaces can run on different systems without rewriting code.
- **Reusability:** UI components can be reused in different applications.
- **Multiple Interfaces:** The same functionality can be accessed through different types of interfaces (e.g., graphical, voice).
- **Customizability:** Both designers and users can customize the interface.

#### Other Names for UIMS

- UI Development System (UIDS)
- UI Development Environment (UIDE)
- Examples include tools like Visual Basic.


### 6. 🧠 Conceptual Models of UIMS: The Seeheim Model

#### Why Conceptual Models?

Conceptual models help us understand the structure and flow of user interfaces, separating **what** the interface does from **how** it is implemented.

#### The Seeheim Model

This model divides the UI into three main components:

1. **Presentation:** Handles the user interface elements and how they are displayed.
2. **Dialogue Control:** Manages the interaction flow between the user and the application.
3. **Application:** Contains the core functionality and logic.

The model also distinguishes between different levels of language in the interface:

- **Lexical:** Basic input/output actions (e.g., mouse movement).
- **Syntactic:** Structure of interactions (e.g., menu highlights).
- **Semantic:** Meaningful feedback (e.g., updating a sum when numbers change).

#### Feedback Types

- **Lexical Feedback:** Immediate, low-level feedback like cursor movement.
- **Syntactic Feedback:** Structural feedback like highlighting menu items.
- **Semantic Feedback:** Changes in the application state, which may be slower but more meaningful.


### 7. 🔄 MVC and PAC: Models for Interface Architecture

#### Model-View-Controller (MVC)

MVC is a popular design pattern that separates an interface into three parts:

- **Model:** The data and logic of the application.
- **View:** How the data is presented to the user.
- **Controller:** Handles user input and updates the model or view accordingly.

MVC is often described as a pipeline: input → control → model → view → output. However, in graphical interfaces, input depends on what is shown, so the controller and view often communicate closely.

#### Presentation-Abstraction-Control (PAC)

PAC is another architectural pattern closer to the Seeheim model. It divides components into:

- **Presentation:** Manages input and output.
- **Abstraction:** The logical state or data.
- **Control:** Mediates between presentation and abstraction, manages hierarchy and multiple views.

PAC is considered cleaner and better for complex systems, but MVC is more widely used in practice (e.g., Java Swing).


### 8. ⚙️ Implementing UIMS: Techniques and Tools

#### Dialogue Control Techniques

To manage the flow of interaction, UIMS use various techniques:

- **Menu Networks:** Define possible menu paths.
- **State Transition Diagrams:** Model interface states and transitions.
- **Grammar Notations:** Describe valid sequences of user actions.
- **Event Languages:** Specify event handling.
- **Declarative Languages:** Define what should happen rather than how.
- **Constraints:** Specify conditions that must always be true (useful in groupware and single-user interfaces).

#### Graphical Specification

- Allows designers to visually create interfaces by placing components on the screen.
- Actions can be linked via scripts or program code.
- Popular in tools like Visual Basic, Dreamweaver, and Flash.

#### Control Drift in Dialogue

- **Internal Control:** The application manages the event loop.
- **External Control:** Control is independent of application logic.
- **Presentation Control:** Control is managed through graphical specification tools.


### Summary

Implementation support in HCI involves multiple layers and tools that help programmers create interactive, user-friendly applications. Starting from **windowing systems** that manage multiple applications and devices, through **toolkits** that provide reusable UI components, to **User Interface Management Systems** that separate interface design from application logic, these layers work together to simplify programming and improve user experience.

Conceptual models like **Seeheim**, and architectural patterns like **MVC** and **PAC**, help us understand and design interfaces more effectively. Finally, various implementation techniques and tools support the practical creation and management of user interfaces.