## 7. Interactive Views

## Questions

#### 1. Which of the following are common ways to manipulate a data visualization interactively?  
A) Printing the visualization on paper  
B) Rearranging the order of data elements  
C) Adjusting filtering parameters  
D) Changing the visual encoding  

#### 2. What are typical pros and cons of using widgets like sliders and dropdowns in interactive visualizations?  
A) They always improve user performance regardless of context  
B) They provide clear affordances and are self-documenting  
C) They consume screen space, potentially cluttering the interface  
D) They eliminate the need for any other interaction methods  

#### 3. Animated transitions in visualizations are primarily used to:  
A) Make the visualization more entertaining without functional benefit  
B) Provide a smooth change between states to help users track items  
C) Replace all static visualizations with animations  
D) Reduce cognitive load by avoiding abrupt changes  

#### 4. When designing for touch interaction on mobile devices, which considerations are important?  
A) Multiple clicks and keyboard shortcuts are the main interaction methods  
B) Hover effects are reliable and should be heavily used  
C) Tap and gesture-based interactions are primary  
D) Screen size constraints limit the number of visible controls  

#### 5. Which of the following statements about selection in interactive visualizations are true?  
A) Selection can be null, meaning no items are selected  
B) Selection semantics can include adding to or replacing the current selection  
C) Hover is always a reliable method for selection on all devices  
D) Multiple selection types (e.g., primary and secondary) can coexist  

#### 6. Highlighting differs from selection because:  
A) Highlighting always uses color changes exclusively  
B) Highlighting can use outlines, size changes, or motion  
C) Highlighting changes the visual encoding without changing the data state  
D) Highlighting and selection are always inseparable and identical  

#### 7. Which navigation techniques correspond to the "camera metaphor" in interactive visualization?  
A) Zoom in/out  
B) Pan/translate/scroll  
C) Rotate/spin (mainly in 3D)  
D) Changing data encoding  

#### 8. What are the main tradeoffs between unconstrained and constrained navigation?  
A) Unconstrained navigation is easier for users to control precisely  
B) Constrained navigation often uses animated transitions to guide the user  
C) Constrained navigation removes all user control over the view  
D) Unconstrained navigation can lead to overshooting or undershooting the target  

#### 9. Scrollytelling as a navigation method has which of the following characteristics?  
A) It can cause unexpected behavior or “scrolljacking”  
B) It always provides direct access to all visualization controls  
C) It supports only discrete steps, not continuous control  
D) It is intuitive because it mimics standard web browsing  

#### 10. Linked views in multiple coordinated visualizations typically:  
A) Allow selections in one view to highlight related data in others  
B) Are rarely used because they confuse users  
C) Share all data items but may show different attributes  
D) Use unidirectional linking exclusively for better performance  

#### 11. Which of the following are advantages of juxtaposing multiple views side by side?  
A) It makes it easier to compare different data slices simultaneously  
B) Each view has more screen space than a single view  
C) It always requires less display area than animated transitions  
D) It reduces cognitive load by allowing eye movement instead of memory reliance  

#### 12. What are the limitations of interaction in data visualization?  
A) Controls may take up valuable screen space or be hard to discover  
B) Users always interact exactly as designers intend  
C) Interaction always speeds up data analysis without any drawbacks  
D) Interaction can impose cognitive load by requiring users to remember previous states  

#### 13. In partitioning data for multiple views, changing the order of splits (e.g., neighborhood then type vs. type then neighborhood) affects:  
A) The spatial proximity encoding of associated items  
B) The total number of data points displayed  
C) The color scheme of the visualization  
D) Which patterns become visible or easier to compare  

#### 14. Which of the following statements about layering in visualizations are true?  
A) Dynamic layering can highlight neighbors based on user selection  
B) Layering can use different visual channels like color and size to distinguish groups  
C) Static layering involves fixed visual elements like roads on a map  
D) More than three layers are easy to distinguish without confusion  

#### 15. Small multiples differ from superimposed views because:  
A) Superimposed views overlay multiple data sets in the same frame  
B) Small multiples always share the same data items across views  
C) Small multiples show different slices of data in separate charts  
D) Superimposed views are better for global comparison tasks  

#### 16. Which of the following are true about tooltips in interactive visualizations?  
A) Tooltips are a good substitute for overview information  
B) Tooltips provide additional detail on demand, often on hover or click  
C) Tooltips can replace the need for any other interaction or highlighting  
D) Important information should not rely solely on tooltips because users may miss them  

