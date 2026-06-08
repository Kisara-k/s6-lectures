## 9. Visualizations for Tabular Data

## Study Notes

### 1. 📊 Introduction to Visualizations for Tabular Data

When working with tabular data—data organized in rows and columns—visualizations help us understand patterns, relationships, and trends that might be hard to see just by looking at numbers. This lecture focuses on how to visualize tabular data effectively, covering different types of charts and graphs, their components, and best practices.

At the core of tabular data visualization are **keys** and **values**:

- **Keys** are independent attributes used to uniquely identify or index data items. For example, in a table of sales data, the product name or date might be a key.
- **Values** are dependent attributes representing the data measured or observed, like sales amount or temperature.

Tables can have one key (simple tables) or multiple keys (multidimensional tables). Visualizations are described by how many keys and values they represent, the data types involved, the marks and visual channels used, the tasks they support, their scalability, and their pros and cons.


### 2. 📈 Scatterplots and Their Variations

#### What is a Scatterplot?

A scatterplot is a fundamental visualization used to display the relationship between two quantitative variables. It plots points on a two-dimensional plane where the horizontal (x) and vertical (y) positions correspond to the values of the two variables.

- **Keys:** None (only values)
- **Data:** Two quantitative attributes
- **Marks:** Points
- **Channels:** Horizontal and vertical position
- **Tasks:** Identify trends, outliers, distribution, correlation, and clusters
- **Scalability:** Can handle hundreds of data points effectively

#### Enhancing Scatterplots

Scatterplots can encode more information by adding channels such as:

- **Color:** Different colors can represent categories or additional quantitative variables.
- **Size:** The size of points can represent a third quantitative variable. Note that size should be proportional to the square root of the value to avoid misleading perception because area grows quadratically with radius.
- **Shape:** Different shapes can distinguish categories.

#### Connected Scatterplots

These are scatterplots where points are connected by lines, often used to show temporal order or progression over time. They are popular in journalism because they combine the clarity of scatterplots with the ability to show sequences.

- **Axes:** Horizontal and vertical represent value attributes
- **Lines:** Show temporal order
- **Use:** Alternative to dual-axis charts
- **Engagement:** Studies show they are engaging but can sometimes make correlation less clear.


### 3. 📊 Bar Charts and Variants

#### Simple Bar Chart

Bar charts are one of the most common ways to visualize data with one categorical key and one quantitative value.

- **Data:** One categorical attribute (key) and one quantitative attribute (value)
- **Marks:** Lines (bars)
- **Channels:** Length of the bar encodes the quantitative value
- **Spatial arrangement:** Bars are separated horizontally and aligned vertically
- **Ordering:** Bars can be ordered alphabetically by category or by value size
- **Tasks:** Compare values and look up specific values
- **Scalability:** Effective for dozens to hundreds of categories

#### Stacked Bar Chart

Stacked bar charts add another categorical key to show part-to-whole relationships.

- **Data:** Two categorical keys and one quantitative value
- **Marks:** Vertical stacks of bars (each segment represents a subcategory)
- **Channels:** Length and color hue
- **Spatial arrangement:** One glyph (stack) per main category, aligned at the base
- **Tasks:** Show how parts contribute to the whole
- **Scalability:** Limited by the number of segments (10-12 per stack) and bars (dozens to hundreds)

#### Streamgraph

A streamgraph is a variation of stacked graphs emphasizing horizontal continuity, often used for time series data.

- **Data:** One categorical key (e.g., movies), one ordered key (time), and one quantitative value (counts)
- **Geometry:** Layers where height encodes counts
- **Scalability:** Can handle hundreds of time points and dozens to hundreds of categories
- **Use:** Visualize changes over time with smooth flowing layers


### 4. 📉 Line and Dot Charts

#### Dot / Line Chart

These charts combine points and connecting lines to show trends over an ordered key (like time).

- **Data:** One ordered key and one quantitative value
- **Marks:** Points connected by lines
- **Channels:** Length and position encode values; lines emphasize order
- **Tasks:** Identify trends and changes over time
- **Scalability:** Suitable for hundreds of key levels

#### Choosing Between Bar and Line Charts

- Use **bar charts** for categorical keys (discrete groups).
- Use **line charts** for ordered keys (like time or sequences).
- Avoid line charts for categorical keys because they imply trends or continuity that don’t exist, which can mislead interpretation.


### 5. 📅 Specialized Charts for Time and Ranking

