## 10. Network and Spatial

## Key Points

#### 1. 🔗 Network Data Basics  
- Networks (graphs) consist of nodes and links, both can have attributes.  
- Trees are a special type of network with no cycles and one parent per node.  

#### 2. 🧩 Network Tasks  
- Topology-based tasks include finding paths, neighbors, centrality, and clusters.  
- Attribute-based tasks involve analyzing node/link attributes like distributions.  
- Combination tasks use both topology and attributes (e.g., find friends-of-friends who like cats).  

#### 3. 🖼️ Node-Link Diagrams  
- Nodes are point marks; links are line marks (straight or arcs).  
- Good layouts minimize edge crossings, node overlaps, drawing area, and edge bends.  
- Good layouts maximize angular distance between edges and maintain aspect ratio.  
- Layout optimization is NP-hard and criteria often conflict.  

#### 4. ⚙️ Force-Directed Placement Algorithm  
- Models links as springs (attraction) and nodes as magnets (repulsion).  
- Iteratively moves nodes to minimize forces until equilibrium.  
- Advantages: good for small, sparse graphs; clusters visible; uniform edge length.  
- Disadvantages: nondeterministic, computationally expensive, poor scalability beyond ~1,000 nodes.  

#### 5. 🔄 Circular Layouts and Arc Diagrams  
- Nodes arranged in a circle or line; node ordering is crucial to reduce edge crossings.  

#### 6. 🔢 Adjacency Matrix Representation  
- Matrix rows and columns represent nodes; cells show presence/strength of links.  
- Good for neighborhood topology tasks but bad for path tracing.  
- Node ordering (reordering) is essential to reveal patterns and reduce clutter.  
- Scales better than node-link for large networks (up to 1,000 nodes, 1 million edges).  

#### 7. 🌳 Tree Visualizations  
- Reingold-Tilford algorithm produces tidy node-link tree drawings.  
- Trees can be visualized in rectilinear or radial layouts.  
- Treemaps use area to encode quantitative attributes at leaf nodes and show hierarchy by containment.  
- Sunburst and Icicle plots show hierarchy implicitly by spatial position (radial and rectilinear respectively).  

#### 8. 🗺️ Spatial Data and Visualizations  
- Spatial data includes geographic or physical location attributes.  
- Common visualizations: choropleth maps, symbol maps, cartograms, dot density maps.  

#### 9. 🌈 Choropleth Maps  
- Use geographic regions colored by quantitative attribute.  
- Require normalization (e.g., by population) to avoid misleading interpretations.  
- Show only one variable at a time.  
- Pros: easy to read, well-established.  
- Cons: region size bias, color choice affects perception.  

#### 10. 📍 Symbol Maps  
- Use symbols placed on geographic locations; size or color encodes data.  
- Mitigate region size bias of choropleths.  
- Cons: symbol overlap and occlusion; complex glyphs need explanation.  

#### 11. 🔄 Cartograms  
- Distort geographic regions so size reflects data values.  
- Contiguous cartograms maintain region adjacency; grid cartograms use uniform shapes in a grid.  
- Pros: highlight size disparities, engaging.  
- Cons: distortion can confuse users; requires familiarity with original geography.  

#### 12. 🔵 Dot Density Maps  
- Represent counts by placing dots, each representing a fixed number of items.  
- Avoid region size bias but hard to extract exact quantities.  
- Rendering many dots can be slow.  
- Normalization is important to avoid misleading patterns.



<br>

