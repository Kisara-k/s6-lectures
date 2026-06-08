## 11. Evaluation of Data Visualizations

## Study Notes

### 1. 📊 Introduction to Evaluating Data Visualizations

Data visualization is a powerful tool that helps us understand complex data by turning it into visual forms like graphs, charts, and images. However, not all visualizations are equally effective. Evaluating the quality and impact of a data visualization is essential to ensure it communicates the intended message clearly and accurately.

This lecture content focuses on two main topics:

- A **Data Visualization Checklist** to guide the creation of effective visualizations.
- A **Theoretical Model** for understanding the value and impact of visualization, including its costs, benefits, and challenges.

The goal is to help you develop visualizations that are not only visually appealing but also meaningful, accurate, and useful for decision-making.


### 2. ✅ Data Visualization Checklist: A Practical Guide

Creating a high-impact data visualization involves many details. The checklist presented here is a practical tool to rate and improve your graphs and charts. Each guideline is scored from 0 to 2 points:

- **2 points:** Guideline fully met
- **1 point:** Partially met
- **0 points:** Not met at all
- **n/a:** Not applicable (used sparingly)

#### Key Areas Covered by the Checklist

##### Text and Titles
- **Concise, descriptive titles:** Titles should be short (6-12 words), descriptive sentences that summarize the main takeaway. Placing the title in the upper left corner aligns with how Western readers scan pages.
- **Subtitles and annotations:** These add context or highlight important data points, helping viewers understand the graph better.
- **Text hierarchy and readability:** Titles are largest, followed by subtitles, labels, and axis labels. Axis labels should be at least 9-point font on paper or 20-point on screen.
- **Horizontal text:** Text should be horizontal for easy reading, except for some axis or line labels.
- **Direct data labels:** Label data points directly rather than relying on legends, which force viewers to look back and forth.
- **Sparing use of labels:** Avoid redundancy, such as labeling every axis tick and also labeling every data point numerically.

##### Arrangement and Accuracy
- **Accurate proportions:** The visual lengths or areas should match the data values. For example, bar charts should start axes at zero to avoid misleading impressions.
- **Logical data order:** Data should be ordered in a way that makes sense (e.g., time series, frequency, alphabetical).
- **Equidistant axis intervals:** Spaces between axis ticks should be uniform.
- **Two-dimensional display:** Avoid 3D effects or bevels that distort perception.
- **Free from decoration:** Remove clipart or unnecessary illustrations unless they support understanding.

##### Color Use
- **Intentional color schemes:** Use colors purposefully, such as brand colors or palettes suitable for colorblind viewers.
- **Highlight key data:** Use bright or “action” colors for important data, muted colors for less important parts.
- **Legibility in black and white:** Visualizations should still be interpretable when printed without color.
- **Colorblind-friendly:** Avoid problematic color combinations like red-green or yellow-blue touching each other.
- **Good contrast:** Text should contrast strongly with the background for readability.

##### Lines and Gridlines
- **Minimal lines:** Excessive gridlines, borders, and tick marks add clutter and distract.
- **Muted gridlines:** If used, gridlines should be faint gray, not black.
- **No border lines:** Graphs should blend into the page or slide without a bounding box.
- **Simple axes:** Use one horizontal and one vertical axis; avoid double y-axes unless absolutely necessary.

##### Overall Effectiveness
- **Highlight significant findings:** Visualizations should have a clear “so what?” or key message.
- **Appropriate graph type:** Use graph types that fit the data relationship (e.g., line graphs for time series).
- **Appropriate precision:** Use numeric precision suitable for the audience; avoid unnecessary decimals or statistical jargon for general audiences.
- **Coherent design:** All elements (text, color, arrangement) should reinforce the main takeaway.

**Summary:** Well-designed visualizations score 90-100% on this checklist, making them easier to read, interpret, and remember.


### 3. 💡 Understanding the Value of Visualization: A Theoretical Model

Beyond practical guidelines, it’s important to understand *why* visualization matters and how to assess its value. Jarke J. van Wijk proposes a model that treats visualization as a technology with costs and benefits, helping us judge its effectiveness and efficiency.

#### 3.1 Visualization as a Process

Visualization transforms raw data into images that users perceive and interpret, increasing their knowledge.

- **Data (D):** The raw information to be visualized (anything from simple numbers to complex 3D fields).
- **Specification (S):** The method, parameters, and hardware used to create the visualization.
- **Image (I):** The visual output, which can be static, animated, or even include sound or haptic feedback.
- **User perception and cognition (P):** How the user interprets the image, influenced by their prior knowledge (K) and perceptual abilities.
- **Knowledge gain (∆K):** The increase in understanding the user achieves by viewing the visualization.

Users can interactively explore data by adjusting the visualization parameters (E), which changes the specification over time.

#### 3.2 Economic Model: Costs and Benefits

To decide if a visualization method is worthwhile, we consider:

- **Costs:**
  - **Initial development cost (Ci):** Time and money to create the visualization method or tool.
  - **Initial user cost (Cu):** Time and effort for users to learn and adopt the method.
  - **Session cost (Cs):** Effort to prepare data and set up each visualization session.
  - **Exploration cost (Ce):** Time spent by users interacting with and interpreting the visualization.

- **Benefits:**
  - **Value of knowledge gained (W(∆K)):** The practical or statistical significance of insights obtained.

The total profit (value) of a visualization method is:


$$
F = nm(W(∆K) - Cs - kCe) - Ci - nCu
$$


Where:

- $n$ = number of users
- $m$ = number of sessions per user
- $k$ = number of exploration steps per session

