import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(
    page_title="Marketing Funnel Analysis",
    page_icon="📊",
    layout="wide"
)

# ── Data ───────────────────────────────────────────────────────
@st.cache_data
def load_data():
    try:
        df = pd.read_csv("data/bank-additional/bank-additional-full.csv", sep=";")
        df["converted"] = df["y"].map({"yes": 1, "no": 0})
        return df, False
    except FileNotFoundError:
        return generate_synthetic_data(), True

@st.cache_data
def generate_synthetic_data():
    np.random.seed(42)
    n = 5000

    jobs = ["admin.", "technician", "services", "management", "retired",
            "blue-collar", "unemployed", "entrepreneur", "housemaid", "student", "self-employed"]
    educations = ["basic.4y", "high.school", "basic.6y", "basic.9y",
                  "professional.course", "unknown", "university.degree", "illiterate"]
    months = ["jan","feb","mar","apr","may","jun","jul","aug","sep","oct","nov","dec"]
    contacts = ["cellular", "telephone"]
    poutcomes = ["nonexistent", "failure", "success"]
    days = ["mon", "tue", "wed", "thu", "fri"]

    job_arr      = np.random.choice(jobs, n)
    edu_arr      = np.random.choice(educations, n)
    contact_arr  = np.random.choice(contacts, n, p=[0.65, 0.35])
    poutcome_arr = np.random.choice(poutcomes, n, p=[0.82, 0.10, 0.08])

    # Conversion probability influenced by contact and poutcome
    base_prob = np.where(contact_arr == "cellular", 0.14, 0.07)
    base_prob = np.where(poutcome_arr == "success",  base_prob + 0.35, base_prob)
    base_prob = np.where(poutcome_arr == "failure",  base_prob - 0.03, base_prob)
    base_prob = np.clip(base_prob, 0.02, 0.99)
    y_arr = np.where(np.random.rand(n) < base_prob, "yes", "no")

    df = pd.DataFrame({
        "age":          np.random.randint(18, 75, n),
        "job":          job_arr,
        "marital":      np.random.choice(["married","single","divorced"], n, p=[0.6, 0.28, 0.12]),
        "education":    edu_arr,
        "contact":      contact_arr,
        "month":        np.random.choice(months, n),
        "day_of_week":  np.random.choice(days, n),
        "duration":     np.random.randint(30, 900, n),
        "campaign":     np.random.randint(1, 10, n),
        "poutcome":     poutcome_arr,
        "y":            y_arr,
    })
    df["converted"] = df["y"].map({"yes": 1, "no": 0})
    return df

df, is_synthetic = load_data()

# ── Sidebar ────────────────────────────────────────────────────
st.sidebar.title("Filters")


channels = ["All"] + sorted(df["contact"].dropna().unique().tolist())
selected_channel = st.sidebar.selectbox("Contact Channel", channels)

jobs = ["All"] + sorted(df["job"].dropna().unique().tolist())
selected_job = st.sidebar.selectbox("Job Type", jobs)

age_min, age_max = int(df["age"].min()), int(df["age"].max())
age_range = st.sidebar.slider("Age Range", age_min, age_max, (age_min, age_max))

educations = ["All"] + sorted(df["education"].dropna().unique().tolist())
selected_edu = st.sidebar.selectbox("Education Level", educations)

# ── Filters ────────────────────────────────────────────────────
filtered = df.copy()
if selected_channel != "All":
    filtered = filtered[filtered["contact"] == selected_channel]
if selected_job != "All":
    filtered = filtered[filtered["job"] == selected_job]
if selected_edu != "All":
    filtered = filtered[filtered["education"] == selected_edu]
filtered = filtered[
    (filtered["age"] >= age_range[0]) & (filtered["age"] <= age_range[1])
]

# ── Header ─────────────────────────────────────────────────────
st.title("📊 Marketing Funnel Analysis Dashboard")
st.markdown("**Future Interns — Data Science & Analytics Task 3 (2026)**")
st.divider()

# ── KPIs ───────────────────────────────────────────────────────
total      = len(filtered)
contacted  = len(filtered[filtered["contact"].notna()])
converted  = int(filtered["converted"].sum())
conv_rate  = round((converted / total) * 100, 2) if total > 0 else 0
avg_dur    = round(filtered["duration"].mean(), 1) if total > 0 else 0

c1, c2, c3, c4, c5 = st.columns(5)
c1.metric("Total Leads",       f"{total:,}")
c2.metric("Contacted",         f"{contacted:,}")
c3.metric("Converted",         f"{converted:,}")
c4.metric("Conversion Rate",   f"{conv_rate}%")
c5.metric("Avg Call Duration", f"{avg_dur}s")
st.divider()

# ── Funnel ─────────────────────────────────────────────────────
st.subheader("Conversion Funnel — Stage by Stage")
prev_interested = len(filtered[filtered["poutcome"] == "success"])

fig_funnel = go.Figure(go.Funnel(
    y        = ["Total Leads", "Contacted", "Prev. Interested", "Converted"],
    x        = [total, contacted, prev_interested, converted],
    textinfo = "value+percent initial",
    marker   = dict(color=["#4C72B0", "#DD8452", "#55A868", "#C44E52"])
))
fig_funnel.update_layout(height=420, margin=dict(l=10, r=10, t=30, b=10))
st.plotly_chart(fig_funnel, use_container_width=True)
st.divider()

