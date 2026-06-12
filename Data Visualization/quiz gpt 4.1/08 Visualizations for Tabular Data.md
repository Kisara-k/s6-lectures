## 9. Visualizations for Tabular Data

## Questions

#### 1. Which of the following statements about keys and values in tabular data visualizations are TRUE?
A) Keys are always categorical attributes.  
B) Multidimensional tables can have multiple keys.  
C) Values are dependent attributes represented in the cells of the table.  
D) Keys are used as unique indices to look up items.  


#### 2. In a scatterplot, which of the following can be used to encode additional data attributes beyond the two main quantitative variables?
A) Size (area) of the points  
B) Color of the points  
C) Length of the axes  
D) Shape of the points  


#### 3. Which limitations are associated with using line charts for categorical key attributes?
A) They can mislead viewers about the nature of the data.  
B) They violate the expressiveness principle.  
C) They may imply trends that do not exist.  
D) They are more accurate than bar charts for categorical data.  


#### 4. Which of the following visualizations are best suited for showing part-to-whole relationships?
A) Pie chart  
B) Stacked bar chart  
C) Normalized stacked bar chart  
D) Scatterplot  


#### 5. When comparing rectilinear bar charts and radial bar charts, which statements are correct?
A) Radial bar charts encode length along a curved axis, which can reduce accuracy.  
B) Both chart types are equally effective for all audiences.  
C) Rectilinear bar charts are generally more accurately perceived than radial bar charts.  
D) Radial bar charts can be useful for cyclic data but are less common.  


#### 6. Which of the following are TRUE about heatmaps and cluster heatmaps?
A) Cluster heatmaps use dendrograms to show hierarchical clustering.  
B) Heatmaps are limited to only two quantitative attributes.  
C) Cluster heatmaps reorder rows and columns based on cluster hierarchy.  
D) Heatmaps can display millions of items if the number of categorical levels is high.  


#### 7. Which statements about parallel coordinates are correct?
A) Each data item is represented as a jagged line crossing multiple parallel axes.  
B) They are more familiar and easier to interpret than scatterplots for most users.  
C) Parallel coordinates can effectively show correlations between many attributes.  
D) Axis ordering has little effect on the patterns visible in parallel coordinates.  


#### 8. Which of the following are best practices for chart axes in tabular data visualizations?
A) Including zero on the y-axis helps prevent misleading impressions of slope or change.  
B) Always label axes unless the context is extremely clear (e.g., small multiples).  
C) Omitting axis labels can be justified if the chart is self-explanatory.  
D) Cropping the y-axis is always acceptable if it makes the chart look cleaner.  


#### 9. Which visualizations are most appropriate for exploring correlations between multiple quantitative variables?
A) Parallel coordinates  
B) Pie chart  
C) Bar chart  
D) Scatterplot matrix (SPLOM)  


#### 10. Which of the following statements about the scalability of different tabular data visualizations are TRUE?
A) Scatterplots can handle hundreds of items effectively.  
B) Pie charts are ideal for datasets with dozens of categories.  
C) Stacked bar charts are limited by the number of segments in each stack.  
D) Heatmaps can scale to millions of items if the matrix is not too sparse.  



<br>

## Answers

#### 1. Which of the following statements about keys and values in tabular data visualizations are TRUE?
A) ✗ Keys can be categorical or ordered, not always categorical.  
B) ✓ Multidimensional tables can have multiple keys (e.g., row and column keys).  
C) ✓ Values are dependent attributes, representing the data in table cells.  
D) ✓ Keys are used as unique indices to look up items in the table.  

**Correct:** B, C, D


#### 2. In a scatterplot, which of the following can be used to encode additional data attributes beyond the two main quantitative variables?
A) ✓ Size (area) of points can encode a third quantitative attribute.  
B) ✓ Color can encode a categorical or quantitative attribute.  
C) ✗ Length of axes is not used to encode additional data attributes; it defines the scale.  
D) ✓ Shape can encode a categorical attribute.  

**Correct:** A, B, D


#### 3. Which limitations are associated with using line charts for categorical key attributes?
A) ✓ Line charts can mislead viewers by suggesting continuity or order where there is none.  
B) ✓ Using line charts for categorical keys violates the expressiveness principle.  
C) ✓ Line charts can imply trends that do not exist in categorical data.  
D) ✗ Bar charts are more accurate for categorical data; line charts are not.  

**Correct:** A, B, C


#### 4. Which of the following visualizations are best suited for showing part-to-whole relationships?
A) ✓ Pie charts are designed for part-to-whole comparisons.  
B) ✓ Stacked bar charts show how parts contribute to a whole.  
C) ✓ Normalized stacked bar charts explicitly show part-to-whole by normalizing to 100%.  
D) ✗ Scatterplots are not used for part-to-whole relationships.  

**Correct:** A, B, C


#### 5. When comparing rectilinear bar charts and radial bar charts, which statements are correct?
A) ✓ Radial bar charts encode length along a curve, reducing perceptual accuracy.  
B) ✗ Rectilinear bar charts are generally more effective; radial charts are not equally effective for all.  
C) ✓ Rectilinear bar charts are more accurately perceived due to aligned lengths.  
D) ✓ Radial bar charts can be useful for cyclic data but are less common in practice.  

**Correct:** A, C, D


#### 6. Which of the following are TRUE about heatmaps and cluster heatmaps?
A) ✓ Cluster heatmaps use dendrograms to show hierarchical clustering.  
B) ✗ Heatmaps typically show one quantitative attribute, not two.  
C) ✓ Cluster heatmaps reorder rows and columns based on cluster hierarchy.  
D) ✓ Heatmaps can display very large datasets, including millions of items, if the matrix is not too sparse.  

**Correct:** A, C, D


#### 7. Which statements about parallel coordinates are correct?
A) ✓ Each data item is represented as a jagged line crossing parallel axes.  
B) ✗ Parallel coordinates are less familiar and require more training than scatterplots.  
C) ✓ Parallel coordinates can show correlations between many attributes.  
D) ✗ Axis ordering greatly affects visible patterns; it is not negligible.  

**Correct:** A, C


#### 8. Which of the following are best practices for chart axes in tabular data visualizations?
A) ✓ Including zero on the y-axis helps prevent misleading impressions of change.  
B) ✓ Axes should be labeled unless context is extremely clear.  
C) ✗ Omitting axis labels is rarely justified; clarity is preferred.  
D) ✗ Cropping the y-axis can mislead and is not always acceptable.  

**Correct:** A, B


#### 9. Which visualizations are most appropriate for exploring correlations between multiple quantitative variables?
A) ✓ Parallel coordinates are effective for exploring multivariate correlations.  
B) ✗ Pie charts are not suitable for correlation analysis.  
C) ✗ Bar charts are not designed for exploring correlations between quantitative variables.  
D) ✓ Scatterplot matrix (SPLOM) is designed for this purpose.  

**Correct:** A, D


#### 10. Which of the following statements about the scalability of different tabular data visualizations are TRUE?
A) ✓ Scatterplots can handle hundreds of items effectively.  
B) ✗ Pie charts are not ideal for datasets with many categories; they become hard to interpret.  
C) ✓ Stacked bar charts are limited by the number of segments in each stack.  
D) ✓ Heatmaps can scale to millions of items if the matrix is not too sparse.  

**Correct:** A, C, D