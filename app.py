import base64
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components
from datetime import datetime

st.set_page_config(
    page_title="Mishthi Jain Portfolio",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Metadata for SEO and social sharing
st.markdown(
    """
    <head>
      <meta name="description" content="Bright portfolio for Mishthi Jain showcasing AI, software engineering, mobile development, and research work." />
      <meta property="og:title" content="Mishthi Jain Portfolio" />
      <meta property="og:description" content="Mishthi Jain is a software engineer and AI developer with full-stack, mobile, and research experience." />
      <meta property="og:image" content="https://images.unsplash.com/photo-1521737604893-d14cc237f11d?auto=format&fit=crop&w=1200&q=80" />
      <meta name="twitter:card" content="summary_large_image" />
    </head>
    """,
    unsafe_allow_html=True,
)

custom_css = '''
<style>
:root {
  color-scheme: light;
  font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
  color: #a67c52;
  background: #fff9d1;
}
html, body, [data-testid='stAppViewContainer'] {
  background: radial-gradient(circle at top left, rgba(254, 249, 195, 0.72), transparent 30%),
              radial-gradient(circle at bottom right, rgba(250, 211, 64, 0.36), transparent 28%),
              #fff9d1;
  color: #a67c52;
  scroll-behavior: smooth;
}
main {
  background: transparent;
}
.block-container {
  padding-left: 3rem;
  padding-right: 3rem;
}
section {
  scroll-margin-top: 98px;
}
.stApp {
  overflow-x: hidden;
}
.navbar {
  position: sticky;
  top: 0;
  z-index: 999;
  backdrop-filter: blur(24px);
  background: rgba(255, 255, 255, 0.14);
  border-bottom: 1px solid rgba(255, 255, 255, 0.24);
  padding: 18px 28px;
  margin: 0 -32px 32px;
}
.navbar a {
  color: #a67c52;
  margin-right: 24px;
  text-decoration: none;
  font-weight: 700;
}
.navbar a:hover {
  color: #a67c52;
}
.hero {
  padding: 80px 0 48px;
  position: relative;
}
.hero h1,
.hero p,
.hero span,
.hero .hero-text {
  color: #a67c52;
}
.hero p {
  max-width: 760px;
  font-size: 1.1rem;
  color: #a67c52;
  margin-bottom: 24px;
}
.glass-card {
  border: 1px solid rgba(255, 255, 255, 0.16);
  background: rgba(255, 255, 255, 0.14);
  border-radius: 28px;
  box-shadow: 0 24px 60px rgba(15, 23, 42, 0.08);
}
.card-grid {
  display: grid;
  gap: 24px;
}
.card-grid-3 { grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); }
.card-grid-2 { grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); }
.card-content {
  padding: 28px;
  color: #a67c52;
}
.card-content h2,
.card-content h3,
.glass-card strong {
  color: #a67c52;
}
.card-content p,
.card-content ul,
.card-content li,
.card-content a {
  color: #a67c52;
}
.card-content a {
  color: #a67c52;
  text-decoration: none;
  font-weight: 700;
}
.card-content a:hover {
  color: #a67c52;
  text-decoration: underline;
}
.card-title {
  font-size: 1.2rem;
  margin-bottom: 10px;
  color: #a67c52;
}
.card-subtitle {
  color: #a67c52;
  margin-bottom: 20px;
}
.timeline {
  position: relative;
  padding-left: 40px;
}
.timeline::before {
  content: '';
  position: absolute;
  left: 12px;
  top: 0;
  bottom: 0;
  width: 3px;
  background: linear-gradient(180deg, #ffffff 0%, #fde047 100%);
  opacity: 0.65;
}
.timeline-item {
  position: relative;
  margin-bottom: 32px;
}
.timeline-item::before {
  content: '';
  position: absolute;
  left: -20px;
  top: 4px;
  width: 14px;
  height: 14px;
  border-radius: 50%;
  background: radial-gradient(circle, #ffffff, #fde047 80%);
  box-shadow: 0 0 18px rgba(251, 191, 36, 0.3);
}
.progress-bar {
  background: rgba(255,255,255,0.16);
  border-radius: 999px;
  height: 12px;
  overflow: hidden;
  margin-top: 12px;
}
.progress-bar-inner {
  height: 100%;
  border-radius: 999px;
  background: linear-gradient(90deg, #ffffff, #fde047);
  transition: width 1.4s ease;
}
.testimonial-card {
  border: 1px solid rgba(255,255,255,0.16);
  background: rgba(255,255,255,0.14);
  border-radius: 24px;
  padding: 28px;
  color: #a67c52;
}
.testimonial-author {
  margin-top: 18px;
  display: flex;
  align-items: center;
  gap: 14px;
}
.testimonial-author img {
  width: 48px;
  border-radius: 50%;
}
.footer {
  padding: 40px 0;
  color: #a67c52;
  text-align: center;
}
@media (max-width: 768px) {
  .navbar { margin: 0 -16px 24px; padding: 18px 16px; }
  .hero { padding: 48px 0 24px; }
}
</style>
'''

st.markdown(custom_css, unsafe_allow_html=True)

profile_image_path = Path(__file__).parent / "profile_picture.jpeg"
if profile_image_path.is_file():
    with open(profile_image_path, "rb") as f:
        profile_image_b64 = base64.b64encode(f.read()).decode()
    profile_image_html = f'<img src="data:image/jpeg;base64,{profile_image_b64}" alt="Profile" style="width:100%; height:100%; object-fit:cover;" />'
else:
    profile_image_html = '<span style="font-size:3rem; color: #a67c52; font-weight:700;">M</span>'

hero_visual = f'''
<div style="position:relative; min-height:360px; padding: 28px; border-radius:32px; overflow:hidden; background: linear-gradient(135deg, #fde047 0%, #fef3c7 48%, #fef9c3 100%); border:1px solid rgba(249, 115, 22, 0.15);">
  <div class="hero-graphic lemon-top"></div>
  <div class="hero-graphic lemon-bottom"></div>
  <div class="hero-graphic lemon-half"></div>
  <div style="position:absolute; inset:0; background: radial-gradient(circle at top left, rgba(255, 255, 255, 0.35), transparent 30%);"></div>
  <div style="position:absolute; inset:0; background: radial-gradient(circle at bottom right, rgba(255, 255, 255, 0.22), transparent 28%);"></div>
  <div style="position:relative; z-index:2; display:flex; flex-direction:column; justify-content:center; height:100%;">
    <div style="display:flex; flex-wrap:wrap; gap:16px; align-items:center; justify-content:center;">
      <div style="width:160px; height:160px; border-radius:32px; background: white; display:flex; align-items:center; justify-content:center; box-shadow: 0 24px 64px rgba(15, 23, 42, 0.12); overflow:hidden; border: 1px solid rgba(251, 191, 36, 0.35);">
        {profile_image_html}
      </div>
    </div>
  </div>
</div>
'''

st.markdown('<div class="navbar"><a href="#hero">Home</a><a href="#about">About</a><a href="#experience">Experience</a><a href="#projects">Projects</a><a href="#education">Education</a><a href="#contact">Contact</a></div>', unsafe_allow_html=True)

with st.container():
    st.markdown('<div id="hero" class="hero"></div>', unsafe_allow_html=True)
    left, right = st.columns([6, 4], gap="large")
    with left:
        st.markdown('<h1 style="color: #a67c52;">Mishthi Jain</h1>', unsafe_allow_html=True)
        st.markdown('<p style="color: #a67c52; margin:0 0 14px;">Software Engineer · AI Developer · Entrepreneur</p>', unsafe_allow_html=True)
        st.markdown('<p style="color: #a67c52; max-width:740px;">Designing bright, production-ready software and AI systems with polished experience, strong infrastructure, and modern launch-ready engineering.</p>', unsafe_allow_html=True)
        st.markdown("<div style='display:flex; gap:14px; flex-wrap:wrap; margin-top:24px;'><span style='padding:14px 20px; border-radius:999px; background:#eff6ff; color: #a67c52; font-weight:600;'>B.Tech CSE</span><span style='padding:14px 20px; border-radius:999px; background:#ecfeff; color: #a67c52; font-weight:600;'>AI & GenAI</span><span style='padding:14px 20px; border-radius:999px; background:#fff7ed; color: #a67c52; font-weight:600;'>Cloud & DevOps</span></div>", unsafe_allow_html=True)
        st.markdown("<div style='display:flex; gap:14px; flex-wrap:wrap; margin-top:24px;'><a href='#experience' style='padding:14px 22px; border-radius:999px; background:#fde047; color: #a67c52; font-weight:700; text-decoration:none;'>View experience</a><a href='#contact' style='padding:14px 22px; border-radius:999px; background:#fbbf24; color: #a67c52; font-weight:700; text-decoration:none;'>Contact</a></div>", unsafe_allow_html=True)
    with right:
        components.html(hero_visual, height=420, scrolling=False)

st.markdown("<div id='about' class='glass-card' style='margin-bottom:32px;'><div class='card-content'><h2>About</h2><p style='color: #a67c52;'>I am a software engineer and AI developer experienced in building modern full-stack platforms, mobile experiences, and AI-driven evaluation systems. I combine technical precision, polished product design, and a keen sense for performance and user experience.</p><p style='margin-top:18px; color: #a67c52;'>Contact: +91-9244314388 · +1 (530) 863-9022 · <a href='mailto:mishthijain2005@gmail.com' style='color: #a67c52;'>mishthijain2005@gmail.com</a></p><p style='color: #a67c52;'>Location: Cupertino, CA · <a href='https://www.linkedin.com/in/mishthijain' style='color: #a67c52;'>linkedin.com/in/mishthijain</a> · <a href='https://github.com/MishthiJain8' style='color: #a67c52;'>github.com/MishthiJain8</a></p></div></div>", unsafe_allow_html=True)

st.markdown("<div id='skills' class='glass-card' style='margin-bottom:32px;'><div class='card-content'><h2>Skills</h2><div class='card-grid card-grid-2' style='margin-top:22px;'>"
            "<div style='background:rgba(255,255,255,0.14); border-radius:24px; padding:26px;'><h3>Core technical skills</h3><p style='color: #a67c52; margin-bottom:16px;'>Python, C++, Java, TypeScript, SQL, React.js, Spring Boot, gRPC, Node.js, PostgreSQL</p>"
            "<ul style='color: #a67c52; margin:0; padding-left:18px; list-style-type: disc;'><li>AI & GenAI: LLM applications, prompt engineering, RAG, evaluation frameworks</li><li>Mobile: React Native, Android, UI design, authentication, REST APIs</li><li>Cloud & DevOps: AWS, CI/CD, Docker, Linux, Git</li><li>Core CS: DS&A, OS, networks, OOP, DBMS</li></ul></div>"
            "<div style='background:rgba(255,255,255,0.14); border-radius:24px; padding:26px;'><h3>Product & design strengths</h3><p style='color: #a67c52; margin-bottom:16px;'>Modern interface design, startup launch experience, observability, and polished data-driven products.</p>"
            "<ul style='color: #a67c52; margin:0; padding-left:18px; list-style-type: disc;'><li>Interactive UI/UX and responsive experiences</li><li>Live AI demos, dashboards, and product storytelling</li><li>Reliable backend architecture and scalable services</li><li>Quality-first deployment workflows and test automation</li></ul></div>"
            "</div></div></div>", unsafe_allow_html=True)

st.markdown("<div id='experience' class='glass-card' style='margin-bottom:32px;'><div class='card-content'><h2>Experience</h2><div style='margin-top:20px;'>"
            "<div style='margin-bottom:20px;'><h3 style='margin-bottom:6px;'>AyLark — Software Developer Intern (Platform & Systems Infrastructure)</h3><p style='color: #a67c52; margin:4px 0 12px;'>Dec 2025 – Mar 2026 · Nagpur, India</p><ul style='color: #a67c52; padding-left:18px;'><li>Developed and optimized backend services using Node.js and PostgreSQL, improving API responsiveness and production-scale workloads.</li><li>Designed CI/CD workflows with automated testing and deployment validation, enhancing release reliability and reducing deployment risks.</li></ul></div>"
            "<div style='margin-bottom:20px;'><h3 style='margin-bottom:6px;'>Palo Alto Networks — AICTE Virtual Internship</h3><p style='color: #a67c52; margin:4px 0 12px;'>Oct 2024 – Dec 2024 · Remote</p><ul style='color: #a67c52; padding-left:18px;'><li>Analyzed network security fundamentals, NGFW, and L4-L7 traffic inspection techniques.</li><li>Modeled enterprise security automation workflows and Zero Trust principles for distributed networks.</li></ul></div>"
            "</div></div></div>", unsafe_allow_html=True)

st.markdown("<div id='projects' class='glass-card' style='margin-bottom:32px;'><div class='card-content'><h2>Projects</h2><div style='margin-top:20px;'>"
            "<div style='margin-bottom:20px;'><h3 style='margin-bottom:6px;'>Discord-Inspired Real-Time Communication Platform</h3><p style='color: #a67c52; margin:4px 0 12px;'>React, TypeScript, Node.js, WebSockets, Redis, PostgreSQL · May 2026</p><ul style='color: #a67c52; padding-left:18px;'><li>Built a scalable communication platform with channels, direct messaging, auth, and live presence.</li><li>Implemented WebSocket architecture with Redis Pub/Sub and PostgreSQL persistence to improve reliability and latency.</li></ul></div>"
            "<div style='margin-bottom:20px;'><h3 style='margin-bottom:6px;'>Agentic Evaluation & Observability Harness</h3><p style='color: #a67c52; margin:4px 0 12px;'>Python, LLM Evaluation, OpenAI APIs, AI Observability · Mar 2026</p><ul style='color: #a67c52; padding-left:18px;'><li>Built an evaluation framework for LLM apps with scoring, hallucination detection, and prompt quality metrics.</li><li>Created observability pipelines to monitor latency, token consumption, and retrieval performance.</li></ul></div>"
            "<div style='margin-bottom:20px;'><h3 style='margin-bottom:6px;'>Distributed Service & RPC Framework</h3><p style='color: #a67c52; margin:4px 0 12px;'>C++, gRPC, Concurrency, Distributed Systems · Jan 2026</p><ul style='color: #a67c52; padding-left:18px;'><li>Engineered a distributed RPC framework using gRPC and thread-safe worker pools for high-throughput request processing.</li><li>Implemented dynamic batching and efficient inter-service communication to improve throughput and utilization.</li></ul></div>"
            "</div></div></div>", unsafe_allow_html=True)

st.markdown(
    """<div id='research' class='glass-card' style='margin-bottom:32px;'><div class='card-content'><h2>Research & Systems Modeling</h2><ul style='color: #a67c52; padding-left:18px; margin-top:18px;'><li><strong>Research Paper (under review):</strong> "Enhancing Deep Learning Classifier Generalization in Data-Scarce through GAN-Based Synthetic Augmentation: A Study on Septoria Detection" submitted to CEECT 2026.</li><li><strong>Journal Submission (under review):</strong> "Soybean Price Forecasting in Maharashtra Using a Machine Learning-Based Approach" submitted to Geoderma Regional (Elsevier).</li></ul></div></div>""",
    unsafe_allow_html=True,
)

st.markdown("<div id='education' class='glass-card' style='margin-bottom:32px;'><div class='card-content'><h2>Education</h2><div class='card-grid card-grid-3' style='margin-top:22px;'>"
            "<div style='background:rgba(255,255,255,0.14); border-radius:24px; padding:24px;'><strong>B.Tech., CSE</strong><p style='color: #a67c52; margin:10px 0 0;'>Shri Ramdeobaba College of Engineering and Management, Nagpur</p><p style='color: #a67c52; margin-top:14px;'>CGPA 8.85 · 2026</p></div>"
            "<div style='background:rgba(255,255,255,0.14); border-radius:24px; padding:24px;'><strong>Senior Secondary</strong><p style='color: #a67c52; margin:10px 0 0;'>Lala Kailashpat Singhania High School, CBSE</p><p style='color: #a67c52; margin-top:14px;'>77% · Feb 2023</p></div>"
            "<div style='background:rgba(255,255,255,0.14); border-radius:24px; padding:24px;'><strong>Secondary</strong><p style='color: #a67c52; margin:10px 0 0;'>Lala Kailashpat Singhania High School, CBSE</p><p style='color: #a67c52; margin-top:14px;'>93% · Aug 2021</p></div>"
            "</div></div></div>", unsafe_allow_html=True)

st.markdown("<div id='achievements' class='glass-card' style='margin-bottom:32px;'><div class='card-content'><h2>Achievements & Leadership</h2><ul style='color: #a67c52; padding-left:18px; margin-top:18px;'><li>Built 25+ software projects across AI, backend systems, distributed platforms, and cloud deployments.</li><li>Solved 250+ problems focusing on graph algorithms, dynamic programming, concurrency, and systems design.</li></ul></div></div>", unsafe_allow_html=True)

st.markdown("<div id='certifications' class='glass-card' style='margin-bottom:32px;'><div class='card-content'><h2>Certifications & Coursework</h2><ul style='color: #a67c52; padding-left:18px; margin-top:18px;'><li><strong>Certifications:</strong> BITS Pilani – Mastering Android App Development; Google – Using Python to Interact with the Operating System; Duke University – Cloud Data Engineering.</li><li><strong>Relevant coursework:</strong> Operating Systems, Software Engineering, Data Structures & Algorithms, Computer Networks, OOP, Distributed Systems, DBMS.</li></ul></div></div>", unsafe_allow_html=True)

st.markdown("<div id='contact' class='glass-card' style='margin-bottom:32px;'><div class='card-content'><h2>Contact</h2><p style='color: #a67c52;'>Let’s discuss AI products, scalable systems, and polished technology launches.</p><div class='card-grid card-grid-2' style='margin-top:24px;'>"
            "<div style='background:rgba(255,255,255,0.14); border-radius:24px; padding:26px;'><h3>Contact details</h3><p style='color: #a67c52;'>Phone: +91-9244314388 · +1 (530) 863-9022</p><p style='color: #a67c52;'>Email: <a href='mailto:mishthijain2005@gmail.com' style='color: #a67c52;'>mishthijain2005@gmail.com</a></p><p style='color: #a67c52;'>LinkedIn: <a href='https://www.linkedin.com/in/mishthijain' style='color: #a67c52;'>linkedin.com/in/mishthijain</a></p><p style='color: #a67c52;'>GitHub: <a href='https://github.com/MishthiJain8' style='color: #a67c52;'>github.com/MishthiJain8</a></p></div>"
            "</div></div></div>", unsafe_allow_html=True)

st.markdown("<div class='footer'><p>Bright portfolio design built with Streamlit for fast deployment, modern storytelling, and polished audience-ready presentation.</p></div>", unsafe_allow_html=True)

components.html(
    """
    <script>
      const links = document.querySelectorAll('.navbar a');
      links.forEach(link => link.addEventListener('click', event => {
        event.preventDefault();
        const target = document.querySelector(link.getAttribute('href'));
        if (target) {
          target.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
      }));
      window.addEventListener('load', () => {
        document.body.style.opacity = 0;
        setTimeout(() => {
          document.body.style.transition = 'opacity 0.8s ease';
          document.body.style.opacity = 1;
        }, 50);
      });
    </script>
    """,
    height=0,
    scrolling=False,
)
