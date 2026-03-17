import streamlit as st
from utils.brand_analysis import analyze_brand_voice
from utils.prompt_templates import build_prompt
from utils.tweet_generator import generate_tweets


def set_style():
    st.markdown(
        """
        <style>
        .stApp {
            background: linear-gradient(135deg, #eff6ff 0%, #dbeafe 40%, #bfdbfe 100%);
            color: #1f2937;
        }
        .stMarkdown h1, .stMarkdown h2, .stMarkdown h3, .stMarkdown p {
            color: #1f2937;
            text-shadow: none;
        }
        .stMarkdown h1 {
            color: #1d4ed8;
            font-size: 2.75rem;
        }
        .stMarkdown h2 {
            color: #1e40af;
            font-size: 2rem;
        }
        .stMarkdown h3 {
            color: #1e3a8a;
            font-size: 1.5rem;
        }
        .stMarkdown p {
            color: #334155;
        }
        .stButton>button {
            background-color: #2563eb;
            color: #ffffff;
            font-weight: 700;
            border-radius: 8px;
        }
        .stDownloadButton>button {
            background-color: #059669;
            color: #ffffff;
            font-weight: 700;
            border-radius: 8px;
        }
        .stTextInput>div>div>input,
        .stTextArea>div>div>textarea,
        .stSelectbox>div>div>div>span {
            background-color: #ffffff !important;
            color: #0f172a !important;
            border: 1px solid #3b82f6;
        }
        .css-1d391kg {
            color: #0f172a !important;
        }
        .stDivider {
            border-color: #93c5fd;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def main():
    st.set_page_config(
        page_title="AI Brand Tweet Generator",
        layout="centered",
        initial_sidebar_state="expanded",
        page_icon="✨",
    )

    set_style()

    st.markdown("# ✨ AI Brand Tweet Generator")
    st.markdown("_Generate 10 on-brand tweets with style — fast, fun, and focused._")

    with st.expander("🚀 How to use", expanded=True):
        st.write("1. Enter your brand details.\n2. Click Generate Tweets.\n3. Copy or download results.")

    with st.form(key="brand_form"):
        col1, col2 = st.columns(2)
        with col1:
            brand_name = st.text_input("Brand Name", value="")
            industry = st.text_input("Industry", value="")

        with col2:
            campaign_objective = st.selectbox(
                "Campaign Objective",
                ["awareness", "engagement", "promotion"],
                index=0,
            )
            description = st.text_area("Brand Description", height=140)

        generate_button = st.form_submit_button("Generate Tweets")

    if generate_button:
        if not brand_name or not industry or not description:
            st.warning("Fill in Brand Name, Industry, and Brand Description to proceed.")
            return

        try:
            with st.spinner("Analyzing brand voice..."):
                brand_voice = analyze_brand_voice(brand_name, industry, description)

            with st.spinner("Building prompt..."):
                prompt = build_prompt(
                    brand_voice,
                    {
                        "brand_name": brand_name,
                        "campaign_objective": campaign_objective,
                    },
                )

            with st.spinner("Generating tweets..."):
                tweets = generate_tweets(prompt, brand_name=brand_name)

            st.divider()
            st.markdown("## 🔹 Brand Voice Summary")

            st.success(f"**Tone:** {brand_voice.get('tone')}")
            st.info(f"**Audience:** {brand_voice.get('target_audience')}")
            themes = brand_voice.get("content_themes", [])
            st.write(f"**Themes:** {', '.join(themes)}")

            st.markdown("## 🔹 Generated Tweets")
            for idx, tweet in enumerate(tweets, start=1):
                st.markdown(f"**{idx}.** {tweet}")

            clipboard_text = "\n".join([f"{i+1}. {t}" for i, t in enumerate(tweets)])

            coldl, coldr = st.columns([1, 1])
            with coldl:
                st.download_button(
                    label="Download tweets as .txt",
                    data=clipboard_text,
                    file_name=f"{brand_name.replace(' ', '_')}_tweets.txt",
                    mime="text/plain",
                )
            with coldr:
                if st.button("Show copy text"):
                    st.code(clipboard_text)

        except Exception as e:
            st.error(f"Failed to generate tweets: {e}")


if __name__ == "__main__":
    main()
