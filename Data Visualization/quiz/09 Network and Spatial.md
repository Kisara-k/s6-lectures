## 10. Network and Spatial

## Questions

#### 1. Which of the following statements correctly describe the characteristics of a tree in network data?  
A) Trees are a special case of networks where each node has exactly one parent except the root.  
B) Each node in a tree can have multiple parents.  
C) A tree is a network with no cycles.  
D) Trees always have bidirectional links between nodes.  

#### 2. In force-directed placement algorithms for node-link diagrams, which of the following are true?  
A) The algorithm iteratively moves nodes until forces reach equilibrium.  
B) The algorithm guarantees a deterministic layout every time it runs.  
C) Links act like springs pulling connected nodes together.  
D) Nodes repel each other like magnets.  

#### 3. When comparing node-link diagrams and adjacency matrix representations, which of the following are accurate?  
A) Adjacency matrices scale better for large networks with many edges.  
B) Node-link diagrams avoid edge crossings better than adjacency matrices.  
C) Adjacency matrices are intuitive for users with no training.  
D) Node-link diagrams are better for path tracing and understanding topology.  

#### 4. Which of the following criteria are important for producing a good node-link layout?  
A) Minimizing edge crossings and node overlaps.  
B) Maximizing the total drawing area to spread out nodes.  
C) Minimizing angular distance between edges connected to the same node.  
D) Emphasizing symmetry so similar graph structures look similar.  

#### 5. Regarding circular layouts and arc diagrams, which statements are true?  
A) Circular layouts always produce layouts with fewer edge crossings than force-directed layouts.  
B) These layouts encode spatial position with direct semantic meaning.  
C) Node ordering is crucial to reduce edge crossings and clutter.  
D) Arc diagrams arrange nodes along a line with edges drawn as arcs above.  

#### 6. Which of the following are advantages of using adjacency matrix representations for network visualization?  
A) They avoid edge crossings even in very dense networks.  
B) Layout is straightforward once node ordering is chosen.  
C) They focus on edges rather than nodes.  
D) They are better suited for tasks involving path tracing.  

#### 7. In spatial data visualization, what are key considerations when using choropleth maps?  
A) Always use raw counts without normalization to show true data values.  
B) Normalize data by population or area to avoid misleading interpretations.  
C) Color choice and binning have little effect on map interpretation.  
D) Use only one variable at a time to avoid confusion.  

#### 8. Which of the following statements about cartograms are correct?  
A) Contiguous cartograms maintain region adjacency but distort shapes.  
B) Grid cartograms use uniform-sized shapes arranged in a grid approximating spatial layout.  
C) Cartograms are always easier to interpret than choropleth maps.  
D) Major distortion in cartograms can make regions unrecognizable and reduce usability.  

#### 9. When visualizing trees, which of the following are true about implicit spatial position layouts like sunburst and icicle plots?  
A) Sunburst plots use radial layout while icicle plots use rectilinear layout.  
B) They show parent-child relationships through explicit link marks.  
C) These layouts emphasize tree depth and sibling order through spatial position.  
D) Only leaf nodes are visible in sunburst plots, while icicle plots show both inner nodes and leaves.  

#### 10. Which of the following statements about dot density maps are accurate?  
A) Like choropleth maps, normalization is important to avoid showing population density instead of the attribute of interest.  
B) Dot density maps avoid the problem of non-uniform region sizes seen in choropleth maps.  
C) Rendering many dots is computationally inexpensive and fast.  
D) Each dot represents a fixed number of items, allowing quantitative interpretation.  



<br>

## Answers

#### 1. Which of the following statements correctly describe the characteristics of a tree in network data?  
A) ✓ Trees are a special case of networks where each node has exactly one parent except the root. This is the defining property of trees.  
B) ✗ Each node in a tree can have multiple parents. Trees have exactly one parent per node except the root.  
C) ✓ A tree is a network with no cycles. Trees by definition have no cycles.  
D) ✗ Trees always have bidirectional links between nodes. Links in trees are typically directed from parent to child or undirected, but not necessarily bidirectional.  

**Correct:** A, C


#### 2. In force-directed placement algorithms for node-link diagrams, which of the following are true?  
A) ✓ The algorithm iteratively moves nodes until forces reach equilibrium. This is the core iterative process.  
B) ✗ The algorithm guarantees a deterministic layout every time it runs. It is nondeterministic; different runs can produce different layouts.  
C) ✓ Links act like springs pulling connected nodes together. This models the attraction between connected nodes.  
D) ✓ Nodes repel each other like magnets. This repulsion prevents node overlap.  

