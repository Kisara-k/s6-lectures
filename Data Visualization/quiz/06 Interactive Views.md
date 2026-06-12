## 7. Interactive Views

## Questions

#### 1. Which of the following are common ways to manipulate an interactive visualization over time?  
A) Rearranging or reordering data elements  
B) Printing the visualization for offline use  
C) Adjusting aggregation levels or filters  
D) Changing the visual encoding (e.g., switching chart types)  

#### 2. What are typical advantages and disadvantages of using widgets (like sliders, buttons, dropdowns) for parameter changes in interactive views?  
A) Widgets consume screen space, potentially cluttering the interface  
B) Widgets provide clear affordances and are self-documenting with labels  
C) Widgets always improve user performance regardless of screen size or device  
D) Widgets eliminate the need for any other interaction methods like clicking or hovering  

#### 3. Animated transitions in visualizations are beneficial because they:  
A) Can be used to support drill-down and roll-up operations in hierarchical data  
B) Are always faster than static updates and reduce cognitive load in every scenario  
C) Help users maintain orientation by smoothly showing changes between states  
D) Should be avoided when many scattered changes or frames occur, as they can confuse users  

#### 4. When designing interaction for different devices, which considerations are important?  
A) Eye tracking and gesture sensors are standard and should always be included  
B) Large screens allow for multiple clicks and complex controls, unlike small screens  
C) Touchscreens lack hover, so tap and gesture interactions must be prioritized  
D) Hover interactions are effective on both desktop and mobile devices  

#### 5. Regarding selection and highlighting in interactive visualizations, which statements are true?  
A) Motion is a commonly recommended channel for highlighting in single-view visualizations  
B) Selection always replaces the previous selection and cannot be additive  
C) Highlighting changes visual encoding but is conceptually separable from selection  
D) Changing item color for highlighting can interfere with existing color encodings  

#### 6. What are the key differences between unconstrained and constrained navigation in interactive views?  
A) Unconstrained navigation allows free movement but can lead to overshooting or undershooting targets  
B) Unconstrained navigation is easier for users to control precisely than constrained navigation  
C) Constrained navigation removes the need for any user input during viewpoint changes  
D) Constrained navigation typically uses animated transitions to guide the user’s viewpoint  

#### 7. Which of the following statements about multiple coordinated views are correct?  
A) Bidirectional linking is generally preferred over unidirectional linking for coordination  
B) Linked highlighting allows selections in one view to update related data in other views  
C) Juxtaposing views side by side reduces cognitive load compared to switching between views  
D) Small multiples always share the same data subset across all views  

#### 8. When partitioning data into multiple views, what are important design considerations?  
A) The order of attribute splits affects which patterns are visible and easy to compare  
B) Recursive subdivision can reveal hierarchical relationships by splitting data multiple times  
C) Grouped bar charts and small multiples are interchangeable with no impact on comparison tasks  
D) Partitioning always makes it easier to compare across all attributes simultaneously  

#### 9. What are the tradeoffs between superimposing layers and juxtaposing multiple views?  
A) Juxtaposing views uses more display area but reduces memory load by allowing eye movement  
B) Superimposing is better for global comparison tasks, while juxtaposing supports local tasks  
C) Superimposing layers can handle many dozens of data layers without clutter  
D) Dynamic visual layering can highlight related data interactively based on user selection  

#### 10. Which of the following describe limitations or challenges of interaction in data visualization?  
A) Interaction can degenerate into inefficient human-powered search if not well designed  
B) Controls may take up valuable screen space or be hidden, reducing discoverability  
C) Interaction always speeds up data analysis and never imposes cognitive load  
D) Users may not interact as designers expect, sometimes ignoring interactive features  



<br>

## Answers

#### 1. Which of the following are common ways to manipulate an interactive visualization over time?  
A) ✓ Rearranging or reordering data elements helps reveal patterns dynamically.  
B) ✗ Printing is static and does not involve interaction or manipulation over time.  
C) ✓ Adjusting aggregation levels or filters changes what data is shown interactively.  
D) ✓ Changing the visual encoding (e.g., switching chart types) is a core manipulation method.  

