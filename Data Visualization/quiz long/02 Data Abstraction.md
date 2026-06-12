## 3. Data Abstraction

## Questions

#### 1. What does the term "semantics" refer to in the context of data?  
A) The real-world meaning behind the data  
B) The format in which data is stored  
C) The mathematical operations that can be performed on data  
D) The programming language used to process data  

#### 2. Which of the following best describes an "item" in a dataset?  
A) A spatial coordinate in 3D space  
B) An individual, discrete entity such as a patient or city  
C) A property or characteristic measured about an entity  
D) A relationship between two entities  

#### 3. Attributes in a dataset are often called "dependent variables" because:  
A) Their values depend on the item they describe  
B) They depend on the programming language used  
C) They are always numerical values  
D) They represent relationships between items  

#### 4. Which of the following are examples of "links" in data?  
A) Temperature readings at different locations  
B) Latitude and longitude coordinates  
C) Protein interactions in biology  
D) Friendship connections on social media  

#### 5. What distinguishes a "flat table" dataset from a "multidimensional table"?  
A) Multidimensional tables cannot represent categorical data  
B) Flat tables are only used for spatial data  
C) Flat tables have one item per row and attributes as columns, multidimensional tables use multiple keys for indexing  
D) Flat tables have multiple keys indexing data, multidimensional tables do not  

#### 6. In a network or graph dataset, which of the following statements are true?  
A) Networks cannot represent hierarchical relationships  
B) A tree is a special type of graph with no cycles  
C) All graphs must be directed  
D) Nodes represent items, and edges represent links between them  

#### 7. Which of the following attribute types allow meaningful arithmetic operations?  
A) Categorical  
B) Quantitative  
C) Ordinal  
D) Nominal  

#### 8. Which of the following is NOT a characteristic of categorical (nominal) data?  
A) Categories represent distinct groups  
B) Values can be compared for equality  
C) Values have no implicit ordering  
D) Arithmetic operations like addition are meaningful  

#### 9. When considering spatial fields, what is the primary difference between scalar, vector, and tensor attributes?  
A) Tensors are only used in 2D data  
B) Scalar attributes have one value per cell, vectors have multiple values, tensors have many values representing complex data  
C) Vectors cannot represent direction  
D) Scalar attributes have multiple values per cell, vectors have one, tensors have none  

#### 10. Which of the following best describes the role of a conceptual model in data abstraction?  
A) It defines the programming language used to process data  
B) It is a mathematical abstraction of data types and operations  
C) It replaces the need for data transformation  
D) It is a mental model that supports reasoning about the meaning of data  

#### 11. How does cardinality relate to data abstraction?  
A) It refers to the number of attributes in a dataset  
B) It refers to the number of unique items or values in a dataset or attribute  
C) It determines the programming language used  
D) It is only relevant for quantitative data  

#### 12. Which of the following are valid reasons to transform data during the abstraction process?  
A) To aggregate data based on task requirements  
B) To convert categorical data into quantitative data without context  
C) To change the conceptual meaning of the data arbitrarily  
D) To normalize values for better comparison  

#### 13. Which of the following statements about derived attributes is true?  
A) Derived attributes are always simpler than original attributes  
B) Derived attributes can be computed from original data using transformations  
C) Derived attributes cannot be quantitative  
D) Derived attributes require acquiring additional data sometimes  

#### 14. In the example of temperature data, which of the following conceptual models could be used depending on the task?  
A) Treating temperature as nominal data for scientific calculations  
B) Treating temperature as continuous quantitative data for weather forecasting  
C) Treating temperature as categorical data for deciding if you should leave the house  
D) Treating temperature as ordinal data for deciding if bath water is ready  

#### 15. Which of the following best describes the difference between data models and conceptual models?  
A) Data models are programming language types, conceptual models represent semantics and support reasoning  
B) Data models are used only for visualization, conceptual models only for storage  
C) Data models are mental constructions, conceptual models are mathematical abstractions  
D) Conceptual models are always more precise than data models  

