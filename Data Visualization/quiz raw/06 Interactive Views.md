## 7. Interactive Views

## Questions

#### 1. Which of the following are typical design choices when implementing parameter changes in interactive visualizations?  
A) Using sliders, buttons, radio buttons, checkboxes, and dropdowns  
B) Embedding all controls within the main canvas without separation  
C) Avoiding any visible controls to maximize screen space  
D) Choosing between separated versus interleaved controls and canvas  

#### 2. What are the main advantages of animated transitions in interactive visualizations?  
A) They eliminate the need for any user interaction  
B) They always improve performance by reducing rendering time  
C) They provide smooth state changes that help users track items  
D) They reduce cognitive load by staging changes  

#### 3. When designing selection interactions, which considerations are important?  
A) Differentiating primary versus secondary selections, such as source and target nodes  
B) Whether selection can be null or must always include at least one item  
C) Allowing multiple click types like shift-click or option-click to modify selection sets  
D) Using hover as the primary selection method on all devices  

#### 4. In the context of navigation in interactive views, what are the trade-offs between unconstrained and constrained navigation?  
A) Unconstrained navigation is easier for users to control precisely  
B) Constrained navigation often uses animated transitions to frame selections nicely  
C) Constrained navigation always requires manual user input for trajectory computation  
D) Unconstrained navigation is easier for designers to implement but harder for users to control  

#### 5. Which of the following statements about linked highlighting in multiple coordinated views are true?  
A) Linked highlighting is only effective when views use identical visual encodings  
B) Bidirectional linking is generally preferred over unidirectional linking  
C) Linked highlighting requires all views to share the exact same data attributes  
D) It allows users to see how items contiguous in one view are distributed in another  

#### 6. What are the main challenges or limitations associated with interaction in data visualization?  
A) Users may not interact as designers expect, leading to underutilization of features  
B) Controls may consume valuable screen space or be hard to discover if invisible  
C) Interaction always reduces cognitive load and never adds complexity  
D) Interaction imposes no time cost and always speeds up data analysis  

#### 7. When partitioning data into multiple views (faceting), what are key design considerations?  
A) Partitioning should avoid spatial proximity encoding to reduce visual clutter  
B) Using recursive subdivision allows hierarchical exploration of data dimensions  
C) The order of attribute splits can significantly affect pattern visibility  
D) Splitting data by attributes always makes cross-group comparisons easier  

#### 8. Regarding superimposed layers in visualization, which statements are accurate?  
A) Dynamic layering can be based on user selection and highlight one-hop neighbors  
B) Using different, non-overlapping visual channels helps distinguish layers  
C) Static layering often uses high luminance contrast for foreground elements  
D) More than three layers can be easily distinguished without careful design  

#### 9. What are the benefits and drawbacks of juxtaposing multiple views side-by-side compared to using animation?  
A) Juxtaposition halves the display area available to each view, potentially reducing detail  
B) Animation is always superior for comparing multiple experimental conditions  
C) Animation is easier to follow when many scattered changes occur across frames  
D) Juxtaposition reduces cognitive load by allowing eye movement instead of memory reliance  

#### 10. Which of the following interaction modalities and technologies require special ergonomic or design considerations?  
A) Touch interaction on small mobile screens without hover capability  
B) Eye tracking interaction, which can provide hands-free control but may have practical limitations  
C) Mouse and keyboard on large desktop screens with hover and multiple clicks  
D) Gesture-based interaction from video or sensor input, balancing realism and usability  



<br>

## Answers

#### 1. Which of the following are typical design choices when implementing parameter changes in interactive visualizations?  
A) ✓ Using sliders, buttons, radio buttons, checkboxes, and dropdowns — These are common widgets for parameter control.  
B) ✗ Embedding all controls within the main canvas without separation — Usually controls are separated or interleaved for clarity, not all embedded.  
C) ✗ Avoiding any visible controls to maximize screen space — Invisible controls reduce discoverability and are generally avoided.  
D) ✓ Choosing between separated versus interleaved controls and canvas — This is a key design decision affecting usability and screen space.  

**Correct:** A, D


#### 2. What are the main advantages of animated transitions in interactive visualizations?  
A) ✗ They eliminate the need for any user interaction — Animation complements interaction but does not replace it.  
B) ✗ They always improve performance by reducing rendering time — Animation often adds rendering overhead, not reduces it.  
C) ✓ They provide smooth state changes that help users track items — Animation supports item tracking and orientation.  
D) ✓ They reduce cognitive load by staging changes — Staging transitions helps users process changes incrementally.  

**Correct:** C, D


