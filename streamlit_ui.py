import streamlit as st
from app import get_watch_recommendations

st.set_page_config(
    page_title="WatchWise | AI Entertainment Discovery",
    page_icon="🎬",
    layout="wide"
)

st.title("🎬 WatchWise")
st.subheader("Your AI-powered entertainment discovery engine")

st.write(
    "Stop endless scrolling. Describe your mood, vibe, or what kind of story "
    "you want to watch, and let WatchWise curate your next watch."
)

discovery_tab, watchlist_tab = st.tabs(["AI Discovery", "My Watchlist"])

with discovery_tab:
    st.header("What are you in the mood for?")

    with st.form("watch_form"):
        user_query = st.text_area(
            "Describe your vibe or query",
            placeholder="E.g., A mind-bending psychological thriller with a plot twist, similar to Shutter Island, with a runtime under 2 hours."
        )
        
        col1, col2 = st.columns(2)
        with col1:
            preferred_platform = st.selectbox(
                "Preferred OTT Platform",
                ["Any Platform", "Netflix", "Amazon Prime Video", "Disney+ Hotstar", "Apple TV+", "SonyLIV", "Zee5"]
            )
        with col2:
            max_runtime = st.selectbox(
                "Runtime / Length Preference",
                ["Any Length", "Quick watch (Under 1.5 hours)", "Standard feature (Under 2 hours)", "Epic length (2+ hours)", "Web Series / Multi-season"]
            )

        submit_btn = st.form_submit_button("Find Recommendations", type="primary")

    if submit_btn:
        if not user_query.strip():
            st.warning("Please describe what you're in the mood to watch...")
        else:
            try:
                with st.spinner("Curating your personalized watchlist..."):
                    result = get_watch_recommendations(user_query, preferred_platform, max_runtime)

                st.success("Curated Recommendations Ready!")

                # Curator Note
                st.info(f"💡 **Curator Note:** {result['curator_note']}")

                st.subheader("Recommended For You")

                # Render recommendations in columns / cards
                recommendations = result["recommendations"]
                for i in range(0, len(recommendations), 2):
                    col_a, col_b = st.columns(2)
                    
                    # Left Card
                    with col_a:
                        rec = recommendations[i]
                        with st.container(border=True):
                            st.markdown(f"### 🎥 {rec['title']}")
                            st.caption(f"**Genres:** {', '.join(rec['genre'])}")
                            st.write(f"⏱️ **Runtime/Seasons:** {rec['runtime_or_seasons']}")
                            st.write(f"📺 **Platform:** {rec['ott_platform']}")
                            st.markdown(f"**Why watch:** {rec['match_reason']}")

                    # Right Card (if available)
                    if i + 1 < len(recommendations):
                        with col_b:
                            rec_right = recommendations[i + 1]
                            with st.container(border=True):
                                st.markdown(f"### 🎥 {rec_right['title']}")
                                st.caption(f"**Genres:** {', '.join(rec_right['genre'])}")
                                st.write(f"⏱️ **Runtime/Seasons:** {rec_right['runtime_or_seasons']}")
                                st.write(f"📺 **Platform:** {rec_right['ott_platform']}")
                                st.markdown(f"**Why watch:** {rec_right['match_reason']}")

            except BaseException as ex:
                st.error(f"Recommendation generation failed: {ex}")

with watchlist_tab:
    st.header("Your Watchlist")
    st.write("Saved items and custom watchlists will appear here.")