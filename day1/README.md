# **The Framework for Solving Problems**

## **Steps to use when Solving Technical Problems**

1. Read instructions/man pages/ documentation/ articles/ books
    - Try examples given in the man pages, documentation, articles, or books.

2. Think of the Solution
    - Use all concepts to come up with relevant algorithms
    - In case of challenges, try rephrasing the problem
        - Ask:- "What am I trying to accomplish here?" | "What should my algorithm do/be?"
    - On a piece of paper, note desired input/parameter(s) & output/return/print value(s)
    - Try to run the algorithm and see if the input-output matches.
    - **`Whiteboarding`** helps take the problem out of your head onto a piece of paper.
        - It helps maintain focus and keep the mind active.
        - Use your mind to think and the paper to store ideas.
        - **`Writing ideas down gives them form (life)`**
        - Problems always seem impossible to solve when in our heads.
            - Writing them down takes their power away.
        - Consider edge cases that may cause the program to crash.
3. Ask why the code runs or does not run without looking at the error message.
    - That's why it is important to understand the concepts, vocabularies, and tools you're using.
    - Question why they exist.
    - Consider a project on bit manipulation:
        - Why is this project important?
        - Why binary?
        - Where do bits play a role?
        - How are bits connected to the machine, memory, bytes, and values of types?
    - For every project, consider why it is important to spend time on it and how it plays a role in the system or comprehension of Computer Science.
    - **`If we feel that something is important, we will spend time researching or solving it, but if is not important we won't waste time on it.`**
4. Read the error messages
    - If the code has issues and you don't understand why it won't run, examine the error message.

5. Google
    - If you still can't understand why your code doesn't work, Google it.
    - **`Caution`**: Ensure that you Google a specific question, error message, or a specific concept.
    - Beware that most solutions provided on the Internet are wrong or incomplete or both.
        - If it does not make sense, ignore it.
6. Ask for help from peers
7. Ask for help from technical mentors (this applies to students only)

## **Additional concepts**

### **Commands to work on Bash command line**

1. `awk` - used for text processing and manipulation
    - allows users to performed advanced operations on files, such as:
        - filtering
        - transforming, and
        - extracting data based on specific patterns
        - Example: to print the 2nd and 4th columns from comma-separated data,
            - `awk -F, '{prin $2, $4}' data.txt`, where `data.txt` is the file argument

2. `basename` - used to strip the directory option from a file path, leaving only the file name.
    - Example: let's say you have a file path `/home/user/Documents/juicy.png`,
        - Running `basename /home/user/Documents/juicy.png` will output `juicy.png`

3. `bg` - used to resume a suspended job or process in the background.
    - jobs are suspended using `Ctrl+Z`
    - typing `bg` resumes the suspended job.
