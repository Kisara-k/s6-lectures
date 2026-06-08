## 9. Visualizations for Tabular Data

## Key Points

#### 1. 🔑 Keys and Values in Tabular Data  
- A **key** is an independent attribute used as a unique index to look up items.  
- Simple tables have one key; multidimensional tables have multiple keys.  
- A **value** is a dependent attribute representing the cell’s data.  
- Visualizations are described by the number of keys and values, data types, marks and channels, tasks, scalability, advantages, and limitations.

#### 2. 📉 Scatterplots  
- Scatterplots represent two quantitative attributes with points positioned horizontally and vertically.  
- Scatterplots have no keys, only values.  
- Additional channels like color, size (area scaled by square root), and shape can encode more data.  
- Connected scatterplots add line marks to show temporal order.  
- Scatterplots are scalable to hundreds of items.

#### 3. 📊 Bar Charts  
- Bar charts visualize one categorical key and one quantitative value.  
- Bars use length to encode quantitative values, separated horizontally and aligned vertically.  
- Bars can be ordered alphabetically or by value size.  
- Scalable to dozens or hundreds of categories.

#### 4. 📚 Stacked Bar Charts  
- Stacked bar charts use two categorical keys and one quantitative value.  
- Marks are vertical stacks of bars with length and color hue channels.  
- Used to show part-to-whole relationships.  
- Scalable to 10-12 segments per stack and dozens to hundreds of bars.

#### 5. 🌊 Streamgraphs  
- Streamgraphs are generalized stacked graphs emphasizing horizontal continuity.  
- Data includes one categorical key, one ordered key (time), and one quantitative value.  
- Scalable to hundreds of time keys and dozens to hundreds of categorical keys.

#### 6. 📈 Line and Dot Charts  
- Dot/line charts use one ordered key and one quantitative value.  
- Marks are points connected by lines to emphasize order and trends.  
- Line charts are appropriate for ordered keys; bar charts for categorical keys.  
- Line charts should not be used for categorical keys as they imply misleading trends.

#### 7. ⚠️ Dual-Axis Line Charts  
- Dual-axis line charts are controversial and can mislead if scales are not commensurate.

#### 8. 📊 Indexed Line Charts  
- Indexed line charts plot normalized values to show relative change over time instead of absolute values.

#### 9. 📉 Slopegraphs  
- Slopegraphs compare two quantitative values per item, connecting points with lines to emphasize changes in rank or value.  
- Scalable to dozens of items.

#### 10. 📅 Gantt Charts  
- Gantt charts visualize one categorical key and two quantitative values (start time and duration).  
- Marks are bars showing temporal overlaps and dependencies.  
- Scalable to dozens of tasks and hundreds of time points.

#### 11. 🔥 Heatmaps  
- Heatmaps visualize two categorical keys and one quantitative value in a 2D matrix.  
- Color encodes the quantitative value.  
- Scalable to millions of items and hundreds of categorical levels.

#### 12. 🌳 Cluster Heatmaps  
- Cluster heatmaps add hierarchical clustering with dendrograms to reorder rows and columns.  
- Used to assess cluster quality.

#### 13. 🔄 Radial and Circular Visualizations  
- Radial bar charts and star plots use length and angle/orientation channels but are less accurate than rectilinear bar charts.  
- Radar plots (radial line charts) are generally discouraged unless data is cyclic.  
- Pie charts encode parts of a whole using angle; accuracy is lower than bar charts.  
- Coxcomb charts are radial bar charts with perception issues due to nonlinear area changes.  
- Pie charts are acceptable for few categories but poor for many.

#### 14. 🔢 Normalized Stacked Bar Charts  
- Normalized stacked bar charts show part-to-whole relationships with bars normalized to full height.  
- Equivalent to a full pie chart but with higher information density.

#### 15. 🔍 Scatterplot Matrix (SPLOM)  
- SPLOM shows all pairwise scatterplots of multiple quantitative variables.  
- Scalable to about a dozen variables and dozens to hundreds of items.

#### 16. ↔️ Parallel Coordinates  
- Parallel coordinates plot multiple quantitative attributes on parallel axes with lines representing items.  
- Axis ordering is critical and challenging; interaction or algorithms are used to reorder axes.  
- Scalable to dozens of attributes and hundreds of items.  
- Positive correlation shows parallel lines; negative correlation shows crossing lines.

#### 17. 🛑 Limitations and Best Practices  
- Always label chart axes clearly.  
- Avoid cropping the y-axis (not starting at zero) unless justified.  
- Rectilinear charts are easier to interpret than radial charts.  
- Radial charts suffer from angle perception issues and nonuniform sector sizes.  
- Parallel coordinates require training and interaction to be effective.  
- Choose chart types based on data type and task to avoid misleading visualizations.



<br>

