## 3. Data Abstraction

## Questions

#### 1. What does the term "semantics" refer to in the context of data?  
A) The mathematical operations that can be performed on data  
B) The real-world meaning behind the data  
C) The format in which data is stored  
D) The programming language used to process data  

#### 2. Which of the following best describes an "item" in a dataset?  
A) A property or characteristic measured about an entity  
B) An individual, discrete entity such as a patient or city  
C) A relationship between two entities  
D) A spatial coordinate in 3D space  

#### 3. Attributes in a dataset are often called "dependent variables" because:  
A) They depend on the programming language used  
B) Their values depend on the item they describe  
C) They are always numerical values  
D) They represent relationships between items  

#### 4. Which of the following are examples of "links" in data?  
A) Latitude and longitude coordinates  
B) Friendship connections on social media  
C) Protein interactions in biology  
D) Temperature readings at different locations  

#### 5. What distinguishes a "flat table" dataset from a "multidimensional table"?  
A) Flat tables have multiple keys indexing data, multidimensional tables do not  
B) Flat tables have one item per row and attributes as columns, multidimensional tables use multiple keys for indexing  
C) Multidimensional tables cannot represent categorical data  
D) Flat tables are only used for spatial data  

#### 6. In a network or graph dataset, which of the following statements are true?  
A) Nodes represent items, and edges represent links between them  
B) A tree is a special type of graph with no cycles  
C) All graphs must be directed  
D) Networks cannot represent hierarchical relationships  

#### 7. Which of the following attribute types allow meaningful arithmetic operations?  
A) Categorical  
B) Ordinal  
C) Quantitative  
D) Nominal  

#### 8. Which of the following is NOT a characteristic of categorical (nominal) data?  
A) Values can be compared for equality  
B) Values have no implicit ordering  
C) Arithmetic operations like addition are meaningful  
D) Categories represent distinct groups  

#### 9. When considering spatial fields, what is the primary difference between scalar, vector, and tensor attributes?  
A) Scalar attributes have multiple values per cell, vectors have one, tensors have none  
B) Scalar attributes have one value per cell, vectors have multiple values, tensors have many values representing complex data  
C) Tensors are only used in 2D data  
D) Vectors cannot represent direction  

#### 10. Which of the following best describes the role of a conceptual model in data abstraction?  
A) It is a mathematical abstraction of data types and operations  
B) It is a mental model that supports reasoning about the meaning of data  
C) It defines the programming language used to process data  
D) It replaces the need for data transformation  

#### 11. How does cardinality relate to data abstraction?  
A) It refers to the number of attributes in a dataset  
B) It refers to the number of unique items or values in a dataset or attribute  
C) It is only relevant for quantitative data  
D) It determines the programming language used  

#### 12. Which of the following are valid reasons to transform data during the abstraction process?  
A) To normalize values for better comparison  
B) To change the conceptual meaning of the data arbitrarily  
C) To aggregate data based on task requirements  
D) To convert categorical data into quantitative data without context  

#### 13. Which of the following statements about derived attributes is true?  
A) Derived attributes are always simpler than original attributes  
B) Derived attributes can be computed from original data using transformations  
C) Derived attributes require acquiring additional data sometimes  
D) Derived attributes cannot be quantitative  

#### 14. In the example of temperature data, which of the following conceptual models could be used depending on the task?  
A) Treating temperature as continuous quantitative data for weather forecasting  
B) Treating temperature as ordinal data for deciding if bath water is ready  
C) Treating temperature as categorical data for deciding if you should leave the house  
D) Treating temperature as nominal data for scientific calculations  

#### 15. Which of the following best describes the difference between data models and conceptual models?  
A) Data models are mental constructions, conceptual models are mathematical abstractions  
B) Data models are programming language types, conceptual models represent semantics and support reasoning  
C) Conceptual models are always more precise than data models  
D) Data models are used only for visualization, conceptual models only for storage  

