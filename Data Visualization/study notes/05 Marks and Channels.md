## 5. Marks and Channels

## Study Notes

### 1. 🎨 Introduction to Marks and Channels in Visualization

When we create visualizations, we need a systematic way to represent data so that people can understand it easily. This is where **marks** and **channels** come in. They are the fundamental building blocks of visual encoding — the process of turning data into visual form.

- **Marks** are the basic geometric shapes or elements that represent data points or connections between data points.
- **Channels** are the visual properties that modify these marks to convey additional information, such as color, size, or position.

Understanding how marks and channels work together helps us design clear, effective visualizations that communicate data accurately and intuitively.


### 2. 🔷 Marks: The Basic Visual Elements

Marks are the geometric primitives used to represent data items or links between items. Think of marks as the "things" you see on a graph or chart.

#### Types of Marks:
- **Points:** Simple dots or small shapes representing individual data items.
- **Lines:** Used to show connections or relationships between points, such as in a network graph.
- **Areas:** Shapes like rectangles or circles that can represent quantities or categories.
- **Volumes (3D marks):** Rarely used because they are harder to interpret accurately.

#### Key Characteristics of Marks:
- Marks have **dimensions** (length, width, area) that can be used to encode data.
- Different marks impose different constraints on what can be encoded. For example:
  - Points have no fixed size constraints, so you can vary their size or shape to encode extra data.
  - Lines have one dimension fixed (length), but you can vary width or color.
  - Areas have two fixed dimensions (length and width), so you cannot use size or shape to encode more data without confusion.

#### Interlocking Areas:
Sometimes areas can be nested or interlocked to show containment or grouping, like Venn diagrams or bubble sets.


### 3. 🌈 Channels: How Marks Change to Show Data

Channels control the **appearance** of marks. They change how marks look based on the data attributes they represent. For example, a point might change color or size depending on the value it represents.

#### What Are Channels?
- Also called **visual variables**, **retinal channels**, or **visual dimensions**.
- Examples include position, color (hue, saturation, brightness), size, shape, orientation, and texture.

#### Why Channels Matter:
- Different channels can convey different types of information.
- Some channels are better suited for certain data types (categorical, ordinal, quantitative).
- Channels differ in how much information they can convey and how accurately humans can perceive them.

#### Redundant Encoding:
Sometimes the same data attribute is encoded using multiple channels simultaneously (e.g., both color and size). This strengthens the message but uses up more visual resources.


### 4. 📏 Constraints and Encoding Capacity of Marks

Marks are not just shapes; they come with **constraints** that affect how much and what kind of data you can encode.

- **Points:** No fixed size, so you can encode multiple attributes by changing size, shape, or color.
- **Lines:** Length is usually fixed by the data relationship, but width or color can encode other attributes.
- **Areas:** Both length and width are fixed, so you cannot use size or shape to encode additional data without confusion.

A quick way to check if you can encode another attribute with size or shape is to ask: *Is size or shape already being used for something else?* If yes, you cannot reuse it without causing confusion.


### 5. 📊 When and How to Use Different Channels

Choosing the right channel depends on two main factors:

#### 1. Expressiveness
- How well does the channel match the type of data?
- For example, position is great for quantitative data because it can show precise values.
- Color hue is better for categorical data because it can distinguish different groups.

#### 2. Effectiveness
- How accurately can people perceive differences in this channel?
- Some channels allow very precise judgments (like position or length).
- Others are less precise (like color saturation or shape).

#### Grouping Channels
Channels can also help group data visually by:
- **Containment:** Using areas or boundaries to group items.
- **Connection:** Using lines or links.
- **Proximity:** Placing related items close together.
- **Similarity:** Using similar colors or shapes to indicate related categories.


### 6. 🎯 Channel Effectiveness: How Well Can We Perceive Data?

Effectiveness of channels is about how well humans can interpret the encoded data. There are several important concepts here:

#### Accuracy
- How precisely can we tell the difference between values encoded by a channel?
- For example, length is very accurate because we can judge linear differences well.
- Other channels like color hue or saturation are less precise.

#### Discriminability
- How many distinct steps or levels can we reliably perceive in a channel?
- For example, line width can only show a few distinct levels before differences become hard to see.

#### Separability
- Can we perceive one channel independently of others?
- Some channels interfere with each other, making it harder to interpret combined encodings.

#### Popout
- Some channels allow certain items to "pop out" immediately from a group, making them easy to spot.
- For example, a red dot among blue dots pops out quickly.
- Popout happens because of parallel processing in our visual system.


### 7. 🔍 Factors Affecting Perceptual Accuracy

Several factors influence how accurately we can interpret visual encodings:

- **Alignment:** When marks are aligned on a common scale, it’s easier to compare them.
- **Distractors:** The presence of many other marks can make it harder to judge differences.
- **Distance:** The spatial distance between marks affects perception.
- **Common Scale:** Using a shared scale or frame improves relative judgments.

#### Relative vs. Absolute Judgments
Our perception is mostly **relative**, not absolute. This means we judge differences based on context rather than exact values.

- For example, Weber’s Law states that the smallest noticeable difference is proportional to the background level.
- This is why aligned scales and common frames improve accuracy.


### 8. 🌟 Special Notes on Color and Luminance

#### Relative Luminance Judgments
- Our perception of brightness depends on the contrast with surrounding areas.
- This is why optical illusions like the checker shadow illusion trick our brains.

#### Relative Color Judgments
- Our visual system maintains **color constancy**, meaning we perceive colors as stable even under different lighting conditions.
- This helps us recognize objects consistently but can complicate precise color encoding.


### Summary

- **Marks** are the geometric shapes representing data points or links.
- **Channels** modify marks’ appearance to encode data attributes.
- Different marks have different constraints on what can be encoded.
- Choosing the right channel depends on the data type and how effectively humans can perceive differences.
- Position and length are among the most accurate channels.
- Color and shape are useful for categorical data but less precise for quantitative data.
- Our perception is mostly relative, so alignment and common scales improve accuracy.
- Understanding marks and channels is essential for designing clear, effective visualizations.