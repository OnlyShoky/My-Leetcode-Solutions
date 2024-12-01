@echo off
:: Define categories with numbering
set categories=01_Arrays_and_Hashing 02_Two_Pointers 03_Sliding_Window 04_Stack 05_Binary_Search 06_Linked_List 07_Trees 08_Heap_Priority_Queue 09_Backtracking 10_Tries 11_Graphs 12_Advanced_Graphs 13_1D_Dynamic_Programming 14_2D_Dynamic_Programming 15_Greedy 16_Intervals 17_Math_Geometry 18_Bit_Manipulation

:: Directory to save notebooks
set output_dir=LeetCode_Notebooks
mkdir %output_dir%

:: Loop through categories and create .ipynb files
for %%c in (%categories%) do (
    echo Creating %%c.ipynb
    (
        echo {
        echo     "cells": [],
        echo     "metadata": {
        echo         "kernelspec": {
        echo             "display_name": "Python 3",
        echo             "language": "python",
        echo             "name": "python3"
        echo         },
        echo         "language_info": {
        echo             "name": "python",
        echo             "version": "3.8"
        echo         }
        echo     },
        echo     "nbformat": 4,
        echo     "nbformat_minor": 5
        echo }
    ) > "%output_dir%\%%c.ipynb"
)

echo Done! All notebooks created in the %output_dir% folder.
pause
