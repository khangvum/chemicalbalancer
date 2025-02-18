# chemicalbalancer

A Python program that **_balances chemical equations_** by determining the correct stoichiometric coefficients for each reactant and product.

## Features

-   Accepts chemical equations in a **_familiar format_** (_e.g._ `Fe3O4 + HNO3 -> Fe(NO3)2 + Fe(NO3)3 + H2O`).
-   Decomposes compounds into **_individual elements_** and their respective **_counts_**.
-   Correctly processes compounds with **_parentheses_** (`()`) and **_brackets_** (`[]`) to account for **_nested groups_** and their multipliers.

## Matrix Algebra for Balancing Equations

Chemical equation balancing can be formulated as a **_system of linear equations_**, which can be solved using **_matrix algebra_**. The process involves the following steps:

1.  **Representing the Equation as a Matrix**

Each chemical equation is **_parsed_** and then **_represented_** as a **_coefficient matrix_** where:

-   **_Rows_** represent **_elements_** (_e.g._ $Fe$, $O$, $H$, etc.).
-   **_Columns_** represent **_compounds_** (reactants and products).
-   Each entry represents the **_number of atoms_** of a given **_element in a compound_**.
-   Example:

$$
Fe_3O_4 + HNO_3 \rightarrow Fe(NO_3)_2 + Fe(NO_3)_3 + H_2O
$$

The matrix is set up by **_counting atoms_** of each elements:

Element |Fe<sub>3</sub>O<sub>4</sub>|HNO<sub>3</sub>    |Fe(NO<sub>3</sub>)<sub>2</sub> |Fe(NO<sub>3</sub>)<sub>3</sub> |H<sub>2</sub>O
:------:|:-------------------------:|:-----------------:|:-----------------------------:|:-----------------------------:|:------------:
**Fe**  |3                          |0                  |-1                             |-1                             |0
**O**   |4                          |3                  |-6                             |-9                             |-1
**H**   |0                          |1                  |0                              |0                              |-2
**N**   |0                          |1                  |-2                             |-3                             |0

2.  **Gaussian Elimination**

The table above forms a **_system of linear equations_**, expressed as a **_matrix equation_** which needs solving: 

$$
Ax = 0
$$

where **A** is the coefficient matrix, and **x** is the vector of unknown stoichiometric coefficients.

**Step 1: Convert to Augmented Matrix Form**

Since the equation is homogeneous ($Ax = 0$), a **_zero column vector_** is appended to the matrix:

```math
\begin{bmatrix}
3 & 0 & -1 & -1 & 0 \\
4 & 3 & -6 & -9 & -1 \\
0 & 1 & 0 & 0 & -2 \\
0 & 1 & -2 & -3 & 0
\end{bmatrix}

\begin{bmatrix}
x_1 \\
x_2 \\
x_3 \\
x_4 \\
x_5
\end{bmatrix}

=

\begin{bmatrix}
0 \\
0 \\
0 \\
0
\end{bmatrix}
```

**Step 2: Transform to Reduced Row Echelon Form (RRRF)**

**_Gaussian elimination_** is applied to transform **A** into an **_RREF matrix_**, where:

-   All rows having **_only zero entries_** are at the **_bottom_**.
-   The **_leading entry_** (the left-most nonzero entry) of every nonzero row, called the **_pivot_**, is on the **_right_** of the leading entry of every row above.
-   The **_leading entry_** in each nonzero row is **_1_** (called a **_leading one_**).
-   Each **_column_** containing a **_leading one_** has **_zeros_** in all its other entries.

After **_row reduction_**, the matrix should have a form of:

$$
\begin{bmatrix}
1 & 0 & 0 & 0 & b_1 \\
0 & 1 & 0 & 0 & b_2 \\
0 & 0 & 1 & 0 & b_3 \\
0 & 0 & 0 & 1 & b_4
\end{bmatrix}
$$

In this case, the coefficient matrix should be:

$$
\begin{bmatrix}
1 & 0 & 0 & 0 & -\frac{1}{4} \\
0 & 1 & 0 & 0 & -2 \\
0 & 0 & 1 & 0 & -\frac{1}{4} \\
0 & 0 & 0 & 1 & -\frac{1}{2}
\end{bmatrix}
$$

**Step 3: Extract the Solution**

Since the system is **_underdetermined_** (more variables than equations), some variables have to be expressed **_in terms of others_**:

$$
x_1 = \frac{1}{4} x_5, \quad x_2 = 2 x_5, \quad x_3 = \frac{1}{4} x_5, \quad x_4 = \frac{1}{2} x_5
$$

A **_free variable_** is then chosen (_e.g._ $x_5 = 1$) and substitute back to solve for integer values for all coefficients.

**Step 4: Integer Scaling**

Since coefficients cannot be in **_fractions_** or **_decimals_**, they need scaling by multiplying them by the **_least common multiple_** (**_LCM_**) of denominators to obtain the **_smallest integer solution_**.

In this case, the solution from step 3 is:

$$
\left(\frac{1}{4}, 2, \frac{1}{4}, \frac{1}{2}, 1\right)
$$

we multiply by 4 to get:

$$
\left(1,8,1,2,4\right)
$$

which are the final stoichiometric coefficients, resulting in the balanced equation:

$$
Fe_3O_4 + 8HNO_3 \rightarrow Fe(NO_3)_2 + 2Fe(NO_3)_3 + 4H_2O
$$

## Collaboration

This project is a collaboration between:

-   
-   **Khang Vu:** [manhkhang0305@gmail.com](mailto:manhkhang0305@gmail.com) 