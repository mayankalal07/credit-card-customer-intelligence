import streamlit as st
import pandas as pd

# Load Data
df = pd.read_csv("customer_360.csv")
feature_importance = pd.read_csv(
    "feature_importance.csv"
)

# Title
st.title("💳 Credit Card Customer Intelligence Platform")
segment_names = {
    0: "Emerging Customers",
    1: "Stable Everyday Customers",
    2: "Premium Power Users",
    3: "Family Shoppers",
    4: "Digital First Customers"
}

page = st.sidebar.selectbox(
    "Choose Page",
    [
        "Overview",
        "Customer Search",
        "Segment Explorer",
        "Feature Importance",
        "AI Customer Analyst",
        "Project Summary Page"
    ]
)
recommendations = {
                0: "Welcome Cashback Offer",
                1: "Loyalty Rewards Program",
                2: "Premium Travel Card",
                3: "Grocery & Retail Cashback",
                4: "E-Commerce Cashback Card"
}

import os

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


if page == "Overview":

    st.subheader("Project Overview")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Customers", len(df))

    with col2:
        st.metric("Segments", df["cluster_5"].nunique())

    with col3:
        st.metric(
            "High Value Customers",
            df["high_value"].sum()
        )

    with col4:
        st.metric(
            "Avg Spend",
            f"${df['total_spend'].mean():,.0f}"
        )

    st.subheader("Cluster Distribution")

    st.bar_chart(
        df["cluster_5"].value_counts()
    )
    st.subheader("Business Insights")

    st.info("""
    Top Driver of Value:
    Transaction Count

    Most Valuable Segment:
    Premium Power Users

    Most Digital Segment:
    Digital First Customers

    Recommended Strategy:
    Segment-based personalization
    """)
    st.markdown("---")

    st.caption(
        "Built by Mayan Kalal | Customer Intelligence Platform | ML + GenAI"
    )
elif page == "Customer Search":

    st.subheader("Customer Search")

    customer_id = st.number_input(
        "Enter Customer ID",
        min_value=0,
        max_value=int(df["User"].max())
    )

    customer = df[
        df["User"] == customer_id
    ]

    if len(customer) > 0:

        cust = customer.iloc[0]

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "Total Spend",
                f"${cust['total_spend']:,.0f}"
            )

            st.metric(
                "Transactions",
                int(cust["transaction_count"])
            )

        with col2:
            st.metric(
                "Tenure",
                f"{cust['tenure']} Years"
            )
            segment_names = {
                0: "Emerging Customers",
                1: "Stable Everyday Customers",
                2: "Premium Power Users",
                3: "Family Shoppers",
                4: "Digital First Customers"
            }


            st.subheader("Customer Segment")

            st.info(
                segment_names[
                    int(cust["cluster_5"])
                ]
            )
            st.subheader("Recommendation")
            recommendations = {
                0: "Welcome Cashback Offer",
                1: "Loyalty Rewards Program",
                2: "Premium Travel Card",
                3: "Grocery & Retail Cashback",
                4: "E-Commerce Cashback Card"
            }

            st.success(
                recommendations[
                    int(cust["cluster_5"])
                ]
            )
            st.subheader("High Value Status")

            if cust["high_value"] == 1:
                st.success("High Value Customer")
            else:
                st.warning("Regular Customer")
    st.markdown("---")

    st.caption(
        "Built by Mayan Kalal | Customer Intelligence Platform | ML + GenAI"
    )
elif page == "Segment Explorer":

    st.subheader("Segment Explorer")

    segment_names = {
        0: "Emerging Customers",
        1: "Stable Everyday Customers",
        2: "Premium Power Users",
        3: "Family Shoppers",
        4: "Digital First Customers"
    }
    selected_segment_name = st.selectbox(
        "Select Segment",
        list(segment_names.values())
    )
    reverse_segment_names = {
        v: k for k, v in segment_names.items()
    }
    selected_segment = reverse_segment_names[
        selected_segment_name
    ]

    segment_data = df[
        df["cluster_5"] == selected_segment
    ]

    st.metric(
        "Customers",
        len(segment_data)
    )

    st.metric(
        "Average Spend",
        f"${segment_data['total_spend'].mean():,.0f}"
    )

    st.dataframe(
        segment_data[
            [
                "User",
                "total_spend",
                "transaction_count",
                "high_value"
            ]
        ]
    )
    segment_descriptions = {
        0: "Low activity and low spend customers.",
        1: "Long-tenure customers with steady everyday usage.",
        2: "Highest spending and most engaged customers.",
        3: "Customers focused on grocery and retail purchases.",
        4: "Customers with high online transaction behavior."
    }
    st.info(
        segment_descriptions[selected_segment]
    )
    st.markdown("---")

    st.caption(
        "Built by Mayan Kalal | Customer Intelligence Platform | ML + GenAI"
    )
