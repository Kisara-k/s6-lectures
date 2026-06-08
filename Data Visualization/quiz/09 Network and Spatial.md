## 10. Network and Spatial

## Questions

#### 1. Which of the following are true about network nodes and links?  
A) Nodes represent entities, and links represent relationships between nodes.  
B) Links can have attributes, but nodes cannot.  
C) A tree is a special type of network with no cycles and exactly one parent per node.  
D) In all networks, nodes must have at least two links.


#### 2. Which tasks are considered topology-based in network analysis?  
A) Finding shortest paths between nodes.  
B) Comparing centrality measures of nodes.  
C) Finding the distribution of node attributes.  
D) Identifying clusters or communities.


#### 3. In force-directed placement algorithms, which of the following statements are correct?  
A) Nodes repel each other like magnets.  
B) Links act like springs pulling connected nodes together.  
C) The algorithm always produces the same layout for the same network.  
D) It scales efficiently to networks with over 10,000 nodes without performance issues.


#### 4. What are the main challenges in creating good node-link layouts?  
A) Minimizing edge crossings and node overlaps.  
B) Maximizing the total drawing area to avoid clutter.  
C) Emphasizing symmetry so similar structures look similar.  
D) Minimizing angular distance between edges.


#### 5. Which of the following are advantages of adjacency matrix representations over node-link diagrams?  
A) Better scalability for large networks.  
B) Easier path tracing between nodes.  
C) Avoidance of edge crossings.  
D) Intuitive understanding for users with no training.


#### 6. Why is node ordering crucial in adjacency matrix visualizations?  
A) It reduces the number of nodes displayed.  
B) It minimizes edge crossings and reveals clusters.  
C) It determines the color scheme used.  
D) It affects the interpretability of neighborhood relationships.


#### 7. Which statements about circular layouts and arc diagrams are true?  
A) Node ordering does not affect the clarity of the layout.  
B) Nodes are arranged around a circle or along a line.  
C) They are a type of restricted node-link layout.  
D) They are best suited for networks with no attributes.


#### 8. What are the key differences between trees and general networks?  
A) Trees have no cycles, while general networks may have cycles.  
B) Each node in a tree has exactly one parent except the root.  
C) Trees cannot have attributes on nodes or links.  
D) Trees always have a radial layout.


#### 9. Which of the following are true about treemaps?  
A) They use area to encode quantitative attributes at leaf nodes.  
B) They emphasize topology and path tracing.  
C) They use containment to show hierarchical structure.  
D) They are suitable for visualizing millions of leaf nodes.


#### 10. When is a choropleth map an appropriate visualization choice?  
A) When the central task is understanding spatial relationships.  
B) When multiple variables need to be shown simultaneously.  
C) When regions are roughly equal in size.  
D) When raw counts are more important than normalized data.


#### 11. What are common pitfalls when using choropleth maps?  
A) Using absolute counts without normalization.  
B) Showing multiple variables on the same map.  
C) Choosing color palettes without considering perceptual effects.  
D) Using choropleth maps for non-spatial data.


#### 12. Which of the following statements about symbol maps are correct?  
A) Symbol size can encode quantitative attributes.  
B) Symbols never overlap or occlude map details.  
C) Glyphs can represent multivariate data.  
D) Symbol maps always preserve the original spatial geometry.


#### 13. What are the main differences between contiguous cartograms and grid cartograms?  
A) Contiguous cartograms maintain region adjacency but distort shapes.  
B) Grid cartograms use uniform-sized shapes arranged in a grid.  
C) Grid cartograms preserve exact geographic shapes.  
D) Contiguous cartograms are easier to interpret than grid cartograms.


#### 14. Which of the following are advantages of dot density maps?  
A) They avoid problems related to region size bias.  
B) They make it easy to extract exact quantities.  
C) They clearly show spatial clustering patterns.  
D) They perform well even with very large datasets.


#### 15. In network visualizations, what does the term “hairball problem” refer to?  
A) The difficulty of interpreting very dense networks with many overlapping edges.  
B) The inability to display node attributes.  
C) The problem of nodes having multiple parents in trees.  
D) The challenge of scaling adjacency matrices beyond 1,000 nodes.


#### 16. Which of the following statements about hierarchical edge bundling are true?  
A) It reduces edge clutter by grouping edges with similar source and destination.  
B) It only works for radial layouts.  
C) It can be applied to any layout of a compound network.  
D) It emphasizes attribute values at leaf nodes.


#### 17. Why might force-directed layouts produce arbitrary spatial positions for nodes?  
A) Because spatial position encodes no direct meaning and is optimized to reduce crossings.  
B) Because node positions are fixed by their attributes.  
C) Because the algorithm always places nodes in a grid.  
D) Because the layout is deterministic and reproducible.


