## 7. Interactive Views

## Questions

#### 1. Which of the following are common ways to manipulate a data visualization interactively?  
A) Adjusting filtering parameters  
B) Rearranging the order of data elements  
C) Changing the visual encoding  
D) Printing the visualization on paper  

#### 2. What are typical pros and cons of using widgets like sliders and dropdowns in interactive visualizations?  
A) They provide clear affordances and are self-documenting  
B) They consume screen space, potentially cluttering the interface  
C) They eliminate the need for any other interaction methods  
D) They always improve user performance regardless of context  

#### 3. Animated transitions in visualizations are primarily used to:  
A) Reduce cognitive load by avoiding abrupt changes  
B) Make the visualization more entertaining without functional benefit  
C) Provide a smooth change between states to help users track items  
D) Replace all static visualizations with animations  

#### 4. When designing for touch interaction on mobile devices, which considerations are important?  
A) Multiple clicks and keyboard shortcuts are the main interaction methods  
B) Hover effects are reliable and should be heavily used  
C) Tap and gesture-based interactions are primary  
D) Screen size constraints limit the number of visible controls  

#### 5. Which of the following statements about selection in interactive visualizations are true?  
A) Selection can be null, meaning no items are selected  
B) Multiple selection types (e.g., primary and secondary) can coexist  
C) Hover is always a reliable method for selection on all devices  
D) Selection semantics can include adding to or replacing the current selection  

#### 6. Highlighting differs from selection because:  
A) Highlighting always uses color changes exclusively  
B) Highlighting changes the visual encoding without changing the data state  
C) Highlighting can use outlines, size changes, or motion  
D) Highlighting and selection are always inseparable and identical  

#### 7. Which navigation techniques correspond to the "camera metaphor" in interactive visualization?  
A) Changing data encoding  
B) Rotate/spin (mainly in 3D)  
C) Zoom in/out  
D) Pan/translate/scroll  

#### 8. What are the main tradeoffs between unconstrained and constrained navigation?  
A) Constrained navigation often uses animated transitions to guide the user  
B) Constrained navigation removes all user control over the view  
C) Unconstrained navigation is easier for users to control precisely  
D) Unconstrained navigation can lead to overshooting or undershooting the target  

#### 9. Scrollytelling as a navigation method has which of the following characteristics?  
A) It always provides direct access to all visualization controls  
B) It can cause unexpected behavior or “scrolljacking”  
C) It supports only discrete steps, not continuous control  
D) It is intuitive because it mimics standard web browsing  

#### 10. Linked views in multiple coordinated visualizations typically:  
A) Are rarely used because they confuse users  
B) Allow selections in one view to highlight related data in others  
C) Share all data items but may show different attributes  
D) Use unidirectional linking exclusively for better performance  

#### 11. Which of the following are advantages of juxtaposing multiple views side by side?  
A) It reduces cognitive load by allowing eye movement instead of memory reliance  
B) Each view has more screen space than a single view  
C) It makes it easier to compare different data slices simultaneously  
D) It always requires less display area than animated transitions  

#### 12. What are the limitations of interaction in data visualization?  
A) Users always interact exactly as designers intend  
B) Interaction always speeds up data analysis without any drawbacks  
C) Interaction can impose cognitive load by requiring users to remember previous states  
D) Controls may take up valuable screen space or be hard to discover  

#### 13. In partitioning data for multiple views, changing the order of splits (e.g., neighborhood then type vs. type then neighborhood) affects:  
A) The total number of data points displayed  
B) The spatial proximity encoding of associated items  
C) Which patterns become visible or easier to compare  
D) The color scheme of the visualization  

#### 14. Which of the following statements about layering in visualizations are true?  
A) More than three layers are easy to distinguish without confusion  
B) Dynamic layering can highlight neighbors based on user selection  
C) Layering can use different visual channels like color and size to distinguish groups  
D) Static layering involves fixed visual elements like roads on a map  

#### 15. Small multiples differ from superimposed views because:  
A) Superimposed views overlay multiple data sets in the same frame  
B) Small multiples show different slices of data in separate charts  
C) Superimposed views are better for global comparison tasks  
D) Small multiples always share the same data items across views  

#### 16. Which of the following are true about tooltips in interactive visualizations?  
A) Tooltips provide additional detail on demand, often on hover or click  
B) Tooltips can replace the need for any other interaction or highlighting  
C) Important information should not rely solely on tooltips because users may miss them  
D) Tooltips are a good substitute for overview information  

