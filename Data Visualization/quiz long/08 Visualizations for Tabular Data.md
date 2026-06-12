## 9. Visualizations for Tabular Data

## Questions

#### 1. Which of the following statements correctly describe the role of keys in tabular data visualizations?  
A) Keys serve as unique indices to look up items in the table.  
B) Keys are always quantitative attributes.  
C) Keys are dependent attributes representing the values in cells.  
D) Simple tables typically have one key, while multidimensional tables have multiple keys.  

#### 2. In a scatterplot, which visual channels are primarily used to encode data?  
A) Length of bars  
B) Size of points (with area proportional to the square root of the value)  
C) Color hue and saturation  
D) Horizontal and vertical position  

#### 3. What are the main advantages of connected scatterplots compared to standard scatterplots?  
A) They reduce visual clutter by removing point marks.  
B) They improve clarity of correlation between variables.  
C) They explicitly show temporal order through line connections.  
D) They serve as an alternative to dual-axis charts.  

#### 4. When is it appropriate to use a line chart instead of a bar chart?  
A) When the key attribute is categorical and unordered.  
B) When the key attribute is ordered, such as time.  
C) When the data represents part-to-whole relationships.  
D) When the key attribute is nominal with no inherent order.  

#### 5. Which of the following are limitations of stacked bar charts?  
A) They are effective for showing part-to-whole relationships.  
B) Ordering of segments within stacks is always clear and intuitive.  
C) Scalability is limited by the number of segments per stack.  
D) They can only display one categorical key attribute.  

#### 6. Why should the radius of points in a scatterplot be scaled by the square root of the quantitative attribute rather than the raw value?  
A) To make the points visually larger and easier to see.  
B) To ensure the area of the point grows linearly with the value.  
C) To avoid misleading viewers about the magnitude of the data.  
D) Because area perception grows quadratically with radius.  

#### 7. Which tasks are best supported by heatmaps?  
A) Showing temporal trends over ordered keys.  
B) Comparing exact quantitative values between two categories.  
C) Finding clusters and outliers in large categorical datasets.  
D) Visualizing part-to-whole relationships.  

#### 8. What are the main challenges when using parallel coordinates for multivariate data visualization?  
A) They can only show two attributes at a time.  
B) They require user interaction or algorithms to reorder axes effectively.  
C) They are intuitive and require no training to interpret.  
D) Axis ordering significantly affects pattern detection.  

#### 9. Which of the following are true about pie charts?  
A) They are generally more accurate than bar charts for comparing values.  
B) They become less accurate as the number of categories increases.  
C) They are effective for part-to-whole judgments with many categories.  
D) They encode data using angle channels representing 2D area.  

#### 10. What is a key difference between a slopegraph and a standard line chart?  
A) Slopegraphs emphasize changes in rank or value between two points.  
B) Slopegraphs connect multiple points over time with continuous lines.  
C) Slopegraphs use line width and color to encode additional variables.  
D) Slopegraphs are best for showing trends across many time points.  

#### 11. Which of the following statements about scatterplot matrices (SPLOM) are correct?  
A) They use radial axes to represent variables.  
B) They are scalable to dozens of variables and hundreds of items.  
C) They show all pairwise relationships between multiple quantitative variables.  
D) They are limited to showing only two variables at a time.  

#### 12. Why is it generally advised to avoid using line charts for categorical key attributes?  
A) Because line charts imply continuity and trends that may not exist.  
B) Because it violates the expressiveness principle of visualization.  
C) Because line charts cannot encode quantitative values.  
D) Because bar charts are always more visually appealing.  

#### 13. What are the main visual channels used in a Gantt chart?  
A) Horizontal position for start time.  
B) Vertical position for quantitative values.  
C) Length of bars for duration.  
D) Color hue for categorical keys.  

#### 14. Which of the following are true about radial visualizations like radar plots and radial bar charts?  
A) They can be useful when data is cyclic or attributes have unequal importance.  
B) Length encoding in radial layouts is less precise due to angle perception issues.  
C) They are more accurately perceived than rectilinear bar charts.  
D) They use uniform sector widths regardless of radial distance.  

#### 15. What is a major limitation of using truncated y-axes in charts?  
A) It can mislead viewers by exaggerating slopes or changes.  
B) It is recommended for all bar charts to save space.  
C) It always improves clarity by focusing on relevant data ranges.  
D) It is acceptable when zero is arbitrary or small changes matter.  

