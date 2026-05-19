## 12. User Support

## Key Points

#### 1. 🧑‍💻 User Support Types  
- User support includes quick reference, task-specific help, full explanation, and tutorials.  
- Help is problem-oriented and specific; documentation is system-oriented and general.  
- Both help and documentation should follow the same design principles.

#### 2. ⏰ Requirements for User Support  
- Availability: continuous access concurrent with the main application.  
- Accuracy and completeness: help must match actual system behavior.  
- Consistency: between different parts of help and paper documentation.  
- Robustness: correct error handling and predictable behavior.  
- Flexibility: allows interaction appropriate to user experience and task.  
- Unobtrusiveness: does not prevent user from continuing work.

#### 3. 🛠 Approaches to User Support  
- Command assistance provides help on specific commands (e.g., UNIX man, DOS help).  
- Command prompts give usage info when errors occur, mainly for simple syntax errors.  
- Context-sensitive help adapts to the current user context (e.g., tooltips).  
- Online tutorials guide users through basics in a test environment but can be inflexible.  
- Online documentation is digital paper documentation, often enhanced with hypertext.

#### 4. 🧙 Wizards and Assistants  
- Wizards guide users step-by-step through complex or infrequent tasks using user input.  
- Wizards constrain task execution but must allow users to go back.  
- Assistants monitor user behavior and offer contextual advice but can be irritating.  
- Assistants must be under user control (e.g., MS paperclip, XP smart tags).

#### 5. 🤖 Adaptive Help Systems  
- Use knowledge of context, user, task, domain, and instruction to adapt help.  
- Problems include knowledge requirements, control of interaction, and scope of adaptation.  
- User modeling types: single generic user, user-configured (adaptable), system-configured (adaptive).  
- User modeling approaches: quantification (expertise levels), stereotypes (user categories), overlay (compare actual to ideal use), error catalog comparison.

#### 6. 🧠 Knowledge Representation  
- Domain and task modeling covers common errors, tasks, and current task context.  
- Advisory strategy chooses the style of advice (reminder, tutorial, etc.).  
- Knowledge representation techniques:  
  - Rule-based (logic, production rules) for large domains.  
  - Frame-based (semantic networks) for small domains.  
  - Network-based (relationships between facts).  
  - Example-based (decision structures trained on examples).

#### 7. ⚠️ Problems in Knowledge Representation and Adaptive Help  
- Knowledge acquisition is difficult and resource-intensive.  
- Interpretation of user behavior is complex.  
- Initiative: deciding if user or system controls help interaction.  
- Effect: deciding what to adapt and what info is needed.  
- Scope: adaptation can be at application or system level; system level is more complex.

#### 8. 🎨 Designing User Support  
- User support should be designed integrally with the system, not as an add-on.  
- Focus on content and context over technology.  
- Help request methods: command, button, function toggle, separate application.  
- Help display methods: new window, full screen, split screen, pop-ups, hint icons.  
- Effective presentation requires clear, familiar, consistent, instructional language, avoiding large text blocks, and clear summaries/examples.

#### 9. 💻 Implementation and Resources  
- Help can be implemented as OS command, meta command, or application feature.  
- Help data structure options: single file, file hierarchy, or database.  
- Available resources affect design: screen space, memory, speed.  
- Flexibility and extensibility are important for future updates.  
- Hard copy documentation supports offline browsing.



<br>

## Study Notes

### 1. 🧑‍💻 Introduction to User Support

User support is a crucial part of any software system designed for end users. It refers to the various ways a system helps users understand, navigate, and effectively use the software. Good user support is not just an afterthought or an add-on; it must be carefully designed and integrated into the system from the start. It involves both **implementation** (how the support is built into the system) and **presentation** (how the support is shown to the user).

User support can take many forms, from quick tips and task-specific help to full tutorials and detailed documentation. The goal is to assist users at different stages and with different needs, ensuring they can complete their tasks efficiently and with minimal frustration.


### 2. 📚 Types of User Support and Their Characteristics

User support can be categorized into several types, each serving different purposes:

- **Quick Reference:** Short, easy-to-access information for users who need immediate answers.
- **Task-Specific Help:** Guidance focused on a particular task or command.
- **Full Explanation:** Detailed information about how the system works.
- **Tutorials:** Step-by-step instructions that teach users how to use the system from the ground up.

These types are usually provided through **help systems** and **documentation**:

- **Help:** Problem-oriented and specific, focusing on solving immediate user issues.
- **Documentation:** System-oriented and general, providing comprehensive information about the system.

Both help and documentation should follow the same design principles to ensure consistency and usability.


### 3. ⏰ Requirements for Effective User Support

For user support to be effective, it must meet several important requirements:

- **Availability:** Support should be accessible continuously and concurrently with the main application, so users can get help whenever they need it.
- **Accuracy and Completeness:** The help content must accurately reflect the system’s behavior and cover all relevant aspects.
- **Consistency:** The language, style, and information should be consistent across different parts of the help system and any printed documentation.
- **Robustness:** The system should handle errors gracefully and avoid unpredictable behavior when users seek help.
- **Flexibility:** Users have different levels of experience and different tasks, so the support system should allow interaction in ways that suit these differences.
- **Unobtrusiveness:** Help should not interrupt or prevent users from continuing their work; it should be available but not intrusive.


### 4. 🛠 Approaches to User Support

There are several common approaches to providing user support, each with its strengths and limitations:

#### Command Assistance
This approach provides help when a user requests information about a specific command. Examples include the UNIX `man` pages or DOS `help` commands. It is useful for quick reference but assumes the user already knows what command they need help with.