#### 16. Which of the following dataset types can represent hierarchical relationships?  
A) Networks/graphs, especially trees  
B) Flat tables  
C) Spatial fields  
D) Multidimensional tables  

#### 17. Which of the following statements about spatial collections is correct?  
A) Lists are unordered and do not allow duplicates  
B) Sets are ordered collections that allow duplicates  
C) Spatial collections only apply to 3D data  
D) Clusters group similar items together  

#### 18. When analyzing a large network, why might one use a derived attribute like the Strahler number?  
A) To visualize all nodes equally without filtering  
B) To ignore the network structure and focus on attributes only  
C) To convert categorical data into quantitative data  
D) To reduce the dataset size by focusing on the most central nodes  

#### 19. Which of the following is NOT a typical concern when working with spatial fields?  
A) Interpolating attribute values between measured points  
B) Sampling locations where attributes are measured  
C) Choosing appropriate grid types for data representation  
D) Ensuring all attributes are categorical  

#### 20. Which of the following statements about the relationship between geometry and visualization is true?  
A) Visualization treats geometry as a design decision, while computer graphics often take geometry as given  
B) Geometry only applies to 3D data, not 2D  
C) Visualization ignores geometry and focuses only on attribute values  
D) Geometry is always fixed and cannot be changed in visualization  



<br>

## Answers

#### 1. What does the term "semantics" refer to in the context of data?  
A) ✓ Semantics is the real-world meaning behind data.  
B) ✗ Format is not semantics.  
C) ✗ Semantics is about meaning, not operations.  
D) ✗ Programming language is unrelated to semantics.  

**Correct:** A


#### 2. Which of the following best describes an "item" in a dataset?  
A) ✗ Positions are spatial data, not items.  
B) ✓ An item is an individual entity like a patient or city.  
C) ✗ This describes an attribute, not an item.  
D) ✗ Links describe relationships, not items.  

**Correct:** B


#### 3. Attributes in a dataset are often called "dependent variables" because:  
A) ✓ Attributes depend on the item they describe.  
B) ✗ Programming language is irrelevant here.  
C) ✗ Attributes can be categorical or non-numerical.  
D) ✗ Attributes are properties, not relationships.  

**Correct:** A


#### 4. Which of the following are examples of "links" in data?  
A) ✗ Temperature readings are attribute values, not links.  
B) ✗ Coordinates are positions, not links.  
C) ✓ Protein interactions are links between items.  
D) ✓ Friendships are relationships, so links.  

**Correct:** C, D


#### 5. What distinguishes a "flat table" dataset from a "multidimensional table"?  
A) ✗ Multidimensional tables can represent categorical data.  
B) ✗ Flat tables are not limited to spatial data.  
C) ✓ Flat tables have one key per row; multidimensional tables use multiple keys.  
D) ✗ Flat tables do not have multiple keys.  

**Correct:** C


#### 6. In a network or graph dataset, which of the following statements are true?  
A) ✗ Networks can represent hierarchies (e.g., trees).  
B) ✓ Trees are graphs without cycles.  
C) ✗ Graphs can be directed or undirected.  
D) ✓ Nodes are items; edges are links.  

**Correct:** B, D


#### 7. Which of the following attribute types allow meaningful arithmetic operations?  
A) ✗ Categorical data does not support arithmetic.  
B) ✓ Quantitative data supports arithmetic operations.  
C) ✗ Ordinal data has order but no meaningful arithmetic.  
D) ✗ Nominal is another term for categorical, no arithmetic.  

**Correct:** B


#### 8. Which of the following is NOT a characteristic of categorical (nominal) data?  
A) ✗ Categories represent distinct groups, which is true.  
B) ✗ Equality comparison is valid for categorical data.  
C) ✗ No implicit ordering is true for categorical data.  
D) ✓ Arithmetic operations are not meaningful for categorical data.  

**Correct:** D


