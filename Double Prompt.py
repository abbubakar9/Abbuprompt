import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Reel Script Prompt Generator", page_icon="🎬", layout="centered")

st.title("🎬 Reel Script Prompt Generator — Choose Prompt Template")
st.write("Enter movie details, pick a prompt template from the dropdown, and generate the final prompt text for your AI.")

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

# Prompt templates dropdown
prompt_templates = {
    "Full Review (Story + Facts + Review)": "Full Review (Story + Facts + Review)",
    "Storyline Hype Only": "Storyline Hype Only"
}

# --- Input Form ---
with st.form("prompt_form"):
    movie_name = st.text_input("Movie Name", placeholder="eg: Dhurandhar")
    language = st.text_input("Language (full name)", placeholder="eg: Telugu, Gujarati, Hindi")
    channel_name = st.text_input("Channel Name", placeholder="eg: Abbu Reviews")
    line_count = st.number_input("Total Lines in Output Script", min_value=10, max_value=200, value=20, step=1)

    selected_template = st.selectbox("Select Prompt Template", list(prompt_templates.keys()))
    tone = st.selectbox("Select Tone Category", list(tone_options.keys()))

    submitted = st.form_submit_button("Generate Prompt")

if submitted:
    if not movie_name.strip() or not language.strip() or not channel_name.strip():
        st.error("Please fill all required fields: Movie Name, Language, Channel Name.")
    else:
        tone_instruction = tone_options[tone]

        if selected_template == "Full Review (Story + Facts + Review)":
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
Provide a compact, cinematic summary:
- Hero పాత్ర ఏం ఎదుర్కుంటుంది
- కథలో భావోద్వేగం / ప్రేమ / ఘర్షణ
- ప్రధాన సమస్య లేదా మిస్టరీ
- Without spoilers, tease the key conflict

3. Actor & Actress Highlights (next 4–8 lines)
Describe:
- Hero presence
- Actress charm
- Chemistry
- Strong scenes they carried
- Expressions and intensity
(Do not use actor names unless user gives.)

4. Daily Movie Facts (next 6–12 lines)
Give short, surprising facts:
- Behind-the-scenes secrets
- Shooting challenges
- Budget vs visuals surprises
- Hidden symbolism
- Crew brilliance
- Rare trivia or records

5. Mini Review Highlights (next 5–10 lines)
Share crisp review points:
- Story strength
- Emotional beats
- Scene composition
- Narrative impact

6. Weak Points (2–4 lines)
Polite, balanced observations.

7. Suspense / Curiosity Questions (2–4 lines)
Ask questions in {{{language}}} that boost curiosity.

8. CTA — Call To Action (last 3–5 lines)
Translate naturally into {{{language}}}:
- If you haven't watched this movie, you must watch it now.
- We will meet again in the next video.
- Like, share, and follow. (Use 2–3 elegant emojis)

📝 STYLE RULES
- Write exactly {{{line_count}}} lines.
- Each line MUST begin with "-" .
- No quotes.
- Lines must be 5–10 words.
- Use pure {{{language}}} with minimal English.
- Maintain cinematic tone blended with hype + curiosity.

🧾 OUTPUT FORMAT
Return ONLY the final script, exactly {{{line_count}}} lines.
Each line must start with "-".
No explanations.
"""
        else:
            # Storyline Hype Only prompt (clean story + suspense, no BTS/music/visuals)
            prompt_text = f"""Generate an Instagram Reel–style movie storyline–only script
that creates hype and curiosity to watch the film.

🎬 Movie: {{{movie_name}}}
🌐 Language: {{{language}}} (Use pure language; minimal English only if needed)
📺 Channel Name: {{{channel_name}}}
🔢 Total Lines: {{{line_count}}}

🎤 Tone Style:
{tone_instruction}
Focus ONLY on story, characters, conflict, suspense, and curiosity.
Do NOT mention music, visuals, cinematography, editing, behind-the-scenes,
budget, songs, or technical elements.

✨ STRUCTURE

1. Welcome + Curiosity Hook (first 3–5 lines)
- Start with a natural translation of “Welcome to {{{channel_name}}}!”
- Introduce the movie in an intriguing way.
- Hint that hidden truths or shocking events await.
- Create hype and curiosity about what happens.

2. Core Story Setup (next 5–8 lines)
- Introduce the main character and their world.
- Explain what they want, what they fear, or what they protect.
- Introduce the central emotional or dramatic situation.
- Reveal what threatens their life, love, family, or peace.
- Do NOT reveal spoilers.

3. Rising Conflict & Stakes (next 5–10 lines)
- Describe how the situation becomes dangerous or unpredictable.
- Hint at betrayals, conflicts, secrets, or major turning points.
- Show the hero’s struggle, doubts, and pressure.
- Build tension that something big is coming.

4. Tease Twists Without Spoiling (3–5 lines)
- Suggest hidden motives, unanswered questions, or mysterious events.
- Hint that not everything is as it appears.
- Build suspense so viewers want to watch the film.

5. Suspense Questions (2–4 lines)
- Ask powerful questions that spark comments:
  “આગળ શું બનશે?”
  “હીરો આ સ્થિતિમાંથી કેવી રીતે બહાર આવશે?”
  “સત્ય કોને ખબર છે?”

6. CTA — Story-Based Call To Action (last 3–5 lines)
Translate these into {{{language}}}:
- If you haven't watched this movie, you should watch it now.
- We will meet again in the next video.
- Like, share, and follow for more. (Use max 2–3 elegant emojis)

📝 STYLE RULES
- Write exactly {{{line_count}}} lines.
- Each line MUST begin with "-" .
- No quotation marks.
- Lines must be 5–10 words.
- Use pure {{{language}}} with minimal English.
- Do NOT mention music, visuals, or behind-the-scenes.
- Maintain the chosen tone: {tone}.
- Keep lines clean, short, cinematic, and audience-friendly.

🧾 OUTPUT FORMAT
Return ONLY the final script, exactly {{{line_count}}} lines,
each starting with "-".
No explanations, no extra text.
"""

        st.subheader("📝 Generated Prompt")
        st.text_area("Copy or edit your prompt here:", prompt_text, height=450)

        # Prepare filename
        safe_movie = movie_name.strip().replace(" ", "_")
        mode_tag = "story_only" if selected_template == "Storyline Hype Only" else "full_review"
        filename = f"{safe_movie}_{mode_tag}_prompt_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

        st.download_button(
            label="📥 Download Prompt as .txt",
            data=prompt_text.encode("utf-8"),
            file_name=filename,
            mime="text/plain",
        )

        st.success("Prompt generated successfully! 🎉")
