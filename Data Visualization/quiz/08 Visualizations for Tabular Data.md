## 9. Visualizations for Tabular Data

## Questions

#### 1. Which of the following statements correctly describe the role of keys and values in tabular data visualizations?  
A) Keys are dependent attributes used to represent the values in cells.  
B) Multidimensional tables can have multiple keys indexing the data.  
C) Values are independent attributes that uniquely identify rows.  
D) Keys serve as unique indices to look up items in the table.  

#### 2. When encoding a third quantitative variable in a scatterplot using point size, which of the following is true?  
A) Using radius directly can mislead viewers because perceived size changes nonlinearly.  
B) Shape is a better channel than size for encoding quantitative variables.  
C) The radius of the point should be proportional to the value to avoid distortion.  
D) The area of the point grows quadratically with radius, so size encoding should use the square root of the value.  

#### 3. What are the main limitations of separated but not aligned spatial regions in categorical data visualizations?  
A) Alignment is unnecessary if regions are ordered alphabetically.  
B) It becomes impossible to order the regions meaningfully.  
C) It is difficult to compare sizes across regions.  
D) Lack of alignment reduces expressiveness for quantitative comparisons.  

#### 4. Which of the following are true about stacked bar charts?  
A) Color hue is not a useful channel for distinguishing stack components.  
B) Scalability is limited by the number of segments per stack and the number of bars.  
C) They can effectively show part-to-whole relationships with two categorical keys.  
D) They are best used when the main key attribute has only a few levels.  

#### 5. Regarding line charts and bar charts, which statements are correct?  
A) Line charts are appropriate for ordered key attributes like time.  
B) Using line charts for categorical keys is acceptable if the categories are alphabetically ordered.  
C) Bar charts should be used for categorical key attributes to avoid implying trends.  
D) Line charts imply continuity and trends, which can mislead if the key is categorical.  

#### 6. What are the key challenges and limitations of parallel coordinates plots?  
A) They are intuitive and require no training for interpretation.  
B) Axis ordering is critical and often requires interactive reordering.  
C) They can only show correlations between neighboring axes effectively.  
D) They scale well visually for more than 10 axes without confusion.  

#### 7. Which of the following statements about radial visualizations like radar plots and radial bar charts are true?  
A) Radar plots should be avoided unless the data is cyclic.  
B) Radial visualizations are always preferable for multivariate data due to their compactness.  
C) Radial layouts generally provide more accurate perception of length than rectilinear layouts.  
D) Radial bar charts suffer from nonuniform sector widths, which can distort perception.  

#### 8. When is it acceptable to truncate the y-axis in a chart?  
A) When the truncation is clearly labeled and justified.  
B) When the zero baseline is arbitrary and small changes matter.  
C) It is never acceptable because it always misleads viewers.  
D) When the data represents percentages that do not start at zero.  

#### 9. Which of the following best describe the tasks supported by heatmaps and cluster heatmaps?  
A) Cluster heatmaps add dendrograms to show hierarchical relationships between rows and columns.  
B) Heatmaps are useful for finding clusters and outliers in two categorical keys with quantitative values.  
C) Heatmaps are limited to small datasets due to scalability issues.  
D) Cluster heatmaps reorder rows and columns based on cluster similarity to improve pattern detection.  

#### 10. What are the advantages and disadvantages of connected scatterplots compared to standard scatterplots?  
A) They improve clarity of correlation between variables compared to standard scatterplots.  
B) They are best used when the data has no inherent ordering.  
C) Connected scatterplots emphasize temporal order by connecting points with lines.  
D) They are more engaging but can sometimes obscure the strength of correlation.  



<br>

## Answers

#### 1. Which of the following statements correctly describe the role of keys and values in tabular data visualizations?  
A) ✗ Keys are independent, not dependent attributes. Values are dependent.  
B) ✓ Multidimensional tables can have multiple keys indexing the data.  
C) ✗ Values are dependent attributes, not unique identifiers.  
D) ✓ Keys serve as unique indices to look up items in the table.  

**Correct:** B, D


#### 2. When encoding a third quantitative variable in a scatterplot using point size, which of the following is true?  
A) ✓ Using radius directly can mislead viewers due to nonlinear perception of area.  
B) ✗ Shape is better for categorical distinctions, not quantitative encoding.  
C) ✗ Radius proportional to value misleads because area grows quadratically.  
D) ✓ Size encoding should use the square root of the value to reflect area correctly.  

**Correct:** A, D


#### 3. What are the main limitations of separated but not aligned spatial regions in categorical data visualizations?  
A) ✗ Alphabetical order does not solve comparison issues caused by lack of alignment.  
B) ✗ Ordering is possible but less effective without alignment.  
C) ✓ Difficult to compare sizes across regions without alignment.  
D) ✓ Lack of alignment reduces expressiveness for quantitative comparisons.  

**Correct:** C, D


#### 4. Which of the following are true about stacked bar charts?  
A) ✗ Color hue is essential to distinguish stack components.  
B) ✓ Scalability is limited by number of segments and bars.  
C) ✓ They show part-to-whole relationships with two categorical keys.  
D) ✗ They can handle dozens to hundreds of main key levels, not just few.  

**Correct:** B, C


#### 5. Regarding line charts and bar charts, which statements are correct?  
A) ✓ Line charts are appropriate for ordered keys like time.  
B) ✗ Line charts for categorical keys mislead by implying trends even if alphabetically ordered.  
C) ✓ Bar charts should be used for categorical keys to avoid implying trends.  
D) ✓ Line charts imply continuity and trends, which can mislead if key is categorical.  

**Correct:** A, C, D


#### 6. What are the key challenges and limitations of parallel coordinates plots?  
A) ✗ They require training and are not intuitive for most users.  
B) ✓ Axis ordering is critical and often requires interactive reordering.  
C) ✓ Correlations are visible mainly between neighboring axes.  
D) ✗ They do not scale well visually beyond a few axes without confusion.  

**Correct:** B, C


#### 7. Which of the following statements about radial visualizations like radar plots and radial bar charts are true?  
A) ✓ Radar plots should be avoided unless data is cyclic.  
B) ✗ Radial visualizations are not always preferable; they have perceptual drawbacks.  
C) ✗ Radial layouts generally provide less accurate length perception than rectilinear layouts.  
D) ✓ Radial bar charts suffer from nonuniform sector widths, distorting perception.  

**Correct:** A, D


#### 8. When is it acceptable to truncate the y-axis in a chart?  
A) ✓ Acceptable if truncation is clearly labeled and justified.  
B) ✓ Acceptable when zero baseline is arbitrary and small changes matter.  
C) ✗ Not always unacceptable; there are justified exceptions.  
D) ✓ Acceptable for percentages or data where zero is not meaningful.  

**Correct:** A, B, D


#### 9. Which of the following best describe the tasks supported by heatmaps and cluster heatmaps?  
A) ✓ Cluster heatmaps add dendrograms showing hierarchical relationships.  
B) ✓ Heatmaps help find clusters and outliers in two categorical keys with quantitative values.  
C) ✗ Heatmaps scale well to large datasets, not limited to small ones.  
D) ✓ Cluster heatmaps reorder rows and columns based on cluster similarity.  

**Correct:** A, B, D


#### 10. What are the advantages and disadvantages of connected scatterplots compared to standard scatterplots?  
A) ✗ They do not necessarily improve clarity of correlation; sometimes less clear.  
B) ✗ They are best used when data has inherent ordering, not no ordering.  
C) ✓ Connected scatterplots emphasize temporal order by connecting points.  
D) ✓ They are more engaging but can obscure correlation strength.  

**Correct:** C, D