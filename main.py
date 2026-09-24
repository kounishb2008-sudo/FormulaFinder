import re
from difflib import SequenceMatcher


# ============================================================
# FORMULA DATABASE
# ============================================================

FORMULAS = {

    # ========================================================
    # MATHEMATICS
    # ========================================================

    "pythagorean_theorem": {
        "name": "Pythagorean Theorem",
        "subject": "Mathematics",
        "topic": "Geometry",

        "formula": "a² + b² = c²",

        "aliases": [
            "pythagoras theorem",
            "pythagorean theorem",
            "pythagoras formula",
            "pythagorean formula",
            "right triangle formula",
            "right angled triangle",
            "right angle triangle",
            "formula for right triangle",
            "right triangle equation",
            "triangle sides formula",
            "longest side of triangle",
            "hypotenuse formula",
            "a2+b2=c2",
            "a²+b²=c²"
        ],

        "keywords": [
            "triangle",
            "right triangle",
            "hypotenuse",
            "geometry",
            "90 degree"
        ],

        "variables": {
            "a": "First shorter side",
            "b": "Second shorter side",
            "c": "Hypotenuse"
        },

        "conditions": [
            "Works for a right-angled triangle.",
            "c must be the hypotenuse.",
            "The triangle must contain a 90° angle."
        ],

        "cases": [
            "Finding the hypotenuse",
            "Finding one of the shorter sides",
            "Checking whether a triangle is right-angled"
        ],

        "example": (
            "If a = 3 and b = 4:\n"
            "c = √(3² + 4²)\n"
            "c = √25\n"
            "c = 5"
        )
    },


    "quadratic_formula": {
        "name": "Quadratic Formula",
        "subject": "Mathematics",
        "topic": "Algebra",

        "formula": "x = (-b ± √(b² - 4ac)) / 2a",

        "aliases": [
            "quadratic formula",
            "quadratic equation formula",
            "formula for quadratic equation",
            "formula for quadratic",
            "quadratic equation",
            "solve quadratic equation",
            "ax2+bx+c",
            "ax²+bx+c"
        ],

        "keywords": [
            "quadratic",
            "equation",
            "algebra",
            "roots",
            "roots of equation"
        ],

        "variables": {
            "a": "Coefficient of x²",
            "b": "Coefficient of x",
            "c": "Constant"
        },

        "conditions": [
            "a must not be zero.",
            "Used for equations of the form ax² + bx + c = 0."
        ],

        "cases": [
            "Two real solutions",
            "One repeated real solution",
            "Two complex solutions"
        ],

        "example": (
            "For x² - 5x + 6 = 0:\n"
            "a = 1, b = -5, c = 6\n"
            "Solutions: x = 2 and x = 3"
        )
    },


    "area_circle": {
        "name": "Area of a Circle",
        "subject": "Mathematics",
        "topic": "Geometry",

        "formula": "A = πr²",

        "aliases": [
            "area of circle",
            "circle area",
            "area circle formula",
            "formula for area of circle",
            "area of a circular shape",
            "circle formula"
        ],

        "keywords": [
            "circle",
            "area",
            "radius"
        ],

        "variables": {
            "A": "Area of the circle",
            "r": "Radius",
            "π": "Pi ≈ 3.14159"
        },

        "conditions": [
            "The radius must be known."
        ],

        "cases": [
            "Finding area from radius",
            "Finding radius from area"
        ],

        "example": (
            "If r = 5 cm:\n"
            "A = π × 5²\n"
            "A ≈ 78.54 cm²"
        )
    },


    "circumference_circle": {
        "name": "Circumference of a Circle",
        "subject": "Mathematics",
        "topic": "Geometry",

        "formula": "C = 2πr",

        "aliases": [
            "circumference formula",
            "circle circumference",
            "circumference of circle",
            "circle perimeter",
            "perimeter of circle"
        ],

        "keywords": [
            "circle",
            "circumference",
            "perimeter",
            "radius"
        ],

        "variables": {
            "C": "Circumference",
            "r": "Radius",
            "π": "Pi"
        },

        "conditions": [
            "The radius or diameter must be known."
        ],

        "cases": [
            "Finding circumference from radius",
            "Finding circumference from diameter"
        ],

        "example": (
            "If r = 7 cm:\n"
            "C = 2 × π × 7\n"
            "C ≈ 43.98 cm"
        )
    },


    "simple_interest": {
        "name": "Simple Interest",
        "subject": "Mathematics",
        "topic": "Commercial Mathematics",

        "formula": "SI = (P × R × T) / 100",

        "aliases": [
            "simple interest",
            "simple interest formula",
            "interest formula",
            "si formula",
            "calculate simple interest"
        ],

        "keywords": [
            "interest",
            "principal",
            "rate",
            "time",
            "money"
        ],

        "variables": {
            "P": "Principal",
            "R": "Rate of interest",
            "T": "Time"
        },

        "conditions": [
            "Rate is generally expressed as a percentage.",
            "Time and rate should use compatible units."
        ],

        "cases": [
            "Finding simple interest",
            "Finding principal",
            "Finding rate",
            "Finding time"
        ],

        "example": (
            "P = ₹10,000, R = 5%, T = 2 years\n"
            "SI = (10000 × 5 × 2) / 100\n"
            "SI = ₹1,000"
        )
    },


    "percentage": {
        "name": "Percentage Formula",
        "subject": "Mathematics",
        "topic": "Arithmetic",

        "formula": "Percentage = (Part / Whole) × 100",

        "aliases": [
            "percentage formula",
            "percent formula",
            "percentage calculation",
            "how to calculate percentage",
            "percentage of a number"
        ],

        "keywords": [
            "percentage",
            "percent",
            "part",
            "whole"
        ],

        "variables": {
            "Part": "The portion being considered",
            "Whole": "The total amount"
        },

        "conditions": [
            "Part and whole must use the same units."
        ],

        "cases": [
            "Finding percentage",
            "Finding part",
            "Finding whole"
        ],

        "example": (
            "20 out of 50:\n"
            "Percentage = (20 / 50) × 100\n"
            "Percentage = 40%"
        )
    },


    # ========================================================
    # PHYSICS
    # ========================================================

    "speed": {
        "name": "Speed",
        "subject": "Physics",
        "topic": "Motion",

        "formula": "Speed = Distance / Time",

        "aliases": [
            "speed formula",
            "formula for speed",
            "distance time formula",
            "how to calculate speed",
            "velocity basic formula"
        ],

        "keywords": [
            "speed",
            "distance",
            "time",
            "motion"
        ],

        "variables": {
            "Distance": "Distance travelled",
            "Time": "Time taken"
        },

        "conditions": [
            "Distance and time must use compatible units."
        ],

        "cases": [
            "Finding speed",
            "Finding distance",
            "Finding time"
        ],

        "example": (
            "Distance = 100 m\n"
            "Time = 20 s\n"
            "Speed = 100 / 20 = 5 m/s"
        )
    },


    "acceleration": {
        "name": "Acceleration",
        "subject": "Physics",
        "topic": "Motion",

        "formula": "a = (v - u) / t",

        "aliases": [
            "acceleration formula",
            "formula for acceleration",
            "motion acceleration formula",
            "change in velocity formula"
        ],

        "keywords": [
            "acceleration",
            "velocity",
            "motion",
            "time"
        ],

        "variables": {
            "a": "Acceleration",
            "v": "Final velocity",
            "u": "Initial velocity",
            "t": "Time"
        },

        "conditions": [
            "Velocity and time must use compatible units."
        ],

        "cases": [
            "Finding acceleration",
            "Finding final velocity",
            "Finding initial velocity"
        ],

        "example": (
            "u = 5 m/s\n"
            "v = 15 m/s\n"
            "t = 2 s\n"
            "a = (15 - 5) / 2 = 5 m/s²"
        )
    },


    "newtons_second_law": {
        "name": "Newton's Second Law",
        "subject": "Physics",
        "topic": "Mechanics",

        "formula": "F = ma",

        "aliases": [
            "newton second law",
            "newtons second law",
            "newton's second law",
            "newton law",
            "force formula",
            "f ma",
            "f=ma",
            "mass acceleration formula"
        ],

        "keywords": [
            "force",
            "mass",
            "acceleration",
            "newton"
        ],

        "variables": {
            "F": "Force",
            "m": "Mass",
            "a": "Acceleration"
        },

        "conditions": [
            "Force is measured in newtons.",
            "Mass is measured in kilograms.",
            "Acceleration is measured in m/s²."
        ],

        "cases": [
            "Finding force",
            "Finding mass",
            "Finding acceleration"
        ],

        "example": (
            "m = 10 kg\n"
            "a = 2 m/s²\n"
            "F = 10 × 2 = 20 N"
        )
    },


    "kinetic_energy": {
        "name": "Kinetic Energy",
        "subject": "Physics",
        "topic": "Energy",

        "formula": "KE = ½mv²",

        "aliases": [
            "kinetic energy formula",
            "kinetic energy",
            "formula for kinetic energy",
            "moving object energy",
            "energy of moving body"
        ],

        "keywords": [
            "energy",
            "kinetic",
            "motion",
            "mass",
            "velocity"
        ],

        "variables": {
            "KE": "Kinetic energy",
            "m": "Mass",
            "v": "Velocity"
        },

        "conditions": [
            "Mass should be in kilograms.",
            "Velocity should be in metres per second."
        ],

        "cases": [
            "Finding kinetic energy",
            "Finding mass",
            "Finding velocity"
        ],

        "example": (
            "m = 2 kg\n"
            "v = 5 m/s\n"
            "KE = ½ × 2 × 5²\n"
            "KE = 25 J"
        )
    },


    "potential_energy": {
        "name": "Gravitational Potential Energy",
        "subject": "Physics",
        "topic": "Energy",

        "formula": "PE = mgh",

        "aliases": [
            "potential energy formula",
            "gravitational potential energy",
            "potential energy",
            "mgh formula",
            "height energy formula"
        ],

        "keywords": [
            "energy",
            "height",
            "gravity",
            "mass"
        ],

        "variables": {
            "m": "Mass",
            "g": "Acceleration due to gravity",
            "h": "Height"
        },

        "conditions": [
            "Near Earth's surface, g is approximately 9.8 m/s²."
        ],

        "cases": [
            "Finding potential energy",
            "Finding height",
            "Finding mass"
        ],

        "example": (
            "m = 2 kg\n"
            "g = 9.8 m/s²\n"
            "h = 5 m\n"
            "PE = 2 × 9.8 × 5 = 98 J"
        )
    },


    "ohms_law": {
        "name": "Ohm's Law",
        "subject": "Physics",
        "topic": "Electricity",

        "formula": "V = IR",

        "aliases": [
            "ohms law",
            "ohm law",
            "ohm's law",
            "voltage formula",
            "current voltage resistance formula",
            "v=ir",
            "electricity formula"
        ],

        "keywords": [
            "voltage",
            "current",
            "resistance",
            "electricity"
        ],

        "variables": {
            "V": "Voltage",
            "I": "Current",
            "R": "Resistance"
        },

        "conditions": [
            "Voltage is measured in volts.",
            "Current is measured in amperes.",
            "Resistance is measured in ohms."
        ],

        "cases": [
            "Finding voltage",
            "Finding current",
            "Finding resistance"
        ],

        "example": (
            "I = 2 A\n"
            "R = 5 Ω\n"
            "V = 2 × 5 = 10 V"
        )
    },


    # ========================================================
    # CHEMISTRY
    # ========================================================

    "molarity": {
        "name": "Molarity",
        "subject": "Chemistry",
        "topic": "Solutions",

        "formula": "M = Moles of solute / Volume of solution",

        "aliases": [
            "molarity formula",
            "molar concentration",
            "molar concentration formula",
            "moles concentration formula",
            "moles per litre formula"
        ],

        "keywords": [
            "molarity",
            "moles",
            "solution",
            "concentration"
        ],

        "variables": {
            "M": "Molarity",
            "n": "Moles of solute",
            "V": "Volume of solution in litres"
        },

        "conditions": [
            "Volume should be expressed in litres for molarity in mol/L."
        ],

        "cases": [
            "Finding molarity",
            "Finding moles",
            "Finding volume"
        ],

        "example": (
            "2 moles of solute in 4 L solution:\n"
            "M = 2 / 4 = 0.5 mol/L"
        )
    },


    "ideal_gas_law": {
        "name": "Ideal Gas Law",
        "subject": "Chemistry",
        "topic": "Gases",

        "formula": "PV = nRT",

        "aliases": [
            "ideal gas law",
            "ideal gas equation",
            "gas equation",
            "pv=nrt",
            "gas formula",
            "pressure volume temperature formula"
        ],

        "keywords": [
            "gas",
            "pressure",
            "volume",
            "temperature",
            "moles"
        ],

        "variables": {
            "P": "Pressure",
            "V": "Volume",
            "n": "Number of moles",
            "R": "Gas constant",
            "T": "Absolute temperature"
        },

        "conditions": [
            "Temperature should be in kelvin.",
            "Units must be consistent with the chosen gas constant."
        ],

        "cases": [
            "Finding pressure",
            "Finding volume",
            "Finding temperature",
            "Finding moles"
        ],

        "example": (
            "For an ideal gas:\n"
            "PV = nRT"
        )
    },


    "ph": {
        "name": "pH",
        "subject": "Chemistry",
        "topic": "Acids and Bases",

        "formula": "pH = −log₁₀[H⁺]",

        "aliases": [
            "ph formula",
            "pH formula",
            "hydrogen ion formula",
            "acidity formula",
            "acid ph",
            "ph calculation"
        ],

        "keywords": [
            "ph",
            "acid",
            "base",
            "hydrogen ion",
            "acidity"
        ],

        "variables": {
            "[H⁺]": "Hydrogen ion concentration"
        },

        "conditions": [
            "Hydrogen ion concentration is expressed in mol/L."
        ],

        "cases": [
            "Finding pH",
            "Comparing acidity",
            "Finding hydrogen ion concentration"
        ],

        "example": (
            "If [H⁺] = 1 × 10⁻³ mol/L:\n"
            "pH = −log₁₀(10⁻³)\n"
            "pH = 3"
        )
    },


    "density": {
        "name": "Density",
        "subject": "Chemistry",
        "topic": "Matter",

        "formula": "ρ = m / V",

        "aliases": [
            "density formula",
            "formula for density",
            "mass volume formula",
            "density equation",
            "rho formula"
        ],

        "keywords": [
            "density",
            "mass",
            "volume",
            "matter"
        ],

        "variables": {
            "ρ": "Density",
            "m": "Mass",
            "V": "Volume"
        },

        "conditions": [
            "Mass and volume must use compatible units."
        ],

        "cases": [
            "Finding density",
            "Finding mass",
            "Finding volume"
        ],

        "example": (
            "Mass = 100 g\n"
            "Volume = 20 cm³\n"
            "Density = 100 / 20 = 5 g/cm³"
        )
    },


    # ========================================================
    # ECONOMICS
    # ========================================================

    "gdp_expenditure": {
        "name": "GDP Expenditure Formula",
        "subject": "Economics",
        "topic": "National Income",

        "formula": "GDP = C + I + G + (X − M)",

        "aliases": [
            "gdp formula",
            "gross domestic product formula",
            "gdp expenditure formula",
            "national income formula",
            "expenditure method gdp",
            "gdp equation",
            "c+i+g+x-m"
        ],

        "keywords": [
            "gdp",
            "national income",
            "consumption",
            "investment",
            "government spending",
            "exports",
            "imports"
        ],

        "variables": {
            "C": "Consumption",
            "I": "Investment",
            "G": "Government spending",
            "X": "Exports",
            "M": "Imports"
        },

        "conditions": [
            "All components should refer to the same period and economy."
        ],

        "cases": [
            "Calculating GDP using expenditure",
            "Analysing consumption",
            "Analysing investment",
            "Analysing government spending"
        ],

        "example": (
            "C = 500\n"
            "I = 200\n"
            "G = 150\n"
            "X = 100\n"
            "M = 50\n\n"
            "GDP = 500 + 200 + 150 + (100 - 50)\n"
            "GDP = 900"
        )
    },


    "profit": {
        "name": "Profit",
        "subject": "Economics",
        "topic": "Business Economics",

        "formula": "Profit = Total Revenue − Total Cost",

        "aliases": [
            "profit formula",
            "business profit formula",
            "economic profit",
            "profit calculation",
            "revenue minus cost"
        ],

        "keywords": [
            "profit",
            "revenue",
            "cost",
            "business"
        ],

        "variables": {
            "TR": "Total Revenue",
            "TC": "Total Cost"
        },

        "conditions": [
            "Revenue and cost must refer to the same period."
        ],

        "cases": [
            "Positive profit",
            "Zero profit",
            "Loss"
        ],

        "example": (
            "Revenue = ₹100,000\n"
            "Cost = ₹70,000\n"
            "Profit = ₹30,000"
        )
    },


    "price_elasticity_demand": {
        "name": "Price Elasticity of Demand",
        "subject": "Economics",
        "topic": "Elasticity",

        "formula": "PED = % Change in Quantity Demanded / % Change in Price",

        "aliases": [
            "price elasticity formula",
            "elasticity of demand",
            "price elasticity of demand",
            "ped formula",
            "demand elasticity formula"
        ],

        "keywords": [
            "elasticity",
            "demand",
            "price",
            "quantity"
        ],

        "variables": {
            "PED": "Price Elasticity of Demand",
            "%ΔQ": "Percentage change in quantity demanded",
            "%ΔP": "Percentage change in price"
        },

        "conditions": [
            "Percentage changes should refer to the same period."
        ],

        "cases": [
            "Elastic demand",
            "Inelastic demand",
            "Unit elastic demand"
        ],

        "example": (
            "Quantity demanded changes by 20%.\n"
            "Price changes by 10%.\n"
            "PED = 20 / 10 = 2"
        )
    },


    "average_cost": {
        "name": "Average Cost",
        "subject": "Economics",
        "topic": "Costs",

        "formula": "AC = Total Cost / Quantity",

        "aliases": [
            "average cost formula",
            "average cost",
            "unit cost formula",
            "cost per unit",
            "average unit cost"
        ],

        "keywords": [
            "cost",
            "average",
            "quantity",
            "production"
        ],

        "variables": {
            "AC": "Average Cost",
            "TC": "Total Cost",
            "Q": "Quantity"
        },

        "conditions": [
            "Quantity must be greater than zero."
        ],

        "cases": [
            "Calculating average cost",
            "Comparing production costs"
        ],

        "example": (
            "Total Cost = ₹10,000\n"
            "Quantity = 500 units\n"
            "AC = 10000 / 500 = ₹20 per unit"
        )
    },


    # ========================================================
    # ACCOUNTING
    # ========================================================

    "accounting_equation": {
        "name": "Accounting Equation",
        "subject": "Accounting",
        "topic": "Basic Accounting",

        "formula": "Assets = Liabilities + Equity",

        "aliases": [
            "accounting equation",
            "basic accounting equation",
            "accounting formula",
            "assets liabilities equity",
            "balance sheet equation",
            "assets = liabilities + equity"
        ],

        "keywords": [
            "assets",
            "liabilities",
            "equity",
            "accounting",
            "balance sheet"
        ],

        "variables": {
            "Assets": "Resources owned by the business",
            "Liabilities": "Amounts owed by the business",
            "Equity": "Owner's claim"
        },

        "conditions": [
            "The equation should remain balanced."
        ],

        "cases": [
            "Finding assets",
            "Finding liabilities",
            "Finding equity"
        ],

        "example": (
            "Liabilities = ₹40,000\n"
            "Equity = ₹60,000\n"
            "Assets = ₹40,000 + ₹60,000\n"
            "Assets = ₹100,000"
        )
    },


    "gross_profit": {
        "name": "Gross Profit",
        "subject": "Accounting",
        "topic": "Profit and Loss",

        "formula": "Gross Profit = Sales − Cost of Goods Sold",

        "aliases": [
            "gross profit formula",
            "gross profit",
            "gross profit calculation",
            "sales minus cost of goods sold",
            "gp formula"
        ],

        "keywords": [
            "gross profit",
            "sales",
            "cogs",
            "cost of goods sold"
        ],

        "variables": {
            "Sales": "Revenue from sales",
            "COGS": "Cost of Goods Sold"
        },

        "conditions": [
            "Sales and COGS should refer to the same accounting period."
        ],

        "cases": [
            "Calculating gross profit",
            "Calculating gross loss"
        ],

        "example": (
            "Sales = ₹100,000\n"
            "COGS = ₹60,000\n"
            "Gross Profit = ₹40,000"
        )
    },


    "net_profit": {
        "name": "Net Profit",
        "subject": "Accounting",
        "topic": "Profit and Loss",

        "formula": "Net Profit = Total Revenue − Total Expenses",

        "aliases": [
            "net profit formula",
            "net profit",
            "profit after expenses",
            "net income formula",
            "bottom line formula"
        ],

        "keywords": [
            "net profit",
            "income",
            "expenses",
            "revenue"
        ],

        "variables": {
            "Revenue": "Total Revenue",
            "Expenses": "Total Expenses"
        },

        "conditions": [
            "Revenue and expenses should cover the same accounting period."
        ],

        "cases": [
            "Calculating net profit",
            "Calculating net loss"
        ],

        "example": (
            "Revenue = ₹200,000\n"
            "Expenses = ₹150,000\n"
            "Net Profit = ₹50,000"
        )
    },


    "current_ratio": {
        "name": "Current Ratio",
        "subject": "Accounting",
        "topic": "Financial Ratios",

        "formula": "Current Ratio = Current Assets / Current Liabilities",

        "aliases": [
            "current ratio",
            "current ratio formula",
            "liquidity ratio",
            "working capital ratio",
            "current assets current liabilities"
        ],

        "keywords": [
            "ratio",
            "liquidity",
            "current assets",
            "current liabilities"
        ],

        "variables": {
            "Current Assets": "Assets expected to be converted to cash within the relevant period",
            "Current Liabilities": "Short-term obligations"
        },

        "conditions": [
            "Both values should refer to the same reporting date."
        ],

        "cases": [
            "Measuring short-term liquidity",
            "Comparing liquidity between periods"
        ],

        "example": (
            "Current Assets = ₹100,000\n"
            "Current Liabilities = ₹50,000\n"
            "Current Ratio = 100000 / 50000 = 2:1"
        )
    },


    "straight_line_depreciation": {
        "name": "Straight-Line Depreciation",
        "subject": "Accounting",
        "topic": "Depreciation",

        "formula": "Depreciation = (Cost − Residual Value) / Useful Life",

        "aliases": [
            "straight line depreciation",
            "depreciation formula",
            "straight line depreciation formula",
            "slm depreciation",
            "fixed asset depreciation",
            "depreciation calculation"
        ],

        "keywords": [
            "depreciation",
            "asset",
            "cost",
            "residual value",
            "useful life"
        ],

        "variables": {
            "Cost": "Original cost of the asset",
            "Residual Value": "Estimated value at the end of useful life",
            "Useful Life": "Expected useful life"
        },

        "conditions": [
            "The useful life must be greater than zero.",
            "Cost and residual value should use the same currency."
        ],

        "cases": [
            "Annual depreciation",
            "Book value calculation"
        ],

        "example": (
            "Cost = ₹100,000\n"
            "Residual Value = ₹10,000\n"
            "Useful Life = 5 years\n\n"
            "Depreciation = (100000 - 10000) / 5\n"
            "Depreciation = ₹18,000 per year"
        )
    }
}


