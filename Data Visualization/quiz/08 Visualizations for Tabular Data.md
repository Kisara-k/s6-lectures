## 9. Visualizations for Tabular Data

## Questions

#### 1. Which of the following statements correctly describe the role of keys in tabular data visualizations?  
A) Keys are dependent attributes representing the values in cells.  
B) Simple tables typically have one key, while multidimensional tables have multiple keys.  
C) Keys serve as unique indices to look up items in the table.  
D) Keys are always quantitative attributes.

#### 2. In a scatterplot, which visual channels are primarily used to encode data?  
A) Color hue and saturation  
B) Size of points (with area proportional to the square root of the value)
C) Length of bars  
D) Horizontal and vertical position  

#### 3. What are the main advantages of connected scatterplots compared to standard scatterplots?  
A) They explicitly show temporal order through line connections.  
B) They serve as an alternative to dual-axis charts.  
C) They reduce visual clutter by removing point marks.
D) They improve clarity of correlation between variables.  

#### 4. When is it appropriate to use a line chart instead of a bar chart?  
A) When the key attribute is ordered, such as time.  
B) When the key attribute is nominal with no inherent order.
C) When the data represents part-to-whole relationships.  
D) When the key attribute is categorical and unordered.  

#### 5. Which of the following are limitations of stacked bar charts?  
A) They are effective for showing part-to-whole relationships.  
B) Ordering of segments within stacks is always clear and intuitive.
C) They can only display one categorical key attribute.  
D) Scalability is limited by the number of segments per stack.  

#### 6. Why should the radius of points in a scatterplot be scaled by the square root of the quantitative attribute rather than the raw value?  
A) Because area perception grows quadratically with radius.  
B) To ensure the area of the point grows linearly with the value.  
C) To avoid misleading viewers about the magnitude of the data.
D) To make the points visually larger and easier to see.  

#### 7. Which tasks are best supported by heatmaps?  
A) Finding clusters and outliers in large categorical datasets.  
B) Showing temporal trends over ordered keys.  
C) Comparing exact quantitative values between two categories.  
D) Visualizing part-to-whole relationships.

#### 8. What are the main challenges when using parallel coordinates for multivariate data visualization?  
A) Axis ordering significantly affects pattern detection.  
B) They can only show two attributes at a time.  
C) They require user interaction or algorithms to reorder axes effectively.  
D) They are intuitive and require no training to interpret.

#### 9. Which of the following are true about pie charts?  
A) They are effective for part-to-whole judgments with many categories.  
B) They become less accurate as the number of categories increases.  
C) They are generally more accurate than bar charts for comparing values.
D) They encode data using angle channels representing 2D area.  

#### 10. What is a key difference between a slopegraph and a standard line chart?  
A) Slopegraphs connect multiple points over time with continuous lines.  
B) Slopegraphs emphasize changes in rank or value between two points.  
C) Slopegraphs are best for showing trends across many time points.  
D) Slopegraphs use line width and color to encode additional variables.

#### 11. Which of the following statements about scatterplot matrices (SPLOM) are correct?  
A) They are scalable to dozens of variables and hundreds of items.  
B) They show all pairwise relationships between multiple quantitative variables.  
C) They are limited to showing only two variables at a time.
D) They use radial axes to represent variables.  

#### 12. Why is it generally advised to avoid using line charts for categorical key attributes?  
A) Because line charts imply continuity and trends that may not exist.  
B) Because bar charts are always more visually appealing.  
C) Because it violates the expressiveness principle of visualization.
D) Because line charts cannot encode quantitative values.  

#### 13. What are the main visual channels used in a Gantt chart?  
A) Color hue for categorical keys.  
B) Vertical position for quantitative values.
C) Horizontal position for start time.  
D) Length of bars for duration.  

#### 14. Which of the following are true about radial visualizations like radar plots and radial bar charts?  
A) They use uniform sector widths regardless of radial distance.
B) They are more accurately perceived than rectilinear bar charts.  
C) They can be useful when data is cyclic or attributes have unequal importance.  
D) Length encoding in radial layouts is less precise due to angle perception issues.  

#### 15. What is a major limitation of using truncated y-axes in charts?  
A) It always improves clarity by focusing on relevant data ranges.  
B) It is acceptable when zero is arbitrary or small changes matter.  
C) It is recommended for all bar charts to save space.
D) It can mislead viewers by exaggerating slopes or changes.  

