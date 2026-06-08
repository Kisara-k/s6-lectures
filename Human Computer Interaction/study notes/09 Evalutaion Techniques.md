## 9. Evalutaion Techniques

## Study Notes

### 1. 🧪 What is Evaluation in HCI?

Evaluation in Human-Computer Interaction (HCI) is the process of testing how usable and functional a system is. It’s a critical step that helps designers and developers understand whether their system works well for users and meets its intended goals. Evaluation can happen in different settings: in a controlled laboratory, out in the real world (field), or directly with users collaborating in the process. Importantly, evaluation is not just about checking the final product; it should be integrated throughout the entire design life cycle, from early concepts to full implementation.

The main goals of evaluation are to:

- **Assess system functionality:** Does the system do what it’s supposed to do?
- **Understand the interface’s effect on users:** How does the design impact user experience and behavior?
- **Identify specific problems:** What issues or obstacles do users face when interacting with the system?

Evaluation helps improve both the design (how the system looks and behaves) and the implementation (how it actually works under the hood).


### 2. 🧠 Evaluating Designs: Cognitive Walkthrough, Heuristic Evaluation, and Review-Based Methods

When evaluating designs, there are several expert-driven techniques that focus on understanding how well a system supports users, especially when learning new tasks.

#### Cognitive Walkthrough

This method was proposed by Polson and colleagues. It involves an expert, often someone with a background in cognitive psychology, stepping through the design as if they were a user trying to learn a task. The expert asks questions like:

- What will the user experience at each step?
- What mental processes does the user need to perform?
- What learning difficulties might arise?

The goal is to see if the design naturally guides users toward the correct goals and actions without confusion. The expert uses psychological principles and structured forms to analyze the design, focusing on how the system supports user learning and problem-solving.

#### Heuristic Evaluation

Developed by Nielsen and Molich, heuristic evaluation uses a set of usability principles (heuristics) to check the design. Experts examine the system to see if it violates any of these heuristics. Some common heuristics include:

- The system’s behavior should be predictable.
- The system should be consistent in its responses.
- The system should provide clear feedback to users.

This method is like debugging the design by spotting usability problems early.

#### Review-Based Evaluation

This approach uses existing research and literature to support or challenge parts of the design. It’s important to be cautious here because findings from other studies may not always apply directly to the new system. Sometimes, cognitive models like GOMS (Goals, Operators, Methods, and Selection) are used to predict user performance and filter design options.


### 3. 👥 Evaluating Through User Participation: Laboratory and Field Studies

User participation is essential for understanding how real people interact with a system. There are two main environments for this:

#### Laboratory Studies

In a lab, the environment is controlled and often equipped with specialized tools. This setup allows for focused observation without distractions. However, labs can lack the natural context where the system will actually be used, and it can be hard to study interactions involving multiple users cooperating.

Labs are best when:

- The system is used in dangerous or impractical locations.
- The system is designed for single users.
- Controlled manipulation of variables is needed.

#### Field Studies

Field studies take place in the user’s natural environment, preserving the context of use. This approach allows for long-term observation and understanding of how the system fits into real workflows. However, field studies can be noisy and distracting, and the presence of observers might influence user behavior.

Field studies are ideal when:

- The context of use is crucial.
- Longitudinal (long-term) studies are needed.
- Studying cooperation and social interaction is important.


### 4. ⚙️ Evaluating Implementations: Experimental Evaluation and Design

Once a system or prototype exists, evaluation can focus on specific interactive behaviors through experiments. This involves:

- Formulating a **hypothesis**: a clear prediction about how a change in the system will affect user behavior.
- Defining **experimental conditions**: different versions or settings of the system that vary only in one controlled way.
- Measuring **dependent variables**: outcomes like time taken, error rates, or user satisfaction.

#### Key Concepts in Experimental Design

- **Subjects:** The people participating in the experiment. They should represent the target user group and be enough in number to produce reliable results.
- **Independent Variable (IV):** The factor you change (e.g., font size, menu style).
- **Dependent Variable (DV):** The factor you measure (e.g., number of errors, task completion time).
- **Hypothesis:** A statement predicting how the IV affects the DV (e.g., “Error rate increases as font size decreases”).
- **Null Hypothesis:** The opposite, stating no effect exists, which the experiment aims to disprove.

#### Types of Experimental Designs

- **Within-groups design:** Each participant experiences all conditions. This reduces variability but risks learning effects.
- **Between-groups design:** Each participant experiences only one condition. This avoids learning effects but requires more participants.

#### Data Analysis

Before analyzing, it’s important to:

- Inspect the raw data carefully.
- Choose the right statistical tests based on data type (discrete or continuous) and the questions asked.

Statistical tests can be:

- **Parametric:** Assume data follows a normal distribution; powerful but require assumptions.
- **Non-parametric:** Don’t assume normality; more reliable but less powerful.
- **Contingency tables:** Used for categorical data to count occurrences.

