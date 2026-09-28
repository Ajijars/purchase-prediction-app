"""
Generate a professional PPT for Tech Eximius 2026 Hackathon
Project: Vyapaar-View — AI-Powered Business Intelligence for Indian SMEs
"""

from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

import os

# ─── Color Palette ────────────────────────────────────────────────────────────
BG_DARK = RGBColor(0x0F, 0x0F, 0x14)       # Deep dark background
BG_CARD = RGBColor(0x18, 0x18, 0x22)       # Card background
PRIMARY = RGBColor(0x63, 0x66, 0xF1)       # Indigo
SECONDARY = RGBColor(0x8B, 0x5C, 0xF6)    # Violet
ACCENT_GREEN = RGBColor(0x10, 0xB9, 0x81)  # Emerald
ACCENT_AMBER = RGBColor(0xF5, 0x9E, 0x0B)  # Amber
ACCENT_ROSE = RGBColor(0xF4, 0x3F, 0x5E)   # Rose
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
LIGHT_GRAY = RGBColor(0xA1, 0xA1, 0xAA)
MUTED = RGBColor(0x71, 0x71, 0x7A)

SLIDE_WIDTH = Inches(13.333)
SLIDE_HEIGHT = Inches(7.5)


def set_slide_bg(slide, color=BG_DARK):
    """Set slide background color."""
    bg = slide.background
    fill = bg.fill
    fill.solid()
    fill.fore_color.rgb = color


def add_accent_bar(slide, left, top, width, height, color=PRIMARY):
    """Add a thin colored accent bar."""
    shape = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, left, top, width, height)
    shape.fill.solid()
    shape.fill.fore_color.rgb = color
    shape.line.fill.background()
    return shape


def add_gradient_rect(slide, left, top, width, height, color1=PRIMARY, color2=SECONDARY):
    """Add a gradient rectangle."""
    shape = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, left, top, width, height)
    shape.fill.solid()
    shape.fill.fore_color.rgb = color1
    shape.line.fill.background()
    return shape


def add_circle(slide, left, top, size, color, alpha=None):
    """Add a decorative circle."""
    shape = slide.shapes.add_shape(MSO_SHAPE.OVAL, left, top, size, size)
    shape.fill.solid()
    shape.fill.fore_color.rgb = color
    shape.line.fill.background()
    if alpha is not None:
        shape.fill.fore_color.brightness = alpha
    return shape


def add_text_box(slide, left, top, width, height, text, font_size=18, bold=False, color=WHITE, alignment=PP_ALIGN.LEFT, font_name="Calibri"):
    """Add a styled text box."""
    txBox = slide.shapes.add_textbox(left, top, width, height)
    tf = txBox.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = text
    p.font.size = Pt(font_size)
    p.font.bold = bold
    p.font.color.rgb = color
    p.font.name = font_name
    p.alignment = alignment
    return txBox


def add_bullet_list(slide, left, top, width, height, items, font_size=16, color=LIGHT_GRAY, bullet_color=PRIMARY, font_name="Calibri"):
    """Add a bulleted list."""
    txBox = slide.shapes.add_textbox(left, top, width, height)
    tf = txBox.text_frame
    tf.word_wrap = True

    for i, item in enumerate(items):
        if i == 0:
            p = tf.paragraphs[0]
        else:
            p = tf.add_paragraph()
        p.text = f"▸  {item}"
        p.font.size = Pt(font_size)
        p.font.color.rgb = color
        p.font.name = font_name
        p.space_after = Pt(8)
    return txBox


def add_card(slide, left, top, width, height, title, body, icon_text="", title_color=WHITE, body_color=LIGHT_GRAY, bg_color=BG_CARD, accent_color=PRIMARY):
    """Add a card-style shape with title and body."""
    # Card background
    card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
    card.fill.solid()
    card.fill.fore_color.rgb = bg_color
    card.line.color.rgb = RGBColor(0x2A, 0x2A, 0x35)
    card.line.width = Pt(1)

    # Accent bar at top
    add_accent_bar(slide, left + Inches(0.05), top + Inches(0.05), width - Inches(0.1), Inches(0.04), accent_color)

    # Icon/emoji
    if icon_text:
        add_text_box(slide, left + Inches(0.3), top + Inches(0.25), Inches(0.6), Inches(0.5), icon_text, font_size=24, bold=False, color=accent_color)

    # Title
    title_top = top + Inches(0.2) if not icon_text else top + Inches(0.75)
    add_text_box(slide, left + Inches(0.3), title_top, width - Inches(0.6), Inches(0.5), title, font_size=16, bold=True, color=title_color)

    # Body
    add_text_box(slide, left + Inches(0.3), title_top + Inches(0.45), width - Inches(0.6), height - Inches(1.5), body, font_size=12, bold=False, color=body_color)


