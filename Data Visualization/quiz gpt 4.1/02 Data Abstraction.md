## 3. Data Abstraction

## Questions

#### 1. Which of the following best describes the difference between an item and an attribute in a dataset?
A) An item represents an individual entity, while an attribute represents a characteristic of that entity  
B) An attribute is a property measured for each item  
C) An item is always a number, while an attribute is always a word  
D) An item is a property measured for each attribute  


#### 2. Which of the following are examples of links in data abstraction?
A) The age of a patient in a medical dataset  
B) The friendship relationship between two people on a social network  
C) The interaction between two proteins in a biological network  
D) The latitude and longitude of a city  


#### 3. Which statements about attribute types are correct?
A) Ordinal attributes allow for meaningful arithmetic operations  
B) Quantitative attributes have meaningful magnitudes and support arithmetic  
C) Ordinal attributes have a defined order but not necessarily equal intervals between values  
D) Categorical attributes have no implicit ordering  


#### 4. Which of the following are valid examples of spatial fields?
A) A 3D MRI scan where each voxel has a measured value  
B) A network graph showing friendships between people  
C) A table listing students and their grades  
D) A map showing temperature values at different locations  


#### 5. Which of the following statements about dataset types is/are correct?
A) In a network, nodes represent items and edges represent links  
B) A tree is a special case of a network/graph with no cycles  
C) Multidimensional tables can be indexed by more than one key  
D) In a flat table, each row represents an attribute and each column an item  


#### 6. Which of the following are considered when performing data abstraction for visualization?
A) Identifying the cardinality of attributes  
B) Translating domain-specific data into a generic visualization language  
C) Considering whether to transform the data based on the analysis task  
D) Determining the programming language used to store the data  


#### 7. Which of the following best illustrates the difference between a data model and a conceptual model?
A) A data model might represent temperature as floating-point numbers, while a conceptual model might interpret those numbers as "hot," "warm," or "cold" depending on the task  
B) A data model is always visual, while a conceptual model is always mathematical  
C) A conceptual model is used for programming, while a data model is used for visualization  
D) A data model defines the mathematical structure of data, while a conceptual model provides real-world meaning and supports reasoning  


#### 8. Which of the following are true about derived attributes?
A) Derived attributes can provide new insights not directly available from the original data  
B) Derived attributes can be computed from original data through simple or complex transformations  
C) Derived attributes must always be quantitative  
D) Derived attributes are always categorical  


#### 9. Which of the following statements about spatial data and geometry are correct?
A) Positions in data can refer to explicit spatial locations such as pixels or latitude/longitude  
B) Geometry in visualization is always taken as given and never a design decision  
C) Geometry can include points, lines, surfaces, and volumes  
D) In visualization, the choice of geometry can be influenced by the design goals  


#### 10. Which of the following are true about cardinality in the context of data abstraction?
A) Cardinality of an attribute refers to the number of unique values it can take  
B) Understanding cardinality can help guide data transformation and visualization choices  
C) Cardinality is only relevant for quantitative attributes  
D) Cardinality refers to the number of items in a dataset  



<br>

## Answers

#### 1. Which of the following best describes the difference between an item and an attribute in a dataset?
A) ✓ An item represents an individual entity, while an attribute is a characteristic of that entity; this is correct.  
B) ✓ An attribute is a property measured for each item; this is correct.  
C) ✗ Items and attributes can be numbers or words; this is not a defining difference.  
D) ✗ An item is not a property measured for each attribute; this reverses the relationship.  

**Correct:** A, B


#### 2. Which of the following are examples of links in data abstraction?
A) ✗ Age is an attribute, not a link.  
B) ✓ Friendship is a relationship between two items (people), which is a link.  
C) ✓ Protein interaction is a relationship between two items (proteins), which is a link.  
D) ✗ Latitude and longitude are positions, not links.  

**Correct:** B, C


#### 3. Which statements about attribute types are correct?
A) ✗ Ordinal attributes have order but do not support meaningful arithmetic operations.  
B) ✓ Quantitative attributes have meaningful magnitudes and support arithmetic; this is correct.  
C) ✓ Ordinal attributes have a defined order but not necessarily equal intervals; this is correct.  
D) ✓ Categorical attributes have no implicit ordering; this is correct.  

**Correct:** B, C, D


#### 4. Which of the following are valid examples of spatial fields?
A) ✓ A 3D MRI scan with values per voxel is a spatial field.  
B) ✗ A network graph is not a spatial field; it represents relationships, not spatially continuous data.  
C) ✗ A table of students and grades is not a spatial field.  
D) ✓ Temperature values mapped to locations are a spatial field.  

**Correct:** A, D


#### 5. Which of the following statements about dataset types is/are correct?
A) ✓ In a network, nodes represent items and edges represent links; this is correct.  
B) ✓ A tree is a special case of a network/graph with no cycles; this is correct.  
C) ✓ Multidimensional tables can be indexed by more than one key; this is correct.  
D) ✗ In a flat table, each row is an item and each column is an attribute, not the other way around.  

**Correct:** A, B, C


#### 6. Which of the following are considered when performing data abstraction for visualization?
A) ✓ Identifying the cardinality of attributes is part of data abstraction.  
B) ✓ Translating domain-specific data into a generic visualization language is a key step.  
C) ✓ Considering whether to transform the data based on the analysis task is part of data abstraction.  
D) ✗ The programming language used is not part of data abstraction.  

**Correct:** A, B, C


#### 7. Which of the following best illustrates the difference between a data model and a conceptual model?
A) ✓ This example shows how the same data model (numbers) can be interpreted differently depending on the conceptual model; this is correct.  
B) ✗ Both models can be visual or mathematical; this is not the distinction.  
C) ✗ Conceptual models are not just for programming, nor are data models just for visualization.  
D) ✓ A data model defines mathematical structure, while a conceptual model provides real-world meaning; this is correct.  

**Correct:** A, D


#### 8. Which of the following are true about derived attributes?
A) ✓ Derived attributes can provide new insights not directly available from the original data; this is correct.  
B) ✓ Derived attributes can be computed from original data through transformations; this is correct.  
C) ✗ Derived attributes are not limited to quantitative types.  
D) ✗ Derived attributes can be any type, not just categorical.  

**Correct:** A, B


#### 9. Which of the following statements about spatial data and geometry are correct?
A) ✓ Positions can refer to explicit spatial locations like pixels or coordinates; this is correct.  
B) ✗ In visualization, geometry can be a design decision, not always taken as given.  
C) ✓ Geometry can include points, lines, surfaces, and volumes; this is correct.  
D) ✓ The choice of geometry in visualization can be influenced by design goals; this is correct.  

**Correct:** A, C, D


#### 10. Which of the following are true about cardinality in the context of data abstraction?
A) ✓ Cardinality of an attribute refers to the number of unique values it can take; this is correct.  
B) ✓ Understanding cardinality can help guide data transformation and visualization choices; this is correct.  
C) ✗ Cardinality is relevant for all attribute types, not just quantitative.  
D) ✓ Cardinality refers to the number of items in a dataset; this is correct.  

**Correct:** A, B, D