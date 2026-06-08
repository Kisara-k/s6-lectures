## 6. Heuristics

## Study Notes

### 1. 🧠 What Are Heuristics? An Introduction

Heuristics are essentially practical rules or guidelines that help designers and evaluators create and assess user interfaces. Think of them as helpful "rules of thumb" that guide decisions to improve usability without needing to test every possible scenario. These can be broad principles grounded in theory or more practical, vendor-specific guidelines tailored to particular platforms.

In the world of user experience (UX) and interface design, heuristics serve as a quick and effective way to spot potential problems and improve how users interact with systems. Sometimes this process is called **heuristic evaluation**, where experts use these heuristics to review an interface and identify usability issues.

There are many heuristics out there—so many that an entire course could be dedicated just to them! However, this lecture focuses on two of the most influential and widely used sets:

- **Nielsen’s 10 Usability Heuristics (1994)**
- **Shneiderman and Plaisant’s 8 Golden Rules (2010)**

You will need to understand both sets well enough to explain and apply them in practical situations.


### 2. 📋 Nielsen’s 10 Usability Heuristics (1994)

Jakob Nielsen’s heuristics are some of the most famous in usability engineering. They were introduced in his book *Usability Engineering* and have become a foundational tool for evaluating user interfaces. These heuristics are broad, theoretically grounded principles that help ensure a system is easy and pleasant to use.

Here’s a detailed explanation of each:

1. **Visibility of System Status**  
   The system should always keep users informed about what is going on, through appropriate feedback within a reasonable time. For example, if a file is loading, a progress bar or spinner should show the user that the system is working.

2. **Match Between System and the Real World**  
   The interface should speak the users’ language, using familiar words, phrases, and concepts rather than technical jargon. It should follow real-world conventions so users can intuitively understand what’s happening.

3. **User Control and Freedom**  
   Users often make mistakes or want to explore. The system should allow them to easily undo or redo actions, giving them a sense of control and freedom to navigate without fear of permanent errors.

4. **Consistency and Standards**  
   Users should not have to wonder whether different words, situations, or actions mean the same thing. The interface should follow platform conventions and maintain consistency throughout.

5. **Error Prevention**  
   It’s better to design the system to prevent problems from occurring in the first place rather than just providing good error messages. For example, disabling irrelevant options or confirming destructive actions.

6. **Recognition Rather Than Recall**  
   Minimize the user’s memory load by making objects, actions, and options visible. Users shouldn’t have to remember information from one part of the interface to another.

7. **Flexibility and Efficiency of Use**  
   The system should cater to both inexperienced and experienced users by providing shortcuts or accelerators for expert users, while still being easy for beginners.

8. **Aesthetic and Minimalist Design**  
   Interfaces should not contain irrelevant or rarely needed information. Every extra unit of information competes with the relevant units and diminishes their visibility.

9. **Help Users Recognize, Diagnose, and Recover from Errors**  
   Error messages should be expressed in plain language (no codes), precisely indicate the problem, and constructively suggest a solution.

10. **Help and Documentation**  
    Even though it’s better if the system can be used without documentation, sometimes help is necessary. This help should be easy to search, focused on the user’s task, and list concrete steps to solve problems.