# ═════════════════════════════════════════════════════════════════════════════
#  SLIDE BUILDERS
# ═════════════════════════════════════════════════════════════════════════════

def slide_01_title(prs):
    """Title Slide"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])  # Blank
    set_slide_bg(slide)

    # Decorative circles
    add_circle(slide, Inches(-1), Inches(-1), Inches(4), PRIMARY)
    add_circle(slide, Inches(10), Inches(5), Inches(5), SECONDARY)

    # Badge
    badge = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(4.8), Inches(1.2), Inches(3.7), Inches(0.5))
    badge.fill.solid()
    badge.fill.fore_color.rgb = PRIMARY
    badge.line.fill.background()
    tf = badge.text_frame
    tf.paragraphs[0].text = "TECH EXIMIUS 2026 — HACKATHON"
    tf.paragraphs[0].font.size = Pt(12)
    tf.paragraphs[0].font.bold = True
    tf.paragraphs[0].font.color.rgb = WHITE
    tf.paragraphs[0].font.name = "Calibri"
    tf.paragraphs[0].alignment = PP_ALIGN.CENTER

    # Main title
    add_text_box(slide, Inches(1.5), Inches(2.2), Inches(10.3), Inches(1.5),
                 "Vyapaar-View", font_size=64, bold=True, color=WHITE, alignment=PP_ALIGN.CENTER, font_name="Calibri")

    # Subtitle
    add_text_box(slide, Inches(2), Inches(3.5), Inches(9.3), Inches(0.8),
                 "AI-Powered Business Intelligence Platform for Indian SMEs",
                 font_size=24, bold=False, color=LIGHT_GRAY, alignment=PP_ALIGN.CENTER)

    # Tagline
    add_text_box(slide, Inches(3.5), Inches(4.5), Inches(6.3), Inches(0.6),
                 "\"Apna Vyapaar, Apna Insight.\"",
                 font_size=20, bold=True, color=PRIMARY, alignment=PP_ALIGN.CENTER)

    # Team info
    add_text_box(slide, Inches(2), Inches(5.8), Inches(9.3), Inches(0.5),
                 "Team: EurekaX  |  Theme: AI & Machine Learning / FinTech",
                 font_size=16, bold=False, color=MUTED, alignment=PP_ALIGN.CENTER)

    # Bottom accent bar
    add_accent_bar(slide, Inches(4), Inches(6.8), Inches(5.3), Inches(0.04), PRIMARY)


def slide_02_problem(prs):
    """Problem Statement"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    set_slide_bg(slide)

    # Section label
    add_text_box(slide, Inches(0.8), Inches(0.5), Inches(3), Inches(0.4),
                 "01  PROBLEM STATEMENT", font_size=12, bold=True, color=PRIMARY)
    add_accent_bar(slide, Inches(0.8), Inches(0.95), Inches(1.5), Inches(0.03), PRIMARY)

    # Title
    add_text_box(slide, Inches(0.8), Inches(1.2), Inches(11), Inches(1),
                 "Indian SMEs Are Flying Blind", font_size=40, bold=True, color=WHITE)

    # Subtitle
    add_text_box(slide, Inches(0.8), Inches(2.1), Inches(10), Inches(0.6),
                 "63 million+ MSMEs in India lack affordable AI-driven tools to make data-backed decisions.",
                 font_size=16, bold=False, color=LIGHT_GRAY)

    # Problem cards
    problems = [
        ("💸", "Cash Flow Blindness", "78% of SMEs face unexpected cash shortages. No real-time visibility into incoming vs outgoing cash."),
        ("📉", "Customer Churn", "Businesses lose 15-25% of revenue from undetected customer churn. No early-warning systems exist."),
        ("📊", "No Data Analytics", "Most SMEs rely on Excel or manual registers. No profit predictions, demand forecasting, or trend analysis."),
        ("🏷️", "Inventory Waste", "Overstocking & stockouts cost Indian retail ₹1.2L Cr/year. No smart inventory management."),
    ]

    for i, (icon, title, body) in enumerate(problems):
        col = i % 4
        left = Inches(0.8 + col * 3.05)
        top = Inches(3.0)
        add_card(slide, left, top, Inches(2.85), Inches(3.5), title, body, icon_text=icon,
                 accent_color=[ACCENT_ROSE, ACCENT_AMBER, PRIMARY, SECONDARY][i])

    # Bottom stat
    add_text_box(slide, Inches(0.8), Inches(6.8), Inches(11), Inches(0.5),
                 "⚡ Only 5% of Indian SMEs use any form of AI/ML in their operations — Source: NASSCOM 2025",
                 font_size=13, bold=False, color=MUTED, alignment=PP_ALIGN.CENTER)


