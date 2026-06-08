## 10. Network and Spatial

## Study Notes

### 1. 🌐 Introduction to Network and Spatial Visualizations

When we talk about **network and spatial visualizations**, we are dealing with two types of data that describe relationships and positions. Networks model how things are connected, like social networks or computer networks, while spatial data involves locations and geography, such as maps or sensor data.

Understanding these visualizations helps us analyze complex relationships and spatial patterns effectively. This lecture covers the fundamental concepts, common visualization techniques, and the challenges involved in representing network and spatial data clearly.


### 2. 🔗 Network Data: What It Is and How We Visualize It

#### What is Network Data?

Network data models relationships between entities. These entities are called **nodes** (or vertices), and the connections between them are called **links** (or edges). Networks are also known as **graphs** in mathematics and computer science.

- **Nodes**: The individual items or points in the network (e.g., people in a social network).
- **Links**: The connections or relationships between nodes (e.g., friendships).

A special type of network is a **tree**, which is a hierarchical structure with no cycles, meaning each node has exactly one parent except the root.

#### Tasks in Network Analysis

Network tasks can be divided into two main types:

- **Topology-based tasks**: These focus on the structure of the network.
  - Finding paths between nodes.
  - Identifying neighbors (nodes directly connected).
  - Comparing centrality or importance of nodes.
  - Detecting clusters or communities within the network.

- **Attribute-based tasks**: These focus on the properties or attributes of nodes or links, similar to working with tables.
  - Finding distributions of attributes.
  - Filtering nodes based on attribute values.

- **Combination tasks**: These involve both topology and attributes, such as finding friends-of-friends who like cats.


### 3. 🖼️ Visualizing Network Data: Common Techniques

#### Node-Link Diagrams

The most intuitive and widely used network visualization is the **node-link diagram**:

- **Nodes** are shown as points.
- **Links** are shown as lines or arcs connecting nodes.

This method is familiar and easy to understand but can become cluttered with many nodes or edges.

##### Criteria for Good Node-Link Layouts

A good layout should:

- Minimize edge crossings and node overlaps to reduce clutter.
- Keep topological neighbors close together.
- Use space efficiently.
- Maximize angular separation between edges to improve clarity.
- Emphasize symmetry so similar structures look similar.

However, these criteria often conflict, and finding the perfect layout is computationally hard (NP-hard).

#### Optimization-Based Layouts

To handle layout challenges, algorithms treat the problem as an optimization task, balancing different criteria by assigning weights to them. Common techniques include:

- **Force-directed placement**: Models links as springs pulling nodes together and nodes as magnets repelling each other. The algorithm iteratively adjusts node positions to minimize energy (forces).

#### Force-Directed Placement Algorithm

- Start with nodes placed randomly.
- Calculate forces on each node:
  - Repulsion from all other nodes.
  - Attraction from connected nodes.
- Move nodes according to the net force until equilibrium is reached.

**Advantages**: Good for small, sparse graphs; clusters become visible; edge lengths are fairly uniform.

**Disadvantages**: Non-deterministic (different runs produce different layouts), computationally expensive, and doesn’t scale well beyond about 1,000 nodes.

#### Other Node-Link Layouts

- **Circular layouts**: Nodes arranged in a circle or line, useful for emphasizing ordering but sensitive to node order.
- **Arc diagrams**: Similar to circular layouts but edges are arcs above a line of nodes.

#### Adjacency Matrix Representation

Instead of drawing nodes and links, networks can be represented as a matrix:

- Rows and columns represent nodes.
- Cells indicate the presence or strength of a link between nodes.

**Advantages**:

- Good for understanding neighborhood relationships.
- Scales better for large networks.
- Avoids edge crossings.

**Disadvantages**:

- Not intuitive for path tracing.
- Node ordering is crucial to reduce clutter and reveal patterns.

#### Hybrid Visualizations

Some tools combine node-link diagrams and adjacency matrices to leverage the strengths of both, such as **NodeTrix**, which uses matrices for dense clusters and node-link for sparse parts.


