## 10. Network and Spatial

## Questions

#### 1. Which of the following are true about network nodes and links?  
A) Nodes represent entities, and links represent relationships between nodes.  
B) In all networks, nodes must have at least two links.
C) A tree is a special type of network with no cycles and exactly one parent per node.  
D) Links can have attributes, but nodes cannot.  


#### 2. Which tasks are considered topology-based in network analysis?  
A) Identifying clusters or communities.
B) Finding shortest paths between nodes.  
C) Finding the distribution of node attributes.  
D) Comparing centrality measures of nodes.  


#### 3. In force-directed placement algorithms, which of the following statements are correct?  
A) It scales efficiently to networks with over 10,000 nodes without performance issues.
B) Nodes repel each other like magnets.  
C) The algorithm always produces the same layout for the same network.  
D) Links act like springs pulling connected nodes together.  


#### 4. What are the main challenges in creating good node-link layouts?  
A) Emphasizing symmetry so similar structures look similar.  
B) Minimizing angular distance between edges.
C) Maximizing the total drawing area to avoid clutter.  
D) Minimizing edge crossings and node overlaps.  


#### 5. Which of the following are advantages of adjacency matrix representations over node-link diagrams?  
A) Better scalability for large networks.  
B) Intuitive understanding for users with no training.
C) Avoidance of edge crossings.  
D) Easier path tracing between nodes.  


#### 6. Why is node ordering crucial in adjacency matrix visualizations?  
A) It reduces the number of nodes displayed.  
B) It determines the color scheme used.  
C) It affects the interpretability of neighborhood relationships.
D) It minimizes edge crossings and reveals clusters.  


#### 7. Which statements about circular layouts and arc diagrams are true?  
A) Node ordering does not affect the clarity of the layout.  
B) They are a type of restricted node-link layout.  
C) They are best suited for networks with no attributes.
D) Nodes are arranged around a circle or along a line.  


#### 8. What are the key differences between trees and general networks?  
A) Trees always have a radial layout.
B) Trees cannot have attributes on nodes or links.  
C) Trees have no cycles, while general networks may have cycles.  
D) Each node in a tree has exactly one parent except the root.  


#### 9. Which of the following are true about treemaps?  
A) They use containment to show hierarchical structure.  
B) They are suitable for visualizing millions of leaf nodes.
C) They use area to encode quantitative attributes at leaf nodes.  
D) They emphasize topology and path tracing.  


#### 10. When is a choropleth map an appropriate visualization choice?  
A) When multiple variables need to be shown simultaneously.  
B) When raw counts are more important than normalized data.
C) When the central task is understanding spatial relationships.  
D) When regions are roughly equal in size.  


#### 11. What are common pitfalls when using choropleth maps?  
A) Choosing color palettes without considering perceptual effects.  
B) Using choropleth maps for non-spatial data.
C) Using absolute counts without normalization.  
D) Showing multiple variables on the same map.  


#### 12. Which of the following statements about symbol maps are correct?  
A) Glyphs can represent multivariate data.  
B) Symbol size can encode quantitative attributes.  
C) Symbols never overlap or occlude map details.  
D) Symbol maps always preserve the original spatial geometry.


#### 13. What are the main differences between contiguous cartograms and grid cartograms?  
A) Grid cartograms use uniform-sized shapes arranged in a grid.  
B) Contiguous cartograms are easier to interpret than grid cartograms.
C) Contiguous cartograms maintain region adjacency but distort shapes.  
D) Grid cartograms preserve exact geographic shapes.  


#### 14. Which of the following are advantages of dot density maps?  
A) They make it easy to extract exact quantities.  
B) They perform well even with very large datasets.
C) They avoid problems related to region size bias.  
D) They clearly show spatial clustering patterns.  


#### 15. In network visualizations, what does the term “hairball problem” refer to?  
A) The difficulty of interpreting very dense networks with many overlapping edges.  
B) The challenge of scaling adjacency matrices beyond 1,000 nodes.
C) The inability to display node attributes.  
D) The problem of nodes having multiple parents in trees.  


#### 16. Which of the following statements about hierarchical edge bundling are true?  
A) It can be applied to any layout of a compound network.  
B) It emphasizes attribute values at leaf nodes.
C) It reduces edge clutter by grouping edges with similar source and destination.  
D) It only works for radial layouts.  


#### 17. Why might force-directed layouts produce arbitrary spatial positions for nodes?  
A) Because spatial position encodes no direct meaning and is optimized to reduce crossings.  
B) Because the algorithm always places nodes in a grid.  
C) Because node positions are fixed by their attributes.  
D) Because the layout is deterministic and reproducible.