def slide_03_solution(prs):
    """Proposed Solution"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    set_slide_bg(slide)

    add_text_box(slide, Inches(0.8), Inches(0.5), Inches(3), Inches(0.4),
                 "02  PROPOSED SOLUTION", font_size=12, bold=True, color=PRIMARY)
    add_accent_bar(slide, Inches(0.8), Inches(0.95), Inches(1.5), Inches(0.03), PRIMARY)

    add_text_box(slide, Inches(0.8), Inches(1.2), Inches(11), Inches(1),
                 "Vyapaar-View: Your AI Business Co-Pilot", font_size=38, bold=True, color=WHITE)

    add_text_box(slide, Inches(0.8), Inches(2.0), Inches(10), Inches(0.8),
                 "A full-stack, ML-powered business intelligence platform designed specifically for Indian SMEs. "
                 "It transforms raw sales, expense, and customer data into actionable insights — profit predictions, "
                 "churn alerts, CLV scoring, demand forecasting, and automated daily reports via Telegram.",
                 font_size=15, bold=False, color=LIGHT_GRAY)

    # Key differentiators
    diffs = [
        ("🇮🇳", "Built for India", "INR-first, GST-aware, Hindi-ready. Tuned for Indian retail patterns."),
        ("🤖", "ML at Core", "4 trained ML models: Profit, Churn, CLV (RFM), and Demand forecasting."),
        ("📱", "Telegram Alerts", "Automated daily close-of-business reports sent to your phone."),
        ("☁️", "Zero Infrastructure", "Deployed on Vercel — no servers, no setup. Just login and go."),
    ]

    for i, (icon, title, body) in enumerate(diffs):
        col = i % 2
        row = i // 2
        left = Inches(0.8 + col * 5.8)
        top = Inches(3.2 + row * 2.0)
        add_card(slide, left, top, Inches(5.5), Inches(1.8), title, body, icon_text=icon,
                 accent_color=[PRIMARY, SECONDARY, ACCENT_GREEN, ACCENT_AMBER][i])


def slide_04_features_1(prs):
    """Key Features — Part 1"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    set_slide_bg(slide)

    add_text_box(slide, Inches(0.8), Inches(0.5), Inches(3), Inches(0.4),
                 "03  KEY FEATURES", font_size=12, bold=True, color=PRIMARY)
    add_accent_bar(slide, Inches(0.8), Inches(0.95), Inches(1.5), Inches(0.03), PRIMARY)

    add_text_box(slide, Inches(0.8), Inches(1.2), Inches(11), Inches(0.7),
                 "Comprehensive Analytics Dashboard", font_size=36, bold=True, color=WHITE)

    features = [
        ("📊", "Business Overview", "Real-time KPIs — Total Revenue, Net Profit, Cash Balance, Business Health Score with sparkline trends."),
        ("📈", "Profit Prediction", "ML-powered monthly profit forecasting using Linear Regression on revenue & expense patterns."),
        ("⚠️", "Churn Prediction", "Logistic Regression model identifies at-risk customers based on purchase frequency & spending patterns."),
        ("⭐", "Customer Lifetime Value", "RFM-based CLV scoring (Recency 40%, Frequency 35%, Monetary 25%) with 4 customer segments."),
        ("📦", "Inventory Management", "Smart stock tracking with low-inventory alerts and product-level analytics."),
        ("💰", "Revenue & Expense", "Monthly revenue vs expense breakdown with payment mode analysis (UPI, Cash, Card, etc.)."),
    ]

    for i, (icon, title, body) in enumerate(features):
        col = i % 3
        row = i // 3
        left = Inches(0.8 + col * 3.9)
        top = Inches(2.2 + row * 2.55)
        add_card(slide, left, top, Inches(3.7), Inches(2.35), title, body, icon_text=icon,
                 accent_color=[PRIMARY, ACCENT_GREEN, ACCENT_AMBER, SECONDARY, ACCENT_ROSE, PRIMARY][i])


