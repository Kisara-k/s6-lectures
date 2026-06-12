## 10. Network and Spatial

## Questions

#### 1. Which of the following are true about network nodes and links?  
A) A tree is a special type of network with no cycles and exactly one parent per node.  
B) Links can have attributes, but nodes cannot.  
C) In all networks, nodes must have at least two links.  
D) Nodes represent entities, and links represent relationships between nodes.  


#### 2. Which tasks are considered topology-based in network analysis?  
A) Finding shortest paths between nodes.  
B) Identifying clusters or communities.  
C) Finding the distribution of node attributes.  
D) Comparing centrality measures of nodes.  


#### 3. In force-directed placement algorithms, which of the following statements are correct?  
A) It scales efficiently to networks with over 10,000 nodes without performance issues.  
B) Links act like springs pulling connected nodes together.  
C) Nodes repel each other like magnets.  
D) The algorithm always produces the same layout for the same network.  


#### 4. What are the main challenges in creating good node-link layouts?  
A) Maximizing the total drawing area to avoid clutter.  
B) Emphasizing symmetry so similar structures look similar.  
C) Minimizing edge crossings and node overlaps.  
D) Minimizing angular distance between edges.  


#### 5. Which of the following are advantages of adjacency matrix representations over node-link diagrams?  
A) Easier path tracing between nodes.  
B) Better scalability for large networks.  
C) Intuitive understanding for users with no training.  
D) Avoidance of edge crossings.  


#### 6. Why is node ordering crucial in adjacency matrix visualizations?  
A) It determines the color scheme used.  
B) It reduces the number of nodes displayed.  
C) It affects the interpretability of neighborhood relationships.  
D) It minimizes edge crossings and reveals clusters.  


#### 7. Which statements about circular layouts and arc diagrams are true?  
A) They are best suited for networks with no attributes.  
B) Node ordering does not affect the clarity of the layout.  
C) Nodes are arranged around a circle or along a line.  
D) They are a type of restricted node-link layout.  


#### 8. What are the key differences between trees and general networks?  
A) Trees always have a radial layout.  
B) Trees cannot have attributes on nodes or links.  
C) Trees have no cycles, while general networks may have cycles.  
D) Each node in a tree has exactly one parent except the root.  


#### 9. Which of the following are true about treemaps?  
A) They use area to encode quantitative attributes at leaf nodes.  
B) They use containment to show hierarchical structure.  
C) They emphasize topology and path tracing.  
D) They are suitable for visualizing millions of leaf nodes.  


#### 10. When is a choropleth map an appropriate visualization choice?  
A) When raw counts are more important than normalized data.  
B) When the central task is understanding spatial relationships.  
C) When regions are roughly equal in size.  
D) When multiple variables need to be shown simultaneously.  


#### 11. What are common pitfalls when using choropleth maps?  
A) Using choropleth maps for non-spatial data.  
B) Using absolute counts without normalization.  
C) Showing multiple variables on the same map.  
D) Choosing color palettes without considering perceptual effects.  


#### 12. Which of the following statements about symbol maps are correct?  
A) Symbol maps always preserve the original spatial geometry.  
B) Symbols never overlap or occlude map details.  
C) Symbol size can encode quantitative attributes.  
D) Glyphs can represent multivariate data.  


#### 13. What are the main differences between contiguous cartograms and grid cartograms?  
A) Contiguous cartograms maintain region adjacency but distort shapes.  
B) Grid cartograms use uniform-sized shapes arranged in a grid.  
C) Contiguous cartograms are easier to interpret than grid cartograms.  
D) Grid cartograms preserve exact geographic shapes.  


#### 14. Which of the following are advantages of dot density maps?  
A) They avoid problems related to region size bias.  
B) They perform well even with very large datasets.  
C) They make it easy to extract exact quantities.  
D) They clearly show spatial clustering patterns.  


#### 15. In network visualizations, what does the term “hairball problem” refer to?  
A) The difficulty of interpreting very dense networks with many overlapping edges.  
B) The inability to display node attributes.  
C) The problem of nodes having multiple parents in trees.  
D) The challenge of scaling adjacency matrices beyond 1,000 nodes.  


#### 16. Which of the following statements about hierarchical edge bundling are true?  
A) It can be applied to any layout of a compound network.  
B) It reduces edge clutter by grouping edges with similar source and destination.  
C) It emphasizes attribute values at leaf nodes.  
D) It only works for radial layouts.  


#### 17. Why might force-directed layouts produce arbitrary spatial positions for nodes?  
A) Because the algorithm always places nodes in a grid.  
B) Because the layout is deterministic and reproducible.  
C) Because node positions are fixed by their attributes.  
D) Because spatial position encodes no direct meaning and is optimized to reduce crossings.  