#### 18. Which of the following are true about the scalability of different network visualization techniques?  
A) Node-link diagrams scale well to networks with millions of nodes.  
B) Adjacency matrices can handle networks with thousands of nodes and millions of edges.  
C) Treemaps can visualize up to a million leaf nodes efficiently.
D) Force-directed layouts become computationally expensive beyond about 1,000 nodes.  


#### 19. What is a key consideration when choosing between node-link diagrams and adjacency matrices?  
A) The number of attributes per node.  
B) Whether the task involves path tracing or neighborhood analysis.  
C) The presence of cycles in the network.
D) The color scheme used in the visualization.  


#### 20. Which of the following statements about implicit tree layouts (like sunburst and icicle plots) are correct?  
A) They show parent-child relationships through relative spatial positions rather than explicit links.  
B) They can show both inner nodes and leaves clearly.  
C) They emphasize tree depth and sibling order.
D) Sunburst plots use rectilinear layouts, while icicle plots use radial layouts.  



<br>

## Answers

#### 1. Which of the following are true about network nodes and links?  
A) ✓ Nodes represent entities, and links represent relationships between nodes.  
B) ✗ In all networks, nodes must have at least two links. (Nodes can have zero or one link.)
C) ✓ A tree is a special type of network with no cycles and exactly one parent per node.  
D) ✗ Links can have attributes, but nodes cannot. (Both nodes and links can have attributes.)  

**Correct:** A, C


#### 2. Which tasks are considered topology-based in network analysis?  
A) ✓ Identifying clusters or communities.
B) ✓ Finding shortest paths between nodes.  
C) ✗ Finding the distribution of node attributes. (This is attribute-based.)  
D) ✓ Comparing centrality measures of nodes.  

**Correct:** A, B, D


#### 3. In force-directed placement algorithms, which of the following statements are correct?  
A) ✗ It scales efficiently to networks with over 10,000 nodes without performance issues. (It struggles beyond ~1,000 nodes.)
B) ✓ Nodes repel each other like magnets.  
C) ✗ The algorithm always produces the same layout for the same network. (It is nondeterministic.)  
D) ✓ Links act like springs pulling connected nodes together.  

**Correct:** B, D


#### 4. What are the main challenges in creating good node-link layouts?  
A) ✓ Emphasizing symmetry so similar structures look similar.  
B) ✗ Minimizing angular distance between edges. (Maximizing angular distance is preferred.)
C) ✗ Maximizing the total drawing area to avoid clutter. (Minimize drawing area is preferred.)  
D) ✓ Minimizing edge crossings and node overlaps.  

**Correct:** A, D


#### 5. Which of the following are advantages of adjacency matrix representations over node-link diagrams?  
A) ✓ Better scalability for large networks.  
B) ✗ Intuitive understanding for users with no training. (Matrices require training.)
C) ✓ Avoidance of edge crossings.  
D) ✗ Easier path tracing between nodes. (Path tracing is harder in matrices.)  

**Correct:** A, C


#### 6. Why is node ordering crucial in adjacency matrix visualizations?  
A) ✗ It reduces the number of nodes displayed. (Ordering does not reduce nodes.)  
B) ✗ It determines the color scheme used. (Color is independent of ordering.)  
C) ✓ It affects the interpretability of neighborhood relationships.
D) ✓ It minimizes edge crossings and reveals clusters.  

**Correct:** C, D


#### 7. Which statements about circular layouts and arc diagrams are true?  
A) ✗ Node ordering does not affect the clarity of the layout. (Ordering is crucial.)  
B) ✓ They are a type of restricted node-link layout.  
C) ✗ They are best suited for networks with no attributes. (Attributes can be shown but ordering is key.)
D) ✓ Nodes are arranged around a circle or along a line.  

**Correct:** B, D


#### 8. What are the key differences between trees and general networks?  
A) ✗ Trees always have a radial layout. (They can have various layouts.)
B) ✗ Trees cannot have attributes on nodes or links. (They can have attributes.)  
C) ✓ Trees have no cycles, while general networks may have cycles.  
D) ✓ Each node in a tree has exactly one parent except the root.  

**Correct:** C, D


#### 9. Which of the following are true about treemaps?  
A) ✓ They use containment to show hierarchical structure.  
B) ✓ They are suitable for visualizing millions of leaf nodes.
C) ✓ They use area to encode quantitative attributes at leaf nodes.  
D) ✗ They emphasize topology and path tracing. (Treemaps emphasize containment and attributes, not topology.)  

**Correct:** A, B, C