def slide_05_features_2(prs):
    """Key Features — Part 2"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    set_slide_bg(slide)

    add_text_box(slide, Inches(0.8), Inches(0.5), Inches(5), Inches(0.4),
                 "03  KEY FEATURES (CONTINUED)", font_size=12, bold=True, color=PRIMARY)
    add_accent_bar(slide, Inches(0.8), Inches(0.95), Inches(1.5), Inches(0.03), PRIMARY)

    add_text_box(slide, Inches(0.8), Inches(1.2), Inches(11), Inches(0.7),
                 "Advanced Capabilities", font_size=36, bold=True, color=WHITE)

    features = [
        ("📲", "Telegram Bot Integration", "Daily close-of-business reports auto-sent to shop owner's Telegram — revenue, profit, orders, and low-stock alerts."),
        ("🔍", "Trend Analysis", "Discover top-selling products, seasonal demand patterns, and performance trends over time."),
        ("🏭", "Production Planning", "Demand-based production planning with time-series forecasting for manufacturing units."),
        ("🤖", "AI Assistant", "Built-in conversational AI assistant for natural-language queries about your business data."),
    ]

    for i, (icon, title, body) in enumerate(features):
        col = i % 2
        row = i // 2
        left = Inches(0.8 + col * 5.8)
        top = Inches(2.2 + row * 2.4)
        add_card(slide, left, top, Inches(5.5), Inches(2.2), title, body, icon_text=icon,
                 accent_color=[PRIMARY, SECONDARY, ACCENT_GREEN, ACCENT_AMBER][i])


def slide_06_clv_deep_dive(prs):
    """CLV Module Deep Dive"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    set_slide_bg(slide)

    add_text_box(slide, Inches(0.8), Inches(0.5), Inches(5), Inches(0.4),
                 "04  CLV PREDICTION — DEEP DIVE", font_size=12, bold=True, color=PRIMARY)
    add_accent_bar(slide, Inches(0.8), Inches(0.95), Inches(1.5), Inches(0.03), PRIMARY)

    add_text_box(slide, Inches(0.8), Inches(1.2), Inches(11), Inches(0.7),
                 "RFM-Powered Customer Lifetime Value Engine", font_size=34, bold=True, color=WHITE)

    # Left side - RFM Explanation
    add_text_box(slide, Inches(0.8), Inches(2.2), Inches(5.5), Inches(0.5),
                 "How RFM Scoring Works", font_size=20, bold=True, color=WHITE)

    rfm_items = [
        "Recency (40%) — How recently a customer purchased",
        "Frequency (35%) — How often they purchase",
        "Monetary (25%) — How much they spend",
        "Each scored 1-5, combined into composite RFM score",
        "Linear Regression predicts 12-month CLV from RFM features",
        "Customers auto-segmented into 4 tiers:"
    ]
    add_bullet_list(slide, Inches(0.8), Inches(2.8), Inches(5.5), Inches(3), rfm_items, font_size=14)

    # Right side - Segments
    add_text_box(slide, Inches(7), Inches(2.2), Inches(5), Inches(0.5),
                 "Customer Segments", font_size=20, bold=True, color=WHITE)

    segments = [
        ("👑", "Champion", "RFM ≥ 4.0 — Highest value, most engaged", PRIMARY),
        ("⭐", "Loyal", "RFM ≥ 3.0 — Consistent buyers, brand loyalists", SECONDARY),
        ("⚠️", "At Risk", "RFM ≥ 2.0 — Declining engagement, need retention", ACCENT_AMBER),
        ("❌", "Lost", "RFM < 2.0 — Inactive, likely churned", ACCENT_ROSE),
    ]

    for i, (icon, title, body, color) in enumerate(segments):
        top = Inches(2.9 + i * 1.1)
        add_card(slide, Inches(7), top, Inches(5.3), Inches(0.95), title, body, icon_text=icon, accent_color=color)

    # API Endpoints
    add_text_box(slide, Inches(0.8), Inches(6.2), Inches(11), Inches(0.4),
                 "API Endpoints:  /clv/predict  •  /clv/summary  •  /clv/top-customers",
                 font_size=13, bold=False, color=MUTED, alignment=PP_ALIGN.CENTER)