#### 17. What is a key benefit of animated transitions combined with constrained navigation?  
A) They make navigation unpredictable and harder to follow  
B) They automatically compute trajectories to frame selected data nicely  
C) They remove the need for any user input during navigation  
D) They preserve shape and layout during zooming or drill-down  

#### 18. Which of the following interaction modalities are considered “lightweight” and which are “heavyweight”?  
A) Multiple click types (shift-click, option-click) are lightweight  
B) Click/tap is heavyweight because it requires explicit user action  
C) Proximity-based selection (touching vs. nearby) can vary in weight depending on design  
D) Hover is lightweight because it requires no click  

#### 19. Why might designers choose to use multiple coordinated views instead of a single animated view?  
A) Animated views are always easier to follow than multiple views  
B) Multiple views reduce cognitive load by externalizing memory to the eyes  
C) Animated views can be hard to follow if many scattered changes occur simultaneously  
D) Juxtaposed views allow easier comparison across different data slices  

#### 20. Which of the following are challenges when designing interactive visualizations for mobile devices?  
A) Lack of hover interaction limits some common desktop interaction patterns  
B) Users expect the same interaction complexity as on desktop
C) Gestures and taps can replace all keyboard shortcuts effectively  
D) Small screen size restricts the number and size of visible controls  



<br>

## Answers

#### 1. Which of the following are common ways to manipulate a data visualization interactively?  
A) ✓ Adjusting filtering parameters changes what data is shown.  
B) ✓ Rearranging order helps reveal patterns or trends.  
C) ✓ Changing the visual encoding allows users to see data differently.  
D) ✗ Printing is static, not interactive.  

**Correct:** A, B, C


#### 2. What are typical pros and cons of using widgets like sliders and dropdowns in interactive visualizations?  
A) ✓ Widgets provide clear affordances and are self-documenting with labels.  
B) ✓ Widgets consume screen space, which can clutter the interface.  
C) ✗ Widgets do not eliminate the need for other interaction methods.  
D) ✗ Widgets do not always improve performance; context matters.  

**Correct:** A, B


#### 3. Animated transitions in visualizations are primarily used to:  
A) ✓ They reduce cognitive load by avoiding abrupt jumps.  
B) ✗ Entertainment is secondary; functional benefit is primary.  
C) ✓ Smooth changes help users track items across states.  
D) ✗ Animations do not replace all static visualizations.  

**Correct:** A, C


#### 4. When designing for touch interaction on mobile devices, which considerations are important?  
A) ✗ Multiple clicks and keyboard shortcuts are not primary on mobile.  
B) ✗ Hover effects are unreliable on touchscreens.  
C) ✓ Tap and gestures are primary interaction methods.  
D) ✓ Small screens limit visible controls.  

**Correct:** C, D


#### 5. Which of the following statements about selection in interactive visualizations are true?  
A) ✓ Selection can be null (no items selected).  
B) ✓ Multiple selection types (primary, secondary) can coexist.  
C) ✗ Hover is not reliable on all devices, especially touchscreens.  
D) ✓ Selection semantics include adding or replacing selections.  

**Correct:** A, B, D


#### 6. Highlighting differs from selection because:  
A) ✗ Highlighting can use many channels, not just color.  
B) ✓ Highlighting changes visual encoding without changing data state.  
C) ✓ Outlines, size, and motion are valid highlighting methods.  
D) ✗ Highlighting and selection are related but separable concepts.  

**Correct:** B, C


#### 7. Which navigation techniques correspond to the "camera metaphor" in interactive visualization?  
A) ✗ Changing data encoding is not navigation.  
B) ✓ Rotate/spin changes the camera angle, mainly in 3D.  
C) ✓ Zoom changes the camera’s distance to the scene.  
D) ✓ Pan/translate/scroll moves the view like a camera.  

**Correct:** B, C, D


#### 8. What are the main tradeoffs between unconstrained and constrained navigation?  
A) ✓ Constrained navigation uses animated transitions to guide users.  
B) ✗ Constrained navigation still allows user control, just guided.  
C) ✗ Unconstrained navigation is often harder to control precisely.  
D) ✓ Unconstrained navigation risks overshooting or undershooting targets.  

