## 10. Network and Spatial

## Questions

#### 1. Which of the following statements about node-link diagrams are TRUE?
A) They can become cluttered with many nodes and edges, especially if edge crossings are not minimized.  
B) They are always deterministic, producing the same layout for the same data every time.  
C) They are best suited for networks with a very high number of nodes and edges (e.g., over 10,000 nodes).  
D) They are intuitive and familiar for most users.  


#### 2. In force-directed placement algorithms for network visualization, which of the following are key characteristics?
A) The layout is optimized to minimize edge crossings and node overlaps.  
B) The algorithm always produces the same layout for the same input data.  
C) Nodes repel each other, while links act like springs pulling connected nodes together.  
D) The algorithm can become computationally expensive as the network size increases.  


#### 3. Which of the following are advantages of adjacency matrix representations for network data?
A) They focus on the presence or absence of edges rather than the spatial position of nodes.  
B) Node ordering within the matrix can significantly affect the clarity of patterns.  
C) They scale well to large networks with many edges.  
D) They are particularly effective for path tracing tasks.  


#### 4. Which of the following are TRUE about treemaps as a visualization technique for trees?
A) They are most effective when encoding quantitative attributes at leaf nodes.  
B) They use area containment to represent hierarchical structure.  
C) They emphasize the explicit connections between parent and child nodes.  
D) They can scale to visualize very large trees with up to a million leaf nodes.  


#### 5. Which of the following are potential disadvantages of choropleth maps?
A) They can mislead if data is not normalized for population or area.  
B) They are limited to showing only one variable at a time.  
C) They are ideal for visualizing precise quantities at specific geographic points.  
D) Large regions may appear more important than small ones, regardless of data values.  


#### 6. Which of the following statements about hybrid network visualizations (such as NodeTrix) are correct?
A) They can help visualize dense clusters within a larger sparse network.  
B) They are only useful for tree structures, not general networks.  
C) They combine node-link diagrams and adjacency matrices to leverage the strengths of both.  
D) They are designed to avoid the "hairball" problem in very large networks.  


#### 7. Which of the following are TRUE about spatial data visualizations?
A) Symbol maps can mitigate the problem of region size bias found in choropleth maps.  
B) Cartograms always preserve the original shapes and positions of regions.  
C) Thematic maps combine geographic reference maps with tabular attribute data.  
D) Dot density maps are effective for showing spatial patterns and clusters.  


#### 8. Which of the following are important considerations when designing a node-link diagram layout?
A) Ensuring that spatial position always encodes a meaningful attribute.  
B) Minimizing edge crossings and node overlaps.  
C) Emphasizing symmetry so that similar structures appear similar.  
D) Maximizing the angular distance between different edges at a node.  


#### 9. Which of the following statements about tree visualization idioms are correct?
A) Radial node-link trees encode depth as distance from the center.  
B) Treemaps use explicit connection marks to show hierarchy.  
C) Rectilinear and radial layouts are two common variants for node-link trees.  
D) Sunburst and icicle plots use spatial position to show parent-child relationships.  


#### 10. Which of the following are TRUE about the scalability of different network and spatial visualization techniques?
A) Treemaps can scale to visualize trees with up to a million leaf nodes.  
B) Adjacency matrices can handle networks with thousands of nodes and millions of edges.  
C) Dot density maps are always preferable for very large datasets due to their performance.  
D) Force-directed node-link diagrams are best suited for small, sparse networks.  



<br>

## Answers

#### 1. Which of the following statements about node-link diagrams are TRUE?
A) ✓ Clutter from edge crossings and overlaps is a known issue, especially in dense networks.  
B) ✗ Node-link diagrams are not deterministic; layouts can vary with each run, especially with force-directed algorithms.  
C) ✗ Node-link diagrams do not scale well to very large networks; they are better for small to medium-sized networks.  
D) ✓ They are intuitive and familiar, making them the most common network visualization.  

**Correct:** A, D