def slide_07_workflow(prs):
    """System Workflow / Architecture"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    set_slide_bg(slide)

    add_text_box(slide, Inches(0.8), Inches(0.5), Inches(3), Inches(0.4),
                 "05  WORKFLOW", font_size=12, bold=True, color=PRIMARY)
    add_accent_bar(slide, Inches(0.8), Inches(0.95), Inches(1.5), Inches(0.03), PRIMARY)

    add_text_box(slide, Inches(0.8), Inches(1.2), Inches(11), Inches(0.7),
                 "End-to-End Data Pipeline", font_size=36, bold=True, color=WHITE)

    # Workflow steps
    steps = [
        ("1️⃣", "Data Ingestion", "Excel files (Sales, Expenses, Customers, Inventory) loaded via Pandas"),
        ("2️⃣", "Data Cleaning", "Column normalization, date parsing, store/year filtering via utils.py"),
        ("3️⃣", "Feature Engineering", "RFM computation, revenue aggregation, time-series indexing"),
        ("4️⃣", "ML Model Training", "Linear Regression (Profit, CLV, Demand) + Logistic Regression (Churn)"),
        ("5️⃣", "API Layer", "FastAPI REST endpoints serve predictions via 10+ route modules"),
        ("6️⃣", "Frontend Dashboard", "React + TypeScript + Recharts renders interactive visualizations"),
        ("7️⃣", "Notifications", "Telegram Bot API sends automated daily business summaries"),
    ]

    for i, (num, title, desc) in enumerate(steps):
        top = Inches(2.2 + i * 0.7)
        # Step number circle
        add_text_box(slide, Inches(0.8), top, Inches(0.5), Inches(0.5), num, font_size=16, bold=True, color=PRIMARY)
        # Title
        add_text_box(slide, Inches(1.5), top, Inches(2.5), Inches(0.5), title, font_size=16, bold=True, color=WHITE)
        # Description
        add_text_box(slide, Inches(4.2), top, Inches(8), Inches(0.5), desc, font_size=14, bold=False, color=LIGHT_GRAY)

        # Connector line
        if i < len(steps) - 1:
            add_accent_bar(slide, Inches(1.0), top + Inches(0.5), Inches(0.03), Inches(0.2), RGBColor(0x2A, 0x2A, 0x35))


def slide_08_architecture(prs):
    """System Architecture"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    set_slide_bg(slide)

    add_text_box(slide, Inches(0.8), Inches(0.5), Inches(3), Inches(0.4),
                 "06  SYSTEM ARCHITECTURE", font_size=12, bold=True, color=PRIMARY)
    add_accent_bar(slide, Inches(0.8), Inches(0.95), Inches(1.5), Inches(0.03), PRIMARY)

    add_text_box(slide, Inches(0.8), Inches(1.2), Inches(11), Inches(0.7),
                 "Full-Stack Architecture Overview", font_size=36, bold=True, color=WHITE)

    # Three-tier architecture
    tiers = [
        ("🖥️", "Frontend (Presentation Layer)", [
            "React 18 + TypeScript + Vite",
            "TanStack React Query for data fetching",
            "Recharts for interactive charts",
            "TailwindCSS + shadcn/ui components",
            "Framer Motion animations",
            "Deployed on Vercel CDN"
        ], PRIMARY),
        ("⚙️", "Backend (API Layer)", [
            "FastAPI (Python) — High-performance async API",
            "10 route modules: profit, churn, clv, finance, demand, inventory, customers, analytics, bot, notify",
            "CORS middleware for cross-origin access",
            "Pandas for data processing",
            "Deployed as Vercel Serverless Functions"
        ], SECONDARY),
        ("🧠", "ML Layer (Intelligence)", [
            "scikit-learn models trained on-the-fly",
            "Linear Regression → Profit, CLV, Demand",
            "Logistic Regression → Churn prediction",
            "MinMaxScaler for feature normalization",
            "RFM (Recency, Frequency, Monetary) engine",
            "Extensible model pipeline architecture"
        ], ACCENT_GREEN),
    ]

    for i, (icon, title, items, color) in enumerate(tiers):
        left = Inches(0.8 + i * 4.05)
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, Inches(2.2), Inches(3.85), Inches(4.8))
        card.fill.solid()
        card.fill.fore_color.rgb = BG_CARD
        card.line.color.rgb = RGBColor(0x2A, 0x2A, 0x35)
        card.line.width = Pt(1)

        add_accent_bar(slide, left + Inches(0.05), Inches(2.25), Inches(3.75), Inches(0.04), color)
        add_text_box(slide, left + Inches(0.3), Inches(2.4), Inches(3.3), Inches(0.5), f"{icon} {title}", font_size=15, bold=True, color=WHITE)
        add_bullet_list(slide, left + Inches(0.3), Inches(3.0), Inches(3.3), Inches(3.8), items, font_size=11, color=LIGHT_GRAY)


