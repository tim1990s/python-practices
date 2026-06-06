# Lesson Generation Rules

This project treats curriculum content as code. Every generated lesson, exercise,
solution, and example must be derived from the specification files in
`specs/curriculum/`, the canonical lesson format in `specs/lesson-template.md`,
and the rules in this file.

## Source Of Truth

- Curriculum modules live in `specs/curriculum/`.
- Each module contains learning goals, Python topics, exercise types,
  prerequisites, difficulty range, and a machine-readable exercise catalog.
- Specifications must not contain full solutions.
- Generated files must be reproducible by running `python tools/generate.py`.
- Generated output should not be edited manually. Change specs or generator rules
  instead, then regenerate.

## Required Lesson Sections

Every lesson must follow `specs/lesson-template.md` exactly and include these
sections in order:

- Lesson Title
- Learning Objectives
- Theory
- Mathematical Background
- Problem Statement
- Input
- Output
- Example
- Algorithm
- Pseudocode
- Python Solution
- Code Explanation
- Complexity Analysis
- Common Mistakes
- Additional Exercises
- Further Reading

## Lesson Quality Rules

Every generated lesson must:

- be written for beginners who have just started learning Python;
- contain at least 1000 words;
- explain the related Python theory before showing code;
- explain the mathematical background or logical reasoning behind the problem;
- include a real-world analogy or practical motivation;
- include a clear problem statement;
- describe input and output precisely;
- include at least one sample input and output;
- include a step-by-step algorithm;
- include pseudocode before Python code;
- include a complete Python 3 solution;
- explain important lines of code in plain language;
- include time complexity and space complexity;
- include common mistakes and how to avoid them;
- include additional exercises that extend the original problem;
- avoid presenting code as the only learning material.

## Solution Quality Rules

Every generated solution must:

- be a standalone Python 3 file;
- follow PEP 8 naming and formatting conventions;
- use type hints where they improve readability;
- read from standard input and write to standard output;
- keep parsing logic simple and explicit;
- contain comments that explain non-obvious steps;
- avoid unnecessary dependencies;
- be easy for a beginner to run and modify.

## Example File Rules

Every generated example file must include:

- Sample Input
- Sample Output
- Explanation

Examples must match the behavior of the generated Python solution.

## Exercise File Rules

Every generated exercise file must include:

- exercise id and title;
- module name;
- difficulty;
- prerequisites;
- Python topics;
- math or reasoning topics;
- problem statement;
- input format;
- output format;
- sample input and output;
- no Python solution.

## Naming Rules

Generated lesson, exercise, solution, and example files must use this naming
format:

```text
NNN-kebab-case-slug.md
NNN-kebab-case-slug.py
NNN-kebab-case-slug-examples.md
```

Where `NNN` is a zero-padded numeric exercise id.

## Regeneration Rules

The generator must:

- recreate `generated/lessons/`, `generated/exercises/`,
  `generated/solutions/`, and `generated/examples/`;
- parse exercise catalogs from curriculum specs;
- fail loudly if duplicate ids or slugs are found;
- fail loudly if a required field is missing;
- validate that lesson word count is at least 1000 words;
- validate that every solution file can be compiled by Python.
