import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Reel Script Prompt Generator", page_icon="🎬", layout="centered")
st.title("🎬 Reel Script Prompt Generator — Genre + Language Templates")
st.write("Enter movie details, pick a prompt template and tone/genre, and generate a final prompt (Telugu / Hindi / Gujarati templates included).")

# Tone/Genre options (keeps previous tone language but also used as genre)
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
prompt_templates = [
    "Full Review (Story + Facts + Review)",
    "Storyline Hype Only"
]

# Genre selection (used for genre-based must-watch reasons)
genre_options = [
    "Cinematic Formal", "Romantic", "Mystery", "Horror", "Suspense", "Thriller", "Action-Mass", "Emotional"
]

# Language templates for short sample phrases used in prompt (automatic)
language_templates = {
    "Telugu": {
        "welcome": "{CHANNEL}కి స్వాగతం!",
        "intrigue1": "ఈరోజు ఒక అద్భుతమైన సినిమా విశేషం…",
        "intrigue2": "మీరు ఈ విషయం వినగానే ఆసక్తి పెరుగుతుంది…",
        "intrigue3": "చాలామందికి తెలియని రహస్యం ఇప్పుడు బయటపడుతుంది!",
        "suspense_q1": "ఈ సన్నివేశం మీలో ఎంత మిగిలింది?",
        "suspense_q2": "ఈ సినిమా దాచుకున్న రహస్యం ఏంటనని అనుకుంటారు?",
        "cta_watch": "మీరు ఇంకా చూడకపోయి ఉంటే, ఇప్పుడే చూడండి.",
        "cta_meet": "మనం మరో వీడియోలో కలుద్దాం.",
        "cta_follow": "లైక్, షేర్, ఫాలో చేయండి."
    },
    "Hindi": {
        "welcome": "{CHANNEL} में आपका स्वागत है!",
        "intrigue1": "आज हम एक अद्भुत फिल्म का रहस्य बताएंगे...",
        "intrigue2": "यह सुनकर आपकी जिज्ञासा बढ़ जाएगी...",
        "intrigue3": "कई लोगों को नहीं पता ऐसे राज आज उजागर होंगे!",
        "suspense_q1": "यह दृश्य आपको कितना प्रभावित करता है?",
        "suspense_q2": "क्या यह फिल्म कोई छिपा हुआ रहस्य रखती है?",
        "cta_watch": "अगर आपने अभी तक नहीं देखा है, अभी देखें.",
        "cta_meet": "हम फिर अगले वीडियो में मिलेंगे.",
        "cta_follow": "लाइक, शेयर और फॉलो करें."
    },
    "Gujarati": {
        "welcome": "{CHANNEL} માં આપનું સ્વાગત છે!",
        "intrigue1": "આજે અમે એક અદ્ભૂત ફિલ્મનું રહસ્ય ખુલાસો કરીશું...",
        "intrigue2": "આ સાંભળતા જ તમારી રસપ્રદતા વધશે...",
        "intrigue3": "ઘણા લોકોને ન ખબર હોય તેવા રહસ્યો હવે બહાર આવશે!",
        "suspense_q1": "આ દૃશ્ય તમને કેટલું પ્રભાવિત કરે છે?",
        "suspense_q2": "શું આ ફિલ્મમાં કોઈ છુપાયેલું રહસ્ય છે?",
        "cta_watch": "જો તમે હજી સુધી ન જોયું હોય, હવે જ જુઓ.",
        "cta_meet": "અમે ફરી આગળના વિડિયોમાં મળશે.",
        "cta_follow": "લાઈક, શેર અને ફોલો કરો."
    }
}

# --- Input Form ---
with st.form("prompt_form"):
    movie_name = st.text_input("Movie Name", placeholder="eg: Dhurandhar")
    language_choice = st.selectbox("Language (choose template)", ["Telugu", "Hindi", "Gujarati", "Other (custom)"])
    custom_language = st.text_input("If Other: enter language name (leave blank if not used)", placeholder="eg: Kannada")
    channel_name = st.text_input("Channel Name", placeholder="eg: Abbu Reviews")
    line_count = st.number_input("Total Lines in Output Script", min_value=10, max_value=200, value=20, step=1)

    selected_template = st.selectbox("Select Prompt Template", prompt_templates)
    tone = st.selectbox("Select Tone (affects wording)", list(tone_options.keys()))
    genre = st.selectbox("Select Genre (drives must-watch reasons)", genre_options)

    submitted = st.form_submit_button("Generate Prompt")

