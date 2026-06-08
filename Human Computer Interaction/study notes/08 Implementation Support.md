## 8. Implementation Support

## Study Notes

### 1. 🖥️ Introduction to Implementation Support in HCI

When we talk about **Implementation Support** in Human-Computer Interaction (HCI), we are focusing on the tools and systems that help programmers create user interfaces and interactive applications. This support is crucial because programming user interfaces is complex: it involves managing how users interact with the system, how the system responds, and how multiple tasks and devices work together smoothly.

Advances in programming have moved beyond just writing code for hardware. Now, programmers work with layers of tools that abstract away hardware details and interaction techniques, making it easier to build consistent, portable, and user-friendly interfaces.

Implementation support includes several layers:

- **Windowing systems**: Manage multiple windows and user tasks simultaneously.
- **Interaction toolkits**: Provide reusable components (widgets) that represent common interface elements.
- **User Interface Management Systems (UIMS)**: Higher-level systems that separate the logic of the application from how it is presented to the user.

Understanding these layers helps programmers design better interfaces and manage complexity effectively.


### 2. 🪟 Windowing Systems: Core Support for User Interaction

#### What is a Windowing System?

A **windowing system** is the foundational software layer that allows multiple applications to run at the same time, each in its own "window" on the screen. It handles the display and input devices (like mouse and keyboard) so that users can interact with several programs simultaneously without interference.

#### Key Features of Windowing Systems

- **Device Independence**: Programmers don’t need to worry about the specifics of hardware devices. The windowing system abstracts input/output devices through *abstract terminal device drivers*. This means the same program can run on different hardware without changes.
  
- **Image Models for Output**: The system uses models to represent graphics on the screen. Examples include:
  - **Pixels**: The smallest unit of display.
  - **PostScript**: A page description language used in systems like MacOS X and NextStep.
  - **Graphical Kernel System (GKS)** and **PHIGS**: Standards for graphics programming.

- **Resource Sharing and Simultaneity**: The windowing system allows multiple user tasks to run independently and simultaneously. It isolates applications so they don’t interfere with each other.

#### Roles of a Windowing System

- Manage multiple applications and their windows.
- Handle input focus (which window receives keyboard/mouse input).
- Support overlapping or tiled windows.
- Facilitate data transfer between applications.

#### Architectures of Windowing Systems

There are three main software architectures for windowing systems, differing in how they manage multiple applications:

1. **Each application manages all processes**: Every app handles its own synchronization. This reduces portability because apps must be customized for each system.
2. **Management within the OS kernel**: The operating system controls window management, but apps become tied to that OS.
3. **Management as a separate application (client-server model)**: The window manager is a separate program, maximizing portability.

#### The Client-Server Architecture and X Windows

The **X Windows system** is a classic example of a client-server windowing system:

- The **X server** controls the display and input devices.
- Applications (clients) communicate with the server using the **X protocol**.
- A separate **window manager** client enforces policies like input focus and window arrangement.
- This architecture supports pixel-based imaging and pointing devices (mouse).


### 3. 💻 Programming the Application: Event Handling Models

Programming interactive applications involves managing user input and system responses. Two main paradigms exist:

#### 1. Read-Evaluation Loop

This is a traditional approach where the program continuously waits for an event, processes it, and then waits for the next event. The structure looks like this:

```pseudo
repeat
  event = read_event()
  switch event.type
    case type_1: handle_type_1()
    case type_2: handle_type_2()
    ...
  end switch
end repeat
```

- This model uses substantial computation per device.
- It’s straightforward but can become complex when handling multiple simultaneous inputs or modes.

#### 2. Notification-Based Programming

In this model, the program sets up **handlers** or **callbacks** for specific events. When an event occurs, the corresponding handler is automatically called.

Example in Java-like pseudocode:

```java
Menu menu = new Menu();
menu.setOption("Save");
menu.setOption("Quit");
menu.setAction("Save", mySave);
menu.setAction("Quit", myQuit);

int mySave(Event e) { /* save file */ }
int myQuit(Event e) { /* quit application */ }
```

- Easier to manage multiple modes and non-modal dialogs.
- More modular and closer to how users think about interaction.

#### Modal vs. Non-Modal Dialogues

- **Modal dialogs** block interaction with other windows until closed.
- **Non-modal dialogs** allow interaction with other windows simultaneously.

The choice of programming model affects how easily these dialogs can be implemented.


### 4. 🧩 Interaction Toolkits: Programming with Interaction Objects