#### 18. Which of the following are true about the scalability of different network visualization techniques?  
A) Force-directed layouts become computationally expensive beyond about 1,000 nodes.  
B) Adjacency matrices can handle networks with thousands of nodes and millions of edges.  
C) Node-link diagrams scale well to networks with millions of nodes.  
D) Treemaps can visualize up to a million leaf nodes efficiently.  


#### 19. What is a key consideration when choosing between node-link diagrams and adjacency matrices?  
A) The number of attributes per node.  
B) The color scheme used in the visualization.  
C) Whether the task involves path tracing or neighborhood analysis.  
D) The presence of cycles in the network.  


#### 20. Which of the following statements about implicit tree layouts (like sunburst and icicle plots) are correct?  
A) They emphasize tree depth and sibling order.  
B) They can show both inner nodes and leaves clearly.  
C) They show parent-child relationships through relative spatial positions rather than explicit links.  
D) Sunburst plots use rectilinear layouts, while icicle plots use radial layouts.  



<br>

## Answers

#### 1. Which of the following are true about network nodes and links?  
A) ✓ A tree is a special type of network with no cycles and exactly one parent per node.  
B) ✗ Links can have attributes, but nodes cannot. (Both nodes and links can have attributes.)  
C) ✗ In all networks, nodes must have at least two links. (Nodes can have zero or one link.)  
D) ✓ Nodes represent entities, and links represent relationships between nodes.  

**Correct:** A, D


#### 2. Which tasks are considered topology-based in network analysis?  
A) ✓ Finding shortest paths between nodes.  
B) ✓ Identifying clusters or communities.  
C) ✗ Finding the distribution of node attributes. (This is attribute-based.)  
D) ✓ Comparing centrality measures of nodes.  

**Correct:** A, B, D


#### 3. In force-directed placement algorithms, which of the following statements are correct?  
A) ✗ It scales efficiently to networks with over 10,000 nodes without performance issues. (It struggles beyond ~1,000 nodes.)  
B) ✓ Links act like springs pulling connected nodes together.  
C) ✓ Nodes repel each other like magnets.  
D) ✗ The algorithm always produces the same layout for the same network. (It is nondeterministic.)  

**Correct:** B, C


#### 4. What are the main challenges in creating good node-link layouts?  
A) ✗ Maximizing the total drawing area to avoid clutter. (Minimize drawing area is preferred.)  
B) ✓ Emphasizing symmetry so similar structures look similar.  
C) ✓ Minimizing edge crossings and node overlaps.  
D) ✗ Minimizing angular distance between edges. (Maximizing angular distance is preferred.)  

**Correct:** B, C


#### 5. Which of the following are advantages of adjacency matrix representations over node-link diagrams?  
A) ✗ Easier path tracing between nodes. (Path tracing is harder in matrices.)  
B) ✓ Better scalability for large networks.  
C) ✗ Intuitive understanding for users with no training. (Matrices require training.)  
D) ✓ Avoidance of edge crossings.  

**Correct:** B, D


#### 6. Why is node ordering crucial in adjacency matrix visualizations?  
A) ✗ It determines the color scheme used. (Color is independent of ordering.)  
B) ✗ It reduces the number of nodes displayed. (Ordering does not reduce nodes.)  
C) ✓ It affects the interpretability of neighborhood relationships.  
D) ✓ It minimizes edge crossings and reveals clusters.  

**Correct:** C, D


#### 7. Which statements about circular layouts and arc diagrams are true?  
A) ✗ They are best suited for networks with no attributes. (Attributes can be shown but ordering is key.)  
B) ✗ Node ordering does not affect the clarity of the layout. (Ordering is crucial.)  
C) ✓ Nodes are arranged around a circle or along a line.  
D) ✓ They are a type of restricted node-link layout.  

**Correct:** C, D


#### 8. What are the key differences between trees and general networks?  
A) ✗ Trees always have a radial layout. (They can have various layouts.)  
B) ✗ Trees cannot have attributes on nodes or links. (They can have attributes.)  
C) ✓ Trees have no cycles, while general networks may have cycles.  
D) ✓ Each node in a tree has exactly one parent except the root.  

**Correct:** C, D


#### 9. Which of the following are true about treemaps?  
A) ✓ They use area to encode quantitative attributes at leaf nodes.  
B) ✓ They use containment to show hierarchical structure.  
C) ✗ They emphasize topology and path tracing. (Treemaps emphasize containment and attributes, not topology.)  
D) ✓ They are suitable for visualizing millions of leaf nodes.  

**Correct:** A, B, D