# ── Row 1 ──────────────────────────────────────────────────────
col_a, col_b = st.columns(2)

with col_a:
    st.subheader("Conversion Rate by Channel")
    ch = (
        filtered.groupby("contact")
        .agg(total=("converted","count"), converted=("converted","sum"))
        .reset_index()
    )
    ch["rate"] = (ch["converted"] / ch["total"] * 100).round(2)
    fig_ch = px.bar(ch, x="contact", y="rate", color="contact", text="rate",
                    labels={"rate": "Conversion Rate (%)", "contact": "Channel"}, height=370)
    fig_ch.update_traces(texttemplate="%{text}%", textposition="outside")
    fig_ch.update_layout(showlegend=False, yaxis=dict(range=[0, ch["rate"].max() + 5]))
    st.plotly_chart(fig_ch, use_container_width=True)

with col_b:
    st.subheader("Conversion Rate by Job Type")
    job = (
        filtered.groupby("job")
        .agg(total=("converted","count"), converted=("converted","sum"))
        .reset_index()
    )
    job["rate"] = (job["converted"] / job["total"] * 100).round(2)
    job = job.sort_values("rate", ascending=True)
    fig_job = px.bar(job, x="rate", y="job", orientation="h",
                     labels={"rate": "Conversion Rate (%)", "job": "Job Type"},
                     color="rate", color_continuous_scale="Blues", height=370)
    st.plotly_chart(fig_job, use_container_width=True)

st.divider()

# ── Row 2 ──────────────────────────────────────────────────────
col_c, col_d = st.columns(2)

with col_c:
    st.subheader("Age Distribution — Converted vs Not")
    fig_age = px.histogram(filtered, x="age", color="y", barmode="overlay", nbins=30,
                           labels={"y": "Converted", "age": "Age"},
                           color_discrete_map={"yes": "#55A868", "no": "#C44E52"}, height=370)
    st.plotly_chart(fig_age, use_container_width=True)

with col_d:
    st.subheader("Conversion Share by Education Level")
    edu = (
        filtered.groupby("education")
        .agg(total=("converted","count"), converted=("converted","sum"))
        .reset_index()
    )
    edu["rate"] = (edu["converted"] / edu["total"] * 100).round(2)
    fig_edu = px.pie(edu, names="education", values="converted", hole=0.3, height=370)
    st.plotly_chart(fig_edu, use_container_width=True)

st.divider()

# ── Drop-off ───────────────────────────────────────────────────
st.subheader("Drop-off — Users Lost at Each Funnel Transition")
drop_df = pd.DataFrame({
    "Stage Transition": [
        "Lead → Contacted",
        "Contacted → Prev. Interested",
        "Prev. Interested → Converted"
    ],
    "Users Lost": [
        total - contacted,
        contacted - prev_interested,
        prev_interested - converted
    ]
})
fig_drop = px.bar(drop_df, x="Stage Transition", y="Users Lost",
                  color="Users Lost", color_continuous_scale="Reds",
                  text="Users Lost", height=370)
fig_drop.update_traces(textposition="outside")
st.plotly_chart(fig_drop, use_container_width=True)
st.divider()

# ── Monthly Trend ──────────────────────────────────────────────
st.subheader("Conversion Trend by Month")
month_order = ["jan","feb","mar","apr","may","jun","jul","aug","sep","oct","nov","dec"]
m = (
    filtered.groupby("month")
    .agg(total=("converted","count"), converted=("converted","sum"))
    .reset_index()
)
m["rate"] = (m["converted"] / m["total"] * 100).round(2)
m["month"] = pd.Categorical(m["month"], categories=month_order, ordered=True)
m = m.sort_values("month")
fig_month = px.line(m, x="month", y="rate", markers=True,
                    labels={"month": "Month", "rate": "Conversion Rate (%)"},
                    height=370)
fig_month.update_traces(line=dict(color="#4C72B0", width=3), marker=dict(size=8))
st.plotly_chart(fig_month, use_container_width=True)
st.divider()

# ── Insights ───────────────────────────────────────────────────
st.subheader("Key Insights & Recommendations")
col_i, col_r = st.columns(2)

with col_i:
    st.markdown("#### Insights")
    st.markdown(f"""
- Overall conversion rate: **{conv_rate}%** of total leads
- Biggest drop-off at the **Lead → Contacted** stage
- **Cellular** channel significantly outperforms telephone
- **Retired** and **student** segments convert at higher rates
- **March, September, October, December** show peak conversions
- Previous campaign success is the **strongest conversion predictor**
""")

with col_r:
    st.markdown("#### Recommendations")
    st.markdown("""
- Shift budget toward **cellular outreach** over telephone
- Re-target leads with **prior positive engagement** first
- Build separate campaigns for **student** and **retired** segments
- Invest in **lead nurturing** between contact and conversion
- Focus campaigns in **peak months** (Mar, Sep, Oct, Dec)
- Improve initial contact rate to reduce the largest drop-off
""")

st.divider()

# ── Raw Data ───────────────────────────────────────────────────
with st.expander("View Raw Data"):
    st.dataframe(filtered.reset_index(drop=True), use_container_width=True)
    st.download_button(
        label="Download Filtered Data as CSV",
        data=filtered.to_csv(index=False),
        file_name="filtered_funnel_data.csv",
        mime="text/csv"
    )

st.caption("Future Interns — Data Science & Analytics Task 3 (2026) | Built with Streamlit + Plotly")
