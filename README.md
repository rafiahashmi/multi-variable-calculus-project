# 📐 Multi-Variable Directional Derivative Calculator

An interactive, textbook-grade engineering tool designed to compute and visualize the instantaneous rate of change of any multi-variable function $f(x, y)$ along a specified direction vector $\mathbf{v}$. 

Built with an isolated, object-oriented math engine using **SymPy** for pure symbolic evaluation and wrapped in a clean web application using **Streamlit**.

---

## 📌 Project Architecture & Core Features

Unlike standard calculators that perform aggressive numerical rounding early in execution, this project uses an enterprise-inspired separation of concerns:

* **Pure Symbolic Engine:** Retains exact fractions, square roots, and trigonometric representations until the final evaluation step, eliminating floating-point errors inside complex LaTeX readouts.
* **Textbook-Grade LaTeX Rendering:** Dynamically formats multi-line mathematical proofs for gradient evaluation, vector normalization, and dot product steps.
* **Built-in Error Handling:** Gracefully handles invalid mathematical strings and intercepts zero-vector operations ($\langle 0, 0 \rangle$) to prevent system crashes.

---

## 🧭 Visualizing the Math

The directional derivative $D_{\mathbf{u}}f$ represents the slope of the surface $z = f(x, y)$ when moving directly in the direction of a normalized unit vector $\mathbf{u}$ from a specific point context:

![Directional Derivative Geometric Context](https://s3-us-west-2.amazonaws.com/courses-images/wp-content/uploads/sites/5667/2021/09/23010025/4-6-1.jpeg)

*The engine calculates the gradient vector $\nabla f(x, y)$, normalizes the direction vector $\mathbf{v}$ to a unit vector $\mathbf{u}$, and computes their dot product $D_{\mathbf{u}}f = \nabla f \cdot \mathbf{u}$.*

---

## 🚀 Getting Started

### Prerequisites
Make sure you have Python 3.8+ installed along with the required analytical and interface packages:
```bash
pip install streamlit sympy