### 4. 🌳 Trees: A Special Network Case

Trees are hierarchical networks with no cycles, often visualized differently to emphasize parent-child relationships.

#### Node-Link Trees

- Use layouts like **Reingold-Tilford** for tidy, compact drawings.
- Variants include **rectilinear** (straight lines) and **radial** (nodes arranged in circles around the root).
- Radial layouts encode depth by distance from the center and sibling relationships by angular proximity.

#### Treemaps and Other Containment Visualizations

- Treemaps use **area** to represent quantitative attributes at leaf nodes.
- They show hierarchy by nesting rectangles inside parent rectangles.
- Useful for tasks like visualizing disk space usage.

#### Implicit Tree Layouts

- **Sunburst** and **Icicle plots** show hierarchy through spatial position rather than explicit links.
- Sunburst uses radial layout; icicle uses rectilinear.
- These layouts emphasize depth and sibling order.


### 5. 🏙️ Spatial Data and Its Visualization

#### What is Spatial Data?

Spatial data includes any data with a geographic or physical location component. This data is visualized to understand spatial relationships and patterns.

Examples include:

- Geographic maps.
- Sensor data.
- Simulation outputs.

#### Common Spatial Visualizations

- **Choropleth maps**: Color-coded regions representing quantitative data.
- **Symbol maps**: Use symbols (e.g., circles) placed on locations, sized or colored by attribute.
- **Cartograms**: Distort geographic regions to reflect data values.
- **Dot density maps**: Use dots to represent counts or density of phenomena.


### 6. 🗺️ Choropleth Maps: Visualizing Data by Region

Choropleth maps color geographic regions (like states or countries) based on a quantitative attribute.

- Use the actual geographic shapes for regions.
- Color intensity or hue encodes the attribute value.

**Important considerations**:

- Normalize data by population or area to avoid misleading interpretations (e.g., total population vs. population density).
- Use only one variable at a time.
- Choose color scales carefully to avoid bias.

**Pros**:

- Easy to understand.
- Well-established and widely used.

**Cons**:

- Larger regions may appear more important regardless of data.
- Color choice heavily influences perception.


### 7. 📍 Symbol Maps and Cartograms

#### Symbol Maps

- Place symbols (e.g., circles) on geographic locations.
- Symbol size or color encodes data values.
- Can use glyphs (complex symbols) for multivariate data.

**Pros**:

- Mitigate region size bias.
- Intuitive for showing quantities at points.

**Cons**:

- Symbols can overlap or occlude map details.
- Complex glyphs may require explanation.

#### Cartograms

- Distort geographic regions so their size reflects a data attribute.
- **Contiguous cartograms** keep regions connected but distort shapes.
- **Grid cartograms** use uniform shapes arranged in a grid approximating spatial layout.

**Pros**:

- Engaging and highlight disparities.
- Useful when size differences are important.

**Cons**:

- Distortion can confuse users.
- Requires familiarity with original geography.
- Difficult to extract exact values.


### 8. 🔵 Dot Density Maps: Showing Distribution with Dots

Dot density maps place dots randomly or systematically within regions to represent counts of a phenomenon.

- Each dot represents a fixed number of items.
- Color can encode additional attributes.

**Pros**:

- Avoid problems of region size bias.
- Easy to understand spatial distribution and clustering.

**Cons**:

- Difficult to extract precise quantities.
- Rendering many dots can be slow.
- Like choropleths, normalization is important to avoid misleading patterns.


### Summary

Network and spatial visualizations are powerful tools for understanding complex relationships and geographic patterns. Networks focus on connections and topology, visualized through node-link diagrams, adjacency matrices, and trees. Spatial data relies on geographic position, visualized through maps like choropleths, symbol maps, cartograms, and dot density maps.

Each visualization method has strengths and weaknesses, and choosing the right one depends on the data, tasks, and scale. Understanding these fundamentals helps create clear, insightful visualizations that reveal meaningful patterns.