#### 16. Which of the following dataset types can represent hierarchical relationships?  
A) Flat tables  
B) Networks/graphs, especially trees  
C) Multidimensional tables  
D) Spatial fields  

#### 17. Which of the following statements about spatial collections is correct?  
A) Sets are ordered collections that allow duplicates  
B) Lists are unordered and do not allow duplicates  
C) Clusters group similar items together  
D) Spatial collections only apply to 3D data  

#### 18. When analyzing a large network, why might one use a derived attribute like the Strahler number?  
A) To reduce the dataset size by focusing on the most central nodes  
B) To convert categorical data into quantitative data  
C) To visualize all nodes equally without filtering  
D) To ignore the network structure and focus on attributes only  

#### 19. Which of the following is NOT a typical concern when working with spatial fields?  
A) Sampling locations where attributes are measured  
B) Interpolating attribute values between measured points  
C) Ensuring all attributes are categorical  
D) Choosing appropriate grid types for data representation  

#### 20. Which of the following statements about the relationship between geometry and visualization is true?  
A) Geometry is always fixed and cannot be changed in visualization  
B) Visualization treats geometry as a design decision, while computer graphics often take geometry as given  
C) Geometry only applies to 3D data, not 2D  
D) Visualization ignores geometry and focuses only on attribute values



<br>

## Answers

#### 1. What does the term "semantics" refer to in the context of data?  
A) ✗ Semantics is about meaning, not operations.  
B) ✓ Semantics is the real-world meaning behind data.  
C) ✗ Format is not semantics.  
D) ✗ Programming language is unrelated to semantics.  

**Correct:** B


#### 2. Which of the following best describes an "item" in a dataset?  
A) ✗ This describes an attribute, not an item.  
B) ✓ An item is an individual entity like a patient or city.  
C) ✗ Links describe relationships, not items.  
D) ✗ Positions are spatial data, not items.  

**Correct:** B


#### 3. Attributes in a dataset are often called "dependent variables" because:  
A) ✗ Programming language is irrelevant here.  
B) ✓ Attributes depend on the item they describe.  
C) ✗ Attributes can be categorical or non-numerical.  
D) ✗ Attributes are properties, not relationships.  

**Correct:** B


#### 4. Which of the following are examples of "links" in data?  
A) ✗ Coordinates are positions, not links.  
B) ✓ Friendships are relationships, so links.  
C) ✓ Protein interactions are links between items.  
D) ✗ Temperature readings are attribute values, not links.  

**Correct:** B, C


#### 5. What distinguishes a "flat table" dataset from a "multidimensional table"?  
A) ✗ Flat tables do not have multiple keys.  
B) ✓ Flat tables have one key per row; multidimensional tables use multiple keys.  
C) ✗ Multidimensional tables can represent categorical data.  
D) ✗ Flat tables are not limited to spatial data.  

**Correct:** B


#### 6. In a network or graph dataset, which of the following statements are true?  
A) ✓ Nodes are items; edges are links.  
B) ✓ Trees are graphs without cycles.  
C) ✗ Graphs can be directed or undirected.  
D) ✗ Networks can represent hierarchies (e.g., trees).  

**Correct:** A, B


#### 7. Which of the following attribute types allow meaningful arithmetic operations?  
A) ✗ Categorical data does not support arithmetic.  
B) ✗ Ordinal data has order but no meaningful arithmetic.  
C) ✓ Quantitative data supports arithmetic operations.  
D) ✗ Nominal is another term for categorical, no arithmetic.  

**Correct:** C


#### 8. Which of the following is NOT a characteristic of categorical (nominal) data?  
A) ✗ Equality comparison is valid for categorical data.  
B) ✗ No implicit ordering is true for categorical data.  
C) ✓ Arithmetic operations are not meaningful for categorical data.  
D) ✗ Categories represent distinct groups, which is true.  

**Correct:** C


#### 9. When considering spatial fields, what is the primary difference between scalar, vector, and tensor attributes?  
A) ✗ This reverses the definitions.  
B) ✓ Scalars have one value per cell; vectors have multiple; tensors have many complex values.  
C) ✗ Tensors apply in multiple dimensions, not only 2D.  
D) ✗ Vectors represent direction and magnitude.  

