## 8. Design Rules

## Key Points

#### 1. 📐 Types of Design Rules  
- Principles are abstract, have low authority, and high generality.  
- Standards are specific, have high authority, and limited application.  
- Guidelines have lower authority than standards and more general application.

#### 2. 🎯 Principles to Support Usability  
- Learnability is the ease with which new users can begin effective interaction and achieve maximal performance.  
- Flexibility is the multiplicity of ways the user and system exchange information.  
- Robustness is the level of support provided to the user in achieving and assessing goal-directed behavior.

#### 3. 🧠 Principles of Learnability  
- Predictability means users can determine the effect of future actions based on past interaction history.  
- Synthesizability is the ability to assess the effect of past actions, immediate or eventual.  
- Familiarity involves applying prior knowledge to new systems, including guessability and affordance.  
- Generalizability is extending specific interaction knowledge to new situations.  
- Consistency means likeness in input/output behavior arising from similar situations or tasks.

#### 4. 🔄 Principles of Flexibility  
- Dialogue initiative allows freedom from system-imposed constraints on input dialogue.  
- Multithreading supports user interaction for more than one task at a time (concurrent or interleaving).  
- Task migratability is passing responsibility for task execution between user and system.  
- Substitutivity allows equivalent input/output values to be substituted for each other.  
- Customizability is modifiability of the user interface by user (adaptability) or system (adaptivity).

#### 5. 🛡️ Principles of Robustness  
- Observability is the ability of users to evaluate the system’s internal state from its perceivable representation.  
- Recoverability is the ability of users to take corrective action once an error is recognized.  
- Responsiveness is how users perceive the rate of communication with the system.  
- Task conformance is the degree to which system services support all user tasks.

#### 6. 📏 Standards and Guidelines  
- Standards are set by national or international bodies and require sound theory and stable technology.  
- Hardware standards are more common than software standards.  
- ISO 9241 defines usability as effectiveness, efficiency, and satisfaction in task accomplishment.  
- Guidelines are more suggestive and general than standards and can be abstract or detailed.

#### 7. ✅ Golden Rules and Heuristics  
- Shneiderman’s 8 Golden Rules include striving for consistency, enabling shortcuts, offering feedback, and error prevention.  
- Norman’s 7 Principles include using knowledge in the world and head, simplifying tasks, making things visible, and designing for error.

#### 8. 🧩 HCI Design Patterns  
- A design pattern is an invariant solution to a recurrent problem within a specific context.  
- Patterns capture design practice, not theory, and represent essential common properties of good design.  
- Patterns exist at multiple levels: social, organizational, conceptual, and detailed.  
- A pattern language links patterns to enable complete design generation.



<br>

## Study Notes

### 1. 🎯 Introduction to Design Rules in Interaction Design

Design rules are fundamental guidelines and principles that help create user interfaces and systems that are easy, efficient, and satisfying to use. The ultimate goal of interaction design is **maximum usability**, meaning the system should be intuitive and effective for users to achieve their goals with minimal effort and frustration.

Design rules provide a structured way to think about usability by offering principles, standards, and guidelines that designers can follow. These rules vary in their **generality** (how broadly they apply) and **authority** (how strongly they are enforced or recommended).

Understanding these design rules is essential because they help designers create systems that are not only functional but also user-friendly, adaptable, and robust.


### 2. 📚 Types of Design Rules: Principles, Standards, and Guidelines

Design rules come in three main types, each with different levels of authority and generality:

- **Principles**: These are abstract, broad rules that apply to many situations. They have **low authority** (meaning they are more like suggestions) but **high generality** (they apply across many contexts). For example, principles like "consistency" or "learnability" guide overall design thinking.

- **Standards**: These are very specific rules set by official bodies (like ISO) and have **high authority**. They are mandatory or strongly recommended and apply to limited contexts, often related to hardware or software compliance. For example, ISO 9241 defines usability in terms of effectiveness, efficiency, and satisfaction.

- **Guidelines**: These fall between principles and standards. They have **lower authority** than standards but are more specific than principles. Guidelines are often found in textbooks or style guides and help designers apply principles in practical ways.

The relationship between these types can be visualized as:

```
Increasing Authority → Standards → Guidelines → Principles
Increasing Generality → Principles → Guidelines → Standards
```


### 3. 🧠 Principles to Support Usability

Usability principles are the foundation for designing systems that users can learn quickly, use flexibly, and rely on robustly. These principles are grouped into three categories:

#### Learnability

Learnability refers to how easy it is for new users to start using a system effectively and reach their goals quickly.

Key principles of learnability include:

- **Predictability**: Users should be able to anticipate what will happen next based on their past interactions. This means the system’s operations should be visible and understandable.

- **Synthesizability**: Users need to assess the effects of their past actions, whether immediately or over time, to understand how their inputs influence the system.

- **Familiarity**: The system should leverage users’ prior knowledge, making it easier to guess how to use new features. This includes affordances—design elements that suggest their function.