#### 18. Which of the following are true about the scalability of different network visualization techniques?  
A) Node-link diagrams scale well to networks with millions of nodes.  
B) Adjacency matrices can handle networks with thousands of nodes and millions of edges.  
C) Force-directed layouts become computationally expensive beyond about 1,000 nodes.  
D) Treemaps can visualize up to a million leaf nodes efficiently.


#### 19. What is a key consideration when choosing between node-link diagrams and adjacency matrices?  
A) Whether the task involves path tracing or neighborhood analysis.  
B) The color scheme used in the visualization.  
C) The number of attributes per node.  
D) The presence of cycles in the network.


#### 20. Which of the following statements about implicit tree layouts (like sunburst and icicle plots) are correct?  
A) They show parent-child relationships through relative spatial positions rather than explicit links.  
B) Sunburst plots use rectilinear layouts, while icicle plots use radial layouts.  
C) They can show both inner nodes and leaves clearly.  
D) They emphasize tree depth and sibling order.



<br>

## Answers

#### 1. Which of the following are true about network nodes and links?  
A) ✓ Nodes represent entities, and links represent relationships between nodes.  
B) ✗ Links can have attributes, but nodes cannot. (Both nodes and links can have attributes.)  
C) ✓ A tree is a special type of network with no cycles and exactly one parent per node.  
D) ✗ In all networks, nodes must have at least two links. (Nodes can have zero or one link.)

**Correct:** A, C


#### 2. Which tasks are considered topology-based in network analysis?  
A) ✓ Finding shortest paths between nodes.  
B) ✓ Comparing centrality measures of nodes.  
C) ✗ Finding the distribution of node attributes. (This is attribute-based.)  
D) ✓ Identifying clusters or communities.

**Correct:** A, B, D


#### 3. In force-directed placement algorithms, which of the following statements are correct?  
A) ✓ Nodes repel each other like magnets.  
B) ✓ Links act like springs pulling connected nodes together.  
C) ✗ The algorithm always produces the same layout for the same network. (It is nondeterministic.)  
D) ✗ It scales efficiently to networks with over 10,000 nodes without performance issues. (It struggles beyond ~1,000 nodes.)

**Correct:** A, B


#### 4. What are the main challenges in creating good node-link layouts?  
A) ✓ Minimizing edge crossings and node overlaps.  
B) ✗ Maximizing the total drawing area to avoid clutter. (Minimize drawing area is preferred.)  
C) ✓ Emphasizing symmetry so similar structures look similar.  
D) ✗ Minimizing angular distance between edges. (Maximizing angular distance is preferred.)

**Correct:** A, C


#### 5. Which of the following are advantages of adjacency matrix representations over node-link diagrams?  
A) ✓ Better scalability for large networks.  
B) ✗ Easier path tracing between nodes. (Path tracing is harder in matrices.)  
C) ✓ Avoidance of edge crossings.  
D) ✗ Intuitive understanding for users with no training. (Matrices require training.)

**Correct:** A, C


#### 6. Why is node ordering crucial in adjacency matrix visualizations?  
A) ✗ It reduces the number of nodes displayed. (Ordering does not reduce nodes.)  
B) ✓ It minimizes edge crossings and reveals clusters.  
C) ✗ It determines the color scheme used. (Color is independent of ordering.)  
D) ✓ It affects the interpretability of neighborhood relationships.

**Correct:** B, D


#### 7. Which statements about circular layouts and arc diagrams are true?  
A) ✗ Node ordering does not affect the clarity of the layout. (Ordering is crucial.)  
B) ✓ Nodes are arranged around a circle or along a line.  
C) ✓ They are a type of restricted node-link layout.  
D) ✗ They are best suited for networks with no attributes. (Attributes can be shown but ordering is key.)

**Correct:** B, C


#### 8. What are the key differences between trees and general networks?  
A) ✓ Trees have no cycles, while general networks may have cycles.  
B) ✓ Each node in a tree has exactly one parent except the root.  
C) ✗ Trees cannot have attributes on nodes or links. (They can have attributes.)  
D) ✗ Trees always have a radial layout. (They can have various layouts.)

**Correct:** A, B


#### 9. Which of the following are true about treemaps?  
A) ✓ They use area to encode quantitative attributes at leaf nodes.  
B) ✗ They emphasize topology and path tracing. (Treemaps emphasize containment and attributes, not topology.)  
C) ✓ They use containment to show hierarchical structure.  
D) ✓ They are suitable for visualizing millions of leaf nodes.

