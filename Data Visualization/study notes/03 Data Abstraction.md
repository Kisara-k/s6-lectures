## 3. Data Abstraction

## Study Notes

### 1. 📊 What is Data? Understanding the Basics of Data Meaning and Context

When we talk about **data**, it’s important to realize that raw numbers or words by themselves don’t carry inherent meaning. For example, consider the sequence of numbers:  
`14, 2.6, 30, 30, 15, 100001`  
What do these numbers represent? Without context, they could mean many things:  
- Coordinates of two points far apart in 3D space?  
- Two points close together in 2D space, with 15 links between them and a link weight of 100001?  
- Something else entirely?

Similarly, a list like `Basil, 7, S, Pear` could mean:  
- A shipment of produce (basil and pear) arriving on the 7th day in satisfactory condition.  
- A neighborhood named Basil Point receiving 7 inches of snow cleared by Pear Creek Limited.  
- A lab rat named Basil making 7 attempts in a maze, rewarded with pear.

This shows that **semantics**, or the real-world meaning behind data, is crucial. Data without context is just symbols or numbers. Understanding what data *means* in the real world is the first step in working with it effectively.


### 2. 🧩 Key Data Concepts: Items, Attributes, and Other Data Types

#### Items and Attributes  
- **Item:** An individual, discrete entity in a dataset. Think of an item as a single "thing" you are studying or measuring, like a patient, a car, or a city. Items are often called "independent variables" because they represent the entities you observe.  
- **Attribute:** A property or characteristic of an item that you measure or record. For example, a patient’s height or blood pressure, or a car’s horsepower or make. Attributes are sometimes called "dependent variables" because their values depend on the item.

Example:  
| Item (Person) | Attributes (Name, Age, Shirt Size, Favorite Fruit) |  
|---------------|----------------------------------------------------|  
| Person A      | Alice, 30, M, Apple                                |  
| Person B      | Bob, 25, L, Banana                                 |

#### Other Data Types  
- **Links:** These express relationships between two items, such as friendships on Facebook or interactions between proteins.  
- **Positions:** Spatial data that specify locations in 2D or 3D space, like pixels in a photo or latitude/longitude coordinates.  
- **Grids:** A way to sample continuous data regularly, like temperature readings on a weather map.


### 3. 🗂️ Dataset Types: How Data is Organized

Data can be organized in different ways depending on the nature of the information and the analysis goals.

#### Flat Tables  
- The simplest form: one item per row, each column is an attribute, and each cell holds the value for that item-attribute pair.  
- Usually has a unique key to identify each item (sometimes implicit).  
Example: A spreadsheet listing patients with columns for name, age, and blood pressure.

#### Multidimensional Tables  
- These tables use multiple keys to index data, like genes measured across multiple patients.  
- Think of it as a table with more than two dimensions.

#### Networks/Graphs  
- Data represented as nodes (items) connected by links (edges).  
- A **tree** is a special type of graph with no cycles and often has a root node.  
- Networks are useful for representing relationships, like social networks or protein interactions.

#### Spatial Fields  
- Data associated with spatial cells, where each cell contains values from a continuous domain.  
- Examples include temperature, pressure, or wind velocity measured or simulated over a geographic area.  
- Important concepts here are **sampling** (where data is measured) and **interpolation** (estimating values between measured points).  
- Attributes per cell can be:  
  - Scalar (single value, e.g., temperature)  
  - Vector (multiple values, e.g., wind velocity with direction and magnitude)  
  - Tensor (complex data, e.g., stress in materials)

#### Geometry  
- Refers to the shape and spatial properties of items, such as points, lines, surfaces, or volumes.  
- This is where computer graphics and visualization overlap: graphics often take geometry as given, while visualization may treat geometry as a design choice.

#### Spatial Collections  
- Ways to group items:  
  - **Sets:** Unique items, no order.  
  - **Lists:** Ordered, duplicates allowed.  
  - **Clusters:** Groups of similar items.


### 4. 🧮 Attribute Types: Understanding the Nature of Data Values

Attributes can be classified based on the type of values they hold and how those values can be interpreted or compared.

- **Categorical (Nominal):** Values represent categories with no inherent order. You can check if two values are equal or not, but you cannot say one is greater than the other. Example: blood type (A, B, AB, O).  
- **Ordinal:** Values have a meaningful order, but the difference between values is not necessarily consistent. Example: rankings like "small," "medium," "large."  
- **Quantitative:** Values have meaningful magnitudes and support arithmetic operations. Example: height in centimeters, temperature in degrees.

Understanding attribute types is essential because it influences how data can be analyzed and visualized.


### 5. 🔄 Data Abstraction: Transforming Raw Data into Visualization-Ready Forms

Data abstraction is the process of translating raw, domain-specific data into a form suitable for visualization. This involves several key steps:

1. **Translate domain-specific language into a generic visualization language:** For example, converting medical records into tables or graphs.  
2. **Identify dataset types and attribute types:** Recognize whether the data is a flat table, network, spatial field, etc., and classify attributes as categorical, ordinal, or quantitative.  
3. **Identify cardinality:**  
   - How many items are in the dataset?  
   - What is the cardinality of each attribute (number of unique values)?  
   - For categorical data, how many levels (categories) exist?  
   - For quantitative data, what is the range of values?  
4. **Consider data transformation:** Sometimes data needs to be transformed (e.g., normalized, aggregated) based on the task or visualization goals.


### 6. 🧠 Data Models vs Conceptual Models: The Difference Between Math and Meaning

- **Data Model:** A mathematical abstraction of data, such as sets of numbers with operations like addition or multiplication. Programming languages use data models to represent variable types (e.g., floats, integers).  
- **Conceptual Model:** A mental or semantic model that helps us understand what the data *means* in the real world. It supports reasoning and decision-making based on the data.

The data abstraction process relies heavily on the conceptual model because it guides how data should be transformed and interpreted for visualization.

#### Example: Temperature Data  
- Data model: A list of floating-point numbers like 32.52, 54.06, -14.35.  
- Conceptual model: Temperature as a physical quantity.  
- Different abstractions based on task:  
  - For weather forecasting: treat temperature as quantitative (continuous values).  
  - For deciding if bath water is ready: treat temperature as ordinal (hot, warm, cold).  
  - For deciding if you should leave the house: treat temperature as categorical (above freezing, below freezing).


### 7. ⚙️ Derived Attributes: Creating New Data from Existing Data

Sometimes, new attributes are computed from original data to provide additional insights or simplify analysis. These are called **derived attributes**.

- Derived attributes can be simple type changes (e.g., converting temperature from Celsius to Fahrenheit).  
- They can involve acquiring additional data or performing complex transformations.

#### Example: Strahler Number in Network Analysis  
- The Strahler number is a centrality metric used in trees or networks to measure the importance or hierarchy of nodes.  
- It is a derived quantitative attribute calculated from the network structure.  
- In a large graph with 500,000 nodes, visualizing the top 5,000 nodes by Strahler number can help reveal the "skeleton" or main structure of the network.


### Summary

Data abstraction is a foundational concept in visualization that involves understanding what data *means*, how it is structured, and how it can be transformed into forms suitable for analysis and visualization. Key ideas include distinguishing between items and attributes, recognizing different dataset types (tables, networks, spatial fields), classifying attribute types (categorical, ordinal, quantitative), and using conceptual models to guide data transformation. Derived attributes further enrich data by creating new, meaningful metrics from existing information. This process ensures that visualizations are not just pretty pictures but meaningful representations of real-world phenomena.