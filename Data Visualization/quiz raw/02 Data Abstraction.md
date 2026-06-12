## 3. Data Abstraction

## Questions

#### 1. What distinguishes an item from an attribute in data abstraction?  
A) Items correspond to rows in a flat table, attributes correspond to columns  
B) An attribute is always independent, while an item is dependent  
C) Items represent dependent variables, attributes represent independent variables  
D) An item is a discrete entity, while an attribute is a property measured or observed about that entity  

#### 2. Which of the following are valid dataset types in visualization data abstraction?  
A) Flat tables with one item per row and attributes as columns  
B) Networks or graphs with nodes and edges  
C) Multidimensional tables indexed by multiple keys  
D) Conceptual models representing mental constructions  

#### 3. How do spatial fields differ from spatial collections in data abstraction?  
A) Spatial fields always represent categorical data  
B) Spatial collections require explicit spatial positions for each item  
C) Spatial fields associate attribute values with cells in a continuous domain  
D) Spatial collections group discrete items into sets, lists, or clusters  

#### 4. Which statements about attribute types are correct?  
A) Ordinal attributes define a meaningful less/greater relationship but no arithmetic operations  
B) All attribute types can be treated identically in visualization design  
C) Categorical attributes have no implicit ordering and only support equality comparison  
D) Quantitative attributes support meaningful arithmetic and magnitude comparisons  

#### 5. What are the key operations involved in data abstraction for visualization?  
A) Determining cardinality and range of attributes  
B) Translating domain-specific data into a generic visualization language  
C) Automatically generating conceptual models from raw data  
D) Identifying dataset and attribute types  

#### 6. Which of the following best describe the relationship between data models and conceptual models?  
A) Data models include semantics and task understanding, conceptual models do not  
B) Data abstraction relies on conceptual models to guide data transformation for visualization tasks  
C) Conceptual models are always derived directly from data models without transformation  
D) Data models are mathematical abstractions, while conceptual models represent mental constructs supporting reasoning  

#### 7. Consider the example of temperature data represented as floats. Which of the following are valid conceptual abstractions depending on task?  
A) Categorizing temperature as ordinal data with labels like hot, warm, cold for general description  
B) Treating temperature as quantitative data with continuous values for weather forecasting  
C) Always treating temperature as nominal categorical data regardless of context  
D) Using temperature as categorical data with binary states like above freezing or below freezing for decision making  

#### 8. Which of the following statements about derived attributes is true?  
A) Derived attributes can be computed by simple type changes or complex transformations  
B) Derived attributes always require acquiring additional external data  
C) Derived attributes are never quantitative  
D) Using Strahler numbers as a centrality metric in trees is an example of a derived quantitative attribute  

#### 9. In the context of networks/graphs as dataset types, which statements are accurate?  
A) Graphs always represent spatial data with explicit positions  
B) Trees are a special case of graphs with no cycles and often have roots and direction  
C) Nodes represent items, and edges represent links or relationships between items  
D) Networks cannot represent attributes associated with nodes or edges  

#### 10. Which of the following are important considerations when working with spatial fields?  
A) Sampling strategy: where attribute values are measured or simulated  
B) Interpolation: how to estimate attribute values at unmeasured locations  
C) Ensuring all spatial fields are represented as unordered sets of items  
D) Grid types and the number of attributes per cell (scalar, vector, tensor)  



<br>

## Answers

#### 1. What distinguishes an item from an attribute in data abstraction?  
A) ✓ Items correspond to rows, attributes to columns in flat tables  
B) ✗ Attribute is dependent, not always independent; this reverses roles  
C) ✗ Items are independent variables, attributes are dependent, so this is reversed  
D) ✓ Item is a discrete entity; attribute is a property measured or observed about that entity  

**Correct:** A, D


#### 2. Which of the following are valid dataset types in visualization data abstraction?  
A) ✓ Flat tables with one item per row and attributes as columns are a basic dataset type  
B) ✓ Networks or graphs with nodes and edges are recognized dataset types  
C) ✓ Multidimensional tables indexed by multiple keys are valid dataset types  
D) ✗ Conceptual models are mental constructs, not dataset types  

**Correct:** A, B, C


#### 3. How do spatial fields differ from spatial collections in data abstraction?  
A) ✗ Spatial fields do not always represent categorical data; they often represent continuous scalar/vector/tensor data  
B) ✗ Spatial collections do not require explicit spatial positions for each item necessarily  
C) ✓ Spatial fields associate attribute values with cells in a continuous domain  
D) ✓ Spatial collections group discrete items into sets, lists, or clusters  

**Correct:** C, D


#### 4. Which statements about attribute types are correct?  
A) ✓ Ordinal attributes define ordering but do not support arithmetic  
B) ✗ Attribute types differ and cannot be treated identically in visualization design  
C) ✓ Categorical attributes have no implicit ordering and only support equality comparison  
D) ✓ Quantitative attributes support meaningful arithmetic and magnitude comparisons  

**Correct:** A, C, D


#### 5. What are the key operations involved in data abstraction for visualization?  
A) ✓ Determining cardinality and range of attributes is part of abstraction  
B) ✓ Translating domain-specific data into generic visualization language is fundamental  
C) ✗ Automatically generating conceptual models is not part of data abstraction operations  
D) ✓ Identifying dataset and attribute types is essential  

**Correct:** A, B, D


#### 6. Which of the following best describe the relationship between data models and conceptual models?  
A) ✗ Data models do not include semantics or task understanding; conceptual models do  
B) ✓ Data abstraction relies on conceptual models to guide data transformation for visualization tasks  
C) ✗ Conceptual models often require transformation and are not always directly derived without change  
D) ✓ Data models are mathematical abstractions; conceptual models are mental constructs supporting reasoning  

**Correct:** B, D


#### 7. Consider the example of temperature data represented as floats. Which of the following are valid conceptual abstractions depending on task?  
A) ✓ Categorizing temperature as ordinal (hot, warm, cold) is a valid abstraction for some tasks  
B) ✓ Treating temperature as quantitative data for forecasting is valid  
C) ✗ Always treating temperature as nominal categorical ignores task context and is incorrect  
D) ✓ Using temperature as categorical (above/below freezing) is valid for decision tasks  

**Correct:** A, B, D


#### 8. Which of the following statements about derived attributes is true?  
A) ✓ Derived attributes can be simple type changes or complex transformations  
B) ✗ Derived attributes do not always require additional external data  
C) ✗ Derived attributes can be quantitative, as in the Strahler number example  
D) ✓ Strahler numbers as a centrality metric are an example of a derived quantitative attribute  

**Correct:** A, D


#### 9. In the context of networks/graphs as dataset types, which statements are accurate?  
A) ✗ Graphs do not always represent spatial data with explicit positions  
B) ✓ Trees are special graphs with no cycles, often rooted and directed  
C) ✓ Nodes represent items; edges represent links or relationships  
D) ✗ Networks can represent attributes on nodes and edges  

**Correct:** B, C


#### 10. Which of the following are important considerations when working with spatial fields?  
A) ✓ Sampling strategy is critical for where attributes are measured or simulated  
B) ✓ Interpolation is important to estimate values at unmeasured locations  
C) ✗ Spatial fields are not unordered sets; they are structured grids or continuous domains  
D) ✓ Grid types and attribute dimensionality (scalar, vector, tensor) matter  

**Correct:** A, B, D