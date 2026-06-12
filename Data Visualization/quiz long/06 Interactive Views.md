## 7. Interactive Views

## Questions

#### 1. Which of the following are common ways to manipulate a data visualization interactively?  
A) Printing the visualization on paper  
B) Adjusting filtering parameters  
C) Rearranging the order of data elements  
D) Changing the visual encoding  

#### 2. What are typical pros and cons of using widgets like sliders and dropdowns in interactive visualizations?  
A) They always improve user performance regardless of context  
B) They eliminate the need for any other interaction methods  
C) They consume screen space, potentially cluttering the interface  
D) They provide clear affordances and are self-documenting  

#### 3. Animated transitions in visualizations are primarily used to:  
A) Reduce cognitive load by avoiding abrupt changes  
B) Provide a smooth change between states to help users track items  
C) Replace all static visualizations with animations  
D) Make the visualization more entertaining without functional benefit  

#### 4. When designing for touch interaction on mobile devices, which considerations are important?  
A) Multiple clicks and keyboard shortcuts are the main interaction methods  
B) Tap and gesture-based interactions are primary  
C) Screen size constraints limit the number of visible controls  
D) Hover effects are reliable and should be heavily used  

#### 5. Which of the following statements about selection in interactive visualizations are true?  
A) Hover is always a reliable method for selection on all devices  
B) Selection semantics can include adding to or replacing the current selection  
C) Multiple selection types (e.g., primary and secondary) can coexist  
D) Selection can be null, meaning no items are selected  

#### 6. Highlighting differs from selection because:  
A) Highlighting can use outlines, size changes, or motion  
B) Highlighting always uses color changes exclusively  
C) Highlighting changes the visual encoding without changing the data state  
D) Highlighting and selection are always inseparable and identical  

#### 7. Which navigation techniques correspond to the "camera metaphor" in interactive visualization?  
A) Pan/translate/scroll  
B) Changing data encoding  
C) Zoom in/out  
D) Rotate/spin (mainly in 3D)  

#### 8. What are the main tradeoffs between unconstrained and constrained navigation?  
A) Constrained navigation often uses animated transitions to guide the user  
B) Unconstrained navigation is easier for users to control precisely  
C) Unconstrained navigation can lead to overshooting or undershooting the target  
D) Constrained navigation removes all user control over the view  

#### 9. Scrollytelling as a navigation method has which of the following characteristics?  
A) It can cause unexpected behavior or “scrolljacking”  
B) It is intuitive because it mimics standard web browsing  
C) It always provides direct access to all visualization controls  
D) It supports only discrete steps, not continuous control  

#### 10. Linked views in multiple coordinated visualizations typically:  
A) Allow selections in one view to highlight related data in others  
B) Share all data items but may show different attributes  
C) Are rarely used because they confuse users  
D) Use unidirectional linking exclusively for better performance  

#### 11. Which of the following are advantages of juxtaposing multiple views side by side?  
A) It makes it easier to compare different data slices simultaneously  
B) It reduces cognitive load by allowing eye movement instead of memory reliance  
C) It always requires less display area than animated transitions  
D) Each view has more screen space than a single view  

#### 12. What are the limitations of interaction in data visualization?  
A) Controls may take up valuable screen space or be hard to discover  
B) Interaction can impose cognitive load by requiring users to remember previous states  
C) Users always interact exactly as designers intend  
D) Interaction always speeds up data analysis without any drawbacks  

#### 13. In partitioning data for multiple views, changing the order of splits (e.g., neighborhood then type vs. type then neighborhood) affects:  
A) The spatial proximity encoding of associated items  
B) The color scheme of the visualization  
C) The total number of data points displayed  
D) Which patterns become visible or easier to compare  

#### 14. Which of the following statements about layering in visualizations are true?  
A) Layering can use different visual channels like color and size to distinguish groups  
B) Static layering involves fixed visual elements like roads on a map  
C) Dynamic layering can highlight neighbors based on user selection  
D) More than three layers are easy to distinguish without confusion  

#### 15. Small multiples differ from superimposed views because:  
A) Small multiples always share the same data items across views  
B) Small multiples show different slices of data in separate charts  
C) Superimposed views are better for global comparison tasks  
D) Superimposed views overlay multiple data sets in the same frame  

