## 3. Data Abstraction

## Questions

#### 1. What does the term "semantics" refer to in the context of data abstraction?  
A) The real-world meaning or interpretation of data  
B) The structure or format of the dataset  
C) The mathematical operations that can be performed on data values  
D) The programming language used to store data  

#### 2. Which of the following best describe an "item" in a dataset?  
A) A property or characteristic measured for an entity  
B) An individual, discrete entity such as a patient or city  
C) A spatial position in 2D or 3D space  
D) A relationship between two entities  

#### 3. Which statements about attribute types are true?  
A) Nominal attributes are a type of quantitative attribute  
B) Quantitative attributes have meaningful magnitudes and support arithmetic  
C) Categorical attributes have no implicit ordering but allow equality comparison  
D) Ordinal attributes support meaningful arithmetic operations like addition  

#### 4. In a network or graph dataset, which of the following are true?  
A) Directed edges imply a direction in the relationship  
B) A tree is a graph that may contain cycles  
C) Nodes represent items or entities  
D) Links represent relationships between nodes  

#### 5. Which of the following are examples of spatial data types?  
A) A table of stock prices over time  
B) Pixels in a photo representing color values  
C) Latitude and longitude coordinates of cities  
D) A list of patient names and ages  

#### 6. When performing data abstraction, which considerations are important?  
A) Identifying the dataset and attribute types  
B) Translating domain-specific data into a generic visualization language  
C) Deciding whether to transform data based on the task  
D) Ignoring the cardinality of attributes to simplify processing  

#### 7. How do conceptual models differ from data models?  
A) Data models represent mental constructions supporting reasoning  
B) Conceptual models help interpret the meaning and guide data transformation  
C) Conceptual models are mathematical abstractions of data types  
D) Data models define operations on data like addition and multiplication  

#### 8. Which of the following statements about derived attributes are correct?  
A) They may involve complex transformations or acquiring additional data  
B) They can provide new insights not directly available from original data  
C) Derived attributes can only be created by simple type conversions  
D) Derived attributes are always categorical  

#### 9. Consider a dataset of temperature readings. Which of the following are valid conceptual abstractions depending on the task?  
A) Treating temperature as ordinal for ranking bath water warmth  
B) Treating temperature as categorical for deciding if water is above freezing  
C) Treating temperature as quantitative for weather forecasting  
D) Treating temperature as nominal for arithmetic calculations  

#### 10. Which of the following correctly describe spatial collections?  
A) Sets are ordered collections that allow duplicates  
B) Sets are unordered and contain unique items only  
C) Lists are ordered and can contain duplicates  
D) Clusters group similar items together  



<br>

## Answers

#### 1. What does the term "semantics" refer to in the context of data abstraction?  
A) ✓ Semantics means the real-world meaning or interpretation of data.  
B) ✗ Structure or format is not semantics but data organization.  
C) ✗ Semantics is about meaning, not mathematical operations.  
D) ✗ Programming language is unrelated to semantics.  

**Correct:** A


#### 2. Which of the following best describe an "item" in a dataset?  
A) ✗ This describes an attribute, not an item.  
B) ✓ An item is an individual, discrete entity like a patient or city.  
C) ✗ Positions are spatial data, not items themselves.  
D) ✗ Relationships are links, not items.  

**Correct:** B


#### 3. Which statements about attribute types are true?  
A) ✗ Nominal (categorical) attributes are not quantitative.  
B) ✓ Quantitative attributes have meaningful magnitudes and support arithmetic.  
C) ✓ Categorical attributes allow equality comparison but no ordering.  
D) ✗ Ordinal attributes have order but do not support meaningful arithmetic.  

**Correct:** B, C


#### 4. In a network or graph dataset, which of the following are true?  
A) ✓ Directed edges imply direction in relationships.  
B) ✗ Trees are graphs without cycles, so this is false.  
C) ✓ Nodes represent items or entities.  
D) ✓ Links represent relationships between nodes.  

**Correct:** A, C, D


#### 5. Which of the following are examples of spatial data types?  
A) ✗ Stock prices over time are temporal, not spatial data.  
B) ✓ Pixels represent spatial positions with attribute values (color).  
C) ✓ Latitude and longitude are spatial coordinates.  
D) ✗ A list of names and ages is non-spatial tabular data.  

**Correct:** B, C


#### 6. When performing data abstraction, which considerations are important?  
A) ✓ Identifying dataset and attribute types is essential.  
B) ✓ Translating domain-specific data into generic visualization language is key.  
C) ✓ Deciding on data transformation based on task is important.  
D) ✗ Ignoring cardinality is incorrect; cardinality matters for abstraction.  

**Correct:** A, B, C


#### 7. How do conceptual models differ from data models?  
A) ✗ Data models are mathematical, not mental constructions.  
B) ✓ Conceptual models help interpret meaning and guide transformation.  
C) ✗ Conceptual models are not mathematical abstractions; data models are.  
D) ✓ Data models define operations on data like addition and multiplication.  

**Correct:** B, D


#### 8. Which of the following statements about derived attributes are correct?  
A) ✓ They may involve complex transformations or additional data.  
B) ✓ Derived attributes provide new insights not directly in original data.  
C) ✗ Derived attributes can be more than simple type conversions.  
D) ✗ Derived attributes can be any type, not always categorical.  

**Correct:** A, B


#### 9. Consider a dataset of temperature readings. Which of the following are valid conceptual abstractions depending on the task?  
A) ✓ Ordinal treatment (hot, warm, cold) is valid for ranking warmth.  
B) ✓ Categorical treatment (above/below freezing) is valid for simple decisions.  
C) ✓ Quantitative treatment is valid for weather forecasting.  
D) ✗ Nominal treatment does not support arithmetic and is not suitable here.  

**Correct:** A, B, C


#### 10. Which of the following correctly describe spatial collections?  
A) ✗ Sets are unordered and contain unique items only.  
B) ✓ Sets are unordered and contain unique items only.  
C) ✓ Lists are ordered and can contain duplicates.  
D) ✓ Clusters group similar items together.  

**Correct:** B, C, D