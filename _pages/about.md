---
permalink: /
title: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

<style>
  :root {
    --navy:   #0f1f3d;
    --blue:   #1a3a6b;
    --accent: #2e6fcf;
    --light:  #e8eef7;
    --muted:  #6b7a99;
    --white:  #ffffff;
    --radius: 10px;
  }

  .tai-hero { margin-bottom: 2.5rem; }

  .tai-hero h1 {
    font-size: 2rem;
    font-weight: 800;
    color: var(--navy);
    margin: 0 0 0.75rem;
    line-height: 1.2;
    letter-spacing: -0.5px;
  }

  .tai-hero h1 span { color: var(--accent); }

  .tai-hero p {
    font-size: 1.05rem;
    color: #3a4a6a;
    line-height: 1.75;
    max-width: 680px;
    margin: 0 0 1.5rem;
  }

  .tai-cta { display: flex; gap: 0.75rem; flex-wrap: wrap; margin-bottom: 2.5rem; }

  .tai-btn {
    display: inline-block;
    padding: 0.55rem 1.3rem;
    border-radius: 6px;
    font-size: 0.9rem;
    font-weight: 600;
    text-decoration: none !important;
    transition: all 0.18s ease;
  }

  .tai-btn-primary { background: var(--accent); color: var(--white) !important; border: 2px solid var(--accent); }
  .tai-btn-primary:hover { background: var(--blue); border-color: var(--blue); }
  .tai-btn-outline { background: transparent; color: var(--accent) !important; border: 2px solid var(--accent); }
  .tai-btn-outline:hover { background: var(--light); }

  .tai-section-title {
    font-size: 0.72rem;
    font-weight: 700;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: var(--muted);
    margin: 0 0 1rem;
  }

  .tai-topics { margin-bottom: 2.5rem; }
  .tai-tags { display: flex; flex-wrap: wrap; gap: 0.5rem; }

  .tai-tag {
    background: var(--light);
    color: var(--blue);
    padding: 0.35rem 0.9rem;
    border-radius: 999px;
    font-size: 0.85rem;
    font-weight: 500;
    border: 1.5px solid #c8d6ee;
  }

  .tai-highlights {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 1.25rem;
    margin-bottom: 2.5rem;
  }

  @media (max-width: 640px) {
    .tai-highlights { grid-template-columns: 1fr; }
  }

  .tai-panel {
    background: var(--white);
    border: 1.5px solid #dde5f0;
    border-radius: var(--radius);
    padding: 1.25rem 1.4rem;
    display: flex;
    flex-direction: column;
  }

  .tai-panel-header {
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    margin-bottom: 1rem;
  }

  .tai-panel-header a {
    font-size: 0.8rem;
    color: var(--accent);
    font-weight: 600;
    text-decoration: none;
  }

  .tai-panel-header a:hover { text-decoration: underline; }

  .tai-item-meta {
    font-size: 0.75rem;
    color: var(--muted);
    font-weight: 600;
    letter-spacing: 0.05em;
    margin-bottom: 0.35rem;
  }

  .tai-item-title {
    font-size: 0.95rem;
    font-weight: 700;
    color: var(--navy);
    margin: 0 0 0.5rem;
    line-height: 1.4;
  }

  .tai-item-authors {
    font-size: 0.82rem;
    color: var(--muted);
    margin: 0 0 0.5rem;
    line-height: 1.4;
  }

  .tai-item-abstract {
    font-size: 0.83rem;
    color: #4a5a7a;
    line-height: 1.55;
    margin: 0 0 1rem;
    display: -webkit-box;
    -webkit-line-clamp: 4;
    -webkit-box-orient: vertical;
    overflow: hidden;
  }

  .tai-item-link {
    font-size: 0.82rem;
    color: var(--accent);
    font-weight: 600;
    text-decoration: none;
    margin-top: auto;
  }

  .tai-item-link:hover { text-decoration: underline; }

  .tai-divider { border: none; border-top: 1.5px solid #e0e8f4; margin: 0 0 2rem; }

  .tai-collab {
    background: var(--light);
    border-radius: var(--radius);
    padding: 1.25rem 1.5rem;
    display: flex;
    align-items: center;
    justify-content: space-between;
    flex-wrap: wrap;
    gap: 1rem;
    margin-bottom: 1rem;
  }

  .tai-collab p { margin: 0; font-size: 0.95rem; color: var(--navy); font-weight: 500; }
</style>

<!-- ── HERO ── -->
<div class="tai-hero">
  <h1>Trustworthy AI Lab<br><span>Hamburg</span></h1>
  <p>
    We are a research group at the <strong>University of Hamburg</strong> led by
    <a href="https://anne-lauscher.de/">Anne Lauscher</a>, working at the
    intersection of artificial intelligence, natural language processing, and
    human-centered computing. Our mission is to build AI systems that are
    reliable, culturally aware, and aligned with human values.
  </p>
  <div class="tai-cta">
    <a href="/publications/" class="tai-btn tai-btn-primary">Our Publications</a>
    <a href="/team/" class="tai-btn tai-btn-outline">Meet the Team</a>
    <a href="/join/" class="tai-btn tai-btn-outline">Join Us</a>
    <a href="/studie/" class="tai-btn tai-btn-outline">Student Projects</a>
  </div>
</div>

<!-- ── RESEARCH AREAS ── -->
<div class="tai-topics">
  <p class="tai-section-title">Research Areas</p>
  <div class="tai-tags">
    <span class="tai-tag">Trustworthy AI</span>
    <span class="tai-tag">Natural Language Processing</span>
    <span class="tai-tag">Fairness & Bias</span>
    <span class="tai-tag">Multilingual NLP</span>
    <span class="tai-tag">Human-Centered AI</span>
    <span class="tai-tag">Cultural Awareness</span>
    <span class="tai-tag">Gender-Inclusive Language</span>
    <span class="tai-tag">Large Language Models</span>
  </div>
</div>

<hr class="tai-divider">

<!-- ── LATEST PUBLICATION + NEWS ── -->
<div class="tai-highlights">

  <!-- Latest Publication — auto-pulled from _data/publications.yml -->
  <div class="tai-panel">
    <div class="tai-panel-header">
      <span class="tai-section-title" style="margin:0">Latest Publication</span>
      <a href="/publications/">All publications →</a>
    </div>

    {% assign latest_pub = site.data.publications | first %}
    {% if latest_pub %}
      <div class="tai-item-meta">
        {{ latest_pub.date }}{% if latest_pub.venue %} · {{ latest_pub.venue }}{% endif %}
      </div>
      <div class="tai-item-title">{{ latest_pub.title }}</div>
      {% if latest_pub.authors %}
        <div class="tai-item-authors">{{ latest_pub.authors }}</div>
      {% endif %}
      {% if latest_pub.abstract %}
        <div class="tai-item-abstract">{{ latest_pub.abstract }}</div>
      {% endif %}
      {% if latest_pub.pdf %}
        <a class="tai-item-link" href="{{ latest_pub.pdf }}" target="_blank">Read paper →</a>
      {% else %}
        <a class="tai-item-link" href="/publications/">View all publications →</a>
      {% endif %}
    {% else %}
      <p style="color:var(--muted);font-size:0.9rem">No publications found.</p>
    {% endif %}
  </div>

  <!-- Latest News — auto-pulled from _posts/ -->
  <div class="tai-panel">
    <div class="tai-panel-header">
      <span class="tai-section-title" style="margin:0">Latest News</span>
      <a href="/news/">All news →</a>
    </div>

  {% for post in site.data.news limit:2 %}
    <div class="tai-item-meta">{{ post.date | date: "%B %d, %Y" }}</div>
    <div class="tai-item-title">{{ post.text }}</div>
  {% else %}
    <p style="color:var(--muted);font-size:0.9rem">No news posts yet.</p>
  {% endfor %}
  </div>





</div>

<hr class="tai-divider">

