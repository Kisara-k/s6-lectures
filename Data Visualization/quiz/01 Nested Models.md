## 2. Nested Models

## Questions

#### 1. Which of the following best describe the purpose of the Domain Situation level in the Nested Model?  
A) Designing the visual encoding and interaction techniques  
B) Optimizing the computational efficiency of the visualization algorithm  
C) Observing users with existing tools to uncover needs and pain points  
D) Identifying the target users and understanding their real-world context  

#### 2. In the Data/Task Abstraction level, what are the key activities involved?  
A) Defining why users are looking at the data and what tasks they want to perform  
B) Translating domain-specific data into a structured form suitable for visualization  
C) Selecting colors and shapes to represent data points  
D) Measuring system memory and runtime performance  

#### 3. Which statements about Visual Encoding and Interaction Idioms are true?  
A) Visual encoding idioms determine how data is graphically represented, such as bars or lines  
B) Algorithmic efficiency is the main concern at this level  
C) Poor choice of visual encoding can make a visualization ineffective even if the data is correct  
D) Interaction idioms refer to how users manipulate the visualization, like zooming or filtering  

#### 4. Why is validation considered difficult in visualization design according to the Nested Model?  
A) Because user feedback is irrelevant to algorithmic performance  
B) Because computational benchmarks alone confirm the effectiveness of visual encoding  
C) Because different validation methods are needed for different levels, involving multiple disciplines  
D) Because errors can occur independently at each of the four levels  

#### 5. Which of the following are examples of validation methods appropriate for the Algorithm level?  
A) Observing users in their natural work environment  
B) Measuring system time and memory usage  
C) Analyzing computational complexity theoretically  
D) Conducting lab studies to measure user task completion time  

#### 6. What are the consequences of misunderstanding the Domain Situation in the Nested Model?  
A) The entire visualization design may fail to meet user needs  
B) The visual encoding might be confusing or ineffective  
C) The algorithm might run too slowly  
D) The visualization may show irrelevant or incorrect data  

#### 7. How do downstream cascading effects and upstream iterative refinement relate to the Nested Model?  
A) Feedback from lower levels can lead to revisiting and improving higher levels  
B) Changes or errors at higher levels affect all subsequent lower levels  
C) Once a level is completed, it should not be revisited to avoid confusion  
D) Iterative refinement only applies to the Algorithm level  

#### 8. Which of the following statements about the relationship between computational benchmarks and user studies is correct?  
A) User studies alone are sufficient to validate the entire visualization design  
B) Lab studies measuring user performance confirm the appropriateness of task abstraction  
C) Computational benchmarks do not confirm the effectiveness of visual encoding or interaction idioms  
D) Computational benchmarks guarantee that the visual encoding is effective  

#### 9. When justifying the choice of data and tasks in the Data/Task Abstraction level, which approaches are valid?  
A) Comparing alternative data abstractions to ensure relevance  
B) Ensuring tasks align with why users need to analyze the data  
C) Ignoring domain experts’ input to avoid bias  
D) Selecting data based solely on what is easiest to visualize  

#### 10. Which of the following best exemplify a problem-driven approach to visualization design and validation?  
A) Focusing exclusively on improving algorithmic speed without considering user tasks  
B) Conducting field studies to document deployed usage and adoption  
C) Developing a new visualization technique without a specific user or domain in mind  
D) Observing and interviewing target users to understand their needs  



<br>

## Answers

#### 1. Which of the following best describe the purpose of the Domain Situation level in the Nested Model?  
A) ✗ Designing visual encoding and interaction belongs to a later level, not Domain Situation.  
B) ✗ Optimizing computational efficiency is related to the Algorithm level, not Domain Situation.  
C) ✓ Observing users with existing tools helps understand their needs, part of Domain Situation analysis.  
D) ✓ Identifying the target users and understanding their real-world context is the core of the Domain Situation level.  

**Correct:** C, D


