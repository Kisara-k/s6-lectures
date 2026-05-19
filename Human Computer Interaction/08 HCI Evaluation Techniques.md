## 9. HCI Evaluation Techniques

## Key Points

#### 1. 🧑‍💻 Evaluation Goals  
- Evaluation tests usability and functionality of a system.  
- Evaluation occurs in laboratory, field, and/or with user collaboration.  
- Evaluation assesses system functionality, interface effect on users, and identifies specific problems.  

#### 2. 🔍 Cognitive Walkthrough  
- Proposed by Polson et al.  
- Evaluates how well design supports user learning of tasks.  
- Performed by cognitive psychology experts who "walk through" tasks using psychological principles.  
- Focuses on whether design helps users generate correct goals and understand tasks.  

#### 3. ✅ Heuristic Evaluation  
- Proposed by Nielsen and Molich.  
- Uses usability heuristics to identify design violations.  
- Example heuristics: system behavior is predictable, consistent, and provides feedback.  
- Acts as a "debugging" process for design usability.  

#### 4. 📚 Review-Based and Model-Based Evaluation  
- Review-based evaluation uses literature results to support or refute design parts.  
- Model-based evaluation uses cognitive models like GOMS to predict user performance.  
- GOMS stands for Goals, Operators, Methods, and Selection rules.  

#### 5. 👥 Laboratory Studies  
- Advantages: specialist equipment, uninterrupted environment.  
- Disadvantages: lack of real-world context, difficult to observe multi-user cooperation.  
- Appropriate for dangerous or impractical system locations and controlled single-user systems.  

#### 6. 🌳 Field Studies  
- Advantages: natural environment, context retained, allows longitudinal studies.  
- Disadvantages: distractions, noise, observation may alter behavior.  
- Appropriate when context is crucial and for long-term studies.  

#### 7. ⚙️ Experimental Evaluation  
- Requires artefact: simulation, prototype, or full implementation.  
- Tests specific interactive behaviors under controlled conditions.  
- Independent variables (IV) are manipulated; dependent variables (DV) are measured.  
- Hypothesis predicts relationship between IV and DV; null hypothesis states no difference.  

#### 8. 📊 Experimental Design  
- Within-groups: each subject experiences all conditions; risk of learning transfer.  
- Between-groups: each subject experiences one condition; requires more subjects, no learning transfer.  

#### 9. 📈 Data Analysis  
- Choice of statistical test depends on data type (discrete or continuous) and information needed.  
- Parametric tests assume normal distribution; non-parametric do not.  
- Contingency tables classify data by discrete attributes.  

#### 10. 👥 Group Experiments  
- Larger subject groups increase cost and variation.  
- Tasks must encourage cooperation and may involve multiple communication channels.  
- Data gathering involves video, audio, and logging; synchronization and volume are challenges.  

#### 11. 🗣️ Observational Methods  
- Think Aloud: user verbalizes thoughts during task; simple but subjective and may alter performance.  
- Cooperative Evaluation: user and evaluator interact during task; encourages criticism and clarification.  
- Protocol Analysis uses paper, audio, video, computer logs, or notebooks for data collection.  
- Post-task walkthroughs involve reviewing recorded sessions to explain user intentions.  

#### 12. ❓ Query Techniques  
- Interviews: one-on-one, flexible, subjective, time-consuming.  
- Questionnaires: fixed questions, quick, reach large groups, less flexible.  
- Question types include open-ended, scalar, multiple choice, and ranked.  

#### 13. 👁️ Physiological Methods  
- Eye tracking measures fixations, saccades, and scan paths to assess cognitive load.  
- Physiological measurements include heart activity, galvanic skin response (GSR), electromyogram (EMG), and electroencephalogram (EEG).  
- Interpretation of physiological data is complex and requires further research.  

#### 14. 🧩 Choosing Evaluation Methods  
- Depends on design stage (design vs. implementation), evaluation style (lab vs. field), objectivity (subjective vs. objective), data type (qualitative vs. quantitative), level of detail, interference level, and available resources.



<br>

## Study Notes

### 1. 🧑‍💻 Introduction to HCI Evaluation Techniques

Human-Computer Interaction (HCI) evaluation techniques are essential tools used to assess how well a system works for its users. Evaluation is not just about checking if a system functions correctly but also about understanding how usable and effective the interface is for real people. This process can happen in different environments—like controlled labs or real-world settings—and often involves users directly. Importantly, evaluation should be integrated throughout the entire design lifecycle, from early concepts to final implementations, to ensure the system meets user needs and expectations.

The main goals of evaluation are to:

- Measure how well the system’s functions work.
- Understand how the interface affects the user’s experience.
- Identify specific problems that users might face.

In this note, we will explore various evaluation methods, from expert reviews to user participation, experimental studies, observational techniques, and physiological measurements. Each method has its strengths and weaknesses, and choosing the right one depends on the stage of design, the type of system, and available resources.


### 2. 🔍 Expert-Based Evaluation Methods