Interaction toolkits provide a higher level of abstraction by offering **interaction objects** (also called widgets or gadgets) that combine input and output elements. For example, buttons, menus, sliders, and text fields.

#### Why Use Toolkits?

- They promote **consistency** across applications by standardizing look and feel.
- They make programming easier by providing reusable components.
- They support **object-oriented programming**, allowing programmers to extend and customize widgets.

#### Examples of Toolkits

- **Java AWT (Abstract Windowing Toolkit)**: Provides basic widgets like buttons and menus.
  - Early versions required subclassing widgets.
  - Later versions introduced callback objects for event handling.
- **Java Swing**: Built on top of AWT, Swing offers more advanced features and uses the **Model-View-Controller (MVC)** architecture for better separation of concerns.


### 5. 🧠 User Interface Management Systems (UIMS): Bridging Design and Implementation

While toolkits help programmers, they can still be complex for non-programmers or designers. **User Interface Management Systems (UIMS)** add another layer of abstraction to separate the **application logic** from the **presentation** (what the user sees).

#### What Does a UIMS Do?

- Separates **application semantics** (meaning and logic) from **presentation** (visual and interactive elements).
- Improves:
  - **Portability**: The same application can run on different systems.
  - **Reusability**: Components can be reused across projects.
  - **Multiple Interfaces**: The same functionality can be accessed through different user interfaces.
  - **Customizability**: Designers and users can modify the interface without changing the core application.

#### Other Names for UIMS

- UI Development System (UIDS)
- UI Development Environment (UIDE)
- Examples: Visual Basic is a simple UIMS.


### 6. 🧩 UIMS Conceptual Architectures: Models for Interface Design

Several conceptual models help organize the components of a user interface:

#### The Seeheim Model

This classic model divides the interface into three main parts:

- **Presentation**: Handles the actual display and user input.
- **Dialogue Control**: Manages the flow of interaction between user and application.
- **Functionality**: The core application logic.

Between these parts is a **switch** that translates between different levels of language:

- **Lexical**: Basic input/output events (e.g., mouse movement).
- **Syntactic**: Structured interaction elements (e.g., menu highlights).
- **Semantic**: Meaningful changes in application state (e.g., updating a sum).

#### Feedback Types

- **Lexical feedback**: Immediate, low-level feedback like cursor movement.
- **Syntactic feedback**: Interface-level feedback like highlighting menu items.
- **Semantic feedback**: Changes in application data or state, often slower but crucial for understanding.

#### Arch/Slinky Model

An extension of Seeheim, this model adds more layers and distinguishes between physical and lexical levels, resembling a spring (slinky) with layers that can vary in importance depending on the system.


### 7. 🔄 MVC and PAC: Popular Interface Architectural Patterns

#### MVC (Model-View-Controller)

- **Model**: Represents the internal data and logic.
- **View**: Displays the data to the user.
- **Controller**: Handles user input and updates the model or view.

MVC is a pipeline: input → control → model → view → output. However, in graphical interfaces, the controller often needs to communicate with the view to understand what the user clicked or interacted with.

#### PAC (Presentation-Abstraction-Control)

- **Presentation**: Manages input/output.
- **Abstraction**: Holds the logical state.
- **Control**: Mediates between presentation and abstraction, managing hierarchy and multiple views.

PAC is considered cleaner conceptually and closer to Seeheim, but MVC is more widely used in practice (e.g., Java Swing).


### 8. 🛠️ Implementing UIMS: Techniques and Tools

To implement dialogue control and interface management, several techniques are used:

- **Menu networks**: Define possible menu paths.
- **State transition diagrams**: Model interface states and transitions.
- **Grammar notations and event languages**: Describe valid sequences of user actions.
- **Declarative languages and constraints**: Specify what should be true rather than how to do it.
- **Graphical specification**: Visually design interfaces by placing components and linking actions (used in tools like Visual Basic, Dreamweaver, Flash).

Constraints are especially useful in groupware (multi-user systems) and single-user interfaces to maintain consistency.


### 9. 📋 Summary: Levels of Programming Support in HCI

To wrap up, here are the main levels of programming support tools in HCI:

- **Windowing Systems**: Provide device independence and support multiple simultaneous tasks.
- **Programming Paradigms**: Include read-evaluation loops and notification-based event handling.
- **Interaction Toolkits**: Offer reusable interaction objects to simplify programming.
- **User Interface Management Systems (UIMS)**: Provide conceptual architectures and tools to separate application logic from presentation, improving portability, reusability, and customizability.

Understanding these layers and models helps programmers and designers create better, more maintainable, and user-friendly interfaces.