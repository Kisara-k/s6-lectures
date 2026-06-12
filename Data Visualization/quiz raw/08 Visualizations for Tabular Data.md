## 9. Visualizations for Tabular Data

## Questions

#### 1. Which of the following statements correctly describe the role of keys and values in tabular data visualizations?  
A) Multidimensional tables can have multiple keys indexing the data.  
B) Keys are always quantitative attributes.  
C) Keys are dependent attributes used to look up values in a table.  
D) Values are dependent attributes representing the content of cells.  

#### 2. When designing a scatterplot to encode additional quantitative attributes beyond the two spatial axes, which of the following practices are appropriate?  
A) Use shape to encode a categorical attribute.  
B) Use color to represent a third quantitative attribute.  
C) Use the radius of points directly to represent a quantitative attribute without adjustment.  
D) Use the size (area) of points, applying square root scaling to avoid misleading perception.  

#### 3. What are the main limitations of separated but not aligned or ordered spatial regions in visualizations?  
A) It makes it impossible to use color encoding.  
B) It is hard to determine the rank or order of regions.  
C) It is difficult to compare sizes across regions.  
D) It violates the expressiveness principle for categorical attributes.  

#### 4. Which of the following are true about stacked bar charts?  
A) They scale well with hundreds of segments per bar.  
B) They use length and color hue as visual channels.  
C) They are best suited for showing part-to-whole relationships.  
D) They represent data with two categorical keys and one quantitative value.  

#### 5. Regarding line charts and bar charts, which statements are correct?  
A) Line charts are appropriate for ordered key attributes.  
B) Bar charts should be used for categorical key attributes.  
C) Line charts can be used for categorical keys if the categories have a natural order.  
D) Using line charts for categorical keys can mislead by implying trends that do not exist.  

#### 6. What are the advantages and challenges of parallel coordinates compared to scatterplots?  
A) Scatterplots can only show two attributes spatially at once.  
B) Axis ordering in parallel coordinates is trivial and does not affect interpretation.  
C) Parallel coordinates can show many attributes simultaneously by lining up axes in parallel.  
D) Parallel coordinates require training and are less familiar to many users.  

#### 7. Which of the following statements about radial visualizations such as radar plots and radial bar charts are true?  
A) Radial layouts generally have lower accuracy in length perception compared to rectilinear layouts.  
B) Radar plots are recommended for most types of data, especially non-cyclic data.  
C) Nonuniform sector widths in radial charts can cause nonlinear area perception issues.  
D) Radial bar charts encode data using length and angle/orientation channels.  

#### 8. When is it acceptable to use dual-axis line charts, and what are the risks?  
A) They are easy to interpret and rarely misleading.  
B) Dual-axis charts can easily mislead viewers if scales are not carefully matched.  
C) Dual-axis charts are acceptable when the two axes represent commensurate quantities.  
D) They are recommended for all time series comparisons.  

#### 9. Which of the following best practices apply to pie charts?  
A) Pie charts encode data using length channels.  
B) Pie charts are effective for part-to-whole judgments with only a few categories.  
C) Pie charts maintain high accuracy even with many categories.  
D) Normalized stacked bar charts can be used as an alternative to pie charts for part-to-whole tasks.  

#### 10. What are the key scalability limitations of scatterplots and scatterplot matrices (SPLOMs)?  
A) SPLOMs scale well to thousands of attributes.  
B) SPLOMs are limited to about a dozen attributes before becoming difficult to interpret.  
C) Scatterplots can encode multiple quantitative attributes spatially without limitation.  
D) Scatterplots can effectively display hundreds of items.  



<br>

## Answers

#### 1. Which of the following statements correctly describe the role of keys and values in tabular data visualizations?  
A) ✓ Multidimensional tables can have multiple keys indexing the data.  
B) ✗ Keys can be categorical or quantitative, not always quantitative.  
C) ✗ Keys are independent attributes, not dependent, used to look up values.  
D) ✓ Values are dependent attributes representing the content of cells.  

