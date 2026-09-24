import html
import streamlit as st

from main import FORMULAS, search_formulas


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Formula Finder",
    page_icon="🧮",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
<style>

.stApp {
    background: #0e1117;
    color: #f5f7ff;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 4rem;
    max-width: 1250px;
}


/* ============================================================
   TITLE
   ============================================================ */

.main-title {
    font-size: 3rem;
    font-weight: 800;
    color: #ffffff;
    letter-spacing: -1px;
    margin-bottom: 0;
}

.subtitle {
    color: #a9b0c3;
    font-size: 1.1rem;
    margin-top: 4px;
    margin-bottom: 30px;
}


/* ============================================================
   SEARCH INPUT
   ============================================================ */

div[data-testid="stTextInput"] input {
    background: rgba(255,255,255,0.055) !important;
    color: #ffffff !important;

    border: 1px solid rgba(255,255,255,0.14) !important;
    border-radius: 14px !important;

    padding: 14px 16px !important;

    box-shadow: none !important;
}

div[data-testid="stTextInput"] input:focus {
    border-color: rgba(139,120,255,0.75) !important;

    box-shadow:
        0 0 0 1px rgba(139,120,255,0.30),
        0 0 18px rgba(139,120,255,0.10) !important;
}

div[data-testid="stTextInput"] input::placeholder {
    color: #777f92 !important;
}


/* ============================================================
   QUICK SEARCH BUTTONS
   ============================================================ */

div.stButton > button {
    width: 100%;

    background: rgba(255,255,255,0.045) !important;

    color: #f3f4f8 !important;

    border: 1px solid rgba(255,255,255,0.16) !important;
    border-radius: 13px !important;

    min-height: 58px;

    font-size: 16px !important;
    font-weight: 600 !important;

    box-shadow: none !important;

    transition:
        background 0.2s ease,
        border-color 0.2s ease,
        transform 0.2s ease;
}

div.stButton > button:hover {
    background: rgba(255,255,255,0.09) !important;

    border-color: rgba(150,130,255,0.55) !important;

    color: #ffffff !important;

    transform: translateY(-2px);
}

div.stButton > button:active {
    transform: translateY(0);
}

div.stButton > button:focus {
    box-shadow: none !important;
}


/* ============================================================
   FORMULA BOX
   ============================================================ */

.formula-box {
    background:
        linear-gradient(
            135deg,
            rgba(139,120,255,0.10),
            rgba(255,255,255,0.045)
        );

    border: 1px solid rgba(160,145,255,0.20);

    border-radius: 18px;

    padding: 32px 20px;

    margin-top: 15px;
    margin-bottom: 20px;

    text-align: center;

    color: #ffffff;

    font-size: 34px;
    font-weight: 700;

    box-shadow:
        0 8px 30px rgba(0,0,0,0.22),
        inset 0 1px 0 rgba(255,255,255,0.05);

    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);

    overflow-x: auto;
}


/* ============================================================
   INFO BOX
   ============================================================ */

.info-box {
    background:
        linear-gradient(
            135deg,
            rgba(255,255,255,0.055),
            rgba(255,255,255,0.035)
        );

    border: 1px solid rgba(255,255,255,0.11);

    border-radius: 15px;

    padding: 17px 20px;

    margin-top: 10px;
    margin-bottom: 12px;

    color: #dfe3ee;

    box-shadow:
        0 5px 20px rgba(0,0,0,0.18);

    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
}


/* ============================================================
   VARIABLES
   ============================================================ */

.variable-row {
    display: flex;
    align-items: baseline;

    padding: 9px 0;

    border-bottom:
        1px solid rgba(255,255,255,0.06);
}

.variable-row:last-child {
    border-bottom: none;
}

.variable-symbol {
    color: #ffffff;

    font-size: 17px;

    font-weight: 700;

    min-width: 30px;
}

.variable-meaning {
    color: #aeb5c5;

    font-size: 15px;
}