**Correct:** A, C, D


#### 3. When comparing node-link diagrams and adjacency matrix representations, which of the following are accurate?  
A) ✓ Adjacency matrices scale better for large networks with many edges. Matrices avoid edge crossings and clutter.  
B) ✗ Node-link diagrams avoid edge crossings better than adjacency matrices. Matrices inherently avoid edge crossings; node-link diagrams often have many crossings.  
C) ✗ Adjacency matrices are intuitive for users with no training. They require training to interpret effectively.  
D) ✓ Node-link diagrams are better for path tracing and understanding topology. They are intuitive for following paths.  

**Correct:** A, D


#### 4. Which of the following criteria are important for producing a good node-link layout?  
A) ✓ Minimizing edge crossings and node overlaps. Reduces clutter and improves readability.  
B) ✗ Maximizing the total drawing area to spread out nodes. Usually, minimizing drawing area is preferred for compactness.  
C) ✗ Minimizing angular distance between edges connected to the same node. Actually, maximizing angular distance improves clarity.  
D) ✓ Emphasizing symmetry so similar graph structures look similar. Helps users recognize patterns.  

**Correct:** A, D


#### 5. Regarding circular layouts and arc diagrams, which statements are true?  
A) ✗ Circular layouts always produce layouts with fewer edge crossings than force-directed layouts. This is not guaranteed; force-directed layouts often reduce crossings better.  
B) ✗ These layouts encode spatial position with direct semantic meaning. Positions are often arbitrary or algorithmic, not semantically meaningful.  
C) ✓ Node ordering is crucial to reduce edge crossings and clutter. Poor ordering causes many crossings.  
D) ✓ Arc diagrams arrange nodes along a line with edges drawn as arcs above. This is the defining characteristic.  

**Correct:** C, D


#### 6. Which of the following are advantages of using adjacency matrix representations for network visualization?  
A) ✓ They avoid edge crossings even in very dense networks. Matrices have no edge crossings by design.  
B) ✓ Layout is straightforward once node ordering is chosen. The matrix layout is a simple grid.  
C) ✓ They focus on edges rather than nodes. Matrices emphasize edge presence and strength.  
D) ✗ They are better suited for tasks involving path tracing. Matrices are poor for path tracing compared to node-link diagrams.  

**Correct:** A, B, C


#### 7. In spatial data visualization, what are key considerations when using choropleth maps?  
A) ✗ Always use raw counts without normalization to show true data values. Raw counts can mislead due to population differences.  
B) ✓ Normalize data by population or area to avoid misleading interpretations. Normalization reveals true rates or densities.  
C) ✗ Color choice and binning have little effect on map interpretation. Color and binning greatly affect perception and interpretation.  
D) ✓ Use only one variable at a time to avoid confusion. Choropleths are best for single-variable visualization.  

**Correct:** B, D


#### 8. Which of the following statements about cartograms are correct?  
A) ✓ Contiguous cartograms maintain region adjacency but distort shapes. This is their defining feature.  
B) ✓ Grid cartograms use uniform-sized shapes arranged in a grid approximating spatial layout. This is how grid cartograms work.  
C) ✗ Cartograms are always easier to interpret than choropleth maps. Cartograms can be confusing due to distortion.  
D) ✓ Major distortion in cartograms can make regions unrecognizable and reduce usability. Distortion is a known drawback.  

**Correct:** A, B, D


#### 9. When visualizing trees, which of the following are true about implicit spatial position layouts like sunburst and icicle plots?  
A) ✓ Sunburst plots use radial layout while icicle plots use rectilinear layout. This is the main difference.  
B) ✗ They show parent-child relationships through explicit link marks. They rely on spatial position, not explicit links.  
C) ✓ These layouts emphasize tree depth and sibling order through spatial position. Position encodes hierarchy and order.  
D) ✗ Only leaf nodes are visible in sunburst plots, while icicle plots show both inner nodes and leaves. Both show inner nodes and leaves.  

**Correct:** A, C


#### 10. Which of the following statements about dot density maps are accurate?  
A) ✓ Like choropleth maps, normalization is important to avoid showing population density instead of the attribute of interest. Normalization prevents misleading patterns.  
B) ✓ Dot density maps avoid the problem of non-uniform region sizes seen in choropleth maps. They show distribution rather than aggregate values.  
C) ✗ Rendering many dots is computationally inexpensive and fast. Rendering many dots can be slow and resource-intensive.  
D) ✓ Each dot represents a fixed number of items, allowing quantitative interpretation. This is the core concept.  

**Correct:** A, B, D