#### 2. In force-directed placement algorithms for network visualization, which of the following are key characteristics?
A) ✓ The layout aims to minimize edge crossings and node overlaps as part of its optimization.  
B) ✗ The algorithm is non-deterministic; different runs can produce different layouts.  
C) ✓ The algorithm models nodes as repelling each other and links as springs pulling connected nodes together.  
D) ✓ Computational expense increases with network size, making it less suitable for large graphs.  

**Correct:** A, C, D


#### 3. Which of the following are advantages of adjacency matrix representations for network data?
A) ✓ Adjacency matrices focus on the presence/absence or strength of edges, not spatial node positions.  
B) ✓ Node ordering is crucial; good ordering can reveal patterns and reduce clutter.  
C) ✓ They scale well to large networks, handling thousands of nodes and millions of edges without edge crossings.  
D) ✗ Adjacency matrices are not ideal for path tracing; node-link diagrams are better for this task.  

**Correct:** A, B, C


#### 4. Which of the following are TRUE about treemaps as a visualization technique for trees?
A) ✓ They are most effective for encoding quantitative attributes at the leaf nodes.  
B) ✓ Treemaps use area containment to represent hierarchical structure.  
C) ✗ Treemaps do not emphasize explicit parent-child connections; they use containment instead.  
D) ✓ Treemaps can scale to very large trees, up to a million leaf nodes.  

**Correct:** A, B, D


#### 5. Which of the following are potential disadvantages of choropleth maps?
A) ✓ Failure to normalize data (e.g., by population) can mislead viewers.  
B) ✓ Choropleth maps are limited to showing one variable at a time for clarity.  
C) ✗ Choropleth maps are not ideal for showing precise quantities at specific points; symbol maps are better for this.  
D) ✓ Large regions can appear more important due to their visual salience, regardless of data.  

**Correct:** A, B, D


#### 6. Which of the following statements about hybrid network visualizations (such as NodeTrix) are correct?
A) ✓ It helps visualize dense clusters within a larger sparse network by using matrices for dense areas.  
B) ✗ NodeTrix is designed for general networks, not just trees.  
C) ✓ NodeTrix combines node-link and matrix representations to leverage both strengths.  
D) ✗ While hybrids can help with readability, they do not fully solve the "hairball" problem in very large networks.  

**Correct:** A, C


#### 7. Which of the following are TRUE about spatial data visualizations?
A) ✓ Symbol maps can reduce region size bias by using symbols rather than area.  
B) ✗ Cartograms distort shapes and positions to encode data, so they do not always preserve original geography.  
C) ✓ Thematic maps combine geographic reference with tabular attribute data.  
D) ✓ Dot density maps are effective for showing spatial patterns and clusters.  

**Correct:** A, C, D


#### 8. Which of the following are important considerations when designing a node-link diagram layout?
A) ✗ Spatial position in node-link diagrams often does not encode a specific attribute; it is usually determined by layout optimization.  
B) ✓ Minimizing edge crossings and node overlaps improves readability.  
C) ✓ Emphasizing symmetry helps similar structures appear similar, aiding interpretation.  
D) ✓ Maximizing angular distance between edges at a node helps distinguish connections.  

**Correct:** B, C, D


#### 9. Which of the following statements about tree visualization idioms are correct?
A) ✓ In radial node-link trees, depth is encoded as distance from the center.  
B) ✗ Treemaps use area containment, not explicit connection marks, to show hierarchy.  
C) ✓ Rectilinear and radial layouts are both common for node-link trees.  
D) ✓ Sunburst and icicle plots use spatial position (not explicit links) to show hierarchy.  

**Correct:** A, C, D


#### 10. Which of the following are TRUE about the scalability of different network and spatial visualization techniques?
A) ✓ Treemaps can scale to trees with up to a million leaf nodes.  
B) ✓ Adjacency matrices can handle very large networks, scaling to thousands of nodes and millions of edges.  
C) ✗ Dot density maps can become slow and hard to interpret with very large datasets; they are not always preferable.  
D) ✓ Force-directed node-link diagrams are best for small, sparse networks due to computational limits.  

**Correct:** A, B, D