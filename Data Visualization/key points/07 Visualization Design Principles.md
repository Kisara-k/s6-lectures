## 8. Visualization Design Principles

## Key Points

#### 1. 📊 Tufte’s Principles of Effective Visualizations  
- Edward R. Tufte is a pioneer in data visualization and authored key books including *The Visual Display of Quantitative Information* (2001) and *Envisioning Information* (1990).  
- The core mantra: **Above all else, show the data.**  
- Visualizations should showcase the data itself, avoiding unnecessary embellishments or distractions.

#### 2. 🖋️ Data-Ink Ratio  
- **Data ink** is the ink used in a graphic that represents actual data.  
- The **Data-Ink Ratio** formula:  

$$
  \text{Data-Ink Ratio} = \frac{\text{Data Ink}}{\text{Total Ink Used to Print the Graphic}}
$$
  
- Maximizing data-ink ratio means erasing non-data ink and redundant data ink to focus on the core data.  
- A data-ink ratio close to 1 indicates an ideal graph with minimal non-data ink.

#### 3. 📈 Data Density  
- **Data density** is the number of data entries per unit area of the graphic:  

$$
  \text{Data Density} = \frac{\text{Number of Entries in Data Matrix}}{\text{Area of Data Graphic}}
$$
  
- High data density allows more information to be displayed in limited space without sacrificing clarity.  
- Techniques to increase data density include small multiples, sparklines, and layering information.

#### 4. 🔍 Context and Comparisons  
- Providing context (benchmarks, historical trends, comparative data) helps viewers understand the significance of the data.  
- Context enables effective comparisons and better interpretation.

#### 5. ⚖️ Integrity and Accuracy  
- Visual representation must be proportional to numerical data values.  
- The **Lie Factor** measures distortion:  

$$
  \text{Lie Factor} = \frac{\text{Size of Effect Shown in Graphic}}{\text{Size of Effect in Data}}
$$
  
- Lie Factor ≈ 1 means accurate representation; values >1.05 or <0.95 indicate distortion.  
- Six principles of graphical integrity include proportional representation, clear labeling, showing data variation not design variation, using deflated monetary units in time series, matching variable dimensions, and avoiding quoting data out of context.

#### 6. 🖱️ Interactivity and Exploration  
- Interactive visualizations (dashboards, zoomable charts, drill-downs) empower users to explore data and discover insights.  
- Interactivity supports personalized data analysis.

#### 7. ♿ Universal Accessibility  
- Visualizations should be accessible to all, including people with disabilities.  
- Consider color blindness types: protanopia, deuteranopia, and tritanopia.  
- Use color schemes and text readability that accommodate these conditions.  
- Provide alternative text for images.

#### 8. 🏞️ 2D vs. 3D Visualization  
- 3D visualizations often cause perspective distortion, occlusion, and legibility problems.  
- 3D is justified mainly for true 3D spatial data and shape perception tasks.  
- For abstract data, 2D visualizations are usually clearer and more effective.  
- Tilted text in 3D is less legible.  
- Extruded 3D curves make detailed comparisons difficult.

#### 9. 👁️ Eyes Beat Memory  
- It is easier to compare data by moving eyes between side-by-side views than by relying on memory.  
- Small multiples are preferred over animations for detailed comparisons.  
- Animation is better suited for storytelling or transitions between two states.

#### 10. 🖥️ Resolution Beats Immersion  
- High resolution (more pixels) is more important than immersive technologies (VR/AR) for abstract data visualization.  
- Desktop environments are better for workflow integration.  
- Immersion adds cognitive load and is rarely justified for abstract data.

#### 11. 🔍 Overview, Zoom, Filter, Details on Demand  
- Shneiderman’s mantra for interactive visualization:  
  - Provide an overview (summary).  
  - Allow zooming and filtering of data.  
  - Offer details on demand.  
- Responsiveness is critical, with different response times needed for perception (0.1s), interaction (1s), and longer tasks (10s).

#### 12. 🎨 Function First, Form Next  
- Visualization design should start with function (clarity, accuracy, usefulness).  
- Aesthetics come later as refinement.  
- Visual hierarchy, alignment, and Gestalt principles improve aesthetics without sacrificing function.  
- Collaboration with graphic designers is recommended if design expertise is lacking.



<br>

