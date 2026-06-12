## 9. Visualizations for Tabular Data

## Questions

#### 1. Which of the following statements correctly describe the role of keys in tabular data visualizations?  
A) Keys are dependent attributes representing the values in cells.  
B) Keys are always quantitative attributes.  
C) Simple tables typically have one key, while multidimensional tables have multiple keys.  
D) Keys serve as unique indices to look up items in the table.  

#### 2. In a scatterplot, which visual channels are primarily used to encode data?  
A) Size of points (with area proportional to the square root of the value)  
B) Length of bars  
C) Color hue and saturation  
D) Horizontal and vertical position  

#### 3. What are the main advantages of connected scatterplots compared to standard scatterplots?  
A) They serve as an alternative to dual-axis charts.  
B) They improve clarity of correlation between variables.  
C) They reduce visual clutter by removing point marks.  
D) They explicitly show temporal order through line connections.  

#### 4. When is it appropriate to use a line chart instead of a bar chart?  
A) When the key attribute is ordered, such as time.  
B) When the key attribute is nominal with no inherent order.  
C) When the data represents part-to-whole relationships.  
D) When the key attribute is categorical and unordered.  

#### 5. Which of the following are limitations of stacked bar charts?  
A) They are effective for showing part-to-whole relationships.  
B) Scalability is limited by the number of segments per stack.  
C) Ordering of segments within stacks is always clear and intuitive.  
D) They can only display one categorical key attribute.  

#### 6. Why should the radius of points in a scatterplot be scaled by the square root of the quantitative attribute rather than the raw value?  
A) Because area perception grows quadratically with radius.  
B) To make the points visually larger and easier to see.  
C) To ensure the area of the point grows linearly with the value.  
D) To avoid misleading viewers about the magnitude of the data.  

#### 7. Which tasks are best supported by heatmaps?  
A) Comparing exact quantitative values between two categories.  
B) Finding clusters and outliers in large categorical datasets.  
C) Showing temporal trends over ordered keys.  
D) Visualizing part-to-whole relationships.  

#### 8. What are the main challenges when using parallel coordinates for multivariate data visualization?  
A) They can only show two attributes at a time.  
B) They are intuitive and require no training to interpret.  
C) Axis ordering significantly affects pattern detection.  
D) They require user interaction or algorithms to reorder axes effectively.  

#### 9. Which of the following are true about pie charts?  
A) They become less accurate as the number of categories increases.  
B) They encode data using angle channels representing 2D area.  
C) They are generally more accurate than bar charts for comparing values.  
D) They are effective for part-to-whole judgments with many categories.  

#### 10. What is a key difference between a slopegraph and a standard line chart?  
A) Slopegraphs emphasize changes in rank or value between two points.  
B) Slopegraphs connect multiple points over time with continuous lines.  
C) Slopegraphs use line width and color to encode additional variables.  
D) Slopegraphs are best for showing trends across many time points.  

#### 11. Which of the following statements about scatterplot matrices (SPLOM) are correct?  
A) They show all pairwise relationships between multiple quantitative variables.  
B) They are scalable to dozens of variables and hundreds of items.  
C) They use radial axes to represent variables.  
D) They are limited to showing only two variables at a time.  

#### 12. Why is it generally advised to avoid using line charts for categorical key attributes?  
A) Because bar charts are always more visually appealing.  
B) Because line charts imply continuity and trends that may not exist.  
C) Because line charts cannot encode quantitative values.  
D) Because it violates the expressiveness principle of visualization.  

#### 13. What are the main visual channels used in a Gantt chart?  
A) Horizontal position for start time.  
B) Color hue for categorical keys.  
C) Vertical position for quantitative values.  
D) Length of bars for duration.  

#### 14. Which of the following are true about radial visualizations like radar plots and radial bar charts?  
A) Length encoding in radial layouts is less precise due to angle perception issues.  
B) They are more accurately perceived than rectilinear bar charts.  
C) They use uniform sector widths regardless of radial distance.  
D) They can be useful when data is cyclic or attributes have unequal importance.  

#### 15. What is a major limitation of using truncated y-axes in charts?  
A) It always improves clarity by focusing on relevant data ranges.  
B) It is acceptable when zero is arbitrary or small changes matter.  
C) It can mislead viewers by exaggerating slopes or changes.  
D) It is recommended for all bar charts to save space.  

