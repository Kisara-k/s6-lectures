## 4. Task Abstraction

## Study Notes

### 1. 🔍 Introduction to Task Abstraction in Visualization Analysis & Design

When designing visualizations, one of the most important steps is **task abstraction**. This means taking the specific, detailed problems and questions from a particular domain (like healthcare, finance, or social media) and translating them into more general, simplified tasks that can guide the design of visualization tools. Task abstraction helps us understand *what* users want to do with their data and *why*, without getting lost in the complex jargon or specifics of the domain.

The goal is to create a clear, generalized vocabulary of tasks and data types that can be applied across different domains. This makes it easier to design visualization techniques that are flexible and effective for a wide range of users and problems.


### 2. 🏞️ From Domain to Abstraction: Understanding the Starting Point

Every visualization project begins with a **domain characterization**. This means understanding the specific context where the visualization will be used:

- **Who are the users?** Are they experts, casual users, or newcomers?
- **What is the target domain?** For example, is it biology, finance, or social networks?
- **What questions or problems do users have?** What do they want to learn or solve?

This domain knowledge is often very detailed and specific. However, to design effective visualizations, we need to **break down these domain-specific questions into simpler, more abstract tasks**. This process involves two key steps:

1. **Task abstraction:** Identifying the general types of tasks users want to perform.
2. **Data abstraction:** Understanding the types of data involved and how they support these tasks.

By mapping the domain-specific language (the jargon and detailed questions) into these abstract tasks and data types, we create a bridge between the real-world problems and the visualization design process.


### 3. 🎯 Task Abstraction: Actions and Targets

At the heart of task abstraction is the idea of **actions** and **targets**:

- **Actions** are what the user wants to *do* with the data.
- **Targets** are the *things* the user wants to act upon.

Together, these form pairs like `{action, target}`, which describe the core tasks users perform. For example:

- **Discover distribution:** The action is "discover," and the target is "distribution" (how data values are spread out).
- **Compare trends:** The action is "compare," and the target is "trends" (patterns over time).
- **Locate outliers:** The action is "locate," and the target is "outliers" (data points that stand out).

These pairs provide a high-level vocabulary for describing user tasks in a way that is independent of any specific domain.


### 4. 🔄 The Design Process: Mapping Domain to Abstraction and Back

The process of designing a visualization system involves several iterative steps:

1. **Characterize the domain situation:** Understand users, their questions, and data.
2. **Map domain-language tasks to abstract tasks:** Translate specific questions into general task categories.
3. **Identify or create suitable idioms or techniques:** Choose or develop visualization methods that support these abstract tasks.
4. **Map domain-language data descriptions to data abstractions:** Simplify and generalize the data types.
5. **Identify or create suitable algorithms:** Develop or select algorithms that can process the abstract data to support the tasks.

This process is not linear; it often requires going back and forth between understanding the domain and refining the abstractions. For example, realizing a task requires a different data representation might lead you to transform or derive new data abstractions.


### 5. 🛠️ Actions in Detail: Analyze, Search, and Query

#### Analyze

Analysis involves *consuming* data to gain insights. It can be split into two classic modes:

- **Discover (Explore):** Users investigate data to find unknown patterns or insights. This is often an open-ended, exploratory process.
- **Present (Explain):** Users communicate known findings, often in a more structured and clear way.

There are also other types of analysis actions:

- **Enjoy:** Casual or social interaction with data, often by newcomers or non-experts.
- **Produce:** Creating new data or annotations, such as recording observations or deriving new data from existing sources.

#### Search

Search actions depend on what the user already knows:

- **Lookup:** Finding a known item by a known key, like looking up a word in a dictionary.
- **Locate:** Finding an item when you know what it looks like but not exactly where it is, like finding your keys in the house.
- **Browse:** Scanning through data without a specific target, like browsing books in a bookstore.
- **Explore:** More open-ended searching, like discovering a new neighborhood in a city.

#### Query

Query actions focus on how much of the data the user wants to consider:

- **Identify (one):** Find a specific item or value.
- **Compare (some):** Look at a few items to understand differences or similarities.
- **Summarize (all):** Understand the overall picture or aggregate information.

These three levels (analyze, search, query) are independent and can be combined in various ways depending on the user's needs.


### 6. 🎯 Targets in Task Abstraction: What Are We Acting On?

Targets are the objects or data elements that users want to interact with. They can be:

- Individual data points
- Groups or subsets of data
- Patterns or distributions
- Trends over time
- Outliers or anomalies
- Topological structures (like networks or spatial layouts)

When abstracting tasks, it’s important to **remove domain-specific jargon** and express targets in general terms. For example, instead of saying "genes" in a biology domain, you might say "nodes" or "entities" in a network.

The interplay between task and data abstraction is crucial: understanding the targets helps define what data abstractions are needed, and sometimes the data abstraction influences how tasks are defined or refined.


### 7. 🔄 Iteration Between Task and Data Abstraction

Task abstraction and data abstraction are tightly linked and often require multiple iterations:

- You start with a first pass at understanding the data and tasks.
- This leads to an initial abstraction of tasks and data.
- As you design, you might realize that the data needs to be transformed or derived differently to support the tasks.
- You then revise the data abstraction and possibly the task abstraction.
- This iterative process continues until you have a clear, workable set of abstract tasks and data types that guide your visualization design.


### Summary

Task abstraction is a foundational step in visualization design that helps translate complex, domain-specific problems into general, understandable tasks. By focusing on **actions** (like analyze, search, query) and **targets** (the data elements acted upon), designers can create flexible visualization tools that meet users’ needs across many domains. This process requires careful domain characterization, iterative mapping between domain language and abstraction, and a clear understanding of both tasks and data. Through this approach, visualization design becomes more systematic, user-centered, and effective.