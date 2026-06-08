## 7. Interactive Views

## Questions

#### 1. Which of the following are common ways to manipulate a data visualization interactively?  
A) Changing the visual encoding  
B) Rearranging the order of data elements  
C) Printing the visualization on paper  
D) Adjusting filtering parameters  

#### 2. What are typical pros and cons of using widgets like sliders and dropdowns in interactive visualizations?  
A) They provide clear affordances and are self-documenting  
B) They consume screen space, potentially cluttering the interface  
C) They always improve user performance regardless of context  
D) They eliminate the need for any other interaction methods  

#### 3. Animated transitions in visualizations are primarily used to:  
A) Provide a smooth change between states to help users track items  
B) Replace all static visualizations with animations  
C) Reduce cognitive load by avoiding abrupt changes  
D) Make the visualization more entertaining without functional benefit  

#### 4. When designing for touch interaction on mobile devices, which considerations are important?  
A) Hover effects are reliable and should be heavily used  
B) Tap and gesture-based interactions are primary  
C) Screen size constraints limit the number of visible controls  
D) Multiple clicks and keyboard shortcuts are the main interaction methods  

#### 5. Which of the following statements about selection in interactive visualizations are true?  
A) Selection can be null, meaning no items are selected  
B) Multiple selection types (e.g., primary and secondary) can coexist  
C) Hover is always a reliable method for selection on all devices  
D) Selection semantics can include adding to or replacing the current selection  

#### 6. Highlighting differs from selection because:  
A) Highlighting changes the visual encoding without changing the data state  
B) Highlighting always uses color changes exclusively  
C) Highlighting can use outlines, size changes, or motion  
D) Highlighting and selection are always inseparable and identical  

#### 7. Which navigation techniques correspond to the "camera metaphor" in interactive visualization?  
A) Pan/translate/scroll  
B) Zoom in/out  
C) Rotate/spin (mainly in 3D)  
D) Changing data encoding  

#### 8. What are the main tradeoffs between unconstrained and constrained navigation?  
A) Unconstrained navigation is easier for users to control precisely  
B) Constrained navigation often uses animated transitions to guide the user  
C) Unconstrained navigation can lead to overshooting or undershooting the target  
D) Constrained navigation removes all user control over the view  

#### 9. Scrollytelling as a navigation method has which of the following characteristics?  
A) It is intuitive because it mimics standard web browsing  
B) It always provides direct access to all visualization controls  
C) It can cause unexpected behavior or “scrolljacking”  
D) It supports only discrete steps, not continuous control  

#### 10. Linked views in multiple coordinated visualizations typically:  
A) Share all data items but may show different attributes  
B) Use unidirectional linking exclusively for better performance  
C) Allow selections in one view to highlight related data in others  
D) Are rarely used because they confuse users  

#### 11. Which of the following are advantages of juxtaposing multiple views side by side?  
A) Each view has more screen space than a single view  
B) It reduces cognitive load by allowing eye movement instead of memory reliance  
C) It makes it easier to compare different data slices simultaneously  
D) It always requires less display area than animated transitions  

#### 12. What are the limitations of interaction in data visualization?  
A) Interaction always speeds up data analysis without any drawbacks  
B) Interaction can impose cognitive load by requiring users to remember previous states  
C) Controls may take up valuable screen space or be hard to discover  
D) Users always interact exactly as designers intend  

#### 13. In partitioning data for multiple views, changing the order of splits (e.g., neighborhood then type vs. type then neighborhood) affects:  
A) Which patterns become visible or easier to compare  
B) The color scheme of the visualization  
C) The spatial proximity encoding of associated items  
D) The total number of data points displayed  

#### 14. Which of the following statements about layering in visualizations are true?  
A) Layering can use different visual channels like color and size to distinguish groups  
B) More than three layers are easy to distinguish without confusion  
C) Static layering involves fixed visual elements like roads on a map  
D) Dynamic layering can highlight neighbors based on user selection  

#### 15. Small multiples differ from superimposed views because:  
A) Small multiples show different slices of data in separate charts  
B) Superimposed views overlay multiple data sets in the same frame  
C) Small multiples always share the same data items across views  
D) Superimposed views are better for global comparison tasks  