**Correct:** A, D


#### 9. Scrollytelling as a navigation method has which of the following characteristics?  
A) ✗ It may lack direct access to all controls.  
B) ✓ It can cause unexpected behavior or “scrolljacking.”  
C) ✗ It supports continuous control, not just discrete steps.  
D) ✓ It is intuitive because it mimics standard web browsing.  

**Correct:** B, D


#### 10. Linked views in multiple coordinated visualizations typically:  
A) ✗ Linked views are common and useful, not confusing.  
B) ✓ Selections in one view highlight related data in others.  
C) ✓ Share all data items but may show different attributes.  
D) ✗ Unidirectional linking is less effective than bidirectional.  

**Correct:** B, C


#### 11. Which of the following are advantages of juxtaposing multiple views side by side?  
A) ✓ Reduces cognitive load by letting eyes move instead of memory.  
B) ✗ Each view has less screen space than a single full view.  
C) ✓ Easier to compare different data slices simultaneously.  
D) ✗ Juxtapose usually requires more display area than animation.  

**Correct:** A, C


#### 12. What are the limitations of interaction in data visualization?  
A) ✗ Users often do not interact as designers expect.  
B) ✗ Interaction does not always speed up analysis; it can add overhead.  
C) ✓ Interaction imposes cognitive load by requiring memory of states.  
D) ✓ Controls take screen space or may be hard to discover.  

**Correct:** A, C, D


#### 13. In partitioning data for multiple views, changing the order of splits (e.g., neighborhood then type vs. type then neighborhood) affects:  
A) ✗ Total data points displayed remain the same.  
B) ✓ Spatial proximity encoding depends on split order.  
C) ✓ Which patterns become visible or easier to compare.  
D) ✗ Color scheme is independent of split order.  

**Correct:** B, C


#### 14. Which of the following statements about layering in visualizations are true?  
A) ✗ More than three layers usually cause confusion.  
B) ✓ Dynamic layering highlights neighbors based on selection.  
C) ✓ Layering uses different visual channels to distinguish groups.  
D) ✓ Static layering involves fixed elements like roads on maps.  

**Correct:** B, C, D


#### 15. Small multiples differ from superimposed views because:  
A) ✓ Superimposed views overlay multiple data sets in one frame.  
B) ✓ Small multiples show different data slices in separate charts.  
C) ✓ Superimposed views are better for local tasks, not global.  
D) ✗ Small multiples do not share the same data items; they show slices.  

**Correct:** A, B


#### 16. Which of the following are true about tooltips in interactive visualizations?  
A) ✓ Tooltips provide additional detail on hover or click.  
B) ✗ Tooltips cannot replace all other interaction or highlighting.  
C) ✓ Important info should not rely solely on tooltips.  
D) ✗ Tooltips do not substitute for overview information.  

**Correct:** A, C


#### 17. What is a key benefit of animated transitions combined with constrained navigation?  
A) ✗ They make navigation unpredictable; they improve predictability.  
B) ✓ Automatically compute trajectories to nicely frame selections.  
C) ✗ They do not remove user input; users still control navigation.  
D) ✓ Preserve shape and layout during zoom or drill-down.  

**Correct:** B, D


#### 18. Which of the following interaction modalities are considered “lightweight” and which are “heavyweight”?  
A) ✗ Multiple click types are heavyweight, not lightweight.  
B) ✓ Click/tap is heavyweight due to explicit user action.  
C) ✓ Proximity-based selection weight depends on design context.  
D) ✓ Hover is lightweight because it requires no click.  

**Correct:** B, C, D


#### 19. Why might designers choose to use multiple coordinated views instead of a single animated view?  
A) ✗ Animated views are not always easier to follow.  
B) ✓ Multiple views reduce cognitive load by externalizing memory.  
C) ✓ Animated views can be hard to follow with many scattered changes.  
D) ✓ Juxtaposed views allow easier comparison across slices.  

**Correct:** B, C, D


#### 20. Which of the following are challenges when designing interactive visualizations for mobile devices?  
A) ✓ Lack of hover limits common desktop interaction patterns.  
B) ✗ Users do not expect the same interaction complexity as desktop.  
C) ✗ Gestures and taps cannot fully replace keyboard shortcuts.  
D) ✓ Small screen size restricts number and size of controls.  

**Correct:** A, D