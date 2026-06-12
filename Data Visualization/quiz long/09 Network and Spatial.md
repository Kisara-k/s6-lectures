## 10. Network and Spatial

## Questions

#### 1. Which of the following are true about network nodes and links?  
A) Links can have attributes, but nodes cannot.  
B) In all networks, nodes must have at least two links.  
C) A tree is a special type of network with no cycles and exactly one parent per node.  
D) Nodes represent entities, and links represent relationships between nodes.  


#### 2. Which tasks are considered topology-based in network analysis?  
A) Finding shortest paths between nodes.  
B) Comparing centrality measures of nodes.  
C) Identifying clusters or communities.  
D) Finding the distribution of node attributes.  


#### 3. In force-directed placement algorithms, which of the following statements are correct?  
A) Nodes repel each other like magnets.  
B) It scales efficiently to networks with over 10,000 nodes without performance issues.  
C) The algorithm always produces the same layout for the same network.  
D) Links act like springs pulling connected nodes together.  


#### 4. What are the main challenges in creating good node-link layouts?  
A) Minimizing angular distance between edges.  
B) Emphasizing symmetry so similar structures look similar.  
C) Minimizing edge crossings and node overlaps.  
D) Maximizing the total drawing area to avoid clutter.  


#### 5. Which of the following are advantages of adjacency matrix representations over node-link diagrams?  
A) Better scalability for large networks.  
B) Easier path tracing between nodes.  
C) Avoidance of edge crossings.  
D) Intuitive understanding for users with no training.  


#### 6. Why is node ordering crucial in adjacency matrix visualizations?  
A) It determines the color scheme used.  
B) It affects the interpretability of neighborhood relationships.  
C) It minimizes edge crossings and reveals clusters.  
D) It reduces the number of nodes displayed.  


#### 7. Which statements about circular layouts and arc diagrams are true?  
A) They are best suited for networks with no attributes.  
B) They are a type of restricted node-link layout.  
C) Nodes are arranged around a circle or along a line.  
D) Node ordering does not affect the clarity of the layout.  


#### 8. What are the key differences between trees and general networks?  
A) Each node in a tree has exactly one parent except the root.  
B) Trees always have a radial layout.  
C) Trees have no cycles, while general networks may have cycles.  
D) Trees cannot have attributes on nodes or links.  


#### 9. Which of the following are true about treemaps?  
A) They use containment to show hierarchical structure.  
B) They use area to encode quantitative attributes at leaf nodes.  
C) They emphasize topology and path tracing.  
D) They are suitable for visualizing millions of leaf nodes.  


#### 10. When is a choropleth map an appropriate visualization choice?  
A) When the central task is understanding spatial relationships.  
B) When multiple variables need to be shown simultaneously.  
C) When raw counts are more important than normalized data.  
D) When regions are roughly equal in size.  


#### 11. What are common pitfalls when using choropleth maps?  
A) Using choropleth maps for non-spatial data.  
B) Using absolute counts without normalization.  
C) Choosing color palettes without considering perceptual effects.  
D) Showing multiple variables on the same map.  


#### 12. Which of the following statements about symbol maps are correct?  
A) Symbols never overlap or occlude map details.  
B) Symbol maps always preserve the original spatial geometry.  
C) Glyphs can represent multivariate data.  
D) Symbol size can encode quantitative attributes.  


#### 13. What are the main differences between contiguous cartograms and grid cartograms?  
A) Grid cartograms preserve exact geographic shapes.  
B) Contiguous cartograms are easier to interpret than grid cartograms.  
C) Grid cartograms use uniform-sized shapes arranged in a grid.  
D) Contiguous cartograms maintain region adjacency but distort shapes.  


#### 14. Which of the following are advantages of dot density maps?  
A) They make it easy to extract exact quantities.  
B) They perform well even with very large datasets.  
C) They avoid problems related to region size bias.  
D) They clearly show spatial clustering patterns.  


#### 15. In network visualizations, what does the term “hairball problem” refer to?  
A) The difficulty of interpreting very dense networks with many overlapping edges.  
B) The inability to display node attributes.  
C) The problem of nodes having multiple parents in trees.  
D) The challenge of scaling adjacency matrices beyond 1,000 nodes.  


#### 16. Which of the following statements about hierarchical edge bundling are true?  
A) It reduces edge clutter by grouping edges with similar source and destination.  
B) It can be applied to any layout of a compound network.  
C) It emphasizes attribute values at leaf nodes.  
D) It only works for radial layouts.  


#### 17. Why might force-directed layouts produce arbitrary spatial positions for nodes?  
A) Because node positions are fixed by their attributes.  
B) Because spatial position encodes no direct meaning and is optimized to reduce crossings.  
C) Because the layout is deterministic and reproducible.  
D) Because the algorithm always places nodes in a grid.  


