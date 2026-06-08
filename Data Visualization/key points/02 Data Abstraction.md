## 3. Data Abstraction

## Key Points

#### 1. 📊 Data Meaning and Semantics  
- Data without context has no inherent meaning.  
- Semantics refers to the real-world meaning behind data values.

#### 2. 🧩 Items and Attributes  
- An **item** is an individual, discrete entity (e.g., patient, car, city).  
- An **attribute** is a property measured or observed for an item (e.g., height, horsepower).  
- Items are often called independent variables; attributes are dependent variables.

#### 3. 🔗 Other Data Types  
- **Links** express relationships between two items (e.g., friendships, protein interactions).  
- **Positions** represent spatial data in 2D or 3D (e.g., pixels, latitude/longitude).  
- **Grids** are sampling strategies for continuous data.

#### 4. 🗂️ Dataset Types  
- **Flat tables:** one item per row, columns are attributes, cells hold item-attribute values.  
- **Multidimensional tables:** indexed by multiple keys (e.g., genes by patients).  
- **Networks/graphs:** nodes connected by edges; trees are graphs without cycles.  
- **Spatial fields:** attributes associated with spatial cells, can be scalar, vector, or tensor.  
- **Spatial collections:** sets (unique, unordered), lists (ordered, duplicates allowed), clusters (groups of similar items).

#### 5. 🧮 Attribute Types  
- **Categorical (nominal):** values with no order, only equality comparison.  
- **Ordinal:** values with meaningful order but no consistent difference magnitude.  
- **Quantitative:** values with meaningful magnitude and support arithmetic operations.

#### 6. 🔄 Data Abstraction Process  
- Translate domain-specific data into generic visualization language.  
- Identify dataset types and attribute types.  
- Determine cardinality: number of items, unique attribute values, levels for categorical data, range for quantitative data.  
- Consider data transformation based on task understanding.

#### 7. 🧠 Data Model vs Conceptual Model  
- **Data model:** mathematical abstraction of data (e.g., floats with arithmetic).  
- **Conceptual model:** mental model representing semantics and supporting reasoning.  
- Data abstraction relies on conceptual models to guide data transformation.

#### 8. ⚙️ Derived Attributes  
- Derived attributes are computed from original data via type changes, additional data, or complex transformations.  
- Example: Strahler number is a derived quantitative attribute measuring centrality in trees/networks.



<br>