#### 16. Which of the following best describe the scalability of scatterplots?  
A) They can effectively display hundreds of data points.  
B) They are limited to fewer than 50 points due to clutter.  
C) Adding color and size channels can increase information density without losing clarity.  
D) They cannot encode more than two quantitative variables.

#### 17. In a normalized stacked bar chart, what is the main purpose of normalization?  
A) To enable part-to-whole comparisons by scaling bars to the same height.  
B) To reduce the number of categories displayed.  
C) To show absolute values of each segment.  
D) To make the chart equivalent to a pie chart in terms of information density.

#### 18. Which of the following are true about cluster heatmaps?  
A) They are less effective than standard heatmaps for finding clusters.  
B) They reorder rows and columns based on hierarchical clustering.  
C) They use dendrograms to show parent-child relationships.  
D) They help assess the quality of clusters found by automatic methods.

#### 19. What are the main tasks supported by scatterplots?  
A) Identifying clusters or groups within data.  
B) Detecting outliers and distribution patterns.
C) Finding correlations between two quantitative variables.  
D) Showing part-to-whole relationships.  

#### 20. Which of the following statements about axis labeling and chart best practices are correct?  
A) Dual-axis charts are always misleading and should be avoided.
B) Including zero on the y-axis prevents misleading interpretations of slopes.  
C) Cropping the y-axis is acceptable in all cases to focus on data variation.  
D) Axes should always be labeled unless the chart is a small multiple sharing labels.  



<br>

## Answers

#### 1. Which of the following statements correctly describe the role of keys in tabular data visualizations?  
A) ✗ Keys are independent, not dependent attributes.  
B) ✓ Simple tables have one key; multidimensional tables have multiple keys.  
C) ✓ Keys serve as unique indices to look up items.  
D) ✗ Keys can be categorical or quantitative, not always quantitative.

**Correct:** B, C


#### 2. In a scatterplot, which visual channels are primarily used to encode data?  
A) ✓ Color can be used to encode additional variables or categories.  
B) ✓ Size of points can encode a third quantitative variable, scaled by square root.
C) ✗ Length of bars is not used in scatterplots.  
D) ✓ Horizontal and vertical position encode the two quantitative variables.  

**Correct:** A, B, D


#### 3. What are the main advantages of connected scatterplots compared to standard scatterplots?  
A) ✓ They show temporal order via connecting lines.  
B) ✓ They can serve as an alternative to dual-axis charts.  
C) ✗ Point marks are still present; lines add to them, not remove.
D) ✗ Correlation clarity can be reduced, not improved.  

**Correct:** A, B


#### 4. When is it appropriate to use a line chart instead of a bar chart?  
A) ✓ Line charts are suitable for ordered keys like time.  
B) ✗ Line charts imply order, so not for nominal keys.
C) ✗ Part-to-whole relationships are better shown with bar charts.  
D) ✗ Line charts are not appropriate for unordered categorical keys.  

**Correct:** A


#### 5. Which of the following are limitations of stacked bar charts?  
A) ✓ They effectively show part-to-whole relationships.  
B) ✗ Ordering segments can be confusing and not always intuitive.
C) ✗ They display two categorical keys, not just one.  
D) ✓ Scalability is limited by the number of segments per stack.  

**Correct:** A, D


#### 6. Why should the radius of points in a scatterplot be scaled by the square root of the quantitative attribute rather than the raw value?  
A) ✓ Area grows quadratically with radius, so square root scaling corrects this.  
B) ✓ To ensure area grows linearly with value, avoiding misperception.  
C) ✓ Avoids misleading viewers about magnitude.
D) ✗ Making points larger is not the main reason.  

**Correct:** A, B, C


#### 7. Which tasks are best supported by heatmaps?  
A) ✓ Heatmaps excel at finding clusters and outliers in categorical data.  
B) ✗ Temporal trends are better shown with line or streamgraphs.  
C) ✗ Exact value comparison is difficult due to color perception limits.  
D) ✗ Part-to-whole is not the primary task for heatmaps.

**Correct:** A


#### 8. What are the main challenges when using parallel coordinates for multivariate data visualization?  
A) ✓ Axis ordering greatly affects pattern detection.  
B) ✗ Parallel coordinates can show many attributes, not just two.  
C) ✓ Reordering axes requires interaction or algorithms.  
D) ✗ They are not intuitive and require training.

