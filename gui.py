import math

import streamlit as st
import sympy as sp

# Define SymPy symbols
x, y = sp.symbols('x y')

st.title(" directional Derivative Calculator")
st.markdown("---")

st.subheader("1. Enter Function $f(x, y)$")

# --- Step 1: Function Input ---
expr_input = st.text_input(
    "Enter your function in terms of 'x' and 'y' (e.g., x**2 + y**3)",
    "x**2 + y**2",
    key="function_input"
)

try:
    # Convert input string to SymPy expression
    f = sp.sympify(expr_input)

    # Calculate partial derivatives
    fx = sp.diff(f, x)   # ∂f/∂x
    fy = sp.diff(f, y)   # ∂f/∂y

    st.success(f"Function $f(x, y) = {sp.latex(f)}$")

    st.markdown("### Partial Derivatives (Gradient):")
    st.latex(f"\\frac{{\\partial f}}{{\\partial x}} = {sp.latex(fx)}")
    st.latex(f"\\frac{{\\partial f}}{{\\partial y}} = {sp.latex(fy)}")

except (sp.SympifyError, TypeError):
    st.error("❌ Invalid function format. Please use 'x', 'y', and valid Python/SymPy syntax (e.g., x**2, sp.sin(y)).")
    st.stop() # Stop execution if function is invalid

st.markdown("---")
st.subheader("2. Enter Point $P(x_0, y_0)$ and Direction Vector $\\mathbf{v}$")

col1, col2, col3, col4 = st.columns(4)

with col1:
    x0 = st.number_input("Enter $x_0$", value=1.0, key="x0_input")
with col2:
    y0 = st.number_input("Enter $y_0$", value=1.0, key="y0_input")

st.write(f"Point $P = ({x0}, {y0})$")

with col3:
    a = st.number_input("Enter vector component $a$", value=3.0, key="a_input")
with col4:
    b = st.number_input("Enter vector component $b$", value=4.0, key="b_input")

st.write(f"Direction Vector $\\mathbf{{v}} = \\langle {a}, {b} \\rangle$")

# Check for zero vector input
if a == 0 and b == 0:
    st.warning("⚠️ The direction vector $\\mathbf{v}$ cannot be $\\langle 0, 0 \\rangle$. Please enter non-zero components.")
    st.stop()

st.markdown("---")
st.subheader("3. Results: Directional Derivative $D_{\\mathbf{u}}f$")

# --- Step 2: Evaluation ---
# Substitute values in fx and fy
fx_val_raw = fx.subs({x: x0, y: y0})
fy_val_raw = fy.subs({x: x0, y: y0})

# Evaluate to float for final calculation
fx_val = float(fx_val_raw.evalf())
fy_val = float(fy_val_raw.evalf())

st.markdown("#### A. Gradient Evaluation:")
st.latex(f"\\nabla f({x0}, {y0}) = \\left\\langle {fx_val:.4f}, {fy_val:.4f} \\right\\rangle")

# --- Step 3: Direction Vector Normalization and Final Calculation ---
mag = sp.sqrt(a**2 + b**2)
u1 = a / mag
u2 = b / mag
mag_val = float(mag.evalf())


st.markdown("#### B. Unit Direction Vector $\\mathbf{u}$:")
st.latex(f"\\text{{Magnitude }} ||\\mathbf{{v}}|| = \\sqrt{{{a}^2 + {b}^2}} = {mag_val:.4f}")
st.latex(f"\\mathbf{{u}} = \\left\\langle u_1, u_2 \\right\\rangle = \\left\\langle \\frac{{{a}}}{{{mag_val:.4f}}}, \\frac{{{b}}}{{{mag_val:.4f}}} \\right\\rangle")


# Final Calculation (Dot Product)
Duf_val = (fx_val * float(u1.evalf()) + fy_val * float(u2.evalf()))

st.markdown("#### C. Directional Derivative $D_{\\mathbf{u}}f$:")
st.latex(
    f"D_{{\\mathbf{{u}}}}f = \\nabla f \\cdot \\mathbf{{u}} = ({fx_val:.4f})\\left(\\frac{{{a}}}{{{mag_val:.4f}}}\\right) + ({fy_val:.4f})\\left(\\frac{{{b}}}{{{mag_val:.4f}}}\\right)"
)

st.success(f"**Final Result:** $D_{{\\mathbf{{u}}}}f ({x0}, {y0}) \\approx {Duf_val:.4f}$")

st.markdown("---")
st.info("This result represents the instantaneous rate of change of the function $f$ at point $P$ in the direction of vector $\\mathbf{v}$.")
