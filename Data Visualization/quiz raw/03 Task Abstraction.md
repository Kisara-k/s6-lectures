## 4. Task Abstraction

## Questions

#### 1. What is the primary purpose of task abstraction in visualization design?  
A) To eliminate the need for domain knowledge entirely  
B) To map domain-specific questions into generalized tasks  
C) To identify the exact data format used in the domain  
D) To break down complex domain problems into simpler abstract tasks  

#### 2. Which of the following are considered high-level actions in task abstraction?  
A) Analyze  
B) Query  
C) Search  
D) Annotate  

#### 3. When characterizing a domain for visualization design, which factors are essential to consider?  
A) Domain jargon and technical terms  
B) Target domain and their problems  
C) Specific data types without transformation  
D) Group of users and their questions  

#### 4. In the context of task abstraction, what does the "target" refer to?  
A) The user performing the task  
B) The visualization technique used  
C) The data or object being acted upon  
D) The domain-specific jargon  

#### 5. Which of the following statements about the interplay between task and data abstraction is true?  
A) Task abstraction only focuses on user actions, not data  
B) Data abstraction is used to specify targets within task abstraction  
C) Data abstraction is independent of task abstraction  
D) Task abstraction can lead to transforming the data  

#### 6. Which of these pairs correctly represent {action, target} examples in task abstraction?  
A) Locate outliers  
B) Discover distribution  
C) Browse topology  
D) Compare trends  

#### 7. How does the "search" action differ based on what the user knows?  
A) Browse involves casually looking through items without a specific target  
B) Explore involves browsing items in alphabetical order  
C) Locate involves finding an unknown item in a known location  
D) Lookup involves finding a known item by exact match  

#### 8. What is a crucial design choice when considering the "analyze" action?  
A) Whether the user is discovering or presenting information  
B) Whether the data is structured or unstructured  
C) Whether the user is browsing or locating items  
D) Whether the user is annotating or recording data  

#### 9. Which of the following best describes the rule of thumb for task abstraction regarding domain jargon?  
A) Replace domain jargon with technical terms from the data abstraction  
B) Keep all domain jargon to maintain precision  
C) Systematically remove all domain jargon to generalize tasks  
D) Use domain jargon only when specifying targets  

#### 10. In query actions, how does the scope of data considered affect the task?  
A) Identifying focuses on one item  
B) Summarizing requires considering all data  
C) Browsing involves ignoring data scope entirely  
D) Comparing involves some subset of data  



<br>

## Answers

#### 1. What is the primary purpose of task abstraction in visualization design?  
A) ✗ To eliminate the need for domain knowledge entirely — Domain knowledge is necessary to characterize and abstract tasks.  
B) ✓ To map domain-specific questions into generalized tasks — This is a core goal of task abstraction.  
C) ✗ To identify the exact data format used in the domain — Data format is part of data abstraction, not the main purpose here.  
D) ✓ To break down complex domain problems into simpler abstract tasks — Task abstraction involves simplifying domain problems.  

**Correct:** B, D


#### 2. Which of the following are considered high-level actions in task abstraction?  
A) ✓ Analyze — One of the three main high-level actions.  
B) ✓ Query — The third main high-level action.  
C) ✓ Search — Another main high-level action.  
D) ✗ Annotate — This is a sub-action under produce, not a high-level action.  

**Correct:** A, B, C


#### 3. When characterizing a domain for visualization design, which factors are essential to consider?  
A) ✗ Domain jargon and technical terms — Should be removed or abstracted away, not emphasized.  
B) ✓ Target domain and their problems — Core to understanding the domain situation.  
C) ✗ Specific data types without transformation — Data types may need transformation; this is not a strict requirement.  
D) ✓ Group of users and their questions — Essential for domain characterization.  

**Correct:** B, D


#### 4. In the context of task abstraction, what does the "target" refer to?  
A) ✗ The user performing the task — The user is not the target; the target is what the action is performed on.  
B) ✗ The visualization technique used — Technique is part of design, not the target.  
C) ✓ The data or object being acted upon — Correct definition of target.  
D) ✗ The domain-specific jargon — Jargon is removed during abstraction, not a target.  

**Correct:** C


#### 5. Which of the following statements about the interplay between task and data abstraction is true?  
A) ✗ Task abstraction only focuses on user actions, not data — It involves both actions and targets (data).  
B) ✓ Data abstraction is used to specify targets within task abstraction — Targets are specified using data abstraction.  
C) ✗ Data abstraction is independent of task abstraction — They are interdependent.  
D) ✓ Task abstraction can lead to transforming the data — Iteration between task and data abstraction often causes data transformation.  

**Correct:** B, D


#### 6. Which of these pairs correctly represent {action, target} examples in task abstraction?  
A) ✓ Locate outliers — Valid pair.  
B) ✓ Discover distribution — Valid {action, target} pair.  
C) ✓ Browse topology — Valid pair.  
D) ✓ Compare trends — Valid pair.  

**Correct:** A, B, C, D


#### 7. How does the "search" action differ based on what the user knows?  
A) ✓ Browse involves casually looking through items without a specific target — Browsing is casual and less directed.  
B) ✗ Explore involves browsing items in alphabetical order — Explore is more open-ended, not alphabetical browsing.  
C) ✓ Locate involves finding an unknown item in a known location — Locate is about finding something in a known place.  
D) ✓ Lookup involves finding a known item by exact match — Correct description of lookup.  

**Correct:** A, C, D


#### 8. What is a crucial design choice when considering the "analyze" action?  
A) ✓ Whether the user is discovering or presenting information — Classic split in analyze action.  
B) ✗ Whether the data is structured or unstructured — Not a primary design choice in analyze action.  
C) ✗ Whether the user is browsing or locating items — These relate to search, not analyze.  
D) ✗ Whether the user is annotating or recording data — These are produce sub-actions, not analyze.  

**Correct:** A


#### 9. Which of the following best describes the rule of thumb for task abstraction regarding domain jargon?  
A) ✗ Replace domain jargon with technical terms from the data abstraction — Not recommended; jargon should be removed, not replaced with other jargon.  
B) ✗ Keep all domain jargon to maintain precision — Opposite of the rule of thumb.  
C) ✓ Systematically remove all domain jargon to generalize tasks — Correct rule of thumb.  
D) ✗ Use domain jargon only when specifying targets — Jargon should be removed systematically, including targets.  

**Correct:** C


#### 10. In query actions, how does the scope of data considered affect the task?  
A) ✓ Identifying focuses on one item — Correct for "one" in query.  
B) ✓ Summarizing requires considering all data — Correct for "all" in query.  
C) ✗ Browsing involves ignoring data scope entirely — Browsing is a search action, not query, and does not ignore data scope.  
D) ✓ Comparing involves some subset of data — Correct for "some" in query.  

**Correct:** A, B, D