#### 18. Which of the following are true about the scalability of different network visualization techniques?  
A) Treemaps can visualize up to a million leaf nodes efficiently.  
B) Force-directed layouts become computationally expensive beyond about 1,000 nodes.  
C) Adjacency matrices can handle networks with thousands of nodes and millions of edges.  
D) Node-link diagrams scale well to networks with millions of nodes.  


#### 19. What is a key consideration when choosing between node-link diagrams and adjacency matrices?  
A) The color scheme used in the visualization.  
B) Whether the task involves path tracing or neighborhood analysis.  
C) The number of attributes per node.  
D) The presence of cycles in the network.  


#### 20. Which of the following statements about implicit tree layouts (like sunburst and icicle plots) are correct?  
A) They can show both inner nodes and leaves clearly.  
B) They emphasize tree depth and sibling order.  
C) Sunburst plots use rectilinear layouts, while icicle plots use radial layouts.  
D) They show parent-child relationships through relative spatial positions rather than explicit links.  



<br>

## Answers

#### 1. Which of the following are true about network nodes and links?  
A) ✗ Links can have attributes, but nodes cannot. (Both nodes and links can have attributes.)  
B) ✗ In all networks, nodes must have at least two links. (Nodes can have zero or one link.)  
C) ✓ A tree is a special type of network with no cycles and exactly one parent per node.  
D) ✓ Nodes represent entities, and links represent relationships between nodes.  

**Correct:** C, D


#### 2. Which tasks are considered topology-based in network analysis?  
A) ✓ Finding shortest paths between nodes.  
B) ✓ Comparing centrality measures of nodes.  
C) ✓ Identifying clusters or communities.  
D) ✗ Finding the distribution of node attributes. (This is attribute-based.)  

**Correct:** A, B, C


#### 3. In force-directed placement algorithms, which of the following statements are correct?  
A) ✓ Nodes repel each other like magnets.  
B) ✗ It scales efficiently to networks with over 10,000 nodes without performance issues. (It struggles beyond ~1,000 nodes.)  
C) ✗ The algorithm always produces the same layout for the same network. (It is nondeterministic.)  
D) ✓ Links act like springs pulling connected nodes together.  

**Correct:** A, D


#### 4. What are the main challenges in creating good node-link layouts?  
A) ✗ Minimizing angular distance between edges. (Maximizing angular distance is preferred.)  
B) ✓ Emphasizing symmetry so similar structures look similar.  
C) ✓ Minimizing edge crossings and node overlaps.  
D) ✗ Maximizing the total drawing area to avoid clutter. (Minimize drawing area is preferred.)  

**Correct:** B, C


#### 5. Which of the following are advantages of adjacency matrix representations over node-link diagrams?  
A) ✓ Better scalability for large networks.  
B) ✗ Easier path tracing between nodes. (Path tracing is harder in matrices.)  
C) ✓ Avoidance of edge crossings.  
D) ✗ Intuitive understanding for users with no training. (Matrices require training.)  

**Correct:** A, C


#### 6. Why is node ordering crucial in adjacency matrix visualizations?  
A) ✗ It determines the color scheme used. (Color is independent of ordering.)  
B) ✓ It affects the interpretability of neighborhood relationships.  
C) ✓ It minimizes edge crossings and reveals clusters.  
D) ✗ It reduces the number of nodes displayed. (Ordering does not reduce nodes.)  

**Correct:** B, C


#### 7. Which statements about circular layouts and arc diagrams are true?  
A) ✗ They are best suited for networks with no attributes. (Attributes can be shown but ordering is key.)  
B) ✓ They are a type of restricted node-link layout.  
C) ✓ Nodes are arranged around a circle or along a line.  
D) ✗ Node ordering does not affect the clarity of the layout. (Ordering is crucial.)  

**Correct:** B, C


#### 8. What are the key differences between trees and general networks?  
A) ✓ Each node in a tree has exactly one parent except the root.  
B) ✗ Trees always have a radial layout. (They can have various layouts.)  
C) ✓ Trees have no cycles, while general networks may have cycles.  
D) ✗ Trees cannot have attributes on nodes or links. (They can have attributes.)  

**Correct:** A, C


#### 9. Which of the following are true about treemaps?  
A) ✓ They use containment to show hierarchical structure.  
B) ✓ They use area to encode quantitative attributes at leaf nodes.  
C) ✗ They emphasize topology and path tracing. (Treemaps emphasize containment and attributes, not topology.)  
D) ✓ They are suitable for visualizing millions of leaf nodes.  

