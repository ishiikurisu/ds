# PROMETHEE-ROC Add In for Excel

This project implements the PROMETHEE-ROC decision model as an Excel macro.
It consists of 2 folders:

- The [`ProRoc`](/ProRoc) project, implementing the required functions for the
model. It consists of a C# shared library using ExcelDNA to enable the use of
PROMETHEE-ROC macros in Microsoft Excel.
- The [`ProRocTest`](/ProRocTest) project, a TDD suite for validating the
implementation using NUnit.

## WARNING

This project is still in experimental stage and should not be used **unless
you know what you are doing**.