#### 9. When considering spatial fields, what is the primary difference between scalar, vector, and tensor attributes?  
A) ✗ Tensors apply in multiple dimensions, not only 2D.  
B) ✓ Scalars have one value per cell; vectors have multiple; tensors have many complex values.  
C) ✗ Vectors represent direction and magnitude.  
D) ✗ This reverses the definitions.  

**Correct:** B


#### 10. Which of the following best describes the role of a conceptual model in data abstraction?  
A) ✗ Programming language is unrelated.  
B) ✗ This describes a data model, not conceptual.  
C) ✗ Conceptual models guide transformation but do not replace it.  
D) ✓ Conceptual models are mental models supporting reasoning about meaning.  

**Correct:** D


#### 11. How does cardinality relate to data abstraction?  
A) ✗ Cardinality refers to counts of unique items or values, not number of attributes.  
B) ✓ Cardinality is the number of unique items or attribute values.  
C) ✗ Programming language choice is unrelated.  
D) ✗ Cardinality applies to all data types, not just quantitative.  

**Correct:** B


#### 12. Which of the following are valid reasons to transform data during the abstraction process?  
A) ✓ Aggregation can be task-driven and valid.  
B) ✗ Converting categorical to quantitative without context is invalid.  
C) ✗ Arbitrary changes to meaning are not valid.  
D) ✓ Normalizing values helps comparison.  

**Correct:** A, D


#### 13. Which of the following statements about derived attributes is true?  
A) ✗ Derived attributes can be more complex, not always simpler.  
B) ✓ They are computed from original data using transformations.  
C) ✗ Derived attributes can be quantitative.  
D) ✓ Sometimes additional data is needed for derivation.  

**Correct:** B, D


#### 14. In the example of temperature data, which of the following conceptual models could be used depending on the task?  
A) ✗ Nominal is not appropriate for temperature in scientific contexts.  
B) ✓ Continuous quantitative for forecasting.  
C) ✓ Categorical for deciding if to leave the house.  
D) ✓ Ordinal for deciding if bath water is ready.  

**Correct:** B, C, D


#### 15. Which of the following best describes the difference between data models and conceptual models?  
A) ✓ Data models are programming types; conceptual models represent semantics and reasoning.  
B) ✗ Both models can be used for visualization and storage.  
C) ✗ This reverses the definitions.  
D) ✗ Conceptual models are not necessarily more precise.  

**Correct:** A


#### 16. Which of the following dataset types can represent hierarchical relationships?  
A) ✓ Networks/graphs, especially trees, represent hierarchies.  
B) ✗ Flat tables do not inherently represent hierarchies.  
C) ✗ Spatial fields represent continuous data, not hierarchies.  
D) ✗ Multidimensional tables do not inherently represent hierarchies.  

**Correct:** A


#### 17. Which of the following statements about spatial collections is correct?  
A) ✗ Lists are ordered and allow duplicates.  
B) ✗ Sets are unordered and do not allow duplicates.  
C) ✗ Spatial collections apply to both 2D and 3D data.  
D) ✓ Clusters group similar items together.  

**Correct:** D


#### 18. When analyzing a large network, why might one use a derived attribute like the Strahler number?  
A) ✗ Visualizing all nodes equally is often impractical.  
B) ✗ Strahler number depends on network structure, not ignoring it.  
C) ✗ It does not convert categorical to quantitative data.  
D) ✓ To focus on the most central or important nodes and reduce complexity.  

**Correct:** D


#### 19. Which of the following is NOT a typical concern when working with spatial fields?  
A) ✗ Interpolation is important for estimating values.  
B) ✗ Sampling locations is a major concern.  
C) ✗ Choosing grid types is important.  
D) ✓ Ensuring all attributes are categorical is not typical; attributes are often continuous.  

**Correct:** D


#### 20. Which of the following statements about the relationship between geometry and visualization is true?  
A) ✓ Visualization treats geometry as a design decision; graphics often take it as given.  
B) ✗ Geometry applies to both 2D and 3D data.  
C) ✗ Visualization does not ignore geometry; it integrates it with attributes.  
D) ✗ Geometry can be designed or modified in visualization.  

**Correct:** A