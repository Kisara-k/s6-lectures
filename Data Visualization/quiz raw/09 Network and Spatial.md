## 10. Network and Spatial

## Questions

#### 1. Which of the following are typical topology-based tasks in network visualization?  
A) Finding distributions of node attributes  
B) Finding paths between nodes  
C) Identifying clusters or communities  
D) Comparing centrality or importance measures  

#### 2. In force-directed placement algorithms for node-link diagrams, which statements about the forces involved are true?  
A) The algorithm iteratively moves nodes until equilibrium is reached  
B) The algorithm guarantees a deterministic layout every run  
C) Links act like springs pulling connected nodes together  
D) Nodes act like magnets repulsing each other  

#### 3. What are the main challenges or criteria conflicts when designing good node-link layouts?  
A) Minimizing edge crossings often conflicts with minimizing drawing area  
B) Most layout criteria are NP-hard to optimize individually  
C) Maximizing angular distance between edges can conflict with minimizing edge bends  
D) Minimizing node overlaps always improves layout symmetry  

#### 4. Regarding adjacency matrix representations of networks, which statements are correct?  
A) They inherently encode spatial position semantics of nodes  
B) They scale well to networks with millions of edges without edge crossings  
C) Node ordering is crucial to reduce clutter and reveal patterns  
D) They are better suited for topology tasks related to neighborhoods than path tracing  

#### 5. Which of the following are advantages of node-link diagrams compared to adjacency matrices?  
A) Flexible layouts that require no training to interpret  
B) Better scalability for very large networks with millions of edges  
C) Intuitive and familiar for path tracing and topology understanding  
D) Emphasize edges over nodes for detailed edge analysis  

#### 6. In tree visualizations, what are the key differences between treemaps and sunburst plots?  
A) Treemaps use area containment with rectilinear layout, sunbursts use radial layout  
B) Treemaps emphasize parent-child containment via size, sunbursts emphasize position only  
C) Both use explicit link marks to show parent-child relationships  
D) Sunbursts show only leaf nodes, treemaps show both inner nodes and leaves  

#### 7. Which statements about choropleth maps are true?  
A) They can mislead if raw counts are shown without normalization by population  
B) They are best used when spatial relationships are central to the task  
C) They allow encoding multiple variables simultaneously on the same map  
D) They encode quantitative attributes using color on geographic regions  

#### 8. What are the main pros and cons of symbol maps compared to choropleth maps?  
A) Symbol maps can suffer from occlusion and overlap of symbols  
B) Symbol maps require less explanation or training than choropleth maps  
C) Symbol maps always preserve the original spatial geometry better than choropleths  
D) Symbol maps mitigate region size bias by encoding attribute value in symbol size  

#### 9. Which of the following statements about cartograms are correct?  
A) Cartograms are easy to interpret without prior familiarity with the original map  
B) Major distortions in cartograms can make regions unrecognizable and reduce usability  
C) Contiguous cartograms maintain region adjacency but distort shape and position  
D) Grid cartograms use uniform-sized shapes arranged in a rectilinear grid approximating spatial position  

#### 10. Regarding dot density maps, which statements are accurate?  
A) They are perceptually effective for extracting exact quantities from the data  
B) They visualize spatial distribution by placing dots where each dot represents a fixed quantity  
C) They avoid the problem of non-uniform region sizes found in choropleth maps  
D) Rendering performance can be a challenge when many dots are required  



<br>

## Answers

#### 1. Which of the following are typical topology-based tasks in network visualization?  
A) ✗ Finding distributions of node attributes is attribute-based, not topology-based.  
B) ✓ Find paths between nodes is a classic topology task involving connectivity.  
C) ✓ Identifying clusters or communities relies on network structure, a topology task.  
D) ✓ Comparing centrality or importance measures depends on network topology.  

**Correct:** B, C, D


#### 2. In force-directed placement algorithms for node-link diagrams, which statements about the forces involved are true?  
A) ✓ The algorithm iteratively moves nodes until forces balance at equilibrium.  
B) ✗ The algorithm is nondeterministic; layouts vary between runs due to random initialization.  
C) ✓ Links modeled as springs pulling connected nodes together is fundamental to the algorithm.  
D) ✓ Nodes modeled as magnets repulsing each other prevents node overlap.  

