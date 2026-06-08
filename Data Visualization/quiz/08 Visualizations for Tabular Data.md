## 9. Visualizations for Tabular Data

## Questions

#### 1. Which of the following statements correctly describe the role of keys in tabular data visualizations?  
A) Keys are dependent attributes representing the values in cells.  
B) Keys serve as unique indices to look up items in the table.  
C) Simple tables typically have one key, while multidimensional tables have multiple keys.  
D) Keys are always quantitative attributes.

#### 2. In a scatterplot, which visual channels are primarily used to encode data?  
A) Horizontal and vertical position  
B) Color hue and saturation  
C) Length of bars  
D) Size of points (with area proportional to the square root of the value)

#### 3. What are the main advantages of connected scatterplots compared to standard scatterplots?  
A) They explicitly show temporal order through line connections.  
B) They improve clarity of correlation between variables.  
C) They serve as an alternative to dual-axis charts.  
D) They reduce visual clutter by removing point marks.

#### 4. When is it appropriate to use a line chart instead of a bar chart?  
A) When the key attribute is categorical and unordered.  
B) When the key attribute is ordered, such as time.  
C) When the data represents part-to-whole relationships.  
D) When the key attribute is nominal with no inherent order.

#### 5. Which of the following are limitations of stacked bar charts?  
A) They can only display one categorical key attribute.  
B) Scalability is limited by the number of segments per stack.  
C) They are effective for showing part-to-whole relationships.  
D) Ordering of segments within stacks is always clear and intuitive.

#### 6. Why should the radius of points in a scatterplot be scaled by the square root of the quantitative attribute rather than the raw value?  
A) To ensure the area of the point grows linearly with the value.  
B) To make the points visually larger and easier to see.  
C) Because area perception grows quadratically with radius.  
D) To avoid misleading viewers about the magnitude of the data.

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
A) They encode data using angle channels representing 2D area.  
B) They are effective for part-to-whole judgments with many categories.  
C) They become less accurate as the number of categories increases.  
D) They are generally more accurate than bar charts for comparing values.

#### 10. What is a key difference between a slopegraph and a standard line chart?  
A) Slopegraphs emphasize changes in rank or value between two points.  
B) Slopegraphs connect multiple points over time with continuous lines.  
C) Slopegraphs are best for showing trends across many time points.  
D) Slopegraphs use line width and color to encode additional variables.

#### 11. Which of the following statements about scatterplot matrices (SPLOM) are correct?  
A) They show all pairwise relationships between multiple quantitative variables.  
B) They use radial axes to represent variables.  
C) They are scalable to dozens of variables and hundreds of items.  
D) They are limited to showing only two variables at a time.

#### 12. Why is it generally advised to avoid using line charts for categorical key attributes?  
A) Because line charts imply continuity and trends that may not exist.  
B) Because line charts cannot encode quantitative values.  
C) Because bar charts are always more visually appealing.  
D) Because it violates the expressiveness principle of visualization.

#### 13. What are the main visual channels used in a Gantt chart?  
A) Horizontal position for start time.  
B) Length of bars for duration.  
C) Color hue for categorical keys.  
D) Vertical position for quantitative values.

#### 14. Which of the following are true about radial visualizations like radar plots and radial bar charts?  
A) They are more accurately perceived than rectilinear bar charts.  
B) Length encoding in radial layouts is less precise due to angle perception issues.  
C) They can be useful when data is cyclic or attributes have unequal importance.  
D) They use uniform sector widths regardless of radial distance.

#### 15. What is a major limitation of using truncated y-axes in charts?  
A) It can mislead viewers by exaggerating slopes or changes.  
B) It always improves clarity by focusing on relevant data ranges.  
C) It is acceptable when zero is arbitrary or small changes matter.  
D) It is recommended for all bar charts to save space.

#### 16. Which of the following best describe the scalability of scatterplots?  
A) They can effectively display hundreds of data points.  
B) They are limited to fewer than 50 points due to clutter.  
C) Adding color and size channels can increase information density without losing clarity.  
D) They cannot encode more than two quantitative variables.

#### 17. In a normalized stacked bar chart, what is the main purpose of normalization?  
A) To show absolute values of each segment.  
B) To enable part-to-whole comparisons by scaling bars to the same height.  
C) To reduce the number of categories displayed.  
D) To make the chart equivalent to a pie chart in terms of information density.

#### 18. Which of the following are true about cluster heatmaps?  
A) They reorder rows and columns based on hierarchical clustering.  
B) They use dendrograms to show parent-child relationships.  
C) They are less effective than standard heatmaps for finding clusters.  
D) They help assess the quality of clusters found by automatic methods.

#### 19. What are the main tasks supported by scatterplots?  
A) Finding correlations between two quantitative variables.  
B) Identifying clusters or groups within data.  
C) Showing part-to-whole relationships.  
D) Detecting outliers and distribution patterns.

#### 20. Which of the following statements about axis labeling and chart best practices are correct?  
A) Axes should always be labeled unless the chart is a small multiple sharing labels.  
B) Cropping the y-axis is acceptable in all cases to focus on data variation.  
C) Including zero on the y-axis prevents misleading interpretations of slopes.  
D) Dual-axis charts are always misleading and should be avoided.



<br>

## Answers

#### 1. Which of the following statements correctly describe the role of keys in tabular data visualizations?  
A) ✗ Keys are independent, not dependent attributes.  
B) ✓ Keys serve as unique indices to look up items.  
C) ✓ Simple tables have one key; multidimensional tables have multiple keys.  
D) ✗ Keys can be categorical or quantitative, not always quantitative.

**Correct:** B, C