#### 10. When is a choropleth map an appropriate visualization choice?  
A) ✗ When multiple variables need to be shown simultaneously. (Choropleths show one variable at a time.)  
B) ✗ When raw counts are more important than normalized data. (Normalization is usually needed.)
C) ✓ When the central task is understanding spatial relationships.  
D) ✓ When regions are roughly equal in size.  

**Correct:** C, D


#### 11. What are common pitfalls when using choropleth maps?  
A) ✓ Choosing color palettes without considering perceptual effects.  
B) ✗ Using choropleth maps for non-spatial data. (Choropleths require spatial data.)
C) ✓ Using absolute counts without normalization.  
D) ✓ Showing multiple variables on the same map.  

**Correct:** A, C, D


#### 12. Which of the following statements about symbol maps are correct?  
A) ✓ Glyphs can represent multivariate data.  
B) ✓ Symbol size can encode quantitative attributes.  
C) ✗ Symbols never overlap or occlude map details. (Overlap and occlusion are common issues.)  
D) ✓ Symbol maps always preserve the original spatial geometry.

**Correct:** A, B, D


#### 13. What are the main differences between contiguous cartograms and grid cartograms?  
A) ✓ Grid cartograms use uniform-sized shapes arranged in a grid.  
B) ✗ Contiguous cartograms are easier to interpret than grid cartograms. (Grid cartograms are often easier to understand.)
C) ✓ Contiguous cartograms maintain region adjacency but distort shapes.  
D) ✗ Grid cartograms preserve exact geographic shapes. (They distort shapes.)  

**Correct:** A, C


#### 14. Which of the following are advantages of dot density maps?  
A) ✗ They make it easy to extract exact quantities. (Quantities are hard to extract.)  
B) ✗ They perform well even with very large datasets. (Rendering many dots can be slow.)
C) ✓ They avoid problems related to region size bias.  
D) ✓ They clearly show spatial clustering patterns.  

**Correct:** C, D


#### 15. In network visualizations, what does the term “hairball problem” refer to?  
A) ✓ The difficulty of interpreting very dense networks with many overlapping edges.  
B) ✗ The challenge of scaling adjacency matrices beyond 1,000 nodes. (Matrices scale better.)
C) ✗ The inability to display node attributes. (Attributes can be displayed.)  
D) ✗ The problem of nodes having multiple parents in trees. (Trees don’t have multiple parents.)  

**Correct:** A


#### 16. Which of the following statements about hierarchical edge bundling are true?  
A) ✓ It can be applied to any layout of a compound network.  
B) ✗ It emphasizes attribute values at leaf nodes. (It emphasizes edge relationships.)
C) ✓ It reduces edge clutter by grouping edges with similar source and destination.  
D) ✗ It only works for radial layouts. (It works for any layout.)  

**Correct:** A, C


#### 17. Why might force-directed layouts produce arbitrary spatial positions for nodes?  
A) ✓ Because spatial position encodes no direct meaning and is optimized to reduce crossings.  
B) ✗ Because the algorithm always places nodes in a grid. (Positions are continuous.)  
C) ✗ Because node positions are fixed by their attributes. (Positions are computed, not fixed.)  
D) ✗ Because the layout is deterministic and reproducible. (It is nondeterministic.)

**Correct:** A


#### 18. Which of the following are true about the scalability of different network visualization techniques?  
A) ✗ Node-link diagrams scale well to networks with millions of nodes. (They do not scale well.)  
B) ✓ Adjacency matrices can handle networks with thousands of nodes and millions of edges.  
C) ✓ Treemaps can visualize up to a million leaf nodes efficiently.
D) ✓ Force-directed layouts become computationally expensive beyond about 1,000 nodes.  

**Correct:** B, C, D


#### 19. What is a key consideration when choosing between node-link diagrams and adjacency matrices?  
A) ✗ The number of attributes per node. (Both can handle attributes.)  
B) ✓ Whether the task involves path tracing or neighborhood analysis.  
C) ✗ The presence of cycles in the network. (Both can represent cycles.)
D) ✗ The color scheme used in the visualization. (Color is secondary.)  

**Correct:** B


#### 20. Which of the following statements about implicit tree layouts (like sunburst and icicle plots) are correct?  
A) ✓ They show parent-child relationships through relative spatial positions rather than explicit links.  
B) ✓ They can show both inner nodes and leaves clearly.  
C) ✓ They emphasize tree depth and sibling order.
D) ✗ Sunburst plots use rectilinear layouts, while icicle plots use radial layouts. (Sunburst is radial; icicle is rectilinear.)  

**Correct:** A, B, C