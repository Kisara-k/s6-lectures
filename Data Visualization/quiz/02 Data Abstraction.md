## 3. Data Abstraction

## Questions

#### 1. What does the term "semantics" refer to in the context of data?  
A) The format in which data is stored  
B) The mathematical operations that can be performed on data  
C) The real-world meaning behind the data  
D) The programming language used to process data  

#### 2. Which of the following best describes an "item" in a dataset?  
A) A spatial coordinate in 3D space  
B) An individual, discrete entity such as a patient or city  
C) A property or characteristic measured about an entity  
D) A relationship between two entities  

#### 3. Attributes in a dataset are often called "dependent variables" because:  
A) They represent relationships between items  
B) They are always numerical values  
C) Their values depend on the item they describe  
D) They depend on the programming language used  

#### 4. Which of the following are examples of "links" in data?  
A) Friendship connections on social media  
B) Temperature readings at different locations  
C) Latitude and longitude coordinates  
D) Protein interactions in biology  

#### 5. What distinguishes a "flat table" dataset from a "multidimensional table"?  
A) Flat tables are only used for spatial data  
B) Flat tables have one item per row and attributes as columns, multidimensional tables use multiple keys for indexing  
C) Multidimensional tables cannot represent categorical data  
D) Flat tables have multiple keys indexing data, multidimensional tables do not  

#### 6. In a network or graph dataset, which of the following statements are true?  
A) Nodes represent items, and edges represent links between them  
B) A tree is a special type of graph with no cycles  
C) Networks cannot represent hierarchical relationships  
D) All graphs must be directed  

#### 7. Which of the following attribute types allow meaningful arithmetic operations?  
A) Quantitative  
B) Categorical  
C) Nominal  
D) Ordinal  

#### 8. Which of the following is NOT a characteristic of categorical (nominal) data?  
A) Categories represent distinct groups  
B) Arithmetic operations like addition are meaningful  
C) Values have no implicit ordering  
D) Values can be compared for equality  

#### 9. When considering spatial fields, what is the primary difference between scalar, vector, and tensor attributes?  
A) Vectors cannot represent direction  
B) Scalar attributes have multiple values per cell, vectors have one, tensors have none  
C) Scalar attributes have one value per cell, vectors have multiple values, tensors have many values representing complex data  
D) Tensors are only used in 2D data  

#### 10. Which of the following best describes the role of a conceptual model in data abstraction?  
A) It is a mental model that supports reasoning about the meaning of data  
B) It is a mathematical abstraction of data types and operations  
C) It defines the programming language used to process data  
D) It replaces the need for data transformation  

#### 11. How does cardinality relate to data abstraction?  
A) It is only relevant for quantitative data  
B) It refers to the number of attributes in a dataset  
C) It determines the programming language used  
D) It refers to the number of unique items or values in a dataset or attribute  

#### 12. Which of the following are valid reasons to transform data during the abstraction process?  
A) To normalize values for better comparison  
B) To convert categorical data into quantitative data without context  
C) To change the conceptual meaning of the data arbitrarily  
D) To aggregate data based on task requirements  

#### 13. Which of the following statements about derived attributes is true?  
A) Derived attributes are always simpler than original attributes  
B) Derived attributes require acquiring additional data sometimes  
C) Derived attributes cannot be quantitative  
D) Derived attributes can be computed from original data using transformations  

#### 14. In the example of temperature data, which of the following conceptual models could be used depending on the task?  
A) Treating temperature as categorical data for deciding if you should leave the house  
B) Treating temperature as continuous quantitative data for weather forecasting  
C) Treating temperature as nominal data for scientific calculations  
D) Treating temperature as ordinal data for deciding if bath water is ready  

#### 15. Which of the following best describes the difference between data models and conceptual models?  
A) Conceptual models are always more precise than data models  
B) Data models are used only for visualization, conceptual models only for storage  
C) Data models are programming language types, conceptual models represent semantics and support reasoning  
D) Data models are mental constructions, conceptual models are mathematical abstractions  