**Correct:** A, C, D


#### 2. What are typical advantages and disadvantages of using widgets (like sliders, buttons, dropdowns) for parameter changes in interactive views?  
A) ✓ Widgets consume screen space, which can clutter the interface.  
B) ✓ Widgets provide clear affordances and self-documentation with labels.  
C) ✗ Widgets do not always improve performance, especially on small screens or complex interfaces.  
D) ✗ Widgets complement other interaction methods; they do not eliminate clicking or hovering.  

**Correct:** A, B


#### 3. Animated transitions in visualizations are beneficial because they:  
A) ✓ They support hierarchical navigation like drill-down and roll-up.  
B) ✗ Animated transitions are not always faster or reduce cognitive load in every case.  
C) ✓ Smooth transitions help users maintain orientation and track changes.  
D) ✓ When many scattered changes occur, animations can confuse users and should be used cautiously.  

**Correct:** A, C, D


#### 4. When designing interaction for different devices, which considerations are important?  
A) ✗ Eye tracking and gesture sensors are emerging but not standard or always necessary.  
B) ✓ Large screens support complex controls and multiple clicks better than small screens.  
C) ✓ Touchscreens require tap and gesture interactions due to lack of hover.  
D) ✗ Hover does not work on most mobile touchscreens, so it is ineffective there.  

**Correct:** B, C


#### 5. Regarding selection and highlighting in interactive visualizations, which statements are true?  
A) ✗ Motion is usually avoided in single views because it can distract users.  
B) ✗ Selection can be additive or replace previous selections depending on design.  
C) ✓ Highlighting changes visual encoding but is conceptually separate from selection.  
D) ✓ Changing color for highlighting can conflict with existing color encodings.  

**Correct:** C, D


#### 6. What are the key differences between unconstrained and constrained navigation in interactive views?  
A) ✓ Unconstrained navigation allows free movement but can cause overshoot or undershoot.  
B) ✗ Unconstrained navigation is harder, not easier, for precise control by users.  
C) ✗ Constrained navigation still requires user input; it just automates trajectory computation.  
D) ✓ Constrained navigation uses animated transitions to guide viewpoint changes.  

**Correct:** A, D


#### 7. Which of the following statements about multiple coordinated views are correct?  
A) ✓ Bidirectional linking is generally better for coordination than unidirectional.  
B) ✓ Linked highlighting updates related data across views based on selection.  
C) ✓ Juxtaposing views side by side reduces cognitive load by allowing eye movement instead of memory.  
D) ✗ Small multiples show different slices of data, so data subsets are not always shared.  

**Correct:** A, B, C


#### 8. When partitioning data into multiple views, what are important design considerations?  
A) ✓ The order of attribute splits affects visible patterns and comparison ease.  
B) ✓ Recursive subdivision reveals hierarchical relationships by multiple splits.  
C) ✗ Grouped bars and small multiples differ in comparison tasks and are not interchangeable.  
D) ✗ Partitioning often makes cross-attribute comparison harder, not easier.  

**Correct:** A, B


#### 9. What are the tradeoffs between superimposing layers and juxtaposing multiple views?  
A) ✓ Juxtaposing uses more space but reduces memory load by letting users move their eyes.  
B) ✗ Superimposing is better for local tasks; juxtaposing supports global tasks, especially with many charts.  
C) ✗ Superimposing many dozens of layers causes clutter and is not practical.  
D) ✓ Dynamic layering can highlight related data interactively based on selection.  

**Correct:** A, D


#### 10. Which of the following describe limitations or challenges of interaction in data visualization?  
A) ✓ Poorly designed interaction can degenerate into inefficient human-powered search.  
B) ✓ Controls take screen space or may be hidden, reducing discoverability.  
C) ✗ Interaction can impose cognitive load and sometimes slow analysis.  
D) ✓ Users often do not interact as designers expect and may ignore features.  

**Correct:** A, B, D