#### 16. Which of the following best describe the scalability of scatterplots?  
A) They cannot encode more than two quantitative variables.  
B) Adding color and size channels can increase information density without losing clarity.  
C) They are limited to fewer than 50 points due to clutter.  
D) They can effectively display hundreds of data points.  

#### 17. In a normalized stacked bar chart, what is the main purpose of normalization?  
A) To enable part-to-whole comparisons by scaling bars to the same height.  
B) To show absolute values of each segment.  
C) To reduce the number of categories displayed.  
D) To make the chart equivalent to a pie chart in terms of information density.  

#### 18. Which of the following are true about cluster heatmaps?  
A) They use dendrograms to show parent-child relationships.  
B) They help assess the quality of clusters found by automatic methods.  
C) They reorder rows and columns based on hierarchical clustering.  
D) They are less effective than standard heatmaps for finding clusters.  

#### 19. What are the main tasks supported by scatterplots?  
A) Identifying clusters or groups within data.  
B) Finding correlations between two quantitative variables.  
C) Showing part-to-whole relationships.  
D) Detecting outliers and distribution patterns.  

#### 20. Which of the following statements about axis labeling and chart best practices are correct?  
A) Dual-axis charts are always misleading and should be avoided.  
B) Including zero on the y-axis prevents misleading interpretations of slopes.  
C) Cropping the y-axis is acceptable in all cases to focus on data variation.  
D) Axes should always be labeled unless the chart is a small multiple sharing labels.  



<br>

## Answers

#### 1. Which of the following statements correctly describe the role of keys in tabular data visualizations?  
A) ✓ Keys serve as unique indices to look up items.  
B) ✗ Keys can be categorical or quantitative, not always quantitative.  
C) ✗ Keys are independent, not dependent attributes.  
D) ✓ Simple tables have one key; multidimensional tables have multiple keys.  

**Correct:** A, D


#### 2. In a scatterplot, which visual channels are primarily used to encode data?  
A) ✗ Length of bars is not used in scatterplots.  
B) ✓ Size of points can encode a third quantitative variable, scaled by square root.  
C) ✓ Color can be used to encode additional variables or categories.  
D) ✓ Horizontal and vertical position encode the two quantitative variables.  

**Correct:** B, C, D


#### 3. What are the main advantages of connected scatterplots compared to standard scatterplots?  
A) ✗ Point marks are still present; lines add to them, not remove.  
B) ✗ Correlation clarity can be reduced, not improved.  
C) ✓ They show temporal order via connecting lines.  
D) ✓ They can serve as an alternative to dual-axis charts.  

**Correct:** C, D


#### 4. When is it appropriate to use a line chart instead of a bar chart?  
A) ✗ Line charts are not appropriate for unordered categorical keys.  
B) ✓ Line charts are suitable for ordered keys like time.  
C) ✗ Part-to-whole relationships are better shown with bar charts.  
D) ✗ Line charts imply order, so not for nominal keys.  

**Correct:** B


#### 5. Which of the following are limitations of stacked bar charts?  
A) ✓ They effectively show part-to-whole relationships.  
B) ✗ Ordering segments can be confusing and not always intuitive.  
C) ✓ Scalability is limited by the number of segments per stack.  
D) ✗ They display two categorical keys, not just one.  

**Correct:** A, C


#### 6. Why should the radius of points in a scatterplot be scaled by the square root of the quantitative attribute rather than the raw value?  
A) ✗ Making points larger is not the main reason.  
B) ✓ To ensure area grows linearly with value, avoiding misperception.  
C) ✓ Avoids misleading viewers about magnitude.  
D) ✓ Area grows quadratically with radius, so square root scaling corrects this.  

**Correct:** B, C, D


#### 7. Which tasks are best supported by heatmaps?  
A) ✗ Temporal trends are better shown with line or streamgraphs.  
B) ✗ Exact value comparison is difficult due to color perception limits.  
C) ✓ Heatmaps excel at finding clusters and outliers in categorical data.  
D) ✗ Part-to-whole is not the primary task for heatmaps.  

**Correct:** C


#### 8. What are the main challenges when using parallel coordinates for multivariate data visualization?  
A) ✗ Parallel coordinates can show many attributes, not just two.  
B) ✓ Reordering axes requires interaction or algorithms.  
C) ✗ They are not intuitive and require training.  
D) ✓ Axis ordering greatly affects pattern detection.  