#### 17. What is a key benefit of animated transitions combined with constrained navigation?  
A) They make navigation unpredictable and harder to follow  
B) They remove the need for any user input during navigation  
C) They preserve shape and layout during zooming or drill-down  
D) They automatically compute trajectories to frame selected data nicely  

#### 18. Which of the following interaction modalities are considered “lightweight” and which are “heavyweight”?  
A) Click/tap is heavyweight because it requires explicit user action  
B) Hover is lightweight because it requires no click  
C) Proximity-based selection (touching vs. nearby) can vary in weight depending on design  
D) Multiple click types (shift-click, option-click) are lightweight  

#### 19. Why might designers choose to use multiple coordinated views instead of a single animated view?  
A) Juxtaposed views allow easier comparison across different data slices  
B) Animated views are always easier to follow than multiple views  
C) Animated views can be hard to follow if many scattered changes occur simultaneously  
D) Multiple views reduce cognitive load by externalizing memory to the eyes  

#### 20. Which of the following are challenges when designing interactive visualizations for mobile devices?  
A) Gestures and taps can replace all keyboard shortcuts effectively  
B) Lack of hover interaction limits some common desktop interaction patterns  
C) Small screen size restricts the number and size of visible controls  
D) Users expect the same interaction complexity as on desktop  



<br>

## Answers

#### 1. Which of the following are common ways to manipulate a data visualization interactively?  
A) ✗ Printing is static, not interactive.  
B) ✓ Rearranging order helps reveal patterns or trends.  
C) ✓ Adjusting filtering parameters changes what data is shown.  
D) ✓ Changing the visual encoding allows users to see data differently.  

**Correct:** B, C, D


#### 2. What are typical pros and cons of using widgets like sliders and dropdowns in interactive visualizations?  
A) ✗ Widgets do not always improve performance; context matters.  
B) ✓ Widgets provide clear affordances and are self-documenting with labels.  
C) ✓ Widgets consume screen space, which can clutter the interface.  
D) ✗ Widgets do not eliminate the need for other interaction methods.  

**Correct:** B, C


#### 3. Animated transitions in visualizations are primarily used to:  
A) ✗ Entertainment is secondary; functional benefit is primary.  
B) ✓ Smooth changes help users track items across states.  
C) ✗ Animations do not replace all static visualizations.  
D) ✓ They reduce cognitive load by avoiding abrupt jumps.  

**Correct:** B, D


#### 4. When designing for touch interaction on mobile devices, which considerations are important?  
A) ✗ Multiple clicks and keyboard shortcuts are not primary on mobile.  
B) ✗ Hover effects are unreliable on touchscreens.  
C) ✓ Tap and gestures are primary interaction methods.  
D) ✓ Small screens limit visible controls.  

**Correct:** C, D


#### 5. Which of the following statements about selection in interactive visualizations are true?  
A) ✓ Selection can be null (no items selected).  
B) ✓ Selection semantics include adding or replacing selections.  
C) ✗ Hover is not reliable on all devices, especially touchscreens.  
D) ✓ Multiple selection types (primary, secondary) can coexist.  

**Correct:** A, B, D


#### 6. Highlighting differs from selection because:  
A) ✗ Highlighting can use many channels, not just color.  
B) ✓ Outlines, size, and motion are valid highlighting methods.  
C) ✓ Highlighting changes visual encoding without changing data state.  
D) ✗ Highlighting and selection are related but separable concepts.  

**Correct:** B, C


#### 7. Which navigation techniques correspond to the "camera metaphor" in interactive visualization?  
A) ✓ Zoom changes the camera’s distance to the scene.  
B) ✓ Pan/translate/scroll moves the view like a camera.  
C) ✓ Rotate/spin changes the camera angle, mainly in 3D.  
D) ✗ Changing data encoding is not navigation.  

**Correct:** A, B, C


#### 8. What are the main tradeoffs between unconstrained and constrained navigation?  
A) ✗ Unconstrained navigation is often harder to control precisely.  
B) ✓ Constrained navigation uses animated transitions to guide users.  
C) ✗ Constrained navigation still allows user control, just guided.  
D) ✓ Unconstrained navigation risks overshooting or undershooting targets.  