**Correct:** B


#### 10. Which of the following best describes the role of a conceptual model in data abstraction?  
A) ✗ This describes a data model, not conceptual.  
B) ✓ Conceptual models are mental models supporting reasoning about meaning.  
C) ✗ Programming language is unrelated.  
D) ✗ Conceptual models guide transformation but do not replace it.  

**Correct:** B


#### 11. How does cardinality relate to data abstraction?  
A) ✗ Cardinality refers to counts of unique items or values, not number of attributes.  
B) ✓ Cardinality is the number of unique items or attribute values.  
C) ✗ Cardinality applies to all data types, not just quantitative.  
D) ✗ Programming language choice is unrelated.  

**Correct:** B


#### 12. Which of the following are valid reasons to transform data during the abstraction process?  
A) ✓ Normalizing values helps comparison.  
B) ✗ Arbitrary changes to meaning are not valid.  
C) ✓ Aggregation can be task-driven and valid.  
D) ✗ Converting categorical to quantitative without context is invalid.  

**Correct:** A, C


#### 13. Which of the following statements about derived attributes is true?  
A) ✗ Derived attributes can be more complex, not always simpler.  
B) ✓ They are computed from original data using transformations.  
C) ✓ Sometimes additional data is needed for derivation.  
D) ✗ Derived attributes can be quantitative.  

**Correct:** B, C


#### 14. In the example of temperature data, which of the following conceptual models could be used depending on the task?  
A) ✓ Continuous quantitative for forecasting.  
B) ✓ Ordinal for deciding if bath water is ready.  
C) ✓ Categorical for deciding if to leave the house.  
D) ✗ Nominal is not appropriate for temperature in scientific contexts.  

**Correct:** A, B, C


#### 15. Which of the following best describes the difference between data models and conceptual models?  
A) ✗ This reverses the definitions.  
B) ✓ Data models are programming types; conceptual models represent semantics and reasoning.  
C) ✗ Conceptual models are not necessarily more precise.  
D) ✗ Both models can be used for visualization and storage.  

**Correct:** B


#### 16. Which of the following dataset types can represent hierarchical relationships?  
A) ✗ Flat tables do not inherently represent hierarchies.  
B) ✓ Networks/graphs, especially trees, represent hierarchies.  
C) ✗ Multidimensional tables do not inherently represent hierarchies.  
D) ✗ Spatial fields represent continuous data, not hierarchies.  

**Correct:** B


#### 17. Which of the following statements about spatial collections is correct?  
A) ✗ Sets are unordered and do not allow duplicates.  
B) ✗ Lists are ordered and allow duplicates.  
C) ✓ Clusters group similar items together.  
D) ✗ Spatial collections apply to both 2D and 3D data.  

**Correct:** C


#### 18. When analyzing a large network, why might one use a derived attribute like the Strahler number?  
A) ✓ To focus on the most central or important nodes and reduce complexity.  
B) ✗ It does not convert categorical to quantitative data.  
C) ✗ Visualizing all nodes equally is often impractical.  
D) ✗ Strahler number depends on network structure, not ignoring it.  

**Correct:** A


#### 19. Which of the following is NOT a typical concern when working with spatial fields?  
A) ✗ Sampling locations is a major concern.  
B) ✗ Interpolation is important for estimating values.  
C) ✓ Ensuring all attributes are categorical is not typical; attributes are often continuous.  
D) ✗ Choosing grid types is important.  

**Correct:** C


#### 20. Which of the following statements about the relationship between geometry and visualization is true?  
A) ✗ Geometry can be designed or modified in visualization.  
B) ✓ Visualization treats geometry as a design decision; graphics often take it as given.  
C) ✗ Geometry applies to both 2D and 3D data.  
D) ✗ Visualization does not ignore geometry; it integrates it with attributes.  

**Correct:** B