#### 16. Which of the following best describe the scalability of scatterplots?  
A) They cannot encode more than two quantitative variables.  
B) They can effectively display hundreds of data points.  
C) They are limited to fewer than 50 points due to clutter.  
D) Adding color and size channels can increase information density without losing clarity.  

#### 17. In a normalized stacked bar chart, what is the main purpose of normalization?  
A) To show absolute values of each segment.  
B) To make the chart equivalent to a pie chart in terms of information density.  
C) To enable part-to-whole comparisons by scaling bars to the same height.  
D) To reduce the number of categories displayed.  

#### 18. Which of the following are true about cluster heatmaps?  
A) They are less effective than standard heatmaps for finding clusters.  
B) They help assess the quality of clusters found by automatic methods.  
C) They reorder rows and columns based on hierarchical clustering.  
D) They use dendrograms to show parent-child relationships.  

#### 19. What are the main tasks supported by scatterplots?  
A) Identifying clusters or groups within data.  
B) Detecting outliers and distribution patterns.  
C) Showing part-to-whole relationships.  
D) Finding correlations between two quantitative variables.  

#### 20. Which of the following statements about axis labeling and chart best practices are correct?  
A) Axes should always be labeled unless the chart is a small multiple sharing labels.  
B) Dual-axis charts are always misleading and should be avoided.  
C) Cropping the y-axis is acceptable in all cases to focus on data variation.  
D) Including zero on the y-axis prevents misleading interpretations of slopes.  



<br>

## Answers

#### 1. Which of the following statements correctly describe the role of keys in tabular data visualizations?  
A) ✗ Keys are independent, not dependent attributes.  
B) ✗ Keys can be categorical or quantitative, not always quantitative.  
C) ✓ Simple tables have one key; multidimensional tables have multiple keys.  
D) ✓ Keys serve as unique indices to look up items.  

**Correct:** C, D


#### 2. In a scatterplot, which visual channels are primarily used to encode data?  
A) ✓ Size of points can encode a third quantitative variable, scaled by square root.  
B) ✗ Length of bars is not used in scatterplots.  
C) ✓ Color can be used to encode additional variables or categories.  
D) ✓ Horizontal and vertical position encode the two quantitative variables.  

**Correct:** A, C, D


#### 3. What are the main advantages of connected scatterplots compared to standard scatterplots?  
A) ✓ They can serve as an alternative to dual-axis charts.  
B) ✗ Correlation clarity can be reduced, not improved.  
C) ✗ Point marks are still present; lines add to them, not remove.  
D) ✓ They show temporal order via connecting lines.  

**Correct:** A, D


#### 4. When is it appropriate to use a line chart instead of a bar chart?  
A) ✓ Line charts are suitable for ordered keys like time.  
B) ✗ Line charts imply order, so not for nominal keys.  
C) ✗ Part-to-whole relationships are better shown with bar charts.  
D) ✗ Line charts are not appropriate for unordered categorical keys.  

**Correct:** A


#### 5. Which of the following are limitations of stacked bar charts?  
A) ✓ They effectively show part-to-whole relationships.  
B) ✓ Scalability is limited by the number of segments per stack.  
C) ✗ Ordering segments can be confusing and not always intuitive.  
D) ✗ They display two categorical keys, not just one.  

**Correct:** A, B


#### 6. Why should the radius of points in a scatterplot be scaled by the square root of the quantitative attribute rather than the raw value?  
A) ✓ Area grows quadratically with radius, so square root scaling corrects this.  
B) ✗ Making points larger is not the main reason.  
C) ✓ To ensure area grows linearly with value, avoiding misperception.  
D) ✓ Avoids misleading viewers about magnitude.  

**Correct:** A, C, D


#### 7. Which tasks are best supported by heatmaps?  
A) ✗ Exact value comparison is difficult due to color perception limits.  
B) ✓ Heatmaps excel at finding clusters and outliers in categorical data.  
C) ✗ Temporal trends are better shown with line or streamgraphs.  
D) ✗ Part-to-whole is not the primary task for heatmaps.  

**Correct:** B


#### 8. What are the main challenges when using parallel coordinates for multivariate data visualization?  
A) ✗ Parallel coordinates can show many attributes, not just two.  
B) ✗ They are not intuitive and require training.  
C) ✓ Axis ordering greatly affects pattern detection.  
D) ✓ Reordering axes requires interaction or algorithms.  