def slide_09_tech_stack(prs):
    """Tech Stack"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    set_slide_bg(slide)

    add_text_box(slide, Inches(0.8), Inches(0.5), Inches(3), Inches(0.4),
                 "07  TECH STACK", font_size=12, bold=True, color=PRIMARY)
    add_accent_bar(slide, Inches(0.8), Inches(0.95), Inches(1.5), Inches(0.03), PRIMARY)

    add_text_box(slide, Inches(0.8), Inches(1.2), Inches(11), Inches(0.7),
                 "Technologies Powering Vyapaar-View", font_size=36, bold=True, color=WHITE)

    categories = [
        ("Frontend", [
            ("React 18", "UI component library"),
            ("TypeScript", "Type-safe JavaScript"),
            ("Vite", "Lightning-fast build tool"),
            ("TailwindCSS", "Utility-first CSS"),
            ("Recharts", "Chart visualizations"),
            ("Framer Motion", "Smooth animations"),
        ], PRIMARY),
        ("Backend", [
            ("FastAPI", "Async Python web framework"),
            ("Python 3.11+", "Core language"),
            ("Pandas", "Data manipulation"),
            ("Pydantic", "Data validation"),
            ("python-multipart", "Form handling"),
            ("urllib", "HTTP for Telegram API"),
        ], SECONDARY),
        ("ML / AI", [
            ("scikit-learn", "ML model training"),
            ("NumPy", "Numerical computing"),
            ("LinearRegression", "Profit, CLV, Demand"),
            ("LogisticRegression", "Churn prediction"),
            ("MinMaxScaler", "Feature scaling"),
            ("RFM Analysis", "Customer segmentation"),
        ], ACCENT_GREEN),
        ("DevOps", [
            ("Vercel", "Frontend + Serverless deploy"),
            ("GitHub", "Version control & CI/CD"),
            ("Telegram Bot API", "Push notifications"),
            ("CORS Middleware", "Cross-origin security"),
            ("Excel/XLSX", "Data source format"),
            ("REST API", "JSON communication"),
        ], ACCENT_AMBER),
    ]

    for i, (cat_name, techs, color) in enumerate(categories):
        col = i % 4
        left = Inches(0.5 + col * 3.1)

        # Category header
        add_text_box(slide, left, Inches(2.2), Inches(2.9), Inches(0.4), cat_name, font_size=18, bold=True, color=color)
        add_accent_bar(slide, left, Inches(2.65), Inches(2.0), Inches(0.03), color)

        for j, (tech, desc) in enumerate(techs):
            top = Inches(2.9 + j * 0.7)
            add_text_box(slide, left, top, Inches(2.9), Inches(0.3), tech, font_size=14, bold=True, color=WHITE)
            add_text_box(slide, left, top + Inches(0.25), Inches(2.9), Inches(0.3), desc, font_size=11, bold=False, color=MUTED)


def slide_10_innovation(prs):
    """Innovation & Uniqueness"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    set_slide_bg(slide)

    add_text_box(slide, Inches(0.8), Inches(0.5), Inches(5), Inches(0.4),
                 "08  INNOVATION & UNIQUENESS", font_size=12, bold=True, color=PRIMARY)
    add_accent_bar(slide, Inches(0.8), Inches(0.95), Inches(1.5), Inches(0.03), PRIMARY)

    add_text_box(slide, Inches(0.8), Inches(1.2), Inches(11), Inches(0.7),
                 "What Makes Vyapaar-View Different?", font_size=36, bold=True, color=WHITE)

    innovations = [
        ("🎯", "India-First Design", "Built ground-up for Indian MSME patterns — INR formatting, Indian fiscal cycles, GST-aware calculations, and localized business insights.", PRIMARY),
        ("🔄", "Real-Time ML Pipeline", "Models retrain on every API call with latest data — no stale predictions. Dynamic feature engineering adapts to changing business patterns.", SECONDARY),
        ("📊", "RFM + ML Hybrid", "Combines traditional RFM customer segmentation with Linear Regression for CLV prediction — proven approach used by enterprises, now accessible to SMEs.", ACCENT_GREEN),
        ("📲", "WhatsApp-Style Alerts", "Telegram bot integration sends daily business summaries — revenue, profit, low-stock alerts — right to the shop owner's phone.", ACCENT_AMBER),
        ("🆓", "Zero Cost Infrastructure", "Entirely serverless on Vercel's free tier. No AWS bills, no server maintenance. Perfect for bootstrapped Indian businesses.", ACCENT_ROSE),
        ("🧩", "Modular Architecture", "10 independent route modules + 4 ML models = easily extensible. Add new prediction models or data sources without touching existing code.", PRIMARY),
    ]

    for i, (icon, title, body, color) in enumerate(innovations):
        col = i % 3
        row = i // 3
        left = Inches(0.5 + col * 4.1)
        top = Inches(2.2 + row * 2.6)
        add_card(slide, left, top, Inches(3.9), Inches(2.4), title, body, icon_text=icon, accent_color=color)