elif page == "Feature Importance":

    st.subheader(
        "Drivers of High Value Customers"
    )

    st.bar_chart(
        feature_importance.set_index("feature")
        ["importance"]
        .head(15)
    )
    st.subheader("Key Insights")

    st.markdown("""
    ### Top Drivers

    1. **Transaction Count**
    - Most important predictor of high-value customers.
    - Frequent card usage is strongly associated with customer value.

    2. **Customer Segment**
    - Segment membership significantly influences customer value.

    3. **Merchant Diversity**
    - Customers shopping across more merchants and categories tend to be more valuable.

    4. **Geographic Diversity**
    - Customers transacting across more cities show higher engagement.
    """)
    st.dataframe(
        feature_importance.head(15)
    )
    st.markdown("---")

    st.caption(
        "Built by Mayan Kalal | Customer Intelligence Platform | ML + GenAI"
    )
elif page == "AI Customer Analyst":

    st.subheader("AI Customer Analyst")
    customer_id = st.number_input(
        "Enter Customer ID",
        min_value=0,
        max_value=int(df["User"].max())
    )

    customer = df[
        df["User"] == customer_id
    ]
    if len(customer) > 0:
        cust = customer.iloc[0]

        segment = segment_names[
            int(cust["cluster_5"])
        ]

        recommendation = recommendations[
            int(cust["cluster_5"])
        ]

        high_value = (
            "High Value Customer"
            if cust["high_value"] == 1
            else "Regular Customer"
        )
        prompt = f"""
        You are a senior banking customer analyst.

        Customer Information:

        Segment:
        {segment}

        Total Spend:
        {cust['total_spend']:,.0f}

        Transactions:
        {cust['transaction_count']}

        Tenure:
        {cust['tenure']}

        Unique Merchant Categories:
        {cust['unique_mcc']}

        Unique Merchants:
        {cust['unique_merchants']}

        Online Transaction Share:
        {cust['online_pct']:.2%}

        Fraud Rate:
        {cust['fraud_rate']:.4f}

        Refund Rate:
        {cust['refund_rate']:.4f}

        Current Recommendation:
        {recommendation}

        Customer Status:
        {high_value}
        Segment Description:
        Long-tenure customers with steady everyday usage.

        Provide:

        1. Executive Summary
        2. Behavioral Analysis
        3. Business Opportunity
        4. Risks
        5. Recommended Actions

        Keep the response business-focused and concise.
        Important:
        When discussing risks, classify them as:

        1. Observed Risks
        2. Potential Risks
        3. Unassessable Risks

        Only place a risk in Observed Risks if supported by the provided data.

        Never state that there are no risks.

        Instead, distinguish between:

        1. Observed risks from available data.
        2. Risks that cannot be assessed due to missing information.
        Important:

Only use the information provided.

Do not assume facts that are not present in the customer data.

If evidence is unavailable, explicitly state that.
Important:

Recommendations must align with the customer's segment
and observed behavior.

Do not recommend behavior changes unless supported
by the customer profile.
        """
    if st.button(
        "Generate AI Analysis"
    ):
        response = (
            client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )
        )     
                    
        analysis = (
            response
            .choices[0]
            .message
            .content
        )
        with st.container():
            st.markdown(analysis)
    st.markdown("---")

    st.caption(
        "Built by Mayan Kalal | Customer Intelligence Platform | ML + GenAI"
    )
elif page == "Project Summary Page":
    st.subheader("Project Summary Page")
    st.metric("Customers", 500)
    st.metric("Segments", 5)
    st.metric("High Value Customers", 100)

    st.subheader("Key Findings")

    st.write("""
    • Premium Power Users generate the highest spend.

    • Digital First Customers have the highest online transaction share.

    • Transaction Count is the strongest predictor of customer value.

    • Merchant diversity is strongly associated with high-value customers.

    • Loyalty programs are recommended for long-tenure customers.
    """)
    st.markdown("---")

    st.caption(
        "Built by Mayan Kalal | Customer Intelligence Platform | ML + GenAI"
    )