#### 10. When is a choropleth map an appropriate visualization choice?  
A) ✗ When raw counts are more important than normalized data. (Normalization is usually needed.)  
B) ✓ When the central task is understanding spatial relationships.  
C) ✓ When regions are roughly equal in size.  
D) ✗ When multiple variables need to be shown simultaneously. (Choropleths show one variable at a time.)  

**Correct:** B, C


#### 11. What are common pitfalls when using choropleth maps?  
A) ✗ Using choropleth maps for non-spatial data. (Choropleths require spatial data.)  
B) ✓ Using absolute counts without normalization.  
C) ✓ Showing multiple variables on the same map.  
D) ✓ Choosing color palettes without considering perceptual effects.  

**Correct:** B, C, D


#### 12. Which of the following statements about symbol maps are correct?  
A) ✓ Symbol maps always preserve the original spatial geometry.  
B) ✗ Symbols never overlap or occlude map details. (Overlap and occlusion are common issues.)  
C) ✓ Symbol size can encode quantitative attributes.  
D) ✓ Glyphs can represent multivariate data.  

**Correct:** A, C, D


#### 13. What are the main differences between contiguous cartograms and grid cartograms?  
A) ✓ Contiguous cartograms maintain region adjacency but distort shapes.  
B) ✓ Grid cartograms use uniform-sized shapes arranged in a grid.  
C) ✗ Contiguous cartograms are easier to interpret than grid cartograms. (Grid cartograms are often easier to understand.)  
D) ✗ Grid cartograms preserve exact geographic shapes. (They distort shapes.)  

**Correct:** A, B


#### 14. Which of the following are advantages of dot density maps?  
A) ✓ They avoid problems related to region size bias.  
B) ✗ They perform well even with very large datasets. (Rendering many dots can be slow.)  
C) ✗ They make it easy to extract exact quantities. (Quantities are hard to extract.)  
D) ✓ They clearly show spatial clustering patterns.  

**Correct:** A, D


#### 15. In network visualizations, what does the term “hairball problem” refer to?  
A) ✓ The difficulty of interpreting very dense networks with many overlapping edges.  
B) ✗ The inability to display node attributes. (Attributes can be displayed.)  
C) ✗ The problem of nodes having multiple parents in trees. (Trees don’t have multiple parents.)  
D) ✗ The challenge of scaling adjacency matrices beyond 1,000 nodes. (Matrices scale better.)  

**Correct:** A


#### 16. Which of the following statements about hierarchical edge bundling are true?  
A) ✓ It can be applied to any layout of a compound network.  
B) ✓ It reduces edge clutter by grouping edges with similar source and destination.  
C) ✗ It emphasizes attribute values at leaf nodes. (It emphasizes edge relationships.)  
D) ✗ It only works for radial layouts. (It works for any layout.)  

**Correct:** A, B


#### 17. Why might force-directed layouts produce arbitrary spatial positions for nodes?  
A) ✗ Because the algorithm always places nodes in a grid. (Positions are continuous.)  
B) ✗ Because the layout is deterministic and reproducible. (It is nondeterministic.)  
C) ✗ Because node positions are fixed by their attributes. (Positions are computed, not fixed.)  
D) ✓ Because spatial position encodes no direct meaning and is optimized to reduce crossings.  

**Correct:** D


#### 18. Which of the following are true about the scalability of different network visualization techniques?  
A) ✓ Force-directed layouts become computationally expensive beyond about 1,000 nodes.  
B) ✓ Adjacency matrices can handle networks with thousands of nodes and millions of edges.  
C) ✗ Node-link diagrams scale well to networks with millions of nodes. (They do not scale well.)  
D) ✓ Treemaps can visualize up to a million leaf nodes efficiently.  

**Correct:** A, B, D


#### 19. What is a key consideration when choosing between node-link diagrams and adjacency matrices?  
A) ✗ The number of attributes per node. (Both can handle attributes.)  
B) ✗ The color scheme used in the visualization. (Color is secondary.)  
C) ✓ Whether the task involves path tracing or neighborhood analysis.  
D) ✗ The presence of cycles in the network. (Both can represent cycles.)  

**Correct:** C


#### 20. Which of the following statements about implicit tree layouts (like sunburst and icicle plots) are correct?  
A) ✓ They emphasize tree depth and sibling order.  
B) ✓ They can show both inner nodes and leaves clearly.  
C) ✓ They show parent-child relationships through relative spatial positions rather than explicit links.  
D) ✗ Sunburst plots use rectilinear layouts, while icicle plots use radial layouts. (Sunburst is radial; icicle is rectilinear.)  

**Correct:** A, B, C