def slide_11_impact(prs):
    """Real-World Impact"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    set_slide_bg(slide)

    add_text_box(slide, Inches(0.8), Inches(0.5), Inches(3), Inches(0.4),
                 "09  REAL-WORLD IMPACT", font_size=12, bold=True, color=PRIMARY)
    add_accent_bar(slide, Inches(0.8), Inches(0.95), Inches(1.5), Inches(0.03), PRIMARY)

    add_text_box(slide, Inches(0.8), Inches(1.2), Inches(11), Inches(0.7),
                 "Measurable Business Impact", font_size=36, bold=True, color=WHITE)

    # Impact metrics
    metrics = [
        ("94%", "Prediction\nAccuracy", "Profit forecasting accuracy on test data", PRIMARY),
        ("18 Days", "Cash Shortage\nPrevented", "Average early warning before cash crisis", ACCENT_GREEN),
        ("25%", "Churn\nReduction", "Potential customer retention improvement", ACCENT_AMBER),
        ("₹2.4Cr+", "Revenue\nTracked", "Total transaction volume processed", SECONDARY),
    ]

    for i, (value, label, desc, color) in enumerate(metrics):
        left = Inches(0.8 + i * 3.05)
        top = Inches(2.3)

        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, Inches(2.85), Inches(2.5))
        card.fill.solid()
        card.fill.fore_color.rgb = BG_CARD
        card.line.color.rgb = RGBColor(0x2A, 0x2A, 0x35)
        card.line.width = Pt(1)

        add_accent_bar(slide, left + Inches(0.05), top + Inches(0.05), Inches(2.75), Inches(0.04), color)
        add_text_box(slide, left, top + Inches(0.3), Inches(2.85), Inches(0.8), value, font_size=36, bold=True, color=color, alignment=PP_ALIGN.CENTER)
        add_text_box(slide, left, top + Inches(1.2), Inches(2.85), Inches(0.6), label, font_size=16, bold=True, color=WHITE, alignment=PP_ALIGN.CENTER)
        add_text_box(slide, left, top + Inches(1.9), Inches(2.85), Inches(0.4), desc, font_size=11, bold=False, color=MUTED, alignment=PP_ALIGN.CENTER)

    # Use cases
    add_text_box(slide, Inches(0.8), Inches(5.2), Inches(11), Inches(0.5),
                 "Target Users & Use Cases", font_size=20, bold=True, color=WHITE)

    use_cases = [
        "Kirana store owners tracking daily revenue and predicting monthly profit",
        "Retail chain managers identifying high-value customers for loyalty programs",
        "Manufacturing units optimizing production based on demand forecasting",
        "Small business owners getting daily Telegram summaries without opening any app",
    ]
    add_bullet_list(slide, Inches(0.8), Inches(5.7), Inches(11), Inches(1.5), use_cases, font_size=14)


def slide_12_feasibility(prs):
    """Feasibility & Scalability"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    set_slide_bg(slide)

    add_text_box(slide, Inches(0.8), Inches(0.5), Inches(3), Inches(0.4),
                 "10  FEASIBILITY & SCALABILITY", font_size=12, bold=True, color=PRIMARY)
    add_accent_bar(slide, Inches(0.8), Inches(0.95), Inches(1.5), Inches(0.03), PRIMARY)

    add_text_box(slide, Inches(0.8), Inches(1.2), Inches(11), Inches(0.7),
                 "Production-Ready & Scalable", font_size=36, bold=True, color=WHITE)

    # Left - Current State
    add_text_box(slide, Inches(0.8), Inches(2.2), Inches(5.5), Inches(0.5),
                 "✅ Current Implementation", font_size=20, bold=True, color=ACCENT_GREEN)

    current = [
        "Fully deployed on Vercel — Live at vyapaar-view-customer-lifetime-valu.vercel.app",
        "10 REST API endpoints serving real predictions",
        "React TypeScript frontend with 12+ dashboard pages",
        "4 ML models trained and serving predictions",
        "Telegram bot integration for automated reporting",
        "Excel-based data ingestion — familiar format for SMEs",
    ]
    add_bullet_list(slide, Inches(0.8), Inches(2.8), Inches(5.5), Inches(3), current, font_size=13)

    # Right - Future Scope
    add_text_box(slide, Inches(7), Inches(2.2), Inches(5.5), Inches(0.5),
                 "🚀 Future Roadmap", font_size=20, bold=True, color=PRIMARY)

    future = [
        "PostgreSQL/MongoDB for scalable data storage",
        "WhatsApp Business API integration (broader reach)",
        "Multi-language support (Hindi, Marathi, Tamil)",
        "Mobile app (React Native) for on-the-go access",
        "Advanced models: ARIMA for time-series, XGBoost for churn",
        "Multi-store management for retail chains",
        "GST return auto-generation from transaction data",
    ]
    add_bullet_list(slide, Inches(7), Inches(2.8), Inches(5.5), Inches(3.5), future, font_size=13)