**Correct:** A, C, D


#### 10. When is a choropleth map an appropriate visualization choice?  
A) ✓ When the central task is understanding spatial relationships.  
B) ✗ When multiple variables need to be shown simultaneously. (Choropleths show one variable at a time.)  
C) ✓ When regions are roughly equal in size.  
D) ✗ When raw counts are more important than normalized data. (Normalization is usually needed.)

**Correct:** A, C


#### 11. What are common pitfalls when using choropleth maps?  
A) ✓ Using absolute counts without normalization.  
B) ✓ Showing multiple variables on the same map.  
C) ✓ Choosing color palettes without considering perceptual effects.  
D) ✗ Using choropleth maps for non-spatial data. (Choropleths require spatial data.)

**Correct:** A, B, C


#### 12. Which of the following statements about symbol maps are correct?  
A) ✓ Symbol size can encode quantitative attributes.  
B) ✗ Symbols never overlap or occlude map details. (Overlap and occlusion are common issues.)  
C) ✓ Glyphs can represent multivariate data.  
D) ✓ Symbol maps always preserve the original spatial geometry.

**Correct:** A, C, D


#### 13. What are the main differences between contiguous cartograms and grid cartograms?  
A) ✓ Contiguous cartograms maintain region adjacency but distort shapes.  
B) ✓ Grid cartograms use uniform-sized shapes arranged in a grid.  
C) ✗ Grid cartograms preserve exact geographic shapes. (They distort shapes.)  
D) ✗ Contiguous cartograms are easier to interpret than grid cartograms. (Grid cartograms are often easier to understand.)

**Correct:** A, B


#### 14. Which of the following are advantages of dot density maps?  
A) ✓ They avoid problems related to region size bias.  
B) ✗ They make it easy to extract exact quantities. (Quantities are hard to extract.)  
C) ✓ They clearly show spatial clustering patterns.  
D) ✗ They perform well even with very large datasets. (Rendering many dots can be slow.)

**Correct:** A, C


#### 15. In network visualizations, what does the term “hairball problem” refer to?  
A) ✓ The difficulty of interpreting very dense networks with many overlapping edges.  
B) ✗ The inability to display node attributes. (Attributes can be displayed.)  
C) ✗ The problem of nodes having multiple parents in trees. (Trees don’t have multiple parents.)  
D) ✗ The challenge of scaling adjacency matrices beyond 1,000 nodes. (Matrices scale better.)

**Correct:** A


#### 16. Which of the following statements about hierarchical edge bundling are true?  
A) ✓ It reduces edge clutter by grouping edges with similar source and destination.  
B) ✗ It only works for radial layouts. (It works for any layout.)  
C) ✓ It can be applied to any layout of a compound network.  
D) ✗ It emphasizes attribute values at leaf nodes. (It emphasizes edge relationships.)

**Correct:** A, C


#### 17. Why might force-directed layouts produce arbitrary spatial positions for nodes?  
A) ✓ Because spatial position encodes no direct meaning and is optimized to reduce crossings.  
B) ✗ Because node positions are fixed by their attributes. (Positions are computed, not fixed.)  
C) ✗ Because the algorithm always places nodes in a grid. (Positions are continuous.)  
D) ✗ Because the layout is deterministic and reproducible. (It is nondeterministic.)

**Correct:** A


#### 18. Which of the following are true about the scalability of different network visualization techniques?  
A) ✗ Node-link diagrams scale well to networks with millions of nodes. (They do not scale well.)  
B) ✓ Adjacency matrices can handle networks with thousands of nodes and millions of edges.  
C) ✓ Force-directed layouts become computationally expensive beyond about 1,000 nodes.  
D) ✓ Treemaps can visualize up to a million leaf nodes efficiently.

**Correct:** B, C, D


#### 19. What is a key consideration when choosing between node-link diagrams and adjacency matrices?  
A) ✓ Whether the task involves path tracing or neighborhood analysis.  
B) ✗ The color scheme used in the visualization. (Color is secondary.)  
C) ✗ The number of attributes per node. (Both can handle attributes.)  
D) ✗ The presence of cycles in the network. (Both can represent cycles.)

**Correct:** A


#### 20. Which of the following statements about implicit tree layouts (like sunburst and icicle plots) are correct?  
A) ✓ They show parent-child relationships through relative spatial positions rather than explicit links.  
B) ✗ Sunburst plots use rectilinear layouts, while icicle plots use radial layouts. (Sunburst is radial; icicle is rectilinear.)  
C) ✓ They can show both inner nodes and leaves clearly.  
D) ✓ They emphasize tree depth and sibling order.

**Correct:** A, C, D