**Correct:** B, D


#### 9. Which of the following are true about pie charts?  
A) ✗ Bar charts are generally more accurate for value comparison.  
B) ✓ Accuracy decreases as category count increases.  
C) ✗ They are poor for many categories due to accuracy issues.  
D) ✓ Pie charts encode data using angles representing 2D area.  

**Correct:** B, D


#### 10. What is a key difference between a slopegraph and a standard line chart?  
A) ✓ Slopegraphs emphasize changes between two points, not continuous trends.  
B) ✗ Slopegraphs do not connect multiple points over time continuously.  
C) ✓ Line width and color can encode change magnitude or direction.  
D) ✗ They are not designed for many time points.  

**Correct:** A, C


#### 11. Which of the following statements about scatterplot matrices (SPLOM) are correct?  
A) ✗ They use rectilinear, not radial, axes.  
B) ✓ They scale to dozens of variables and hundreds of items.  
C) ✓ SPLOMs show all pairwise relationships between quantitative variables.  
D) ✗ They show multiple pairs simultaneously, not just two variables.  

**Correct:** B, C


#### 12. Why is it generally advised to avoid using line charts for categorical key attributes?  
A) ✓ Line charts imply continuity and trends that may not exist.  
B) ✓ Using line charts for categorical keys violates expressiveness principles.  
C) ✗ Line charts can encode quantitative values.  
D) ✗ Visual appeal is not the main reason.  

**Correct:** A, B


#### 13. What are the main visual channels used in a Gantt chart?  
A) ✓ Horizontal position encodes start time.  
B) ✗ Vertical position encodes categorical keys, not quantitative values.  
C) ✓ Length encodes duration.  
D) ✗ Color hue is optional but not a main channel.  

**Correct:** A, C


#### 14. Which of the following are true about radial visualizations like radar plots and radial bar charts?  
A) ✓ Useful when data is cyclic or attributes have unequal importance.  
B) ✓ Length encoding is less precise due to angle perception issues.  
C) ✗ They are less accurately perceived than rectilinear charts.  
D) ✗ Sector widths vary with radial distance, not uniform.  

**Correct:** A, B


#### 15. What is a major limitation of using truncated y-axes in charts?  
A) ✓ It can mislead viewers by exaggerating slopes or changes.  
B) ✗ Not recommended for all bar charts.  
C) ✗ It does not always improve clarity; often misleading.  
D) ✓ Acceptable only in specific cases like arbitrary zero or small changes.  

**Correct:** A, D


#### 16. Which of the following best describe the scalability of scatterplots?  
A) ✗ Can encode more than two quantitative variables via additional channels.  
B) ✓ Adding color and size channels increases information density without losing clarity.  
C) ✗ Not limited to fewer than 50 points.  
D) ✓ Can effectively display hundreds of points.  

**Correct:** A, B, D


#### 17. In a normalized stacked bar chart, what is the main purpose of normalization?  
A) ✓ Enables part-to-whole comparisons by scaling bars to the same height.  
B) ✗ It does not show absolute values.  
C) ✗ Does not reduce the number of categories.  
D) ✓ Makes the chart equivalent to a pie chart in information density.  

**Correct:** A, D


#### 18. Which of the following are true about cluster heatmaps?  
A) ✓ Use dendrograms to show parent-child relationships.  
B) ✓ Help assess cluster quality from automatic methods.  
C) ✓ They reorder rows and columns based on hierarchical clustering.  
D) ✗ More effective than standard heatmaps for finding clusters.  

**Correct:** A, B, C


#### 19. What are the main tasks supported by scatterplots?  
A) ✓ Identifying clusters or groups.  
B) ✓ Finding correlations between two quantitative variables.  
C) ✗ Not designed for part-to-whole relationships.  
D) ✓ Detecting outliers and distribution patterns.  

**Correct:** A, B, D


#### 20. Which of the following statements about axis labeling and chart best practices are correct?  
A) ✗ Dual-axis charts are controversial but not always misleading.  
B) ✓ Including zero on y-axis prevents misleading slope interpretations.  
C) ✗ Cropping y-axis is not acceptable in all cases.  
D) ✓ Axes should always be labeled unless small multiples share labels.  

**Correct:** B, D