**Correct:** B, D


#### 9. Scrollytelling as a navigation method has which of the following characteristics?  
A) ✓ It can cause unexpected behavior or “scrolljacking.”  
B) ✗ It may lack direct access to all controls.  
C) ✗ It supports continuous control, not just discrete steps.  
D) ✓ It is intuitive because it mimics standard web browsing.  

**Correct:** A, D


#### 10. Linked views in multiple coordinated visualizations typically:  
A) ✓ Selections in one view highlight related data in others.  
B) ✗ Linked views are common and useful, not confusing.  
C) ✓ Share all data items but may show different attributes.  
D) ✗ Unidirectional linking is less effective than bidirectional.  

**Correct:** A, C


#### 11. Which of the following are advantages of juxtaposing multiple views side by side?  
A) ✓ Easier to compare different data slices simultaneously.  
B) ✗ Each view has less screen space than a single full view.  
C) ✗ Juxtapose usually requires more display area than animation.  
D) ✓ Reduces cognitive load by letting eyes move instead of memory.  

**Correct:** A, D


#### 12. What are the limitations of interaction in data visualization?  
A) ✓ Controls take screen space or may be hard to discover.  
B) ✗ Users often do not interact as designers expect.  
C) ✗ Interaction does not always speed up analysis; it can add overhead.  
D) ✓ Interaction imposes cognitive load by requiring memory of states.  

**Correct:** A, B, D


#### 13. In partitioning data for multiple views, changing the order of splits (e.g., neighborhood then type vs. type then neighborhood) affects:  
A) ✓ Spatial proximity encoding depends on split order.  
B) ✗ Total data points displayed remain the same.  
C) ✗ Color scheme is independent of split order.  
D) ✓ Which patterns become visible or easier to compare.  

**Correct:** A, D


#### 14. Which of the following statements about layering in visualizations are true?  
A) ✓ Dynamic layering highlights neighbors based on selection.  
B) ✓ Layering uses different visual channels to distinguish groups.  
C) ✓ Static layering involves fixed elements like roads on maps.  
D) ✗ More than three layers usually cause confusion.  

**Correct:** A, B, C


#### 15. Small multiples differ from superimposed views because:  
A) ✓ Superimposed views overlay multiple data sets in one frame.  
B) ✗ Small multiples do not share the same data items; they show slices.  
C) ✓ Small multiples show different data slices in separate charts.  
D) ✓ Superimposed views are better for local tasks, not global.  

**Correct:** A, C


#### 16. Which of the following are true about tooltips in interactive visualizations?  
A) ✗ Tooltips do not substitute for overview information.  
B) ✓ Tooltips provide additional detail on hover or click.  
C) ✗ Tooltips cannot replace all other interaction or highlighting.  
D) ✓ Important info should not rely solely on tooltips.  

**Correct:** B, D


#### 17. What is a key benefit of animated transitions combined with constrained navigation?  
A) ✗ They make navigation unpredictable; they improve predictability.  
B) ✗ They do not remove user input; users still control navigation.  
C) ✓ Preserve shape and layout during zoom or drill-down.  
D) ✓ Automatically compute trajectories to nicely frame selections.  

**Correct:** C, D


#### 18. Which of the following interaction modalities are considered “lightweight” and which are “heavyweight”?  
A) ✓ Click/tap is heavyweight due to explicit user action.  
B) ✓ Hover is lightweight because it requires no click.  
C) ✓ Proximity-based selection weight depends on design context.  
D) ✗ Multiple click types are heavyweight, not lightweight.  

**Correct:** A, B, C


#### 19. Why might designers choose to use multiple coordinated views instead of a single animated view?  
A) ✓ Juxtaposed views allow easier comparison across slices.  
B) ✗ Animated views are not always easier to follow.  
C) ✓ Animated views can be hard to follow with many scattered changes.  
D) ✓ Multiple views reduce cognitive load by externalizing memory.  

**Correct:** A, C, D


#### 20. Which of the following are challenges when designing interactive visualizations for mobile devices?  
A) ✗ Gestures and taps cannot fully replace keyboard shortcuts.  
B) ✓ Lack of hover limits common desktop interaction patterns.  
C) ✓ Small screen size restricts number and size of controls.  
D) ✗ Users do not expect the same interaction complexity as desktop.  

**Correct:** B, C