**Correct:** A, C


#### 9. Which of the following are true about pie charts?  
A) ✗ They are poor for many categories due to accuracy issues.  
B) ✓ Accuracy decreases as category count increases.  
C) ✗ Bar charts are generally more accurate for value comparison.
D) ✓ Pie charts encode data using angles representing 2D area.  

**Correct:** B, D


#### 10. What is a key difference between a slopegraph and a standard line chart?  
A) ✗ Slopegraphs do not connect multiple points over time continuously.  
B) ✓ Slopegraphs emphasize changes between two points, not continuous trends.  
C) ✗ They are not designed for many time points.  
D) ✓ Line width and color can encode change magnitude or direction.

**Correct:** B, D


#### 11. Which of the following statements about scatterplot matrices (SPLOM) are correct?  
A) ✓ They scale to dozens of variables and hundreds of items.  
B) ✓ SPLOMs show all pairwise relationships between quantitative variables.  
C) ✗ They show multiple pairs simultaneously, not just two variables.
D) ✗ They use rectilinear, not radial, axes.  

**Correct:** A, B


#### 12. Why is it generally advised to avoid using line charts for categorical key attributes?  
A) ✓ Line charts imply continuity and trends that may not exist.  
B) ✗ Visual appeal is not the main reason.  
C) ✓ Using line charts for categorical keys violates expressiveness principles.
D) ✗ Line charts can encode quantitative values.  

**Correct:** A, C


#### 13. What are the main visual channels used in a Gantt chart?  
A) ✗ Color hue is optional but not a main channel.  
B) ✗ Vertical position encodes categorical keys, not quantitative values.
C) ✓ Horizontal position encodes start time.  
D) ✓ Length encodes duration.  

**Correct:** C, D


#### 14. Which of the following are true about radial visualizations like radar plots and radial bar charts?  
A) ✗ Sector widths vary with radial distance, not uniform.
B) ✗ They are less accurately perceived than rectilinear charts.  
C) ✓ Useful when data is cyclic or attributes have unequal importance.  
D) ✓ Length encoding is less precise due to angle perception issues.  

**Correct:** C, D


#### 15. What is a major limitation of using truncated y-axes in charts?  
A) ✗ It does not always improve clarity; often misleading.  
B) ✓ Acceptable only in specific cases like arbitrary zero or small changes.  
C) ✗ Not recommended for all bar charts.
D) ✓ It can mislead viewers by exaggerating slopes or changes.  

**Correct:** B, D


#### 16. Which of the following best describe the scalability of scatterplots?  
A) ✓ Can effectively display hundreds of points.  
B) ✗ Not limited to fewer than 50 points.  
C) ✓ Adding color and size channels increases information density without losing clarity.  
D) ✗ Can encode more than two quantitative variables via additional channels.

**Correct:** A, C, D


#### 17. In a normalized stacked bar chart, what is the main purpose of normalization?  
A) ✓ Enables part-to-whole comparisons by scaling bars to the same height.  
B) ✗ Does not reduce the number of categories.  
C) ✗ It does not show absolute values.  
D) ✓ Makes the chart equivalent to a pie chart in information density.

**Correct:** A, D


#### 18. Which of the following are true about cluster heatmaps?  
A) ✗ More effective than standard heatmaps for finding clusters.  
B) ✓ They reorder rows and columns based on hierarchical clustering.  
C) ✓ Use dendrograms to show parent-child relationships.  
D) ✓ Help assess cluster quality from automatic methods.

**Correct:** B, C, D


#### 19. What are the main tasks supported by scatterplots?  
A) ✓ Identifying clusters or groups.  
B) ✓ Detecting outliers and distribution patterns.
C) ✓ Finding correlations between two quantitative variables.  
D) ✗ Not designed for part-to-whole relationships.  

**Correct:** A, B, C


#### 20. Which of the following statements about axis labeling and chart best practices are correct?  
A) ✗ Dual-axis charts are controversial but not always misleading.
B) ✓ Including zero on y-axis prevents misleading slope interpretations.  
C) ✗ Cropping y-axis is not acceptable in all cases.  
D) ✓ Axes should always be labeled unless small multiples share labels.  

**Correct:** B, D