- **Generalizability**: Skills learned in one part of the system should transfer to other parts or similar systems.

- **Consistency**: Similar tasks or situations should behave in similar ways, reducing confusion and learning time.

#### Flexibility

Flexibility is about allowing users and the system to exchange information in multiple ways, supporting different user preferences and contexts.

Key principles of flexibility include:

- **Dialogue Initiative**: Users should have freedom in how they interact, without the system forcing rigid input sequences. The system and user can take turns leading the interaction.

- **Multithreading**: The system should support users working on multiple tasks simultaneously, either by handling tasks concurrently or allowing users to switch between tasks easily.

- **Task Migratability**: Responsibility for tasks can shift between the user and the system. For example, the system might automate some steps but allow the user to intervene when needed.

- **Substitutivity**: Users should be able to use different but equivalent inputs or outputs interchangeably (e.g., typing or voice commands).

- **Customizability**: Users or the system can modify the interface to better suit individual needs, either through adaptability (system-driven) or adaptability (user-driven).

#### Robustness

Robustness ensures the system supports users in achieving their goals reliably and recovering from errors.

Key principles of robustness include:

- **Observability**: Users should be able to understand the system’s internal state through visible cues, such as clear feedback, defaults, and persistent information.

- **Recoverability**: Users must be able to correct mistakes easily, with options to undo actions or recover from errors without excessive effort.

- **Responsiveness**: The system should communicate promptly, so users feel the system is reacting quickly and reliably.

- **Task Conformance**: The system should fully support all the tasks users need to perform, ensuring completeness and adequacy.


### 4. 🛠️ Using Design Rules in Practice

Design rules are not just theoretical—they guide real design decisions to improve usability. Their use depends on their **authority** and **generality**:

- **Standards**: These are mandatory or strongly recommended rules, often set by international organizations. They ensure consistency and safety across many products. For example, hardware standards are common and stable, while software standards are less frequent due to rapid change.

- **Guidelines**: These are more flexible and suggestive. They can be abstract (broad principles) or detailed (specific style guides). Understanding why a guideline exists helps designers resolve conflicts when rules clash.

- **Golden Rules and Heuristics**: These are broad, practical rules that serve as quick checks for good design. They are not strict laws but help designers avoid common pitfalls.


### 5. 🏅 Golden Rules and Heuristics for Usability

Several well-known sets of golden rules and heuristics provide practical advice for designers:

#### Shneiderman’s 8 Golden Rules

1. **Strive for consistency**: Make similar operations and elements behave the same way.
2. **Enable frequent users to use shortcuts**: Allow experienced users to speed up interaction.
3. **Offer informative feedback**: Always inform users about what is happening.
4. **Design dialogs to yield closure**: Provide clear beginnings, middles, and ends to interactions.
5. **Offer error prevention and simple error handling**: Help users avoid errors and recover easily.
6. **Permit easy reversal of actions**: Allow undoing mistakes.
7. **Support internal locus of control**: Let users feel in charge of the system.
8. **Reduce short-term memory load**: Don’t overload users with information to remember.

#### Norman’s 7 Principles

1. Use both **knowledge in the world** (visible cues) and **knowledge in the head** (memory).
2. Simplify the structure of tasks to reduce complexity.
3. Make things visible to bridge the gap between what users want to do and what the system shows.
4. Get the mappings right—ensure controls correspond logically to their effects.
5. Exploit constraints to prevent errors naturally.
6. Design for error by anticipating and mitigating mistakes.
7. When all else fails, standardize to reduce confusion.


### 6. 🧩 HCI Design Patterns: Reusing Successful Solutions

Design patterns are reusable solutions to common design problems within specific contexts. They originated in architecture but are now widely used in Human-Computer Interaction (HCI).

- A **pattern** captures a proven design approach that solves a recurring problem.
- Patterns are **invariant**, meaning they work reliably across different situations.
- Examples include architectural patterns like “Light on Two Sides of Every Room” or HCI patterns like “Go back to a safe place” (providing an easy way to undo or exit).

#### Characteristics of HCI Design Patterns

- They capture **practical design knowledge**, not just theory.
- They represent the **common properties** of good designs.
- They exist at multiple levels: social, organizational, conceptual, and detailed.
- They embody **values** such as usability and humane design.
- They are **intuitive and readable**, making them useful for communication among designers, developers, and stakeholders.
- A **pattern language** links multiple patterns to create complete, coherent designs.


### 7. 📝 Summary: Principles and Rules for Usability

Designing for usability is about creating systems that are easy to learn, flexible to use, and robust in operation. This requires:

- Abstracting general principles from good designs to guide new projects.
- Applying standards and guidelines to ensure consistency and quality.
- Using golden rules and heuristics as practical checks.
- Leveraging design patterns to reuse proven solutions.

Successful usability design combines **creative insight** (innovative ideas) with **principled practice** (following established rules). By understanding and applying these design rules, designers can create interfaces that truly meet users’ needs.