#### Command Prompts
When a user makes an error, the system provides immediate feedback about the correct usage of a command. This is helpful for simple syntax errors but also assumes some prior knowledge of the command.

#### Context-Sensitive Help
This type of help adapts to the current context or situation of the user. For example, tooltips that appear when hovering over a button provide relevant information about that specific element.

#### Online Tutorials
These are interactive lessons that guide users through the basics of the application in a controlled environment. Tutorials are useful for beginners but can sometimes be inflexible or too rigid.

#### Online Documentation
This is the digital version of printed manuals, available within the system. It is always accessible and can be enhanced with hypertext links to make browsing easier, though it can sometimes be difficult to navigate.


### 5. 🧙 Wizards and Assistants

Two special types of user support tools are **wizards** and **assistants**:

- **Wizards:** These are task-specific tools that guide users step-by-step through complex or infrequent tasks by asking questions and using the answers to complete the task safely. For example, a resume-building wizard helps users create a resume by prompting them for information. Wizards constrain the task execution to reduce errors but must allow users to go back and change answers.

- **Assistants:** These tools monitor user behavior and offer contextual advice or suggestions. A famous example is the Microsoft Office paperclip assistant. While assistants can be helpful, they can also be annoying if they interrupt too often or are not under user control. Modern assistants like XP smart tags offer contextual help but must respect user preferences.


### 6. 🤖 Adaptive Help Systems

Adaptive help systems aim to provide personalized support by using knowledge about the user, the task, the domain, and the context. These systems try to tailor help to the user’s specific needs, which can improve effectiveness but also introduces challenges:

- **Knowledge Requirements:** The system needs detailed information about the user and the task.
- **Control:** Deciding who controls the interaction—the user or the system—is critical.
- **Scope:** Determining what aspects to adapt and how broadly (application-level or system-wide) is complex.

#### User Modeling
All help systems have some model of the user, which can be:

- **Generic (Non-intelligent):** Assumes a single type of user.
- **User-configured (Adaptable):** The user sets preferences or expertise levels.
- **System-configured (Adaptive):** The system automatically adjusts based on observed behavior.

Approaches to user modeling include:

- **Quantification:** Measuring user expertise on a scale.
- **Stereotypes:** Classifying users into categories (e.g., beginner, expert).
- **Overlay Models:** Comparing actual user behavior to an ideal expert model.
- **Error Catalogues:** Comparing user errors to known common mistakes.


### 7. 🧠 Knowledge Representation in Help Systems

To provide intelligent help, systems need to represent knowledge about the domain, tasks, and user behavior. This involves:

- **Domain and Task Modeling:** Understanding common errors, typical tasks, and the current task context. This often requires analyzing sequences of commands or actions.
- **Advisory Strategy:** Choosing the right style of advice (e.g., reminder, tutorial) based on the situation.

Common techniques for knowledge representation include:

- **Rule-Based Systems:** Use logical rules and facts interpreted by an inference engine. Suitable for large domains.
- **Frame-Based Systems:** Use structured data with slots to fill, good for smaller domains.
- **Network-Based Systems:** Represent knowledge as relationships between facts, linking frames.
- **Example-Based Systems:** Use decision structures trained on examples rather than explicit rules, requiring less manual knowledge acquisition.


### 8. ⚠️ Challenges in Knowledge Representation and Adaptive Help

There are several challenges in building adaptive help systems:

- **Knowledge Acquisition:** Gathering and encoding the necessary knowledge is difficult and resource-intensive.
- **Resource Constraints:** Systems must operate within limits of memory, processing speed, and screen space.
- **User Behavior Interpretation:** Understanding what the user is doing and why can be complex.
- **Initiative:** Deciding whether the system should wait for the user to ask for help or proactively offer it.
- **Effect and Scope:** Determining what to adapt and how broadly (just one application or the whole system).


### 9. 🎨 Designing and Presenting User Support

User support should be designed as an integral part of the system, not just added later. The focus should be on the **content** and **context** of the help rather than just the technology.

#### How Help is Requested
Help can be accessed in various ways:

- Commands typed by the user.
- Buttons or icons clicked.
- Functions toggled on or off.
- Separate help applications.

#### How Help is Displayed
Help can be shown in different formats:

- New windows or full-screen displays.
- Split screens showing help alongside the main application.
- Pop-up boxes or hint icons.

#### Effective Presentation Principles
- Use clear, familiar, and consistent language.
- Prefer instructional language (telling users what to do) over descriptive language (just describing the system).
- Avoid large blocks of text; break information into manageable chunks.
- Clearly indicate summaries and examples to help users find key information quickly.


### 10. 💻 Implementation and Resource Considerations

When implementing help systems, consider:

- Whether help is integrated as an operating system command, a meta-command, or part of the application itself.
- The structure of help data: it can be stored in a single file, a hierarchy of files, or a database.
- Available resources such as screen space, memory capacity, and processing speed.
- The need for flexibility and extensibility to allow future updates or expansions.
- The option for hard copy documentation for offline browsing.


### Summary

User support is a multi-faceted, essential component of software systems that helps users navigate and use applications effectively. It ranges from quick command help to adaptive, personalized assistance. Designing good user support requires careful attention to availability, accuracy, consistency, and user control. Various approaches like command assistance, context-sensitive help, wizards, and adaptive systems each have their place. Knowledge representation and user modeling are key to intelligent help, but they come with challenges. Finally, the design and presentation of help must be user-friendly, clear, and integrated into the system from the start.