#### Dual-Axis Line Charts

These charts plot two different quantitative variables on two y-axes. They are controversial because they can be misleading if the scales are not comparable.

#### Indexed Line Charts

Instead of plotting raw values, indexed line charts plot normalized values to show relative change over time, making it easier to compare trends.

#### Slopegraphs

Slopegraphs compare two quantitative values for multiple items, connecting points with lines to emphasize changes in rank or value.

- **Data:** Two quantitative values per item
- **Marks:** Points connected by lines
- **Tasks:** Highlight changes between two points in time or conditions
- **Scalability:** Effective for dozens of items

#### Gantt Charts

Used to visualize tasks or events over time, showing start and end times as bars.

- **Data:** One categorical key (task) and two quantitative values (start and duration)
- **Marks:** Bars aligned horizontally
- **Tasks:** Show temporal overlaps and dependencies
- **Scalability:** Dozens of tasks, hundreds of time points


### 6. 🔥 Heatmaps and Cluster Heatmaps

#### Heatmap

A heatmap visualizes data with two categorical keys arranged in a matrix, where color encodes a quantitative value.

- **Data:** Two categorical keys and one quantitative value
- **Marks:** Colored cells in a grid
- **Channels:** Color hue or intensity
- **Tasks:** Identify clusters, patterns, and outliers
- **Scalability:** Can handle millions of items and hundreds of categories

#### Cluster Heatmap

Adds hierarchical clustering to reorder rows and columns based on similarity, often shown with dendrograms (tree diagrams).

- **Derived data:** Cluster hierarchies
- **Tasks:** Assess cluster quality and relationships


### 7. 🌟 Radial and Circular Visualizations

#### Radial Bar Chart and Star Plot

These charts arrange bars or lines radially around a central point.

- **Channels:** Length and angle/orientation
- **Accuracy:** Less accurate than rectilinear bar charts because length is not aligned linearly
- **Use:** Sometimes used for data with cyclic or equal importance attributes

#### Radar Plot

A radial line chart connecting points on multiple axes arranged in a circle.

- **Use:** Generally discouraged unless data is cyclic
- **Reason:** Difficult to interpret and compare values accurately

#### Pie and Coxcomb Charts

- **Pie chart:** Uses angle to encode parts of a whole; area perception is less accurate than length.
- **Coxcomb chart:** Radial bar chart variant with line marks; perception issues due to nonlinear area changes.
- **Best practice:** Pie charts are okay for very few categories but become confusing with many.


### 8. 🔄 Multivariate Visualizations: SPLOM and Parallel Coordinates

#### Scatterplot Matrix (SPLOM)

A grid of scatterplots showing all pairwise relationships between multiple quantitative variables.

- **Axes:** Rectilinear
- **Marks:** Points
- **Scalability:** Works well for a dozen variables and dozens to hundreds of items
- **Tasks:** Explore correlations between pairs of variables

#### Parallel Coordinates

Visualizes high-dimensional data by plotting each attribute on a parallel vertical axis and representing each data item as a line crossing these axes.

- **Marks:** Jagged lines connecting attribute values
- **Challenges:** Axis ordering is critical for pattern detection; requires interaction or algorithms to reorder axes
- **Scalability:** Can handle dozens of attributes and hundreds of items
- **Tasks:** Detect correlations and patterns across multiple variables


### 9. ⚠️ Limitations and Best Practices

#### Axis Labeling and Scaling

- Always label axes clearly to avoid confusion.
- Avoid cropping the y-axis (not starting at zero) unless justified, as it can mislead viewers about the magnitude of changes.

#### Orientation and Perception

- Rectilinear charts are easier to interpret than radial ones.
- Radial charts suffer from angle perception issues and nonuniform sector sizes.
- Parallel coordinates require training and interaction to be effective.

#### Choosing the Right Chart

- Match the chart type to the data and task.
- Avoid misleading visualizations that imply trends or relationships not present in the data.
- Consider scalability and clarity when dealing with large datasets.


### Summary

Visualizing tabular data effectively requires understanding the nature of your data (keys and values), the tasks you want to accomplish (comparison, trend detection, part-to-whole relationships), and the strengths and limitations of different chart types. Scatterplots, bar charts, line charts, heatmaps, and multivariate plots like SPLOM and parallel coordinates each serve different purposes and come with their own best practices. Always prioritize clarity, accurate perception, and appropriate encoding channels to make your visualizations both informative and trustworthy.