#### 3. When designing selection interactions, which considerations are important?  
A) ✓ Differentiating primary versus secondary selections, such as source and target nodes — Helps clarify interaction roles in complex selections.  
B) ✓ Whether selection can be null or must always include at least one item — Important for interaction semantics and user control.  
C) ✓ Allowing multiple click types like shift-click or option-click to modify selection sets — Enables richer selection manipulation.  
D) ✗ Using hover as the primary selection method on all devices — Hover is not available on most touchscreens, so not always viable.  

**Correct:** A, B, C


#### 4. In the context of navigation in interactive views, what are the trade-offs between unconstrained and constrained navigation?  
A) ✗ Unconstrained navigation is easier for users to control precisely — It is actually harder to control precisely due to overshoot/undershoot.  
B) ✓ Constrained navigation often uses animated transitions to frame selections nicely — This is a common technique to guide users.  
C) ✗ Constrained navigation always requires manual user input for trajectory computation — Trajectories are typically computed automatically.  
D) ✓ Unconstrained navigation is easier for designers to implement but harder for users to control — True trade-off described in the lecture.  

**Correct:** B, D


#### 5. Which of the following statements about linked highlighting in multiple coordinated views are true?  
A) ✗ Linked highlighting is only effective when views use identical visual encodings — Different encodings can still be linked effectively.  
B) ✓ Bidirectional linking is generally preferred over unidirectional linking — Bidirectional linking provides better interaction flexibility.  
C) ✗ Linked highlighting requires all views to share the exact same data attributes — Views can share all items but have different attributes or encodings.  
D) ✓ It allows users to see how items contiguous in one view are distributed in another — This is a key benefit of linked views.  

**Correct:** B, D


#### 6. What are the main challenges or limitations associated with interaction in data visualization?  
A) ✓ Users may not interact as designers expect, leading to underutilization of features — Empirical evidence shows this happens frequently.  
B) ✓ Controls may consume valuable screen space or be hard to discover if invisible — Both are common practical issues.  
C) ✗ Interaction always reduces cognitive load and never adds complexity — Interaction can add cognitive load and complexity.  
D) ✗ Interaction imposes no time cost and always speeds up data analysis — Interaction can have a time cost and sometimes slow users down.  

**Correct:** A, B


#### 7. When partitioning data into multiple views (faceting), what are key design considerations?  
A) ✗ Partitioning should avoid spatial proximity encoding to reduce visual clutter — Spatial proximity is often used intentionally to encode association.  
B) ✓ Using recursive subdivision allows hierarchical exploration of data dimensions — Recursive subdivision supports multi-level faceting.  
C) ✓ The order of attribute splits can significantly affect pattern visibility — Changing split order changes what patterns are easy to see.  
D) ✗ Splitting data by attributes always makes cross-group comparisons easier — It often makes cross-group comparisons harder, not easier.  

**Correct:** B, C


#### 8. Regarding superimposed layers in visualization, which statements are accurate?  
A) ✓ Dynamic layering can be based on user selection and highlight one-hop neighbors — Interactive layering adapts based on selection.  
B) ✓ Using different, non-overlapping visual channels helps distinguish layers — Essential for clear visual separation.  
C) ✓ Static layering often uses high luminance contrast for foreground elements — High contrast helps foreground elements stand out.  
D) ✗ More than three layers can be easily distinguished without careful design — More than two or three layers require careful design to avoid confusion.  

**Correct:** A, B, C


#### 9. What are the benefits and drawbacks of juxtaposing multiple views side-by-side compared to using animation?  
A) ✓ Juxtaposition halves the display area available to each view, potentially reducing detail — Side-by-side views share screen space.  
B) ✗ Animation is always superior for comparing multiple experimental conditions — Juxtaposition is often better for comparing multiple conditions.  
C) ✗ Animation is easier to follow when many scattered changes occur across frames — Animation is harder to follow with many scattered changes.  
D) ✓ Juxtaposition reduces cognitive load by allowing eye movement instead of memory reliance — Moving eyes is easier than remembering previous states.  

**Correct:** A, D


#### 10. Which of the following interaction modalities and technologies require special ergonomic or design considerations?  
A) ✓ Touch interaction on small mobile screens without hover capability — Requires tap-based interaction design due to lack of hover.  
B) ✓ Eye tracking interaction, which can provide hands-free control but may have practical limitations — Eye tracking has unique ergonomic and technical challenges.  
C) ✓ Mouse and keyboard on large desktop screens with hover and multiple clicks — Requires design for hover and multi-click interactions.  
D) ✓ Gesture-based interaction from video or sensor input, balancing realism and usability — Ergonomics and practicality must be considered.  

**Correct:** A, B, C, D