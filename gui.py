import streamlit as st
import sympy as sp


# -----------------------------------------------------------------------------
# CORE LOGIC ENGINE (Backend)
# -----------------------------------------------------------------------------
class DirectionalDerivativeCalculator:
    """Handles exact symbolic multi-variable derivative math using SymPy."""

    def __init__(self):
        self.x, self.y = sp.symbols('x y')
        self.f = None
        self.fx = None
        self.fy = None

    def parse_function(self, expr_str: str):
        """Converts raw string input to exact SymPy expression and gradients."""
        self.f = sp.sympify(expr_str)
        self.fx = sp.diff(self.f, self.x)  # ∂f/∂x
        self.fy = sp.diff(self.f, self.y)  # ∂f/∂y
        return self.f, self.fx, self.fy

    def calculate(self, x0: float, y0: float, a: float, b: float):
        """Performs precise symbolic evaluation and directional derivative calculation."""
        # Exact symbolic evaluations
        fx_val = self.fx.subs({self.x: x0, self.y: y0})
        fy_val = self.fy.subs({self.x: x0, self.y: y0})

        # Vector operations (exact)
        a_sym, b_sym = sp.sympify(a), sp.sympify(b)
        magnitude = sp.sqrt(a_sym**2 + b_sym**2)
        u1 = a_sym / magnitude
        u2 = b_sym / magnitude

        # Dot product: ∇f · u (exact)
        duf_exact = (fx_val * u1) + (fy_val * u2)

        return {
            "fx_val": fx_val,
            "fy_val": fy_val,
            "magnitude": magnitude,
            "u1": u1,
            "u2": u2,
            "duf_exact": duf_exact,
            "duf_float": float(duf_exact.evalf())
        }

# -----------------------------------------------------------------------------
# USER INTERFACE (Frontend)
# -----------------------------------------------------------------------------
st.set_page_config(page_title="Directional Derivative Calculator", page_icon="📐", layout="centered")

st.title("📐 Directional Derivative Calculator")
st.markdown("Compute the instantaneous rate of change of a multi-variable function $f(x,y)$ along a vector direction.")
st.markdown("---")

calculator = DirectionalDerivativeCalculator()

# --- Section 1: Function Definition ---
st.subheader("1. Define Function $f(x, y)$")
expr_input = st.text_input(
    "Enter an expression using 'x' and 'y' (e.g., x**2 - 3*x*y + y**3):",
    "x**2 + y**2",
    key="func_input"
)

try:
    f, fx, fy = calculator.parse_function(expr_input)

    # Render function and its gradients cleanly
    st.success(f"**Function:** $f(x, y) = {sp.latex(f)}$")

    with st.expander("View Analytical Gradient (Partial Derivatives)", expanded=True):
        col_fx, col_fy = st.columns(2)
        with col_fx:
            st.latex(f"\\frac{{\\partial f}}{{\\partial x}} = {sp.latex(fx)}")
        with col_fy:
            st.latex(f"\\frac{{\\partial f}}{{\\partial y}} = {sp.latex(fy)}")

except (sp.SympifyError, TypeError, ValueError):
    st.error("❌ Syntax Error: Please ensure you use explicit operators like `*` for multiplication (e.g., `2*x` instead of `2x`).")
    st.stop()

st.markdown("---")

# --- Section 2: Evaluation Constraints ---
st.subheader("2. Define Point Context & Direction Vector")

input_container = st.container()
with input_container:
    col_x, col_y, col_a, col_b = st.columns(4)
    with col_x:
        x0 = st.number_input("Point $x_0$", value=1.0, step=0.5)
    with col_y:
        y0 = st.number_input("Point $y_0$", value=1.0, step=0.5)
    with col_a:
        a = st.number_input("Vector $a$", value=3.0, step=0.5)
    with col_b:
        b = st.number_input("Vector $b$", value=4.0, step=0.5)

# Safety Validation
if a == 0 and b == 0:
    st.error("⚠️ Mathematical Restriction: The direction vector $\\mathbf{v}$ cannot be the zero vector $\\langle 0, 0 \\rangle$.")
    st.stop()

# --- Section 3: Step-by-Step Computational Breakdown ---
st.markdown("---")
st.subheader("3. Computational Breakdown & Evaluation")

res = calculator.calculate(x0, y0, a, b)

# A. Gradient at P
st.markdown("#### A. Gradient Evaluation at Point $P$")
st.markdown(f"Substituting $x = {x0}$ and $y = {y0}$ into $\\nabla f$:")
st.latex(f"\\nabla f({x0}, {y0}) = \\left\\langle {sp.latex(res['fx_val'])}, {sp.latex(res['fy_val'])} \\right\\rangle")

# B. Vector Normalization
st.markdown("#### B. Direction Vector Normalization")
st.markdown("To compute the directional derivative, the direction vector must be a unit vector (magnitude $= 1$):")

# FIXED: Using %s completely ignores all LaTeX curly braces
mag_str = "\\|\\mathbf{v}\\| = \\sqrt{%s^2 + (%s)^2} = %s"
st.latex(mag_str % (sp.latex(a), sp.latex(b), sp.latex(res['magnitude'])))

# FIXED: Unit Vector
u_str = "\\mathbf{u} = \\frac{\\mathbf{v}}{\\|\\mathbf{v}\\|} = \\left\\langle %s, %s \\right\\rangle"
st.latex(u_str % (sp.latex(res['u1']), sp.latex(res['u2'])))

# --- Section C: Final Dot Product ---
st.markdown("---")
st.markdown("#### C. Directional Derivative Calculation ($D_{\\mathbf{u}}f$)")
st.markdown("Applying the dot product definition: $D_{\\mathbf{u}}f = \\nabla f \\cdot \\mathbf{u}$")

# FIXED: Dot Product Breakdown
dot_str = "D_{\\mathbf{u}}f = \\left( %s \\right)\\left( %s \\right) + \\left( %s \\right)\\left( %s \\right)"
st.latex(dot_str % (
    sp.latex(res['fx_val']),
    sp.latex(res['u1']),
    sp.latex(res['fy_val']),
    sp.latex(res['u2'])
))

# FIXED: Exact Solution
exact_str = "\\text{Exact Solution: } D_{\\mathbf{u}}f = %s"
st.latex(exact_str % sp.latex(res['duf_exact']))

# Highlight Final Numerical Output

# FIXED: Final Success Message
success_str = "### **Final Approximate Value:** $D_{\\mathbf{u}}f(%s, %s) \\approx %.4f$"
st.success(success_str % (x0, y0, res['duf_float']))

st.info("💡 **Interpretation:** If you move from point $P$ strictly in the direction of vector $\\mathbf{v}$, the function's value changes at this instantaneous rate.")