Expert-based evaluations involve specialists reviewing the design to predict usability issues before involving actual users. These methods are often quicker and less costly than user testing but rely heavily on the expertise of the evaluators.

#### Cognitive Walkthrough

The Cognitive Walkthrough method was proposed by Polson and colleagues. It focuses on how well a design supports a user learning to perform tasks. Typically, an expert in cognitive psychology "walks through" the interface step-by-step, imagining how a new user would interact with it. The expert uses psychological principles to identify where users might struggle.

Key questions during a walkthrough include:

- What effect will this interaction have on the user?
- What mental processes does the user need to perform?
- What learning difficulties might arise?

The analysis centers on whether the design helps users form the correct goals and understand what to do next. This method is especially useful early in design to catch potential problems in user understanding.

#### Heuristic Evaluation

Developed by Nielsen and Molich, heuristic evaluation uses a set of usability principles (heuristics) as a checklist. Experts examine the design to see if it violates any of these principles. Common heuristics include:

- Predictability: The system behaves as users expect.
- Consistency: Similar actions produce similar results.
- Feedback: The system provides clear responses to user actions.

Heuristic evaluation acts like a "debugging" process for design, helping to identify usability flaws quickly.

#### Review-Based Evaluation

This method uses existing research and literature to support or challenge parts of a design. For example, if studies show that certain color schemes improve readability, designers might apply those findings. However, care must be taken to ensure that results from previous studies are relevant and transferable to the new design context.

#### Model-Based Evaluation

Model-based evaluation uses cognitive models like GOMS (Goals, Operators, Methods, and Selection rules) to predict user performance. GOMS breaks down tasks into goals (what the user wants to achieve), operators (basic actions), methods (procedures to achieve goals), and selection rules (deciding which method to use). This approach helps designers estimate how long tasks will take or how complex they are, guiding design decisions.


### 3. 👥 User Participation in Evaluation

Involving real users in evaluation provides direct insight into how a system performs in practice. User participation can happen in controlled labs or natural environments.

#### Laboratory Studies

Laboratory studies take place in controlled settings where specialist equipment is available, and distractions are minimized. This environment allows precise measurement of user behavior and system performance.

**Advantages:**

- Access to specialized tools and equipment.
- Controlled environment reduces external variables.

**Disadvantages:**

- Lack of real-world context; users may behave differently than in natural settings.
- Difficult to observe interactions involving multiple users cooperating.

Laboratory studies are ideal when safety is a concern or when precise control over variables is needed.

#### Field Studies

Field studies occur in the user’s natural environment, preserving the context in which the system will be used.

**Advantages:**

- Realistic setting captures authentic user behavior.
- Allows long-term (longitudinal) studies to observe changes over time.

**Disadvantages:**

- More distractions and noise can affect data quality.
- Observation itself may influence user behavior.

Field studies are best when understanding the context of use is critical, such as in collaborative or complex environments.


### 4. ⚙️ Evaluating Implementations Through Experiments

Once a prototype or full system is available, experimental evaluation can test specific aspects of user interaction under controlled conditions.

#### Experimental Evaluation Basics

- The evaluator defines a hypothesis to test.
- Different experimental conditions are created by changing one or more variables.
- User behavior is measured to see how it changes across conditions.

#### Key Experimental Factors

- **Subjects:** Who participates? They should represent the target user group and be sufficient in number to produce reliable results.
- **Variables:** Independent variables (IV) are what the experimenter changes (e.g., font size, interface style). Dependent variables (DV) are what is measured (e.g., task completion time, error rate).
- **Hypothesis:** A clear prediction about how changes in IV will affect DV (e.g., "Error rate increases as font size decreases").
- **Experimental Design:** How the experiment is structured, either within-groups (each participant experiences all conditions) or between-groups (each participant experiences only one condition).

#### Experimental Designs

- **Within-Groups Design:** Each participant tries all conditions. This reduces variability because the same people are compared across conditions but may introduce learning effects.
- **Between-Groups Design:** Different participants try different conditions. This avoids learning effects but requires more participants and can introduce variability between groups.

#### Data Analysis

Before analyzing data statistically, it’s important to:

- Inspect the raw data carefully.
- Choose the right statistical test based on data type (discrete or continuous) and the question being asked.

**Types of statistical tests:**

- **Parametric tests:** Assume data follows a normal distribution; powerful and commonly used.
- **Non-parametric tests:** Do not assume normal distribution; more reliable for unusual data but less powerful.
- **Contingency tables:** Used for categorical data to count occurrences in different groups.

Analysis aims to determine:

- Whether there is a significant difference between conditions.
- The size of the difference.
- The confidence in the results.


### 5. 👥 Group Experiments and Field Studies

Evaluating systems used by groups is more complex than single-user studies because of social dynamics and cooperation.

#### Challenges in Group Experiments

- Recruiting enough participants is costly and time-consuming.
- Tasks must encourage cooperation and may involve multiple communication channels.
- Data collection is complicated by the need to capture interactions from multiple perspectives (e.g., video, audio, system logs).
- Analysis must handle large volumes of data and account for variability between groups.