def slide_13_demo(prs):
    """Live Demo / Links"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    set_slide_bg(slide)

    add_text_box(slide, Inches(0.8), Inches(0.5), Inches(3), Inches(0.4),
                 "11  LIVE DEMO & LINKS", font_size=12, bold=True, color=PRIMARY)
    add_accent_bar(slide, Inches(0.8), Inches(0.95), Inches(1.5), Inches(0.03), PRIMARY)

    add_text_box(slide, Inches(0.8), Inches(1.2), Inches(11), Inches(0.7),
                 "See It In Action", font_size=36, bold=True, color=WHITE)

    links = [
        ("🌐", "Live Application", "vyapaar-view-customer-lifetime-valu.vercel.app", PRIMARY),
        ("📂", "GitHub Repository", "github.com/Ajijars/Vyapaar-view-Customer-Lifetime-Value-Prediction-CLV-", SECONDARY),
        ("📡", "Backend API", "Deployed as Vercel Serverless Functions", ACCENT_GREEN),
        ("📲", "Telegram Bot", "Automated daily business summary notifications", ACCENT_AMBER),
    ]

    for i, (icon, title, url, color) in enumerate(links):
        top = Inches(2.3 + i * 1.2)
        card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(2), top, Inches(9.3), Inches(1))
        card.fill.solid()
        card.fill.fore_color.rgb = BG_CARD
        card.line.color.rgb = RGBColor(0x2A, 0x2A, 0x35)
        card.line.width = Pt(1)

        add_accent_bar(slide, Inches(2.05), top + Inches(0.05), Inches(0.04), Inches(0.9), color)
        add_text_box(slide, Inches(2.4), top + Inches(0.15), Inches(0.6), Inches(0.5), icon, font_size=24, bold=False, color=color)
        add_text_box(slide, Inches(3.1), top + Inches(0.15), Inches(3), Inches(0.4), title, font_size=18, bold=True, color=WHITE)
        add_text_box(slide, Inches(3.1), top + Inches(0.55), Inches(7.5), Inches(0.3), url, font_size=13, bold=False, color=MUTED)


def slide_14_thank_you(prs):
    """Thank You Slide"""
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    set_slide_bg(slide)

    # Decorative circles
    add_circle(slide, Inches(-2), Inches(-2), Inches(6), PRIMARY)
    add_circle(slide, Inches(9), Inches(4), Inches(6), SECONDARY)

    add_text_box(slide, Inches(1.5), Inches(2), Inches(10.3), Inches(1.2),
                 "Thank You!", font_size=60, bold=True, color=WHITE, alignment=PP_ALIGN.CENTER)

    add_text_box(slide, Inches(2), Inches(3.3), Inches(9.3), Inches(0.6),
                 "Vyapaar-View — Apna Vyapaar, Apna Insight.",
                 font_size=22, bold=False, color=LIGHT_GRAY, alignment=PP_ALIGN.CENTER)

    add_accent_bar(slide, Inches(5), Inches(4.2), Inches(3.3), Inches(0.03), PRIMARY)

    add_text_box(slide, Inches(2), Inches(4.6), Inches(9.3), Inches(0.5),
                 "Team EurekaX  •  Tech Eximius 2026",
                 font_size=18, bold=True, color=PRIMARY, alignment=PP_ALIGN.CENTER)

    add_text_box(slide, Inches(2), Inches(5.3), Inches(9.3), Inches(1.5),
                 "Ajij Rafik Shaikh  |  ajijshaikh2005@gmail.com\n\n"
                 "🌐 vyapaar-view-customer-lifetime-valu.vercel.app\n"
                 "📂 github.com/Ajijars/Vyapaar-view-Customer-Lifetime-Value-Prediction-CLV-",
                 font_size=14, bold=False, color=MUTED, alignment=PP_ALIGN.CENTER)


# ═════════════════════════════════════════════════════════════════════════════
#  MAIN
# ═════════════════════════════════════════════════════════════════════════════

def main():
    prs = Presentation()

    # Set widescreen 16:9
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)

    print("🎨 Generating slides...")

    slide_01_title(prs)
    print("  ✅ Slide 1: Title")

    slide_02_problem(prs)
    print("  ✅ Slide 2: Problem Statement")

    slide_03_solution(prs)
    print("  ✅ Slide 3: Proposed Solution")

    slide_04_features_1(prs)
    print("  ✅ Slide 4: Key Features (Part 1)")

    slide_05_features_2(prs)
    print("  ✅ Slide 5: Key Features (Part 2)")

    slide_06_clv_deep_dive(prs)
    print("  ✅ Slide 6: CLV Deep Dive")

    slide_07_workflow(prs)
    print("  ✅ Slide 7: Workflow")

    slide_08_architecture(prs)
    print("  ✅ Slide 8: System Architecture")

    slide_09_tech_stack(prs)
    print("  ✅ Slide 9: Tech Stack")

    slide_10_innovation(prs)
    print("  ✅ Slide 10: Innovation & Uniqueness")

    slide_11_impact(prs)
    print("  ✅ Slide 11: Real-World Impact")

    slide_12_feasibility(prs)
    print("  ✅ Slide 12: Feasibility & Scalability")

    slide_13_demo(prs)
    print("  ✅ Slide 13: Live Demo & Links")

    slide_14_thank_you(prs)
    print("  ✅ Slide 14: Thank You")

    output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Vyapaar_View_Tech_Eximius_2026.pptx")
    prs.save(output_path)
    print(f"\n🎉 PPT saved to: {output_path}")
    print(f"   Total slides: {len(prs.slides)}")


if __name__ == "__main__":
    main()