#### 16. Which of the following are true about tooltips in interactive visualizations?  
A) Important information should not rely solely on tooltips because users may miss them  
B) Tooltips provide additional detail on demand, often on hover or click  
C) Tooltips can replace the need for any other interaction or highlighting  
D) Tooltips are a good substitute for overview information  

#### 17. What is a key benefit of animated transitions combined with constrained navigation?  
A) They automatically compute trajectories to frame selected data nicely  
B) They make navigation unpredictable and harder to follow  
C) They preserve shape and layout during zooming or drill-down  
D) They remove the need for any user input during navigation  

#### 18. Which of the following interaction modalities are considered “lightweight” and which are “heavyweight”?  
A) Multiple click types (shift-click, option-click) are lightweight  
B) Click/tap is heavyweight because it requires explicit user action  
C) Proximity-based selection (touching vs. nearby) can vary in weight depending on design  
D) Hover is lightweight because it requires no click  

#### 19. Why might designers choose to use multiple coordinated views instead of a single animated view?  
A) Animated views can be hard to follow if many scattered changes occur simultaneously  
B) Multiple views reduce cognitive load by externalizing memory to the eyes  
C) Juxtaposed views allow easier comparison across different data slices  
D) Animated views are always easier to follow than multiple views  

#### 20. Which of the following are challenges when designing interactive visualizations for mobile devices?  
A) Lack of hover interaction limits some common desktop interaction patterns  
B) Gestures and taps can replace all keyboard shortcuts effectively  
C) Small screen size restricts the number and size of visible controls  
D) Users expect the same interaction complexity as on desktop  



<br>

## Answers

#### 1. Which of the following are common ways to manipulate a data visualization interactively?  
A) ✗ Printing is static, not interactive.  
B) ✓ Adjusting filtering parameters changes what data is shown.  
C) ✓ Rearranging order helps reveal patterns or trends.  
D) ✓ Changing the visual encoding allows users to see data differently.  

**Correct:** B, C, D


#### 2. What are typical pros and cons of using widgets like sliders and dropdowns in interactive visualizations?  
A) ✗ Widgets do not always improve performance; context matters.  
B) ✗ Widgets do not eliminate the need for other interaction methods.  
C) ✓ Widgets consume screen space, which can clutter the interface.  
D) ✓ Widgets provide clear affordances and are self-documenting with labels.  

**Correct:** C, D


#### 3. Animated transitions in visualizations are primarily used to:  
A) ✓ They reduce cognitive load by avoiding abrupt jumps.  
B) ✓ Smooth changes help users track items across states.  
C) ✗ Animations do not replace all static visualizations.  
D) ✗ Entertainment is secondary; functional benefit is primary.  

**Correct:** A, B


#### 4. When designing for touch interaction on mobile devices, which considerations are important?  
A) ✗ Multiple clicks and keyboard shortcuts are not primary on mobile.  
B) ✓ Tap and gestures are primary interaction methods.  
C) ✓ Small screens limit visible controls.  
D) ✗ Hover effects are unreliable on touchscreens.  

**Correct:** B, C


#### 5. Which of the following statements about selection in interactive visualizations are true?  
A) ✗ Hover is not reliable on all devices, especially touchscreens.  
B) ✓ Selection semantics include adding or replacing selections.  
C) ✓ Multiple selection types (primary, secondary) can coexist.  
D) ✓ Selection can be null (no items selected).  

**Correct:** B, C, D


#### 6. Highlighting differs from selection because:  
A) ✓ Outlines, size, and motion are valid highlighting methods.  
B) ✗ Highlighting can use many channels, not just color.  
C) ✓ Highlighting changes visual encoding without changing data state.  
D) ✗ Highlighting and selection are related but separable concepts.  

**Correct:** A, C


#### 7. Which navigation techniques correspond to the "camera metaphor" in interactive visualization?  
A) ✓ Pan/translate/scroll moves the view like a camera.  
B) ✗ Changing data encoding is not navigation.  
C) ✓ Zoom changes the camera’s distance to the scene.  
D) ✓ Rotate/spin changes the camera angle, mainly in 3D.  

**Correct:** A, C, D


#### 8. What are the main tradeoffs between unconstrained and constrained navigation?  
A) ✓ Constrained navigation uses animated transitions to guide users.  
B) ✗ Unconstrained navigation is often harder to control precisely.  
C) ✓ Unconstrained navigation risks overshooting or undershooting targets.  
D) ✗ Constrained navigation still allows user control, just guided.  