**Correct:** A, B, D


#### 10. When is a choropleth map an appropriate visualization choice?  
A) ✓ When the central task is understanding spatial relationships.  
B) ✗ When multiple variables need to be shown simultaneously. (Choropleths show one variable at a time.)  
C) ✗ When raw counts are more important than normalized data. (Normalization is usually needed.)  
D) ✓ When regions are roughly equal in size.  

**Correct:** A, D


#### 11. What are common pitfalls when using choropleth maps?  
A) ✗ Using choropleth maps for non-spatial data. (Choropleths require spatial data.)  
B) ✓ Using absolute counts without normalization.  
C) ✓ Choosing color palettes without considering perceptual effects.  
D) ✓ Showing multiple variables on the same map.  

**Correct:** B, C, D


#### 12. Which of the following statements about symbol maps are correct?  
A) ✗ Symbols never overlap or occlude map details. (Overlap and occlusion are common issues.)  
B) ✓ Symbol maps always preserve the original spatial geometry.  
C) ✓ Glyphs can represent multivariate data.  
D) ✓ Symbol size can encode quantitative attributes.  

**Correct:** B, C, D


#### 13. What are the main differences between contiguous cartograms and grid cartograms?  
A) ✗ Grid cartograms preserve exact geographic shapes. (They distort shapes.)  
B) ✗ Contiguous cartograms are easier to interpret than grid cartograms. (Grid cartograms are often easier to understand.)  
C) ✓ Grid cartograms use uniform-sized shapes arranged in a grid.  
D) ✓ Contiguous cartograms maintain region adjacency but distort shapes.  

**Correct:** C, D


#### 14. Which of the following are advantages of dot density maps?  
A) ✗ They make it easy to extract exact quantities. (Quantities are hard to extract.)  
B) ✗ They perform well even with very large datasets. (Rendering many dots can be slow.)  
C) ✓ They avoid problems related to region size bias.  
D) ✓ They clearly show spatial clustering patterns.  

**Correct:** C, D


#### 15. In network visualizations, what does the term “hairball problem” refer to?  
A) ✓ The difficulty of interpreting very dense networks with many overlapping edges.  
B) ✗ The inability to display node attributes. (Attributes can be displayed.)  
C) ✗ The problem of nodes having multiple parents in trees. (Trees don’t have multiple parents.)  
D) ✗ The challenge of scaling adjacency matrices beyond 1,000 nodes. (Matrices scale better.)  

**Correct:** A


#### 16. Which of the following statements about hierarchical edge bundling are true?  
A) ✓ It reduces edge clutter by grouping edges with similar source and destination.  
B) ✓ It can be applied to any layout of a compound network.  
C) ✗ It emphasizes attribute values at leaf nodes. (It emphasizes edge relationships.)  
D) ✗ It only works for radial layouts. (It works for any layout.)  

**Correct:** A, B


#### 17. Why might force-directed layouts produce arbitrary spatial positions for nodes?  
A) ✗ Because node positions are fixed by their attributes. (Positions are computed, not fixed.)  
B) ✓ Because spatial position encodes no direct meaning and is optimized to reduce crossings.  
C) ✗ Because the layout is deterministic and reproducible. (It is nondeterministic.)  
D) ✗ Because the algorithm always places nodes in a grid. (Positions are continuous.)  

**Correct:** B


#### 18. Which of the following are true about the scalability of different network visualization techniques?  
A) ✓ Treemaps can visualize up to a million leaf nodes efficiently.  
B) ✓ Force-directed layouts become computationally expensive beyond about 1,000 nodes.  
C) ✓ Adjacency matrices can handle networks with thousands of nodes and millions of edges.  
D) ✗ Node-link diagrams scale well to networks with millions of nodes. (They do not scale well.)  

**Correct:** A, B, C


#### 19. What is a key consideration when choosing between node-link diagrams and adjacency matrices?  
A) ✗ The color scheme used in the visualization. (Color is secondary.)  
B) ✓ Whether the task involves path tracing or neighborhood analysis.  
C) ✗ The number of attributes per node. (Both can handle attributes.)  
D) ✗ The presence of cycles in the network. (Both can represent cycles.)  

**Correct:** B


#### 20. Which of the following statements about implicit tree layouts (like sunburst and icicle plots) are correct?  
A) ✓ They can show both inner nodes and leaves clearly.  
B) ✓ They emphasize tree depth and sibling order.  
C) ✗ Sunburst plots use rectilinear layouts, while icicle plots use radial layouts. (Sunburst is radial; icicle is rectilinear.)  
D) ✓ They show parent-child relationships through relative spatial positions rather than explicit links.  

**Correct:** A, B, D