#### 16. Which of the following are true about tooltips in interactive visualizations?  
A) Tooltips provide additional detail on demand, often on hover or click  
B) Tooltips are a good substitute for overview information  
C) Important information should not rely solely on tooltips because users may miss them  
D) Tooltips can replace the need for any other interaction or highlighting  

#### 17. What is a key benefit of animated transitions combined with constrained navigation?  
A) They automatically compute trajectories to frame selected data nicely  
B) They remove the need for any user input during navigation  
C) They preserve shape and layout during zooming or drill-down  
D) They make navigation unpredictable and harder to follow  

#### 18. Which of the following interaction modalities are considered “lightweight” and which are “heavyweight”?  
A) Hover is lightweight because it requires no click  
B) Click/tap is heavyweight because it requires explicit user action  
C) Multiple click types (shift-click, option-click) are lightweight  
D) Proximity-based selection (touching vs. nearby) can vary in weight depending on design  

#### 19. Why might designers choose to use multiple coordinated views instead of a single animated view?  
A) Animated views are always easier to follow than multiple views  
B) Multiple views reduce cognitive load by externalizing memory to the eyes  
C) Juxtaposed views allow easier comparison across different data slices  
D) Animated views can be hard to follow if many scattered changes occur simultaneously  

#### 20. Which of the following are challenges when designing interactive visualizations for mobile devices?  
A) Lack of hover interaction limits some common desktop interaction patterns  
B) Small screen size restricts the number and size of visible controls  
C) Gestures and taps can replace all keyboard shortcuts effectively  
D) Users expect the same interaction complexity as on desktop



<br>

## Answers

#### 1. Which of the following are common ways to manipulate a data visualization interactively?  
A) ✓ Changing the visual encoding allows users to see data differently.  
B) ✓ Rearranging order helps reveal patterns or trends.  
C) ✗ Printing is static, not interactive.  
D) ✓ Adjusting filtering parameters changes what data is shown.  

**Correct:** A, B, D


#### 2. What are typical pros and cons of using widgets like sliders and dropdowns in interactive visualizations?  
A) ✓ Widgets provide clear affordances and are self-documenting with labels.  
B) ✓ Widgets consume screen space, which can clutter the interface.  
C) ✗ Widgets do not always improve performance; context matters.  
D) ✗ Widgets do not eliminate the need for other interaction methods.  

**Correct:** A, B


#### 3. Animated transitions in visualizations are primarily used to:  
A) ✓ Smooth changes help users track items across states.  
B) ✗ Animations do not replace all static visualizations.  
C) ✓ They reduce cognitive load by avoiding abrupt jumps.  
D) ✗ Entertainment is secondary; functional benefit is primary.  

**Correct:** A, C


#### 4. When designing for touch interaction on mobile devices, which considerations are important?  
A) ✗ Hover effects are unreliable on touchscreens.  
B) ✓ Tap and gestures are primary interaction methods.  
C) ✓ Small screens limit visible controls.  
D) ✗ Multiple clicks and keyboard shortcuts are not primary on mobile.  

**Correct:** B, C


#### 5. Which of the following statements about selection in interactive visualizations are true?  
A) ✓ Selection can be null (no items selected).  
B) ✓ Multiple selection types (primary, secondary) can coexist.  
C) ✗ Hover is not reliable on all devices, especially touchscreens.  
D) ✓ Selection semantics include adding or replacing selections.  

**Correct:** A, B, D


#### 6. Highlighting differs from selection because:  
A) ✓ Highlighting changes visual encoding without changing data state.  
B) ✗ Highlighting can use many channels, not just color.  
C) ✓ Outlines, size, and motion are valid highlighting methods.  
D) ✗ Highlighting and selection are related but separable concepts.  

**Correct:** A, C


#### 7. Which navigation techniques correspond to the "camera metaphor" in interactive visualization?  
A) ✓ Pan/translate/scroll moves the view like a camera.  
B) ✓ Zoom changes the camera’s distance to the scene.  
C) ✓ Rotate/spin changes the camera angle, mainly in 3D.  
D) ✗ Changing data encoding is not navigation.  

**Correct:** A, B, C


#### 8. What are the main tradeoffs between unconstrained and constrained navigation?  
A) ✗ Unconstrained navigation is often harder to control precisely.  
B) ✓ Constrained navigation uses animated transitions to guide users.  
C) ✓ Unconstrained navigation risks overshooting or undershooting targets.  
D) ✗ Constrained navigation still allows user control, just guided.  