if submitted:
    if not movie_name.strip() or not channel_name.strip():
        st.error("Please fill the required fields: Movie Name and Channel Name.")
    else:
        # determine language key and template phrases
        if language_choice == "Other (custom)":
            lang_label = custom_language.strip() or "YourLanguage"
            tpl = {
                "welcome": "{CHANNEL} కి స్వాగతం!",
                "intrigue1": "An intriguing intro line goes here...",
                "intrigue2": "This line should increase curiosity...",
                "intrigue3": "Hidden secrets may be revealed in this movie!",
                "suspense_q1": "What will happen next?",
                "suspense_q2": "Who hides the truth?",
                "cta_watch": "If you haven't watched, watch it now.",
                "cta_meet": "We will meet in the next video.",
                "cta_follow": "Like, share, and follow."
            }
        else:
            lang_label = language_choice
            tpl = language_templates.get(language_choice, language_templates["Telugu"])

        tone_instruction = tone_options[tone]

        # Build the prompt_text based on selected template
        # Insert AI-powered strong-point detection and genre-based must-watch reasons
        if selected_template == "Full Review (Story + Facts + Review)":
            prompt_text = f"""Generate an Instagram Reel–style movie storyline + actor & actress highlights + interesting facts + mini review script.

🎬 Movie: {movie_name}
🌐 Language: {lang_label} (Use pure language; minimal English only if needed)
📺 Channel Name: {channel_name}
🔢 Total Lines: {line_count}

🎤 Tone Style:
{tone_instruction}
Flow must feel smooth, polished, and captivating.

✨ STRUCTURE

1. Welcome + Powerful Curiosity Hook (first 3–5 lines)
Start with a natural translation of: "{tpl['welcome']}". Insert the channel name in place of {{CHANNEL}}.
Use intrigue examples adapted to {lang_label}:
- {tpl['intrigue1']}
- {tpl['intrigue2']}
- {tpl['intrigue3']}

2. Short Storyline Summary (next 5–8 lines)
Provide a compact, cinematic summary:
- Hero's struggle
- Emotion / love / conflict
- Main problem or mystery
- Tease the key conflict without spoilers

3. Actor & Actress Highlights (next 4–8 lines)
Describe:
- Screen presence
- Chemistry
- Emotional impact
- Strong scenes
- Expressions and intensity
(Do not use actor names unless provided.)

4. Daily Movie Facts (next 6–12 lines)
Give short, surprising facts:
- Hidden details
- Shooting challenges
- Interesting trivia
- Story inspirations

5. Mini Review Highlights (next 5–10 lines)
Share crisp review points:
- Narrative strength
- Emotional weight
- Scene richness
- Story flow

6. Weak Points (2–4 lines)
Polite, balanced observations.

7. Why People Should Watch (3–5 lines)
🧠 AI-Powered Strong-Point Detection:
Analyze the movie's storyline and automatically identify:
- The strongest emotional hook or core conflict
- The highest-tension moment or turning point
- The unique plot element or twist viewers must see
- The decision or scene that defines the film

🎭 Genre-Based Must-Watch Reasons (focus: {genre}):
- If genre = Romantic → emphasize emotional chemistry, love vs conflict, heart-melting moments
- If genre = Mystery/Thriller/Suspense → emphasize hidden clues, twists, conspiracies, and high stakes
- If genre = Horror → emphasize terrifying tension, dread, and unforgettable scares
- If genre = Action-Mass → emphasize hero elevation, powerful confrontations, and goosebump moments
- If genre = Emotional → emphasize character sacrifice, touching arcs, and emotional payoffs

Write 3–5 strong, persuasive lines in {lang_label} that make viewers feel:
"This movie is impossible to miss."

8. Suspense / Curiosity Questions (2–4 lines)
Use sample curiosity questions adapted to {lang_label}:
- {tpl['suspense_q1']}
- {tpl['suspense_q2']}

9. CTA — Call To Action (last 3–5 lines)
Translate and include these in {lang_label}:
- {tpl['cta_watch']}
- {tpl['cta_meet']}
- {tpl['cta_follow']}

📝 STYLE RULES
- Write exactly {line_count} lines.
- Every line MUST begin with "-".
- No quotation marks.
- Lines must be 5–10 words.
- Use pure {lang_label} with minimal English.
- Maintain cinematic tone blended with hype + curiosity.
- Use genre-focused strong-points and AI analysis.

🧾 OUTPUT FORMAT
Return ONLY the final script, exactly {line_count} lines.
Each line must start with "-".
No explanations.
"""
        else:
            # Storyline Hype Only prompt (clean story + suspense, no BTS/music/visuals)
            prompt_text = f"""Generate an Instagram Reel–style movie storyline–only script
that creates hype and curiosity to watch the film.

🎬 Movie: {movie_name}
🌐 Language: {lang_label} (Use pure language; minimal English only if needed)
📺 Channel Name: {channel_name}
🔢 Total Lines: {line_count}

🎤 Tone Style:
{tone_instruction}
Focus ONLY on story, characters, conflict, suspense, and curiosity.
Do NOT mention music, visuals, cinematography, editing, behind-the-scenes,
budget, songs, or technical elements.

✨ STRUCTURE

1. Welcome + Curiosity Hook (first 3–5 lines)
Start with a natural translation of: "{tpl['welcome']}". Insert the channel name in place of {{CHANNEL}}.
Use intrigue examples adapted to {lang_label}:
- {tpl['intrigue1']}
- {tpl['intrigue2']}
- {tpl['intrigue3']}

2. Core Story Setup (next 5–8 lines)
- Introduce the main character and their world.
- Explain their want, fear, or what they protect.
- Introduce the central emotional or dramatic situation.
- Reveal what threatens their life, love, family, or peace.
- Do NOT reveal spoilers.

3. Rising Conflict & Stakes (next 5–10 lines)
- Describe how the situation becomes dangerous or unpredictable.
- Hint at betrayals, conflicts, secrets, or turning points.
- Show the hero’s struggle, doubts, and pressure.
- Build tension that something big is coming.

4. Tease Twists Without Spoiling (3–5 lines)
- Suggest hidden motives, unanswered questions, or mysterious events.
- Hint that not everything is as it appears.
- Build suspense so viewers want to watch the film.

5. Why People Should Watch (3–5 lines)
🧠 AI-Powered Strong-Point Detection:
Analyze the storyline and pick out:
- The strongest conflict or emotional core
- The twist setup or highest-stakes turning point
- The single most compelling reason viewers should watch

🎭 Genre-Based Strength Focus (focus: {genre}):
- Romantic → highlight chemistry and emotional stakes
- Mystery/Thriller/Suspense → highlight twists and hidden truths
- Horror → highlight dread and terrifying moments
- Action-Mass → highlight hero escalation and intense confrontations
- Emotional → highlight moving arcs and memorable payoffs

Write 3–5 urgent, persuasive lines in {lang_label} that make viewers say:
"You must watch this now."

6. Suspense Questions (2–4 lines)
Sample curiosity prompts in {lang_label}:
- {tpl['suspense_q1']}
- {tpl['suspense_q2']}

7. CTA — Story-Based Call To Action (last 3–5 lines)
Translate into {lang_label}:
- {tpl['cta_watch']}
- {tpl['cta_meet']}
- {tpl['cta_follow']}

📝 STYLE RULES
- Write exactly {line_count} lines.
- Each line MUST begin with "-".
- No quotation marks.
- Lines must be 5–10 words.
- Use pure {lang_label} with minimal English.
- Do NOT mention music, visuals, or behind-the-scenes.
- Maintain the chosen tone: {tone}.

🧾 OUTPUT FORMAT
Return ONLY the final script, exactly {line_count} lines,
each starting with "-".
No explanations, no extra text.
"""

        st.subheader("📝 Generated Prompt")
        st.text_area("Copy or edit your prompt here:", prompt_text, height=520)

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