You can find the full list and explanations on Nielsen’s website: [Nielsen’s Heuristics](http://www.useit.com/papers/heuristic/heuristic_list.html).


### 3. ✨ Shneiderman and Plaisant’s 8 Golden Rules (2010)

Ben Shneiderman and Catherine Plaisant proposed another influential set of usability principles in their book *Designing the User Interface*. These "golden rules" are practical guidelines aimed at creating user-friendly interfaces that cater to a wide range of users.

Here’s a detailed look at each rule:

1. **Strive for Consistency**  
   Consistency in design helps users build accurate mental models. This means using the same terminology, layout, and behavior throughout the system.

2. **Cater to Universal Usability**  
   Design should accommodate a wide variety of users, including those with different skill levels, ages, and abilities. This means providing multiple ways to perform tasks and ensuring accessibility.

3. **Offer Informative Feedback**  
   Every user action should result in some feedback, so users know their input was received and what the system is doing.

4. **Design Dialogues to Yield Closure**  
   Actions should have a clear beginning, middle, and end. For example, after completing a form, the system should confirm submission so users know the task is finished.

5. **Prevent Errors**  
   Like Nielsen’s heuristics, this rule emphasizes designing systems that minimize the chance of user errors.

6. **Permit Easy Reversal of Actions**  
   Users should be able to undo or redo actions easily, which encourages exploration and reduces anxiety.

7. **Support Internal Locus of Control**  
   Users want to feel in charge of the system, not controlled by it. The interface should empower users to initiate and control actions.

8. **Reduce Short-Term Memory Load**  
   Interfaces should avoid requiring users to remember information across different screens or steps. This can be done by displaying options and instructions clearly.

These rules are found in *Designing the User Interface* (pp. 88-89) and provide a complementary perspective to Nielsen’s heuristics.


### 4. 🔍 Comparing Nielsen’s Heuristics and Shneiderman & Plaisant’s Golden Rules

Both sets of heuristics aim to improve usability but come from slightly different angles:

- **Nielsen’s heuristics** tend to focus more on the system’s behavior and how it communicates with users, emphasizing error prevention, recognition, and minimalist design.
- **Shneiderman and Plaisant’s rules** emphasize user empowerment, universal usability, and the psychological experience of interaction, such as closure and internal locus of control.

Despite differences, there is significant overlap. For example, both stress consistency, error prevention, and providing feedback. Understanding both sets gives a richer toolkit for evaluating and designing interfaces.


### 5. 🖥️ Vendor-Specific Guidelines

Beyond these general heuristics, many companies provide their own detailed guidelines tailored to their platforms. These are often more prescriptive and focused on maintaining a consistent user experience within their ecosystem.

Examples include:

- **Apple’s Mac OS X Human Interface Guidelines**  
  These guidelines provide detailed advice on designing apps that fit well with the Mac environment, focusing on aesthetics, behavior, and user expectations.  
  [Apple HIG](http://developer.apple.com/library/mac/#documentation/UserExperience/Conceptual/AppleHIGuidelines/Intro/Intro.html)

- **Microsoft’s Official User Interface Guidelines**  
  Microsoft offers extensive documentation on designing for Windows, covering everything from layout to interaction patterns.  
  [Microsoft UI Guidelines](http://msdn.microsoft.com/en-us/library/Aa511327)

These vendor-specific guidelines are useful when designing for a particular platform but are more narrow in scope compared to the broad heuristics discussed earlier.


### 6. 🕵️ Usability Inspection: Expert Evaluation Methods

Usability inspection refers to methods where experts evaluate an interface to find usability problems without involving actual users. These methods are often called "cheap and cheerful" because they are less expensive and faster than full user studies.

The key difference between usability inspection and user studies is:

- **User studies** involve real users performing tasks to observe actual behavior.
- **Usability inspection** relies on experts using their knowledge and heuristics to identify issues.

Two primary usability inspection methods are:

- **Heuristic Evaluation** (focus of this lecture)
- **Cognitive Walk-through** (not covered here)


### 7. ✅ Heuristic Evaluation: What It Is and How It Works

Heuristic evaluation is an informal but systematic method developed by Jakob Nielsen in the late 1980s. It involves usability experts reviewing an interface based on a set of heuristics (like Nielsen’s or Shneiderman’s) to identify usability problems.

Key points about heuristic evaluation:

- It is **holistic**, meaning experts look at the entire system rather than focusing on specific tasks.
- Research shows that a **single expert** is unlikely to find all usability issues.
- However, combining evaluations from **3 to 5 experts** significantly improves the coverage of problems found.
- The method is cost-effective and can be done early in the design process to catch issues before user testing.

The foundational paper for heuristic evaluation is:  
Nielsen, J. and Molich, R. (1990). *Heuristic evaluation of user interfaces*. Proceedings of CHI 1990, 249-256.  
[DOI link](http://dx.doi.org/10.1145/97243.97281)


### Summary

Heuristics are essential tools in usability design and evaluation. Nielsen’s 10 heuristics and Shneiderman & Plaisant’s 8 golden rules provide comprehensive, practical guidelines to create user-friendly interfaces. Vendor-specific guidelines add detailed, platform-focused advice. Usability inspection methods like heuristic evaluation allow experts to efficiently identify usability problems without involving users directly, making them valuable in the design process.

Understanding and applying these heuristics will help you design better interfaces and evaluate existing ones effectively.