**Correct:** B, C


#### 9. Scrollytelling as a navigation method has which of the following characteristics?  
A) ✓ It is intuitive because it mimics standard web browsing.  
B) ✗ It may lack direct access to all controls.  
C) ✓ It can cause unexpected behavior or “scrolljacking.”  
D) ✗ It supports continuous control, not just discrete steps.  

**Correct:** A, C


#### 10. Linked views in multiple coordinated visualizations typically:  
A) ✓ Share all data items but may show different attributes.  
B) ✗ Unidirectional linking is less effective than bidirectional.  
C) ✓ Selections in one view highlight related data in others.  
D) ✗ Linked views are common and useful, not confusing.  

**Correct:** A, C


#### 11. Which of the following are advantages of juxtaposing multiple views side by side?  
A) ✗ Each view has less screen space than a single full view.  
B) ✓ Reduces cognitive load by letting eyes move instead of memory.  
C) ✓ Easier to compare different data slices simultaneously.  
D) ✗ Juxtapose usually requires more display area than animation.  

**Correct:** B, C


#### 12. What are the limitations of interaction in data visualization?  
A) ✗ Interaction does not always speed up analysis; it can add overhead.  
B) ✓ Interaction imposes cognitive load by requiring memory of states.  
C) ✓ Controls take screen space or may be hard to discover.  
D) ✗ Users often do not interact as designers expect.  

**Correct:** B, C, D


#### 13. In partitioning data for multiple views, changing the order of splits (e.g., neighborhood then type vs. type then neighborhood) affects:  
A) ✓ Which patterns become visible or easier to compare.  
B) ✗ Color scheme is independent of split order.  
C) ✓ Spatial proximity encoding depends on split order.  
D) ✗ Total data points displayed remain the same.  

**Correct:** A, C


#### 14. Which of the following statements about layering in visualizations are true?  
A) ✓ Layering uses different visual channels to distinguish groups.  
B) ✗ More than three layers usually cause confusion.  
C) ✓ Static layering involves fixed elements like roads on maps.  
D) ✓ Dynamic layering highlights neighbors based on selection.  

**Correct:** A, C, D


#### 15. Small multiples differ from superimposed views because:  
A) ✓ Small multiples show different data slices in separate charts.  
B) ✓ Superimposed views overlay multiple data sets in one frame.  
C) ✗ Small multiples do not share the same data items; they show slices.  
D) ✓ Superimposed views are better for local tasks, not global.  

**Correct:** A, B


#### 16. Which of the following are true about tooltips in interactive visualizations?  
A) ✓ Tooltips provide additional detail on hover or click.  
B) ✗ Tooltips do not substitute for overview information.  
C) ✓ Important info should not rely solely on tooltips.  
D) ✗ Tooltips cannot replace all other interaction or highlighting.  

**Correct:** A, C


#### 17. What is a key benefit of animated transitions combined with constrained navigation?  
A) ✓ Automatically compute trajectories to nicely frame selections.  
B) ✗ They do not remove user input; users still control navigation.  
C) ✓ Preserve shape and layout during zoom or drill-down.  
D) ✗ They make navigation unpredictable; they improve predictability.  

**Correct:** A, C


#### 18. Which of the following interaction modalities are considered “lightweight” and which are “heavyweight”?  
A) ✓ Hover is lightweight because it requires no click.  
B) ✓ Click/tap is heavyweight due to explicit user action.  
C) ✗ Multiple click types are heavyweight, not lightweight.  
D) ✓ Proximity-based selection weight depends on design context.  

**Correct:** A, B, D


#### 19. Why might designers choose to use multiple coordinated views instead of a single animated view?  
A) ✗ Animated views are not always easier to follow.  
B) ✓ Multiple views reduce cognitive load by externalizing memory.  
C) ✓ Juxtaposed views allow easier comparison across slices.  
D) ✓ Animated views can be hard to follow with many scattered changes.  

**Correct:** B, C, D


#### 20. Which of the following are challenges when designing interactive visualizations for mobile devices?  
A) ✓ Lack of hover limits common desktop interaction patterns.  
B) ✓ Small screen size restricts number and size of controls.  
C) ✗ Gestures and taps cannot fully replace keyboard shortcuts.  
D) ✗ Users do not expect the same interaction complexity as desktop.  

**Correct:** A, B