**Correct:** A, C, D


#### 3. What are the main challenges or criteria conflicts when designing good node-link layouts?  
A) ✓ Minimizing edge crossings can conflict with minimizing drawing area, as tighter layouts may increase crossings.  
B) ✓ Most layout criteria are NP-hard individually, making optimization challenging.  
C) ✓ Maximizing angular distance between edges can conflict with minimizing edge bends, as both affect edge geometry.  
D) ✗ Minimizing node overlaps does not always improve symmetry; symmetry is a separate aesthetic criterion.  

**Correct:** A, B, C


#### 4. Regarding adjacency matrix representations of networks, which statements are correct?  
A) ✗ Matrices do not encode spatial position semantics; layout is abstract and depends on ordering.  
B) ✗ While matrices scale better than node-link for edges, millions of edges still pose challenges without edge crossing.  
C) ✓ Node ordering is crucial to reduce clutter and reveal structural patterns in the matrix.  
D) ✓ Matrices are good for neighborhood-related topology tasks but poor for path tracing.  

**Correct:** C, D


#### 5. Which of the following are advantages of node-link diagrams compared to adjacency matrices?  
A) ✓ Flexible layouts require no training, making node-link diagrams accessible.  
B) ✗ Node-link diagrams do not scale well to very large networks with millions of edges due to clutter.  
C) ✓ Node-link diagrams are intuitive and familiar for path tracing and topology understanding.  
D) ✗ Node-link diagrams emphasize nodes and their connections, not edges over nodes.  

**Correct:** A, C


#### 6. In tree visualizations, what are the key differences between treemaps and sunburst plots?  
A) ✓ Treemaps use rectilinear area containment; sunbursts use radial layout.  
B) ✓ Treemaps emphasize size-based containment; sunbursts emphasize position to show hierarchy.  
C) ✗ Neither treemaps nor sunbursts use explicit link marks; they rely on containment or position.  
D) ✗ Sunbursts show both inner nodes and leaves, not only leaves.  

**Correct:** A, B


#### 7. Which statements about choropleth maps are true?  
A) ✓ Showing raw counts without normalization can mislead due to population distribution effects.  
B) ✓ They are best when spatial relationships are central to the analysis task.  
C) ✗ Choropleths typically show only one variable at a time; multiple variables cause confusion.  
D) ✓ Choropleths encode quantitative attributes using color on geographic regions.  

**Correct:** A, B, D


#### 8. What are the main pros and cons of symbol maps compared to choropleth maps?  
A) ✓ Symbol maps can suffer from occlusion and overlap of symbols, especially in dense areas.  
B) ✗ Complex glyphs in symbol maps may require explanation or training, unlike simple choropleths.  
C) ✗ Both symbol maps and choropleths preserve spatial geometry; symbol maps do not inherently preserve it better.  
D) ✓ Symbol maps mitigate region size bias by encoding attribute value in symbol size.  

**Correct:** A, D


#### 9. Which of the following statements about cartograms are correct?  
A) ✗ Cartograms require familiarity with the original map; they are not easy to interpret without it.  
B) ✓ Major distortions can make regions unrecognizable, reducing usability and aesthetic appeal.  
C) ✓ Contiguous cartograms maintain adjacency but distort shape and position to reflect data values.  
D) ✓ Grid cartograms use uniform-sized shapes arranged in a grid approximating spatial layout.  

**Correct:** B, C, D


#### 10. Regarding dot density maps, which statements are accurate?  
A) ✗ They are perceptually poor for extracting exact quantities; dots are better for pattern recognition.  
B) ✓ Dot density maps place dots where each dot represents a fixed quantity to show distribution.  
C) ✓ They avoid non-uniform region size problems found in choropleth maps by using dots instead of areas.  
D) ✓ Rendering many dots can be slow, posing performance challenges.  

**Correct:** B, C, D