#### 2. In a scatterplot, which visual channels are primarily used to encode data?  
A) ✓ Horizontal and vertical position encode the two quantitative variables.  
B) ✓ Color can be used to encode additional variables or categories.  
C) ✗ Length of bars is not used in scatterplots.  
D) ✓ Size of points can encode a third quantitative variable, scaled by square root.

**Correct:** A, B, D


#### 3. What are the main advantages of connected scatterplots compared to standard scatterplots?  
A) ✓ They show temporal order via connecting lines.  
B) ✗ Correlation clarity can be reduced, not improved.  
C) ✓ They can serve as an alternative to dual-axis charts.  
D) ✗ Point marks are still present; lines add to them, not remove.

**Correct:** A, C


#### 4. When is it appropriate to use a line chart instead of a bar chart?  
A) ✗ Line charts are not appropriate for unordered categorical keys.  
B) ✓ Line charts are suitable for ordered keys like time.  
C) ✗ Part-to-whole relationships are better shown with bar charts.  
D) ✗ Line charts imply order, so not for nominal keys.

**Correct:** B


#### 5. Which of the following are limitations of stacked bar charts?  
A) ✗ They display two categorical keys, not just one.  
B) ✓ Scalability is limited by the number of segments per stack.  
C) ✓ They effectively show part-to-whole relationships.  
D) ✗ Ordering segments can be confusing and not always intuitive.

**Correct:** B, C


#### 6. Why should the radius of points in a scatterplot be scaled by the square root of the quantitative attribute rather than the raw value?  
A) ✓ To ensure area grows linearly with value, avoiding misperception.  
B) ✗ Making points larger is not the main reason.  
C) ✓ Area grows quadratically with radius, so square root scaling corrects this.  
D) ✓ Avoids misleading viewers about magnitude.

**Correct:** A, C, D


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
A) ✓ Pie charts encode data using angles representing 2D area.  
B) ✗ They are poor for many categories due to accuracy issues.  
C) ✓ Accuracy decreases as category count increases.  
D) ✗ Bar charts are generally more accurate for value comparison.

**Correct:** A, C


#### 10. What is a key difference between a slopegraph and a standard line chart?  
A) ✓ Slopegraphs emphasize changes between two points, not continuous trends.  
B) ✗ Slopegraphs do not connect multiple points over time continuously.  
C) ✗ They are not designed for many time points.  
D) ✓ Line width and color can encode change magnitude or direction.

**Correct:** A, D


#### 11. Which of the following statements about scatterplot matrices (SPLOM) are correct?  
A) ✓ SPLOMs show all pairwise relationships between quantitative variables.  
B) ✗ They use rectilinear, not radial, axes.  
C) ✓ They scale to dozens of variables and hundreds of items.  
D) ✗ They show multiple pairs simultaneously, not just two variables.

**Correct:** A, C


#### 12. Why is it generally advised to avoid using line charts for categorical key attributes?  
A) ✓ Line charts imply continuity and trends that may not exist.  
B) ✗ Line charts can encode quantitative values.  
C) ✗ Visual appeal is not the main reason.  
D) ✓ Using line charts for categorical keys violates expressiveness principles.

**Correct:** A, D


#### 13. What are the main visual channels used in a Gantt chart?  
A) ✓ Horizontal position encodes start time.  
B) ✓ Length encodes duration.  
C) ✗ Color hue is optional but not a main channel.  
D) ✗ Vertical position encodes categorical keys, not quantitative values.

**Correct:** A, B


#### 14. Which of the following are true about radial visualizations like radar plots and radial bar charts?  
A) ✗ They are less accurately perceived than rectilinear charts.  
B) ✓ Length encoding is less precise due to angle perception issues.  
C) ✓ Useful when data is cyclic or attributes have unequal importance.  
D) ✗ Sector widths vary with radial distance, not uniform.

**Correct:** B, C


#### 15. What is a major limitation of using truncated y-axes in charts?  
A) ✓ It can mislead viewers by exaggerating slopes or changes.  
B) ✗ It does not always improve clarity; often misleading.  
C) ✓ Acceptable only in specific cases like arbitrary zero or small changes.  
D) ✗ Not recommended for all bar charts.

**Correct:** A, C


#### 16. Which of the following best describe the scalability of scatterplots?  
A) ✓ Can effectively display hundreds of points.  
B) ✗ Not limited to fewer than 50 points.  
C) ✓ Adding color and size channels increases information density without losing clarity.  
D) ✗ Can encode more than two quantitative variables via additional channels.

**Correct:** A, C, D


#### 17. In a normalized stacked bar chart, what is the main purpose of normalization?  
A) ✗ It does not show absolute values.  
B) ✓ Enables part-to-whole comparisons by scaling bars to the same height.  
C) ✗ Does not reduce the number of categories.  
D) ✓ Makes the chart equivalent to a pie chart in information density.

**Correct:** B, D


#### 18. Which of the following are true about cluster heatmaps?  
A) ✓ They reorder rows and columns based on hierarchical clustering.  
B) ✓ Use dendrograms to show parent-child relationships.  
C) ✗ More effective than standard heatmaps for finding clusters.  
D) ✓ Help assess cluster quality from automatic methods.

**Correct:** A, B, D


#### 19. What are the main tasks supported by scatterplots?  
A) ✓ Finding correlations between two quantitative variables.  
B) ✓ Identifying clusters or groups.  
C) ✗ Not designed for part-to-whole relationships.  
D) ✓ Detecting outliers and distribution patterns.

**Correct:** A, B, D


#### 20. Which of the following statements about axis labeling and chart best practices are correct?  
A) ✓ Axes should always be labeled unless small multiples share labels.  
B) ✗ Cropping y-axis is not acceptable in all cases.  
C) ✓ Including zero on y-axis prevents misleading slope interpretations.  
D) ✗ Dual-axis charts are controversial but not always misleading.

**Correct:** A, C