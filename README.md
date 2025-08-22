# Tumour-Mutation-Clustering-Using-Divide-and-Conquer-Convex-Hull-Algorithm-
**Author:** Samitha Leslie  

---

## Overview
This project demonstrates how **divide-and-conquer** algorithms can be applied to **cancer genomics** by clustering tumor mutation data using a **Convex Hull algorithm**. The goal is to visualize mutation patterns and identify tumor clusters, providing insights that could support cancer research.

---

## Problem Statement
- Cancer genomic datasets are often large and complex.
- Clustering tumor mutation patterns can reveal biologically significant groups.
- Convex hulls provide a minimal enclosing boundary to visualize and segment genomic data efficiently.

---

## Algorithmic Approach
- **Divide Step:** Split the dataset into two halves.
- **Conquer Step:** Recursively compute convex hulls for each half.
- **Combine Step:** Merge the two hulls using a custom `merge_hulls()` procedure.

**Key Features:**
- Efficient **O(n log n)** performance using divide-and-conquer.
- Uses **optimal substructure** property and recursion.
- Handles missing values using `.dropna()` for clean input data.

---

## Dataset
- **Inputs:** 
  - X-axis: Mutation Count
  - Y-axis: Overall Survival (Months)
- **Format:** CSV file containing tumor genomic data.
- Missing values are removed before computation.

---

## Implementation
- **Language:** Python  
- **Libraries:** `pandas`, `matplotlib`  
- **Environment:** Google Colab (drive mounting for data access)

### Core Steps:
1. Load mutation-survival data from CSV.
2. Preprocess data and remove missing values.
3. Sort points lexicographically (x, then y).
4. Apply **divide-and-conquer convex hull algorithm**:
   ```python
   convex_hull = divide_and_conquer(points)