**Correct:** A, C


#### 9. Scrollytelling as a navigation method has which of the following characteristics?  
A) ✓ It can cause unexpected behavior or “scrolljacking.”  
B) ✓ It is intuitive because it mimics standard web browsing.  
C) ✗ It may lack direct access to all controls.  
D) ✗ It supports continuous control, not just discrete steps.  

**Correct:** A, B


#### 10. Linked views in multiple coordinated visualizations typically:  
A) ✓ Selections in one view highlight related data in others.  
B) ✓ Share all data items but may show different attributes.  
C) ✗ Linked views are common and useful, not confusing.  
D) ✗ Unidirectional linking is less effective than bidirectional.  

**Correct:** A, B


#### 11. Which of the following are advantages of juxtaposing multiple views side by side?  
A) ✓ Easier to compare different data slices simultaneously.  
B) ✓ Reduces cognitive load by letting eyes move instead of memory.  
C) ✗ Juxtapose usually requires more display area than animation.  
D) ✗ Each view has less screen space than a single full view.  

**Correct:** A, B


#### 12. What are the limitations of interaction in data visualization?  
A) ✓ Controls take screen space or may be hard to discover.  
B) ✓ Interaction imposes cognitive load by requiring memory of states.  
C) ✗ Users often do not interact as designers expect.  
D) ✗ Interaction does not always speed up analysis; it can add overhead.  

**Correct:** A, B, C


#### 13. In partitioning data for multiple views, changing the order of splits (e.g., neighborhood then type vs. type then neighborhood) affects:  
A) ✓ Spatial proximity encoding depends on split order.  
B) ✗ Color scheme is independent of split order.  
C) ✗ Total data points displayed remain the same.  
D) ✓ Which patterns become visible or easier to compare.  

**Correct:** A, D


#### 14. Which of the following statements about layering in visualizations are true?  
A) ✓ Layering uses different visual channels to distinguish groups.  
B) ✓ Static layering involves fixed elements like roads on maps.  
C) ✓ Dynamic layering highlights neighbors based on selection.  
D) ✗ More than three layers usually cause confusion.  

**Correct:** A, B, C


#### 15. Small multiples differ from superimposed views because:  
A) ✗ Small multiples do not share the same data items; they show slices.  
B) ✓ Small multiples show different data slices in separate charts.  
C) ✓ Superimposed views are better for local tasks, not global.  
D) ✓ Superimposed views overlay multiple data sets in one frame.  

**Correct:** B, D


#### 16. Which of the following are true about tooltips in interactive visualizations?  
A) ✓ Important info should not rely solely on tooltips.  
B) ✓ Tooltips provide additional detail on hover or click.  
C) ✗ Tooltips cannot replace all other interaction or highlighting.  
D) ✗ Tooltips do not substitute for overview information.  

**Correct:** A, B


#### 17. What is a key benefit of animated transitions combined with constrained navigation?  
A) ✓ Automatically compute trajectories to nicely frame selections.  
B) ✗ They make navigation unpredictable; they improve predictability.  
C) ✓ Preserve shape and layout during zoom or drill-down.  
D) ✗ They do not remove user input; users still control navigation.  

**Correct:** A, C


#### 18. Which of the following interaction modalities are considered “lightweight” and which are “heavyweight”?  
A) ✗ Multiple click types are heavyweight, not lightweight.  
B) ✓ Click/tap is heavyweight due to explicit user action.  
C) ✓ Proximity-based selection weight depends on design context.  
D) ✓ Hover is lightweight because it requires no click.  

**Correct:** B, C, D


#### 19. Why might designers choose to use multiple coordinated views instead of a single animated view?  
A) ✓ Animated views can be hard to follow with many scattered changes.  
B) ✓ Multiple views reduce cognitive load by externalizing memory.  
C) ✓ Juxtaposed views allow easier comparison across slices.  
D) ✗ Animated views are not always easier to follow.  

**Correct:** A, B, C


#### 20. Which of the following are challenges when designing interactive visualizations for mobile devices?  
A) ✓ Lack of hover limits common desktop interaction patterns.  
B) ✗ Gestures and taps cannot fully replace keyboard shortcuts.  
C) ✓ Small screen size restricts number and size of controls.  
D) ✗ Users do not expect the same interaction complexity as desktop.  

**Correct:** A, C