# ============================================================
# SEARCH ENGINE
# ============================================================

def normalize_text(text):
    """
    Converts text into a simpler form for searching.
    """

    text = str(text).lower()

    # Convert common mathematical symbols
    replacements = {
        "²": "2",
        "³": "3",
        "√": "sqrt",
        "−": "-",
        "×": "x",
        "÷": "/",
        "π": "pi",
        "Ω": "ohm"
    }

    for old, new in replacements.items():
        text = text.replace(old, new)

    # Remove punctuation
    text = re.sub(r"[^a-z0-9\s]", " ", text)

    # Remove extra spaces
    text = re.sub(r"\s+", " ", text).strip()

    return text


def similarity(a, b):
    """
    Returns similarity between two strings from 0 to 1.
    """

    return SequenceMatcher(
        None,
        normalize_text(a),
        normalize_text(b)
    ).ratio()


def search_formulas(query, subject="All"):
    """
    Searches the formula database using:
    - formula name
    - aliases
    - keywords
    - topic
    - subject
    - formula itself
    - fuzzy matching
    """

    query = normalize_text(query)

    if not query:
        return []

    results = []

    for formula_id, data in FORMULAS.items():

        # Subject filtering
        if subject != "All":
            if data["subject"] != subject:
                continue

        searchable_items = []

        searchable_items.append(data["name"])
        searchable_items.append(data["subject"])
        searchable_items.append(data["topic"])
        searchable_items.append(data["formula"])

        searchable_items.extend(
            data.get("aliases", [])
        )

        searchable_items.extend(
            data.get("keywords", [])
        )

        best_score = 0

        for item in searchable_items:

            item_normalized = normalize_text(item)

            # Exact phrase
            if query == item_normalized:
                score = 1.0

            # Query contained in item
            elif query in item_normalized:
                score = 0.92

            # Item contained in query
            elif item_normalized in query:
                score = 0.88

            # Fuzzy match
            else:
                score = similarity(query, item)

            if score > best_score:
                best_score = score

        # Good match
        if best_score >= 0.45:

            results.append({
                "id": formula_id,
                "score": best_score,
                "data": data
            })

    # Highest match first
    results.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return results


# ============================================================
# TERMINAL VERSION
# ============================================================

def run_terminal():

    print("\n==========================================")
    print("          FORMULA AI")
    print("==========================================")
    print("Subjects:")
    print("Mathematics")
    print("Physics")
    print("Chemistry")
    print("Economics")
    print("Accounting")
    print("==========================================")

    while True:

        query = input(
            "\nSearch formula (or type exit): "
        ).strip()

        if query.lower() == "exit":
            print("Goodbye!")
            break

        results = search_formulas(query)

        if not results:
            print("\nNo formula found.")
            continue

        best = results[0]["data"]

        print("\n------------------------------------------")
        print(best["name"])
        print("------------------------------------------")

        print("\nFormula:")
        print(best["formula"])

        print("\nSubject:")
        print(best["subject"])

        print("\nTopic:")
        print(best["topic"])

        print("\nVariables:")

        for variable, meaning in best["variables"].items():
            print(f"  {variable} = {meaning}")

        print("\nConditions:")

        for condition in best["conditions"]:
            print(f"  • {condition}")

        print("\nImportant Cases:")

        for case in best["cases"]:
            print(f"  • {case}")

        print("\nExample:")
        print(best["example"])


if __name__ == "__main__":
    run_terminal()