#### Types of Group Tasks

- Creative tasks (e.g., writing a report).
- Decision-making games (e.g., survival scenarios).
- Control tasks (e.g., managing a simulated bottling plant).

#### Field Studies for Groups

Field studies are more naturalistic and capture "distributed cognition," where knowledge and actions are shared across people and tools in a real environment. This approach contrasts with psychology’s controlled experiments by focusing on rich, contextual data typical of sociology and anthropology.


### 6. 🗣️ Observational and Protocol-Based Methods

These methods involve watching users as they interact with the system and collecting verbal or behavioral data to understand their thought processes.

#### Think Aloud

Users perform tasks while verbalizing their thoughts, explaining what they are doing and why.

**Advantages:**

- Simple and requires little training.
- Provides insight into user reasoning and actual system use.

**Disadvantages:**

- Subjective and selective; users may not verbalize everything.
- Talking aloud can change how users perform tasks.

#### Cooperative Evaluation

A variation of think aloud where users and evaluators interact, asking questions and clarifying points during the session.

**Advantages:**

- More flexible and less constrained.
- Encourages users to criticize and explain their actions.

#### Protocol Analysis

Collecting data through:

- Paper and pencil notes (cheap but limited).
- Audio recordings (good for think aloud but hard to synchronize).
- Video recordings (accurate but requires equipment and can be intrusive).
- Computer logs (automatic and unobtrusive but generate large data sets).
- User notebooks (subjective but useful for long-term studies).

#### Automated Analysis Tools

For example, EVA (Experimental Video Annotator) helps analyze video data by tagging important events, reducing manual effort.

#### Post-Task Walkthroughs

Users review a recording or transcript of their session after the fact to explain their intentions and decisions.

**Advantages:**

- Allows focused analysis without interrupting the task.
- Helps uncover reasons behind user actions.

**Disadvantages:**

- May lose immediacy and freshness.
- Risk of users rationalizing actions after the fact.


### 7. ❓ Query Techniques: Interviews and Questionnaires

These methods gather user opinions and experiences through direct questioning.

#### Interviews

One-on-one conversations guided by prepared questions but flexible to explore new topics.

**Advantages:**

- Can adapt to the context and probe deeply.
- Useful for uncovering unexpected issues.

**Disadvantages:**

- Subjective and time-consuming.
- Requires skilled interviewers.

#### Questionnaires

Structured sets of questions given to many users.

**Advantages:**

- Quick to administer to large groups.
- Easier to analyze statistically.

**Disadvantages:**

- Less flexible and probing.
- Requires careful design to get useful data.

**Question types include:**

- Open-ended (free text).
- Scalar (rating scales).
- Multiple choice.
- Ranked preferences.


### 8. 👁️ Physiological Evaluation Methods

These methods measure physical responses to understand user reactions to interfaces, often revealing subconscious or emotional responses.

#### Eye Tracking

Special equipment tracks where and how the user’s eyes move on the screen.

- **Fixations:** When the eye rests on a point; longer fixations suggest difficulty or interest.
- **Saccades:** Rapid eye movements between fixations.
- **Scan paths:** The route the eyes take; efficient paths indicate good design.

Eye tracking helps identify which parts of the interface demand more cognitive effort.

#### Other Physiological Measurements

- **Heart activity:** Measures like pulse and blood pressure can indicate stress or engagement.
- **Galvanic Skin Response (GSR):** Measures sweat gland activity, linked to emotional arousal.
- **Electromyogram (EMG):** Measures muscle electrical activity.
- **Electroencephalogram (EEG):** Measures brain electrical activity.

These methods can provide objective data on user emotions but are complex to interpret and require further research.


### 9. 🧩 Choosing the Right Evaluation Method

Selecting an evaluation technique depends on many factors:

- **Design stage:** Early design may benefit from expert reviews; later stages require user testing.
- **Evaluation style:** Laboratory (controlled) vs. field (naturalistic).
- **Objectivity:** Subjective (user opinions) vs. objective (measurable data).
- **Type of data:** Qualitative (descriptions, feelings) vs. quantitative (times, error rates).
- **Level of detail:** High-level (overall impressions) vs. low-level (specific interactions).
- **Interference:** Obtrusive methods may disrupt users; unobtrusive methods minimize interference.
- **Resources:** Time, number of users, equipment, and expertise available.

A well-planned evaluation often combines multiple methods to get a comprehensive understanding of usability and user experience.


### Summary

HCI evaluation is a broad field with many techniques designed to assess usability and user experience from different angles. Expert reviews like cognitive walkthroughs and heuristic evaluations help catch problems early. User participation in labs or the field provides real-world insights. Experimental studies offer controlled, measurable data, while observational and physiological methods reveal deeper cognitive and emotional responses. Interviews and questionnaires gather user opinions, and choosing the right method depends on the project’s goals, stage, and resources. Together, these techniques ensure that interactive systems are effective, efficient, and satisfying for users.