**Interpretation:** A great visualization method is widely used (high $n$), used often (high $m$), yields valuable knowledge (high $W(∆K)$), and has low costs ($Ci, Cu, Cs, Ce$).


### 4. 🔍 Implications and Challenges in Visualization

#### 4.1 Measuring Valuable Knowledge

- **Insight is hard to quantify:** We can’t directly measure how much insight a visualization provides or its value.
- **Operational approach:** Link visualization to *actions* users take based on insights (e.g., medical decisions, stock trades).
- **Value assessment:** Estimate how visualization supports decisions and the economic impact of those decisions (e.g., time saved, errors avoided).

#### 4.2 Alternative Methods and Competition

- Visualization must be compared to other ways of extracting information, including automated methods.
- If a better or cheaper method exists, new visualization methods may not be adopted.
- Developers should justify why visualization is needed over automated analysis.
- Integration of visualization with automated data mining (Visual Analytics) is promising.

#### 4.3 High Initial Costs Limit Adoption

- Users face high upfront costs to learn and implement new visualization methods.
- Many users rely on built-in, simple visualization tools in commercial software because they are easy and cheap.
- Lack of accessible introductory resources and integration with existing workflows discourages adoption.
- Sharing costs among groups or integrating visualization into popular software can help.

#### 4.4 Subjectivity in Visualization

- Visualization outcomes depend on:
  - The chosen method and parameters (specification $S$)
  - The user’s prior knowledge and perceptual skills ($K$ and $P$)
- Different users may interpret the same visualization differently.
- Visualization is exploratory and hypothesis-generating rather than definitive proof.
- Transparency (sharing visualizations openly) helps reduce subjectivity but cannot eliminate it.

#### 4.5 Risk of Misleading Visualizations (Negative Knowledge)

- Poor choices in interpolation, scaling, or design can create artifacts or false patterns.
- Example: Interpolation in wave simulations created non-existent wave patterns.
- Expert judgment is crucial to validate visualizations.
- More published case studies on pitfalls would benefit the field.

#### 4.6 Interaction: Pros and Cons

- Interaction allows users to explore large or complex data sets by adjusting views.
- However, interaction can increase subjectivity and exploration costs.
- Developers should provide good default settings and limit unnecessary complexity.
- Interaction is essential when data cannot be fully understood in a single static image.


### 5. 🛠️ Examples of Visualization Adoption and Use

#### 5.1 Texture-Based Flow Visualization

- Developed in the 1990s to show fluid flow using dense textures.
- Despite technical advances and quality, it is rarely used in commercial CFD software.
- Reasons include:
  - Small user base ($n$)
  - High initial user costs ($Cu$)
  - Existing simpler methods suffice
  - Unclear if it provides significantly better knowledge ($∆K$)
- Demonstrates that technical quality alone does not guarantee adoption.

#### 5.2 Cushion Treemaps and SequoiaView

- Treemaps visualize hierarchical data by subdividing rectangles.
- SequoiaView, a freeware tool using cushion treemaps, has been downloaded hundreds of thousands of times.
- Success factors:
  - Large potential user base ($n$) — all PC users
  - Clear, actionable insights (finding large files to delete)
  - Low costs (free, easy to use)
  - Few alternatives for the same task
- Shows how meeting real user needs with low barriers leads to success.

#### 5.3 Presentation vs. Exploration

- Visualization is used both for exploring unknown data and for presenting known results.
- Presentation is often undervalued but is crucial for communication, marketing, and funding.
- Presentation visualizations have large audiences ($n$) with low prior knowledge ($K_0$), making them highly valuable.
- Visualization helps make complex scientific or technical results understandable and persuasive.


### 6. 🎯 Discussion: Visualization as Technology, Art, and Science

#### 6.1 Visualization as Technology

- Visualization should be judged by its utility: effectiveness and efficiency.
- Innovation is difficult; many ideas never become widely used products.
- There is a gap between research and practical adoption due to costs and incentives.
- Bridging this gap requires funding, commercial efforts, or open-source projects.
- Time alone is not enough; methods must prove their value.

#### 6.2 Visualization as Art

- Visualization can be appreciated for its aesthetic and intellectual beauty.
- Some visualizations are created as puzzles or experiments, not for practical use.
- Artistic value can inspire new ideas but may not convince users or funders.
- Elegance and simplicity are valued in both art and technology.

#### 6.3 Visualization as Science

- Visualization research should aim to develop theories, models, and laws.
- Taxonomies and classifications help organize methods and data types.
- Empirical evaluation of visualization effectiveness is crucial.
- Understanding user perception and cognition is key to improving visualization.
- Automated visualization generation and guidelines can reduce user effort.
- The field is complex and interdisciplinary, requiring ongoing research.


### 7. 📝 Conclusion: Assessing the Value of Visualization

- The value of visualization depends on perspective:
  - As **technology**, it must be effective, efficient, and cost-beneficial.
  - As **art**, it can be valuable for creativity and inspiration.
  - As **science**, it requires empirical study and theoretical grounding.
- The economic model helps explain why some visualization methods succeed and others don’t.
- Practical adoption depends on user needs, costs, and clear benefits.
- Visualization remains a vital tool for insight, communication, and decision-making, but must be carefully designed and evaluated.


**Additional Resources:**

- Stephanie Evergreen’s books and blog for practical visualization tips.
- Ann K. Emery’s blog for data presentation strategies.
- Color Brewer (colorbrewer2.org) for colorblind-friendly palettes.
- Edward Tufte’s books for principles of graphical excellence.
- Jarke van Wijk’s papers for theoretical insights on visualization value.