**Correct:** A, D


#### 2. When designing a scatterplot to encode additional quantitative attributes beyond the two spatial axes, which of the following practices are appropriate?  
A) ✓ Shape is appropriate for encoding categorical attributes, not quantitative.  
B) ✓ Color can encode a third quantitative attribute effectively.  
C) ✗ Using radius directly misleads perception because area grows quadratically.  
D) ✓ Using size (area) with square root scaling corrects for perceptual distortion.  

**Correct:** A, B, D


#### 3. What are the main limitations of separated but not aligned or ordered spatial regions in visualizations?  
A) ✗ Color encoding is still possible regardless of alignment or order.  
B) ✗ Rank or order is not relevant if regions are not ordered; this limitation applies when aligned but unordered.  
C) ✓ Difficult to compare sizes across regions without alignment.  
D) ✗ It does not violate expressiveness for categorical attributes; separation is consistent with expressiveness.  

**Correct:** C


#### 4. Which of the following are true about stacked bar charts?  
A) ✗ They do not scale well with many segments per bar; 10-12 segments is typical max.  
B) ✓ They use length and color hue as visual channels.  
C) ✓ They are suited for showing part-to-whole relationships.  
D) ✓ They represent data with two categorical keys and one quantitative value.  

**Correct:** B, C, D


#### 5. Regarding line charts and bar charts, which statements are correct?  
A) ✓ Line charts are appropriate for ordered key attributes.  
B) ✓ Bar charts should be used for categorical key attributes.  
C) ✗ Line charts should not be used for categorical keys even if ordered, as it implies trends.  
D) ✓ Using line charts for categorical keys can mislead by implying trends that do not exist.  

**Correct:** A, B, D


#### 6. What are the advantages and challenges of parallel coordinates compared to scatterplots?  
A) ✓ Scatterplots spatially encode only two attributes at once.  
B) ✗ Axis ordering is a major challenge and affects interpretation significantly.  
C) ✓ Parallel coordinates can show many attributes simultaneously by lining up axes in parallel.  
D) ✓ Parallel coordinates require training and are less familiar to many users.  

**Correct:** A, C, D


#### 7. Which of the following statements about radial visualizations such as radar plots and radial bar charts are true?  
A) ✓ Radial layouts generally have lower accuracy in length perception than rectilinear layouts.  
B) ✗ Radar plots are generally discouraged except for cyclic data.  
C) ✓ Nonuniform sector widths cause nonlinear area perception issues.  
D) ✓ Radial bar charts encode data using length and angle/orientation channels.  

**Correct:** A, C, D


#### 8. When is it acceptable to use dual-axis line charts, and what are the risks?  
A) ✗ They are often misleading and not easy to interpret.  
B) ✓ They can easily mislead if scales are not carefully matched.  
C) ✓ Acceptable if the two axes represent commensurate quantities.  
D) ✗ Not recommended for all time series comparisons; use cautiously.  

**Correct:** B, C


#### 9. Which of the following best practices apply to pie charts?  
A) ✗ Pie charts encode data using angle/area, not length channels.  
B) ✓ Effective for part-to-whole judgments with few categories.  
C) ✗ Accuracy decreases with many categories; pie charts become ineffective.  
D) ✓ Normalized stacked bar charts are a good alternative for part-to-whole tasks.  

**Correct:** B, D


#### 10. What are the key scalability limitations of scatterplots and scatterplot matrices (SPLOMs)?  
A) ✗ SPLOMs do not scale well to thousands of attributes; limited to about a dozen.  
B) ✓ SPLOMs become difficult to interpret beyond about a dozen attributes.  
C) ✗ Scatterplots spatially encode only two quantitative attributes at once.  
D) ✓ Scatterplots can display hundreds of items effectively.  

**Correct:** B, D