#### 16. Which of the following dataset types can represent hierarchical relationships?  
A) Spatial fields  
B) Flat tables  
C) Multidimensional tables  
D) Networks/graphs, especially trees  

#### 17. Which of the following statements about spatial collections is correct?  
A) Clusters group similar items together  
B) Sets are ordered collections that allow duplicates  
C) Lists are unordered and do not allow duplicates  
D) Spatial collections only apply to 3D data  

#### 18. When analyzing a large network, why might one use a derived attribute like the Strahler number?  
A) To visualize all nodes equally without filtering  
B) To ignore the network structure and focus on attributes only  
C) To reduce the dataset size by focusing on the most central nodes  
D) To convert categorical data into quantitative data  

#### 19. Which of the following is NOT a typical concern when working with spatial fields?  
A) Ensuring all attributes are categorical  
B) Sampling locations where attributes are measured  
C) Interpolating attribute values between measured points  
D) Choosing appropriate grid types for data representation  

#### 20. Which of the following statements about the relationship between geometry and visualization is true?  
A) Geometry is always fixed and cannot be changed in visualization  
B) Visualization treats geometry as a design decision, while computer graphics often take geometry as given  
C) Geometry only applies to 3D data, not 2D  
D) Visualization ignores geometry and focuses only on attribute values



<br>

## Answers

#### 1. What does the term "semantics" refer to in the context of data?  
A) ✗ Format is not semantics.  
B) ✗ Semantics is about meaning, not operations.  
C) ✓ Semantics is the real-world meaning behind data.  
D) ✗ Programming language is unrelated to semantics.  

**Correct:** C


#### 2. Which of the following best describes an "item" in a dataset?  
A) ✗ Positions are spatial data, not items.  
B) ✓ An item is an individual entity like a patient or city.  
C) ✗ This describes an attribute, not an item.  
D) ✗ Links describe relationships, not items.  

**Correct:** B


#### 3. Attributes in a dataset are often called "dependent variables" because:  
A) ✗ Attributes are properties, not relationships.  
B) ✗ Attributes can be categorical or non-numerical.  
C) ✓ Attributes depend on the item they describe.  
D) ✗ Programming language is irrelevant here.  

**Correct:** C


#### 4. Which of the following are examples of "links" in data?  
A) ✓ Friendships are relationships, so links.  
B) ✗ Temperature readings are attribute values, not links.  
C) ✗ Coordinates are positions, not links.  
D) ✓ Protein interactions are links between items.  

**Correct:** A, D


#### 5. What distinguishes a "flat table" dataset from a "multidimensional table"?  
A) ✗ Flat tables are not limited to spatial data.  
B) ✓ Flat tables have one key per row; multidimensional tables use multiple keys.  
C) ✗ Multidimensional tables can represent categorical data.  
D) ✗ Flat tables do not have multiple keys.  

**Correct:** B


#### 6. In a network or graph dataset, which of the following statements are true?  
A) ✓ Nodes are items; edges are links.  
B) ✓ Trees are graphs without cycles.  
C) ✗ Networks can represent hierarchies (e.g., trees).  
D) ✗ Graphs can be directed or undirected.  

**Correct:** A, B


#### 7. Which of the following attribute types allow meaningful arithmetic operations?  
A) ✓ Quantitative data supports arithmetic operations.  
B) ✗ Categorical data does not support arithmetic.  
C) ✗ Nominal is another term for categorical, no arithmetic.  
D) ✗ Ordinal data has order but no meaningful arithmetic.  

**Correct:** A


#### 8. Which of the following is NOT a characteristic of categorical (nominal) data?  
A) ✗ Categories represent distinct groups, which is true.  
B) ✓ Arithmetic operations are not meaningful for categorical data.  
C) ✗ No implicit ordering is true for categorical data.  
D) ✗ Equality comparison is valid for categorical data.  

**Correct:** B


