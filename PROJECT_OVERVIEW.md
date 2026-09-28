# Vyapaar-View: Project Overview

**"Apna Vyapaar, Apna Insight."**

An AI-powered Business Intelligence Platform designed specifically for Indian SMEs (Small and Medium Enterprises) to help them make data-backed decisions.

---

## 1. Problem Statement (PS)
**Indian SMEs are flying blind.** 
Over 63 million MSMEs in India lack affordable, easy-to-use AI-driven tools. This results in:
- **Cash Flow Blindness:** 78% of SMEs face unexpected cash shortages with no real-time visibility into incoming vs. outgoing cash.
- **Customer Churn:** Businesses lose 15-25% of revenue from undetected customer churn because no early-warning systems exist.
- **No Data Analytics:** Most rely on Excel or manual registers. No profit predictions, demand forecasting, or trend analysis.
- **Inventory Waste:** Overstocking and stockouts cost Indian retail ₹1.2L Cr/year due to a lack of smart inventory management.

## 2. The Solution
**Vyapaar-View: Your AI Business Co-Pilot.**
A full-stack, ML-powered business intelligence platform that transforms raw sales, expense, and customer data into actionable insights. 
- **Built for India:** INR-first, GST-aware, Hindi-ready, and tuned for Indian retail patterns.
- **ML at Core:** 4 trained ML models for Profit, Churn, Customer Lifetime Value (RFM), and Demand forecasting.
- **Telegram Alerts:** Automated daily close-of-business reports sent directly to the owner's phone.
- **Zero Infrastructure:** Deployed on Vercel—no servers, no complex setup. Just login and go.

## 3. Key Features
- **Comprehensive Analytics Dashboard:** Real-time KPIs (Total Revenue, Net Profit, Cash Balance, Business Health Score) with sparkline trends.
- **Profit Prediction:** ML-powered monthly profit forecasting using Linear Regression on revenue & expense patterns.
- **Churn Prediction:** Logistic Regression model identifies at-risk customers based on purchase frequency & spending patterns.
- **Customer Lifetime Value (CLV):** RFM-based CLV scoring (Recency 40%, Frequency 35%, Monetary 25%) segmenting customers into Champion, Loyal, At Risk, and Lost.
- **Inventory Management:** Smart stock tracking with low-inventory alerts and product-level analytics.
- **Telegram Bot Integration:** Daily close-of-business reports auto-sent to the owner's Telegram (revenue, profit, orders, low-stock alerts).
- **AI Assistant & Trend Analysis:** Conversational AI for natural-language queries and discovery of top-selling products and seasonal patterns.

## 4. Tech Stack
- **Frontend (Presentation Layer):**
  - React 18 & TypeScript
  - Vite (Build Tool)
  - TailwindCSS & shadcn/ui (Styling & Components)
  - Recharts (Data Visualizations)
  - Framer Motion (Animations)
- **Backend (API Layer):**
  - FastAPI (Async Python framework)
  - Python 3.11+
  - Pandas (Data processing)
  - Pydantic (Data validation)
- **Machine Learning (Intelligence):**
  - scikit-learn & NumPy
  - Linear Regression (Profit, CLV, Demand)
  - Logistic Regression (Churn prediction)
  - MinMaxScaler & RFM Engine
- **DevOps & Infrastructure:**
  - Vercel (Frontend + Serverless Backend deployment)
  - Telegram Bot API (Push notifications)

## 5. Unique Selling Proposition (USP) & Innovation
- **India-First Design:** Built ground-up for Indian MSME patterns (INR formatting, Indian fiscal cycles, GST-aware calculations).
- **Real-Time ML Pipeline:** Models retrain on the fly with every API call using the latest data, ensuring no stale predictions.
- **RFM + ML Hybrid:** Combines traditional RFM customer segmentation with Linear Regression for CLV prediction.
- **WhatsApp-Style Alerts:** Telegram bot integration makes receiving daily business summaries effortless without opening an app.
- **Zero Cost Infrastructure:** Entirely serverless on Vercel's free tier, avoiding AWS bills and server maintenance for bootstrapped businesses.
- **Modular Architecture:** 10 independent route modules and 4 ML models allow easy extensibility and adding new features.

---
**Team:** EurekaX
**Theme:** AI & Machine Learning / FinTech
**Hackathon:** Tech Eximius 2026