#### 2. In the Data/Task Abstraction level, what are the key activities involved?  
A) ✓ Defining why users look at data and their tasks is the task abstraction part.  
B) ✓ Translating domain-specific data into structured forms is exactly what data abstraction means.  
C) ✗ Selecting colors and shapes is part of visual encoding, not data/task abstraction.  
D) ✗ Measuring system performance is related to the Algorithm level.  

**Correct:** A, B


#### 3. Which statements about Visual Encoding and Interaction Idioms are true?  
A) ✓ Visual encoding idioms define how data is graphically represented, such as bars or lines.  
B) ✗ Algorithmic efficiency is a concern of the Algorithm level, not visual encoding/interaction.  
C) ✓ Poor visual encoding can make a visualization ineffective even if the data is correct.  
D) ✓ Interaction idioms describe how users manipulate the visualization, like zooming or filtering.  

**Correct:** A, C, D


#### 4. Why is validation considered difficult in visualization design according to the Nested Model?  
A) ✗ User feedback is relevant to many levels, including interaction and domain understanding.  
B) ✗ Computational benchmarks alone do not confirm visual encoding effectiveness.  
C) ✓ Different validation methods from multiple disciplines are needed for different levels.  
D) ✓ Errors can occur independently at each of the four levels, complicating validation.  

**Correct:** C, D


#### 5. Which of the following are examples of validation methods appropriate for the Algorithm level?  
A) ✗ Observing users in their environment is for Domain Situation validation, not algorithms.  
B) ✓ Measuring system time and memory usage is a direct way to validate algorithm performance.  
C) ✓ Analyzing computational complexity theoretically is a standard algorithm validation method.  
D) ✗ Lab studies measuring user task time relate to visual encoding/interaction, not algorithms.  

**Correct:** B, C


#### 6. What are the consequences of misunderstanding the Domain Situation in the Nested Model?  
A) ✓ The entire visualization can fail if it does not meet actual user needs.  
B) ✗ Confusing visual encoding is a separate issue, usually downstream of domain understanding.  
C) ✗ Slow algorithms are unrelated to domain misunderstanding; they relate to implementation.  
D) ✓ Showing irrelevant or incorrect data often results from misunderstanding user needs.  

**Correct:** A, D


#### 7. How do downstream cascading effects and upstream iterative refinement relate to the Nested Model?  
A) ✓ Feedback from lower levels can lead to revisiting and improving higher levels (iterative refinement).  
B) ✓ Changes or errors at higher levels affect all subsequent lower levels (cascading effects).  
C) ✗ Levels should be revisited as needed; avoiding this would hinder design improvement.  
D) ✗ Iterative refinement applies to all levels, not just the Algorithm level.  

**Correct:** A, B


#### 8. Which of the following statements about the relationship between computational benchmarks and user studies is correct?  
A) ✗ User studies alone cannot validate the entire design, especially algorithmic aspects.  
B) ✗ Lab studies measure user performance but do not confirm task abstraction correctness.  
C) ✓ Computational benchmarks do not confirm the effectiveness of visual encoding or interaction idioms.  
D) ✗ Computational benchmarks do not guarantee visual encoding effectiveness.  

**Correct:** C


#### 9. When justifying the choice of data and tasks in the Data/Task Abstraction level, which approaches are valid?  
A) ✓ Comparing alternative abstractions ensures relevance and appropriateness.  
B) ✓ Ensuring tasks align with user goals is essential for useful abstraction.  
C) ✗ Ignoring domain experts risks misunderstanding user needs and tasks.  
D) ✗ Selecting data just because it is easy to visualize ignores domain relevance.  

**Correct:** A, B


#### 10. Which of the following best exemplify a problem-driven approach to visualization design and validation?  
A) ✗ Focusing only on algorithm speed without considering user tasks is technique-driven.  
B) ✓ Conducting field studies to document real-world usage fits problem-driven work.  
C) ✗ Developing techniques without specific users or domains is technique-driven, not problem-driven.  
D) ✓ Observing and interviewing users to understand needs is problem-driven.  

**Correct:** B, D