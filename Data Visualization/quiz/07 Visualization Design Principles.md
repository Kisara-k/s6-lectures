## 8. Visualization Design Principles

## Questions

#### 1. Which of the following best describe the concept of "data-ink ratio" in visualization design?  
A) The proportion of ink used to decorate a graphic compared to the total ink used  
B) The amount of ink used to print the graphic divided by the number of data points  
C) The ratio of ink used to represent actual data to the total ink used in the graphic  
D) The percentage of ink used for gridlines and labels in a chart  

#### 2. When is the use of 3D visualization justified over 2D?  
A) When representing abstract data like time series or categorical data  
B) When interactive navigation allows synthesis across multiple viewpoints  
C) When the goal is to impress the audience with visual effects  
D) When the task requires shape perception of true 3D spatial data  

#### 3. Which of the following statements about data density are true?  
A) Data density is calculated as the number of data entries divided by the area of the graphic  
B) High data density can be achieved by layering information and using small multiples  
C) Increasing data density always improves clarity and insight extraction  
D) Data density should be maximized even if it causes overcrowding and confusion  

#### 4. What does a Lie Factor significantly greater than 1.05 indicate in a data visualization?  
A) The graphic accurately represents the data without distortion  
B) The visualization underrepresents the magnitude of the data change  
C) The size of the effect shown in the graphic exaggerates the actual data effect  
D) The graphic uses proportional scaling between data and visual elements  

#### 5. Which of the following are recommended practices to ensure integrity and accuracy in visualizations?  
A) Omitting axis labels to reduce clutter and improve aesthetics  
B) Starting the y-axis at a non-zero value to highlight small differences  
C) Using consistent and proportional scales for graphical elements  
D) Clearly labeling important events and providing detailed explanations on the graph  

#### 6. Why is it generally better to use 2D visualizations instead of 3D for abstract data?  
A) 3D visualizations avoid occlusion and perspective distortion  
B) 2D visualizations are easier to interpret and less likely to mislead  
C) 3D visualizations always have a higher data-ink ratio than 2D  
D) Text and labels are more legible in 2D than when tilted in 3D space  

#### 7. Which of the following are true about designing for universal accessibility in visualizations?  
A) Considering readability for visually impaired audiences by using appropriate font sizes and contrasts  
B) Using color schemes that are distinguishable by people with different types of color blindness  
C) Relying solely on color differences to convey important information  
D) Providing alternative text descriptions for images and charts  

#### 8. The principle "Eyes Beat Memory" implies which of the following design choices?  
A) Use animations with many changing elements to show data over time  
B) Avoid forcing users to remember previous views to understand current data  
C) Rely on users’ memory to compare data points across different charts  
D) Use small multiples to allow side-by-side comparison of data  

#### 9. According to Shneiderman’s mantra "Overview first, zoom and filter, details on demand," which of the following is NOT a correct interpretation?  
A) Allow users to zoom into areas of interest and filter irrelevant data  
B) Enable users to request detailed information only when needed  
C) Provide a summary view of the entire dataset initially  
D) Show all details upfront to avoid the need for interaction  

#### 10. What are the risks of using unjustified 3D effects in data visualization?  
A) Reduced legibility of tilted text and labels  
B) Occlusion hiding important parts of the data  
C) Improved clarity and higher data density compared to 2D charts  
D) Perspective distortion that interferes with accurate size perception  



<br>

## Answers

#### 1. Which of the following best describe the concept of "data-ink ratio" in visualization design?  
A) ✗ Data-ink ratio is about ink representing data, not decoration.  
B) ✗ Ink amount is not divided by data points; it’s a ratio of data ink to total ink.  
C) ✓ The data-ink ratio measures the proportion of ink used to show actual data versus total ink.  
D) ✗ Gridlines and labels are usually non-data ink and should be minimized.  

**Correct:** C


#### 2. When is the use of 3D visualization justified over 2D?  
A) ✗ Abstract data like time series is better shown in 2D to avoid distortion.  
B) ✓ Interactive navigation in 3D helps synthesize multiple viewpoints, justifying 3D use.  
C) ✗ Using 3D just to impress is discouraged due to distortion and occlusion risks.  
D) ✓ True 3D spatial data requiring shape perception benefits from 3D visualization.  

**Correct:** B, D


#### 3. Which of the following statements about data density are true?  
A) ✓ Data density is defined as number of data entries divided by graphic area.  
B) ✓ Small multiples and layering are effective ways to increase data density without losing clarity.  
C) ✗ Increasing data density can overwhelm and reduce clarity if overdone.  
D) ✗ Overcrowding data reduces clarity and should be avoided.  

**Correct:** A, B


#### 4. What does a Lie Factor significantly greater than 1.05 indicate in a data visualization?  
A) ✗ Lie Factor >1.05 means distortion, not accurate representation.  
B) ✗ Underrepresentation corresponds to Lie Factor <0.95, not >1.05.  
C) ✓ The graphic exaggerates the size of the effect compared to actual data.  
D) ✗ Proportional scaling would produce a Lie Factor close to 1, not >1.05.  

**Correct:** C


#### 5. Which of the following are recommended practices to ensure integrity and accuracy in visualizations?  
A) ✗ Omitting axis labels causes ambiguity and reduces clarity.  
B) ✗ Starting y-axis at non-zero can mislead by exaggerating differences.  
C) ✓ Proportional scales ensure accurate visual representation of data.  
D) ✓ Detailed labeling and explanations prevent distortion and confusion.  

**Correct:** C, D


#### 6. Why is it generally better to use 2D visualizations instead of 3D for abstract data?  
A) ✗ 3D visualizations often cause occlusion and perspective distortion.  
B) ✓ 2D is easier to interpret and less likely to mislead viewers.  
C) ✗ 3D does not inherently have a higher data-ink ratio than 2D.  
D) ✓ Text and labels are more legible in 2D than when tilted in 3D space.  

**Correct:** B, D


#### 7. Which of the following are true about designing for universal accessibility in visualizations?  
A) ✓ Readability considerations like font size and contrast aid accessibility.  
B) ✓ Color schemes must accommodate different types of color blindness.  
C) ✗ Relying only on color differences excludes color-blind users.  
D) ✓ Alternative text helps visually impaired users understand images.  

**Correct:** A, B, D


#### 8. The principle "Eyes Beat Memory" implies which of the following design choices?  
A) ✗ Animations with many changing elements overload memory and reduce clarity.  
B) ✓ Avoiding reliance on memory improves comprehension and reduces errors.  
C) ✗ Relying on memory to compare data is less effective than visual comparison.  
D) ✓ Small multiples allow easy side-by-side comparison without memory load.  

**Correct:** B, D


#### 9. According to Shneiderman’s mantra "Overview first, zoom and filter, details on demand," which of the following is NOT a correct interpretation?  
A) ✓ Allowing zoom and filter is part of the mantra.  
B) ✓ Enabling details on demand matches the mantra’s guidance.  
C) ✓ Providing a summary view initially is correct.  
D) ✗ Showing all details upfront contradicts the "details on demand" principle.  

**Correct:** D


#### 10. What are the risks of using unjustified 3D effects in data visualization?  
A) ✓ Tilted text in 3D is harder to read, reducing legibility.  
B) ✓ Occlusion hides important data elements.  
C) ✗ 3D often reduces clarity and data density compared to 2D.  
D) ✓ Perspective distortion misleads size perception.  

**Correct:** A, B, D