#### 9. When considering spatial fields, what is the primary difference between scalar, vector, and tensor attributes?  
A) ✗ Vectors represent direction and magnitude.  
B) ✗ This reverses the definitions.  
C) ✓ Scalars have one value per cell; vectors have multiple; tensors have many complex values.  
D) ✗ Tensors apply in multiple dimensions, not only 2D.  

**Correct:** C


#### 10. Which of the following best describes the role of a conceptual model in data abstraction?  
A) ✓ Conceptual models are mental models supporting reasoning about meaning.  
B) ✗ This describes a data model, not conceptual.  
C) ✗ Programming language is unrelated.  
D) ✗ Conceptual models guide transformation but do not replace it.  

**Correct:** A


#### 11. How does cardinality relate to data abstraction?  
A) ✗ Cardinality applies to all data types, not just quantitative.  
B) ✗ Cardinality refers to counts of unique items or values, not number of attributes.  
C) ✗ Programming language choice is unrelated.  
D) ✓ Cardinality is the number of unique items or attribute values.  

**Correct:** D


#### 12. Which of the following are valid reasons to transform data during the abstraction process?  
A) ✓ Normalizing values helps comparison.  
B) ✗ Converting categorical to quantitative without context is invalid.  
C) ✗ Arbitrary changes to meaning are not valid.  
D) ✓ Aggregation can be task-driven and valid.  

**Correct:** A, D


#### 13. Which of the following statements about derived attributes is true?  
A) ✗ Derived attributes can be more complex, not always simpler.  
B) ✓ Sometimes additional data is needed for derivation.  
C) ✗ Derived attributes can be quantitative.  
D) ✓ They are computed from original data using transformations.  

**Correct:** B, D


#### 14. In the example of temperature data, which of the following conceptual models could be used depending on the task?  
A) ✓ Categorical for deciding if to leave the house.  
B) ✓ Continuous quantitative for forecasting.  
C) ✗ Nominal is not appropriate for temperature in scientific contexts.  
D) ✓ Ordinal for deciding if bath water is ready.  

**Correct:** A, B, D


#### 15. Which of the following best describes the difference between data models and conceptual models?  
A) ✗ Conceptual models are not necessarily more precise.  
B) ✗ Both models can be used for visualization and storage.  
C) ✓ Data models are programming types; conceptual models represent semantics and reasoning.  
D) ✗ This reverses the definitions.  

**Correct:** C


#### 16. Which of the following dataset types can represent hierarchical relationships?  
A) ✗ Spatial fields represent continuous data, not hierarchies.  
B) ✗ Flat tables do not inherently represent hierarchies.  
C) ✗ Multidimensional tables do not inherently represent hierarchies.  
D) ✓ Networks/graphs, especially trees, represent hierarchies.  

**Correct:** D


#### 17. Which of the following statements about spatial collections is correct?  
A) ✓ Clusters group similar items together.  
B) ✗ Sets are unordered and do not allow duplicates.  
C) ✗ Lists are ordered and allow duplicates.  
D) ✗ Spatial collections apply to both 2D and 3D data.  

**Correct:** A


#### 18. When analyzing a large network, why might one use a derived attribute like the Strahler number?  
A) ✗ Visualizing all nodes equally is often impractical.  
B) ✗ Strahler number depends on network structure, not ignoring it.  
C) ✓ To focus on the most central or important nodes and reduce complexity.  
D) ✗ It does not convert categorical to quantitative data.  

**Correct:** C


#### 19. Which of the following is NOT a typical concern when working with spatial fields?  
A) ✓ Ensuring all attributes are categorical is not typical; attributes are often continuous.  
B) ✗ Sampling locations is a major concern.  
C) ✗ Interpolation is important for estimating values.  
D) ✗ Choosing grid types is important.  

**Correct:** A


#### 20. Which of the following statements about the relationship between geometry and visualization is true?  
A) ✗ Geometry can be designed or modified in visualization.  
B) ✓ Visualization treats geometry as a design decision; graphics often take it as given.  
C) ✗ Geometry applies to both 2D and 3D data.  
D) ✗ Visualization does not ignore geometry; it integrates it with attributes.  

**Correct:** B