**Correct:** C, D


#### 9. Which of the following are true about pie charts?  
A) ✓ Accuracy decreases as category count increases.  
B) ✓ Pie charts encode data using angles representing 2D area.  
C) ✗ Bar charts are generally more accurate for value comparison.  
D) ✗ They are poor for many categories due to accuracy issues.  

**Correct:** A, B


#### 10. What is a key difference between a slopegraph and a standard line chart?  
A) ✓ Slopegraphs emphasize changes between two points, not continuous trends.  
B) ✗ Slopegraphs do not connect multiple points over time continuously.  
C) ✓ Line width and color can encode change magnitude or direction.  
D) ✗ They are not designed for many time points.  

**Correct:** A, C


#### 11. Which of the following statements about scatterplot matrices (SPLOM) are correct?  
A) ✓ SPLOMs show all pairwise relationships between quantitative variables.  
B) ✓ They scale to dozens of variables and hundreds of items.  
C) ✗ They use rectilinear, not radial, axes.  
D) ✗ They show multiple pairs simultaneously, not just two variables.  

**Correct:** A, B


#### 12. Why is it generally advised to avoid using line charts for categorical key attributes?  
A) ✗ Visual appeal is not the main reason.  
B) ✓ Line charts imply continuity and trends that may not exist.  
C) ✗ Line charts can encode quantitative values.  
D) ✓ Using line charts for categorical keys violates expressiveness principles.  

**Correct:** B, D


#### 13. What are the main visual channels used in a Gantt chart?  
A) ✓ Horizontal position encodes start time.  
B) ✗ Color hue is optional but not a main channel.  
C) ✗ Vertical position encodes categorical keys, not quantitative values.  
D) ✓ Length encodes duration.  

**Correct:** A, D


#### 14. Which of the following are true about radial visualizations like radar plots and radial bar charts?  
A) ✓ Length encoding is less precise due to angle perception issues.  
B) ✗ They are less accurately perceived than rectilinear charts.  
C) ✗ Sector widths vary with radial distance, not uniform.  
D) ✓ Useful when data is cyclic or attributes have unequal importance.  

**Correct:** A, D


#### 15. What is a major limitation of using truncated y-axes in charts?  
A) ✗ It does not always improve clarity; often misleading.  
B) ✓ Acceptable only in specific cases like arbitrary zero or small changes.  
C) ✓ It can mislead viewers by exaggerating slopes or changes.  
D) ✗ Not recommended for all bar charts.  

**Correct:** B, C


#### 16. Which of the following best describe the scalability of scatterplots?  
A) ✗ Can encode more than two quantitative variables via additional channels.  
B) ✓ Can effectively display hundreds of points.  
C) ✗ Not limited to fewer than 50 points.  
D) ✓ Adding color and size channels increases information density without losing clarity.  

**Correct:** A, B, D


#### 17. In a normalized stacked bar chart, what is the main purpose of normalization?  
A) ✗ It does not show absolute values.  
B) ✓ Makes the chart equivalent to a pie chart in information density.  
C) ✓ Enables part-to-whole comparisons by scaling bars to the same height.  
D) ✗ Does not reduce the number of categories.  

**Correct:** B, C


#### 18. Which of the following are true about cluster heatmaps?  
A) ✗ More effective than standard heatmaps for finding clusters.  
B) ✓ Help assess cluster quality from automatic methods.  
C) ✓ They reorder rows and columns based on hierarchical clustering.  
D) ✓ Use dendrograms to show parent-child relationships.  

**Correct:** B, C, D


#### 19. What are the main tasks supported by scatterplots?  
A) ✓ Identifying clusters or groups.  
B) ✓ Detecting outliers and distribution patterns.  
C) ✗ Not designed for part-to-whole relationships.  
D) ✓ Finding correlations between two quantitative variables.  

**Correct:** A, B, D


#### 20. Which of the following statements about axis labeling and chart best practices are correct?  
A) ✓ Axes should always be labeled unless small multiples share labels.  
B) ✗ Dual-axis charts are controversial but not always misleading.  
C) ✗ Cropping y-axis is not acceptable in all cases.  
D) ✓ Including zero on y-axis prevents misleading slope interpretations.  

**Correct:** A, D