Analysis answers questions like:

- Is there a significant difference between conditions?
- How large is the difference?
- How confident can we be in the results?


### 5. 👥 Group Experiments and Field Studies: Challenges and Approaches

Studying groups rather than individuals adds complexity. Challenges include:

- Recruiting enough participants (more expensive and time-consuming).
- Designing tasks that encourage cooperation (e.g., creative tasks, decision games).
- Managing large volumes of data (video recordings, logs).

Solutions include:

- Using within-groups designs to reduce variability.
- Micro-analysis of interactions (e.g., speech gaps).
- Combining qualitative (anecdotal) and quantitative data.

Field studies of groups focus on real-world social and physical contexts, recognizing that cognition is distributed across people and tools. This contrasts with psychology’s controlled experiments by emphasizing rich, naturalistic data.


### 6. 🗣️ Observational Methods: Think Aloud, Cooperative Evaluation, and Protocol Analysis

Observational methods involve watching users as they interact with the system and gathering insights about their thought processes.

#### Think Aloud

Users verbalize what they are doing and thinking while performing tasks. This method is simple and requires little expertise, providing direct insight into user behavior. However, it can be subjective and may alter how users perform tasks because they have to talk while working.

#### Cooperative Evaluation

A variation of think aloud where users and evaluators interact during the session. Both can ask questions, making the process more flexible and encouraging users to criticize the system openly.

#### Protocol Analysis

This involves recording user behavior in various ways:

- **Paper and pencil:** Cheap but limited by writing speed.
- **Audio:** Good for capturing think aloud but hard to synchronize with other data.
- **Video:** Accurate and realistic but requires equipment and can be intrusive.
- **Computer logging:** Automatic and unobtrusive but produces large data sets that are hard to analyze.
- **User notebooks:** Subjective but useful for long-term studies.

Often, multiple methods are combined for richer data.


### 7. 🎥 Post-Task Walkthroughs and Automated Analysis

#### Post-Task Walkthroughs

After a task, users review a recording or transcript of their session and comment on their actions and decisions. This method helps clarify intentions and reasoning that might not be obvious during the task. It can be done immediately (when memories are fresh) or later (allowing evaluators to prepare questions).

#### Automated Analysis: EVA (Experimental Video Annotator)

EVA is a tool developed to help analysts annotate video recordings after the fact. It reduces interruptions during the task and allows focused analysis of important events. However, it may lose some immediacy and can involve interpretation biases.


### 8. ❓ Query Techniques: Interviews and Questionnaires

#### Interviews

One-on-one conversations where an analyst asks prepared or spontaneous questions. Interviews are flexible and can explore unexpected issues but are subjective and time-consuming.

#### Questionnaires

Structured sets of questions given to many users. They are quick and allow for statistical analysis but are less flexible and probing than interviews.

Questionnaires must be carefully designed to:

- Collect the right information.
- Use appropriate question types (open-ended, scalar, multiple-choice, ranked).


### 9. 👁️ Physiological Methods: Eye Tracking and Other Measurements

Physiological methods measure physical responses to understand user reactions beyond what they say or do.

#### Eye Tracking

Special equipment tracks where and how the user’s eyes move. Key measurements include:

- **Fixations:** When the eye stays still, indicating focus and cognitive effort.
- **Saccades:** Rapid eye movements between points.
- **Scan paths:** The route the eyes take, with direct paths indicating easier processing.

Eye tracking helps reveal which parts of the interface are easy or hard to process.

#### Other Physiological Measurements

These include:

- Heart activity (pulse, blood pressure).
- Sweat gland activity (Galvanic Skin Response).
- Muscle electrical activity (Electromyogram).
- Brain electrical activity (Electroencephalogram).

These can indicate emotional responses but are complex to interpret and require more research.


### 10. 🧩 Choosing the Right Evaluation Method

Selecting an evaluation method depends on many factors:

- **Stage in the process:** Are you evaluating design ideas or a working implementation?
- **Style of evaluation:** Laboratory (controlled) vs. field (naturalistic).
- **Objectivity:** Subjective (user opinions) vs. objective (measurable data).
- **Type of measures:** Qualitative (descriptions, feelings) vs. quantitative (numbers, times).
- **Level of detail:** High-level overview vs. detailed low-level data.
- **Interference:** How much the evaluation interrupts normal use.
- **Resources:** Time, number of users, equipment, and expertise available.

Balancing these factors helps ensure the evaluation is effective, efficient, and provides meaningful insights.


### Summary

Evaluation in HCI is a broad and essential activity that ensures systems are usable, functional, and meet user needs. It involves a variety of techniques, from expert reviews and cognitive walkthroughs to user studies in labs and the field, experimental designs, observational methods, and physiological measurements. Each method has strengths and weaknesses, and the best approach depends on the goals, context, and resources of the project. Understanding these techniques in detail helps create better, more user-friendly systems.