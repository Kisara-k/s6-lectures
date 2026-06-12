## 2. Nested Models

## Questions

#### 1. Which of the following are components of the Nested Model for visualization design and validation?  
A) Data/task abstraction  
B) Algorithm  
C) Domain situation  
D) Visual encoding/interaction idiom  

#### 2. In the Nested Model, what does the "domain situation" level primarily address?  
A) Efficient computation algorithms  
B) Who the target users are and their needs  
C) What data is shown and why  
D) How to draw the visualization  

#### 3. Why is validation considered difficult in the Nested Model framework?  
A) Because only one method can be used for validation  
B) Because lab studies always confirm task abstraction  
C) Because errors can occur at multiple levels independently  
D) Because computational benchmarks always confirm design choices  

#### 4. Which of the following are appropriate validation methods for the "algorithm" level?  
A) Measuring system time and memory usage  
B) Conducting lab studies measuring human time  
C) Observing target users after deployment  
D) Analyzing computational complexity  

#### 5. What is a potential consequence of misunderstanding the "data/task abstraction" level?  
A) Writing inefficient code  
B) Misidentifying the target user group  
C) Showing the wrong data or tasks to users  
D) Choosing an inappropriate visual encoding idiom  

#### 6. Which disciplines are suggested as sources of validation methods for different levels of the Nested Model?  
A) Mechanical engineering  
B) Cognitive psychology  
C) Anthropology/ethnography  
D) Computer science  

#### 7. Which of the following statements about the relationship between levels in the Nested Model is true?  
A) Iterative refinement can occur upstream from algorithm to domain situation  
B) There are cascading downstream effects from higher to lower levels  
C) Changes at the algorithm level have no effect on visual encoding  
D) Validation at one level guarantees correctness at all other levels  

#### 8. When justifying the design of visual encoding and interaction idioms, which methods are commonly used?  
A) Measuring system time and memory  
B) Testing on target users and collecting utility anecdotes  
C) Qualitative result image analysis  
D) Analyzing computational complexity  

#### 9. Which of the following is NOT a typical reason why a visualization might fail at the "visual encoding/interaction idiom" level?  
A) The interaction idiom is confusing or ineffective  
B) The way the data is shown does not work for the user  
C) The visual encoding does not support the intended tasks  
D) The code is too slow to render the visualization  

#### 10. In practice, why might computational benchmarks not confirm idiom design, and lab studies not confirm task abstraction?  
A) Because computational benchmarks only measure efficiency, not usability  
B) Because task abstraction is always obvious and does not require validation  
C) Because idiom design is unrelated to algorithm performance  
D) Because lab studies often fail to capture real-world user goals and contexts  



<br>

## Answers

#### 1. Which of the following are components of the Nested Model for visualization design and validation?  
A) ✓ Data/task abstraction is the second level, defining what data and tasks are shown.  
B) ✓ Algorithm is the fourth level, defining efficient computation methods.  
C) ✓ The domain situation is the first level, defining target users and context.  
D) ✓ Visual encoding/interaction idiom is the third level, defining how data is shown and manipulated.  

**Correct:** A, B, C, D


#### 2. In the Nested Model, what does the "domain situation" level primarily address?  
A) ✗ Algorithm level deals with computation, not domain situation.  
B) ✓ Domain situation focuses on who the users are and their needs.  
C) ✗ Data/task abstraction defines what data is shown and why, not domain situation.  
D) ✗ This relates to visual encoding, not domain situation.  

**Correct:** B


#### 3. Why is validation considered difficult in the Nested Model framework?  
A) ✗ Multiple methods from different fields are needed, not just one.  
B) ✗ Lab studies do not always confirm task abstraction.  
C) ✓ Errors can occur independently at each level, complicating validation.  
D) ✗ Computational benchmarks do not always confirm design choices.  

**Correct:** C


#### 4. Which of the following are appropriate validation methods for the "algorithm" level?  
A) ✓ Measuring system time and memory is a direct algorithm-level validation.  
B) ✗ Lab studies measuring human time relate to user performance, not algorithm efficiency.  
C) ✗ Observing users is for domain or idiom levels, not algorithm.  
D) ✓ Analyzing computational complexity is a core algorithm validation method.  

**Correct:** A, D


#### 5. What is a potential consequence of misunderstanding the "data/task abstraction" level?  
A) ✗ Writing inefficient code relates to algorithm level, not data/task abstraction.  
B) ✗ Misidentifying target users relates to domain situation, not data/task abstraction.  
C) ✓ Showing the wrong data or tasks is a direct consequence.  
D) ✗ Choosing inappropriate visual encoding relates to idiom level.  

**Correct:** C


#### 6. Which disciplines are suggested as sources of validation methods for different levels of the Nested Model?  
A) ✗ Mechanical engineering is not mentioned as a source for validation methods here.  
B) ✓ Cognitive psychology helps validate user tasks and interaction.  
C) ✓ Anthropology/ethnography supports understanding domain situation and user context.  
D) ✓ Computer science provides methods for algorithm and system validation.  

**Correct:** B, C, D


#### 7. Which of the following statements about the relationship between levels in the Nested Model is true?  
A) ✓ Iterative refinement can occur upstream, from algorithm back to domain situation.  
B) ✓ There are cascading downstream effects from higher to lower levels.  
C) ✗ Algorithm changes can affect visual encoding indirectly; no level is isolated.  
D) ✗ Validation at one level does not guarantee correctness at others.  

**Correct:** A, B


#### 8. When justifying the design of visual encoding and interaction idioms, which methods are commonly used?  
A) ✗ Measuring system time/memory relates to algorithm, not idiom design.  
B) ✓ Testing on target users and collecting anecdotes supports idiom validation.  
C) ✓ Qualitative image analysis helps justify visual encoding effectiveness.  
D) ✗ Computational complexity analysis is for algorithm validation, not idiom design.  

**Correct:** B, C


#### 9. Which of the following is NOT a typical reason why a visualization might fail at the "visual encoding/interaction idiom" level?  
A) ✗ Confusing or ineffective interaction idioms cause failure at this level.  
B) ✗ This is a common reason for failure at the idiom level.  
C) ✗ Visual encoding not supporting tasks is a typical idiom-level failure.  
D) ✓ Code being too slow is an algorithm-level issue, not idiom failure.  

**Correct:** D


#### 10. In practice, why might computational benchmarks not confirm idiom design, and lab studies not confirm task abstraction?  
A) ✓ Computational benchmarks measure efficiency, not usability or design quality.  
B) ✗ Task abstraction is not always obvious and does require validation.  
C) ✗ Idiom design can relate to algorithm performance, but benchmarks alone don’t confirm design quality.  
D) ✓ Lab studies may fail to capture real-world user goals and contexts, limiting task abstraction validation.  

**Correct:** A, D