/* ============================================================
   SUBJECT BADGE
   ============================================================ */

.subject-badge {
    display: inline-block;

    background: rgba(139,120,255,0.11);

    border: 1px solid rgba(150,135,255,0.22);

    color: #d9d4ff;

    border-radius: 999px;

    padding: 8px 15px;

    font-size: 14px;

    font-weight: 600;

    margin-top: 2px;
    margin-bottom: 14px;
}


/* ============================================================
   SECTION TITLE
   ============================================================ */

.section-title {
    font-size: 1.35rem;

    font-weight: 700;

    color: #ffffff;

    margin-top: 20px;
    margin-bottom: 8px;
}


/* ============================================================
   SEARCH HELP
   ============================================================ */

.search-help {
    color: #858da0;

    font-size: 14px;

    margin-top: -5px;
    margin-bottom: 22px;
}


/* ============================================================
   EXPANDERS
   ============================================================ */

div[data-testid="stExpander"] {
    background: rgba(255,255,255,0.04) !important;

    border: 1px solid rgba(255,255,255,0.11) !important;

    border-radius: 14px !important;

    overflow: hidden;
}

div[data-testid="stExpander"] details {
    background: transparent !important;
}

div[data-testid="stExpander"] summary {
    background: transparent !important;
    color: #f5f7ff !important;
}


/* ============================================================
   SELECT BOX
   ============================================================ */

div[data-testid="stSelectbox"] > div > div {
    background: rgba(255,255,255,0.05) !important;

    color: #ffffff !important;

    border-color: rgba(255,255,255,0.13) !important;

    border-radius: 12px !important;
}


/* ============================================================
   SIDEBAR
   ============================================================ */

section[data-testid="stSidebar"] {
    background: #11151d !important;

    border-right:
        1px solid rgba(255,255,255,0.08);
}

section[data-testid="stSidebar"] * {
    color: #f0f2f7;
}


/* ============================================================
   DIVIDER
   ============================================================ */

hr {
    border: none !important;

    border-top:
        1px solid rgba(255,255,255,0.11) !important;

    margin-top: 28px !important;
    margin-bottom: 28px !important;
}


/* ============================================================
   HIDE STREAMLIT UI
   ============================================================ */

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

