import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Reel Script Prompt Generator", page_icon="🎬", layout="centered")

st.title("🎬 Reel Script Prompt Generator — With Tone Selection")
st.write("Generate a perfected prompt for movie storyline + actor/actress highlights + facts + mini review.")

# Tone options
tone_options = {
    "Cinematic Formal": "Formal yet exciting, cinematic yet respectful. Create hype, curiosity, emotional connection, and audience engagement.",
    "Romantic": "Soft, emotional, heartwarming tone. Highlight chemistry, emotions, love, feelings.",
    "Mystery": "Dark, curious, secretive tone. Build intrigue, hidden clues, unknown truths.",
    "Horror": "Scary, chilling, unsettling tone with atmospheric tension.",
    "Suspense": "Edge-of-seat tension, gripping pauses, shocking reveals.",
    "Action-Mass": "High-energy, powerful tone with mass dialogues and intensity.",
    "Emotional": "Deep feelings, sentimental tone, impactful emotional narration."
}

# --- Input Form ---
with st.form("prompt_form"):
    movie_name = st.text_input("Movie Name", placeholder="eg: Dhurandhar")
    language = st.text_input("Language (full name)", placeholder="eg: Telugu, Gujarati, Hindi")
    channel_name = st.text_input("Channel Name", placeholder="eg: Abbu Reviews")
    line_count = st.number_input("Total Lines in Output Script", min_value=10, max_value=200, value=20, step=1)

    tone = st.selectbox("Select Tone Category", list(tone_options.keys()))

    submitted = st.form_submit_button("Generate Prompt")

if submitted:
    if not movie_name.strip() or not language.strip() or not channel_name.strip():
        st.error("Please fill all required fields: Movie Name, Language, Channel Name.")
    else:

        tone_instruction = tone_options[tone]

        # Build final prompt text
        prompt_text = f"""Generate an Instagram Reel–style movie storyline + actor & actress highlights + interesting facts + mini review script.

🎬 Movie: {{{movie_name}}}
🌐 Language: {{{language}}} (Use pure language; minimal English only if needed)
📺 Channel Name: {{{channel_name}}}
🔢 Total Lines: {{{line_count}}}

🎤 Tone Style:
{tone_instruction}
Flow must feel smooth, polished, and captivating.

✨ STRUCTURE
1. Welcome + Powerful Curiosity Hook (first 3–5 lines)

Start with: “Welcome to {{{channel_name}}}!” (translate naturally)
Build intrigue:
“ఈరోజు ఒక అద్భుతమైన సినిమా విశేషం…”
“మీరు ఈ విషయం వినగానే ఆసక్తి పెరుగుతుంది…”
Create hype:
“చాలామందికి తెలియని రహస్యాలు ఇవాళ బయటపడతాయి!”

2. Short Storyline Summary (next 5–8 lines)
Provide a compact, cinematic, curiosity-based story outline:
- Hero పాత్ర ఏం ఎదుర్కుంటుంది
- కథలో ప్రేమ / భావోద్వేగం / ఘర్షణ
- ప్రధాన సమస్య లేదా మిస్టరీ
- Without spoilers, tease the key conflict

3. Actor & Actress Highlights (next 4–8 lines)
Describe:
- Hero performance & screen presence
- Actress emotional depth or charm
- Their chemistry, intensity, expressions
- Strong scenes they carried
(Do not use actor names unless the user gives.)

4. Daily Movie Facts (next 6–12 lines)
Give short, surprising facts:
- Behind-the-scenes secrets
- Shooting challenges
- Budget vs visuals surprises
- Hidden symbolism
- Crew brilliance
- Rare trivia or records

5. Mini Review Highlights (next 5–10 lines)
Share crisp, formal review points:
- Visual depth
- Music impact
- Cinematic presence
- Action/emotional intensity
- Scene composition
- Narrative flow

6. Weak Points (2–4 lines)
Polite, balanced observations:
- Slight pacing issues
- Minor narrative dips

7. Suspense / Curiosity Questions (2–4 lines)
Ask questions to spark comments:
“ఏ సన్నివేశం మీలో ఎక్కువగా మిగిలింది?”
“ఈ సినిమా దాచుకున్న రహస్యం ఏంటని అనుకుంటారు?”
“మీరు చూసి ఏ అంశం ఆశ્ચర్యపడ్డారు?”

8. CTA — Call To Action (last 2–4 lines)
Formal + engaging:
“మీ అభిప్రాయాన్ని కామెంట్స్‌లో పంచుకోండి.”
“వీడియో నచ్చితే లైక్ & ఫాలో చేయండి.”
Use max 2–3 elegant emojis.

📝 STYLE RULES
Write exactly {{{line_count}}} lines.
Each line MUST begin with “-”.
No quotes.
Lines must be 5–10 words.
Use pure {{{language}}} with minimal English.
Maintain cinematic tone blended with hype + curiosity.

🧾 OUTPUT FORMAT
Return ONLY the final script, exactly {{{line_count}}} lines, each starting with “-”.
No explanations.
"""

        st.subheader("📝 Generated Prompt")
        st.text_area("Copy or edit your prompt here:", prompt_text, height=450)

        # Prepare filename
        safe_movie = movie_name.strip().replace(" ", "_")
        filename = f"{safe_movie}_prompt_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

        st.download_button(
            label="📥 Download Prompt as .txt",
            data=prompt_text.encode("utf-8"),
            file_name=filename,
            mime="text/plain",
        )

        st.success("Prompt generated successfully! 🎉")