</style>
""",
    unsafe_allow_html=True,
)


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def get_value(data, key, default=""):
    value = data.get(key, default)

    if value is None or value == "":
        return default

    return value


def safe_text(value):
    """
    Prevents accidental HTML from being interpreted.
    """
    return html.escape(str(value))


def format_list(value):

    if not value:
        return "Not specified"

    if isinstance(value, list):

        return "<br>".join(
            "• " + safe_text(item)
            for item in value
        )

    if isinstance(value, dict):

        return "<br>".join(
            "<b>"
            + safe_text(key)
            + "</b>: "
            + safe_text(val)
            for key, val in value.items()
        )

    return safe_text(value)


# ============================================================
# VARIABLES
# ============================================================

def display_variables(variables):

    if not variables:
        return

    st.markdown(
        '<div class="section-title">Variables</div>',
        unsafe_allow_html=True
    )

    # --------------------------------------------------------
    # DICTIONARY
    # --------------------------------------------------------

    if isinstance(variables, dict):

        rows = []

        for symbol, meaning in variables.items():

            row = (
                '<div class="variable-row">'
                '<span class="variable-symbol">'
                + safe_text(symbol)
                + '</span>'
                '<span class="variable-meaning">'
                '— '
                + safe_text(meaning)
                + '</span>'
                '</div>'
            )

            rows.append(row)

        # IMPORTANT:
        # Everything is joined with NO indentation.
        # This prevents Streamlit from treating it as
        # a Markdown code block.

        variable_html = "".join(rows)

        full_html = (
            '<div class="info-box">'
            + variable_html
            + '</div>'
        )

        st.markdown(
            full_html,
            unsafe_allow_html=True
        )

        return

    # --------------------------------------------------------
    # LIST
    # --------------------------------------------------------

    if isinstance(variables, list):

        rows = []

        for item in variables:

            if isinstance(item, dict):

                for symbol, meaning in item.items():

                    rows.append(
                        '<div class="variable-row">'
                        '<span class="variable-symbol">'
                        + safe_text(symbol)
                        + '</span>'
                        '<span class="variable-meaning">'
                        '— '
                        + safe_text(meaning)
                        + '</span>'
                        '</div>'
                    )

            else:

                rows.append(
                    '<div class="variable-row">'
                    '<span class="variable-meaning">'
                    + safe_text(item)
                    + '</span>'
                    '</div>'
                )

        variable_html = "".join(rows)

        full_html = (
            '<div class="info-box">'
            + variable_html
            + '</div>'
        )

        st.markdown(
            full_html,
            unsafe_allow_html=True
        )

        return

    # --------------------------------------------------------
    # NORMAL TEXT
    # --------------------------------------------------------

    full_html = (
        '<div class="info-box">'
        '<div class="variable-row">'
        '<span class="variable-meaning">'
        + safe_text(variables)
        + '</span>'
        '</div>'
        '</div>'
    )

    st.markdown(
        full_html,
        unsafe_allow_html=True
    )


# ============================================================
# DISPLAY FORMULA
# ============================================================

def display_formula_result(data):

    name = get_value(
        data,
        "name",
        "Formula"
    )

    subject = get_value(
        data,
        "subject",
        ""
    )

    topic = get_value(
        data,
        "topic",
        ""
    )

    formula = get_value(
        data,
        "formula",
        ""
    )

    variables = data.get(
        "variables",
        {}
    )

    conditions = data.get(
        "conditions",
        []
    )

    cases = data.get(
        "cases",
        []
    )

    example = data.get(
        "example",
        ""
    )

    aliases = data.get(
        "aliases",
        []
    )


    # ========================================================
    # NAME
    # ========================================================

    st.markdown(
        '<h1 style="'
        'color:#ffffff;'
        'font-size:2.5rem;'
        'margin-bottom:10px;'
        '">'
        '📐 '
        + safe_text(name)
        + '</h1>',
        unsafe_allow_html=True
    )


    # ========================================================
    # SUBJECT / TOPIC
    # ========================================================

    if subject or topic:

        badge = ""

        if subject:
            badge += safe_text(subject)

        if subject and topic:
            badge += " → "

        if topic:
            badge += safe_text(topic)

        st.markdown(
            '<div class="subject-badge">'
            + badge
            + '</div>',
            unsafe_allow_html=True
        )


    # ========================================================
    # FORMULA
    # ========================================================

    st.markdown(
        '<div class="section-title">'
        'Formula 🔗'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="formula-box">'
        + safe_text(formula)
        + '</div>',
        unsafe_allow_html=True
    )


    # ========================================================
    # VARIABLES
    # ========================================================

    display_variables(variables)


    # ========================================================
    # CONDITIONS
    # ========================================================

    if conditions:

        st.markdown(
            '<div class="section-title">'
            'Conditions'
            '</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="info-box">'
            + format_list(conditions)
            + '</div>',
            unsafe_allow_html=True
        )


    # ========================================================
    # CASES
    # ========================================================

    if cases:

        st.markdown(
            '<div class="section-title">'
            'Cases'
            '</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="info-box">'
            + format_list(cases)
            + '</div>',
            unsafe_allow_html=True
        )


    # ========================================================
    # EXAMPLE
    # ========================================================

    if example:

        st.markdown(
            '<div class="section-title">'
            'Example'
            '</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="info-box">'
            + format_list(example)
            + '</div>',
            unsafe_allow_html=True
        )


    # ========================================================
    # ALIASES
    # ========================================================

    if aliases:

        st.markdown(
            '<div class="section-title">'
            'Also known as'
            '</div>',
            unsafe_allow_html=True
        )

        if isinstance(aliases, list):

            alias_text = " • ".join(
                safe_text(alias)
                for alias in aliases
            )

        else:

            alias_text = safe_text(aliases)

        st.markdown(
            '<div class="info-box">'
            + alias_text
            + '</div>',
            unsafe_allow_html=True
        )


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown(
        "## 🧮 Formula Finder"
    )

    st.markdown(
        '<p style="'
        'color:#9098aa;'
        'font-size:14px;'
        '">'
        'Search formulas by name, topic, '
        'subject, keyword or alias.'
        '</p>',
        unsafe_allow_html=True
    )

    st.divider()


    # ========================================================
    # SUBJECTS
    # ========================================================

    subjects = set()

    for formula_data in FORMULAS.values():

        subject = formula_data.get(
            "subject"
        )

        if subject:
            subjects.add(subject)

    subject_options = (
        ["All"]
        + sorted(subjects)
    )


    # ========================================================
    # SUBJECT FILTER
    # ========================================================

    selected_subject = st.selectbox(
        "Subject",
        subject_options
    )


    st.divider()


    # ========================================================
    # DATABASE
    # ========================================================

    st.markdown(
        "### 📚 Database"
    )

    st.markdown(
        '<div class="info-box">'
        '<b>'
        + str(len(FORMULAS))
        + '</b> formulas available'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="info-box">'
        '<b>'
        + str(len(subjects))
        + '</b> subjects'
        '</div>',
        unsafe_allow_html=True
    )


# ============================================================
# MAIN HEADER
# ============================================================

st.markdown(
    '<div class="main-title">'
    '🧮 Formula Finder'
    '</div>'

    '<div class="subtitle">'
    'Search mathematics, physics, chemistry, '
    'economics and accounting formulas instantly.'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# SESSION STATE
# ============================================================

if "search_query" not in st.session_state:
    st.session_state.search_query = ""


# ============================================================
# SEARCH BOX
# ============================================================

query = st.text_input(
    "🔎 Search for a formula",

    value=st.session_state.search_query,

    placeholder=(
        "Example: Pythagorean theorem, "
        "quadratic formula, GDP..."
    )
)

st.session_state.search_query = query


st.markdown(
    '<div class="search-help">'
    'You can search using a formula name, subject, '
    'topic, keyword or alternative name.'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# QUICK SEARCH
# ============================================================

st.markdown(
    "## ⚡ Quick Search"
)


quick_searches = [
    (
        "Pythagoras Theorem",
        "pythagorean theorem"
    ),
    (
        "Quadratic Formula",
        "quadratic formula"
    ),
    (
        "Newton Second Law",
        "newton second law"
    ),
    (
        "Ohms Law",
        "ohms law"
    ),
    (
        "Molarity",
        "molarity"
    ),
    (
        "Gdp Formula",
        "gdp formula"
    ),
    (
        "Accounting Equation",
        "accounting equation"
    ),
    (
        "Depreciation Formula",
        "depreciation formula"
    ),
]


# ============================================================
# QUICK SEARCH BUTTONS
# ============================================================

for row_start in range(
    0,
    len(quick_searches),
    4
):

    row_items = quick_searches[
        row_start:
        row_start + 4
    ]

    columns = st.columns(4)

    for column, (
        button_name,
        search_value
    ) in zip(
        columns,
        row_items
    ):

        with column:

            if st.button(
                button_name,
                key=f"quick_{search_value}",
                use_container_width=True
            ):

                st.session_state.search_query = (
                    search_value
                )

                st.rerun()


# ============================================================
# DIVIDER
# ============================================================

st.divider()


# ============================================================
# SEARCH
# ============================================================

if query.strip():

    results = search_formulas(
        query,
        selected_subject
    )


    # ========================================================
    # NO RESULTS
    # ========================================================

    if not results:

        st.warning(
            "No matching formula was found. "
            "Try another name, keyword or subject."
        )


    # ========================================================
    # RESULTS
    # ========================================================

    else:

        st.success(
            f"Found {len(results)} possible formula(s)."
        )


        # ====================================================
        # BEST RESULT
        # ====================================================

        best_result = results[0]


        if isinstance(
            best_result,
            tuple
        ):

            if len(best_result) == 3:

                (
                    _score,
                    formula_key,
                    formula_data
                ) = best_result

            elif len(best_result) == 2:

                first, second = best_result

                if isinstance(
                    second,
                    dict
                ):

                    formula_key = first
                    formula_data = second

                else:

                    formula_key = second

                    formula_data = FORMULAS.get(
                        formula_key,
                        {}
                    )

            else:

                formula_key = None
                formula_data = {}


        elif isinstance(
            best_result,
            dict
        ):

            formula_key = best_result.get(
                "key"
            )

            formula_data = best_result.get(
                "data",
                best_result
            )


        else:

            formula_key = best_result

            formula_data = FORMULAS.get(
                formula_key,
                {}
            )


        # ====================================================
        # GET FORMULA FROM DATABASE
        # ====================================================

        if (
            not formula_data
            and formula_key in FORMULAS
        ):

            formula_data = FORMULAS[
                formula_key
            ]


        # ====================================================
        # DISPLAY BEST RESULT
        # ====================================================

        if formula_data:

            display_formula_result(
                formula_data
            )


        # ====================================================
        # OTHER MATCHES
        # ====================================================

        if len(results) > 1:

            st.divider()

            st.markdown(
                "## 🔍 Other Possible Matches"
            )


            for result in results[1:]:

                # ------------------------------------------------
                # TUPLE
                # ------------------------------------------------

                if isinstance(
                    result,
                    tuple
                ):

                    if len(result) == 3:

                        (
                            _score,
                            other_key,
                            other_data
                        ) = result

                    elif len(result) == 2:

                        first, second = result

                        if isinstance(
                            second,
                            dict
                        ):

                            other_key = first
                            other_data = second

                        else:

                            other_key = second

                            other_data = FORMULAS.get(
                                other_key,
                                {}
                            )

                    else:

                        continue


                # ------------------------------------------------
                # DICTIONARY
                # ------------------------------------------------

                elif isinstance(
                    result,
                    dict
                ):

                    other_key = result.get(
                        "key"
                    )

                    other_data = result.get(
                        "data",
                        result
                    )


                # ------------------------------------------------
                # KEY
                # ------------------------------------------------

                else:

                    other_key = result

                    other_data = FORMULAS.get(
                        other_key,
                        {}
                    )


                if not other_data:
                    continue


                other_name = other_data.get(
                    "name",
                    str(other_key)
                )

                other_subject = other_data.get(
                    "subject",
                    ""
                )

                other_topic = other_data.get(
                    "topic",
                    ""
                )

                other_formula = other_data.get(
                    "formula",
                    ""
                )


                # ------------------------------------------------
                # EXPANDER
                # ------------------------------------------------

                with st.expander(
                    "📘 " + str(other_name)
                ):

                    if (
                        other_subject
                        or other_topic
                    ):

                        badge = ""

                        if other_subject:
                            badge += safe_text(
                                other_subject
                            )

                        if (
                            other_subject
                            and other_topic
                        ):
                            badge += " → "

                        if other_topic:
                            badge += safe_text(
                                other_topic
                            )

                        st.markdown(
                            '<div class="subject-badge">'
                            + badge
                            + '</div>',
                            unsafe_allow_html=True
                        )


                    st.markdown(
                        '<div class="formula-box">'
                        + safe_text(other_formula)
                        + '</div>',
                        unsafe_allow_html=True
                    )


# ============================================================
# EMPTY SEARCH
# ============================================================

else:

    st.markdown(
        '<div class="info-box" '
        'style="'
        'margin-top:25px;'
        'text-align:center;'
        'padding:25px !important;'
        '">'
        '🔎 Start typing above or choose one of the '
        'Quick Search buttons to find a formula.'
        '</div>',
        unsafe_allow_html=True
    )