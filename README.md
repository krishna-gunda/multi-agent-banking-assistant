<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>README — Multi Assistant RAG System</title>
<link rel="preconnect" href="https://fonts.googleapis.com"/>
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600&family=Inter:wght@300;400;500;600;700&family=Playfair+Display:wght@700&display=swap" rel="stylesheet"/>
<style>
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
:root{
  --bg:#0d1117;--surface:#161b22;--surface2:#21262d;--border:#30363d;
  --gold:#f0b429;--gold-dim:#7d5f0e;--blue:#58a6ff;--green:#3fb950;
  --purple:#bc8cff;--red:#ff7b72;--cyan:#39d353;
  --text:#e6edf3;--muted:#8b949e;--radius:10px;
  --mono:'JetBrains Mono',monospace;--sans:'Inter',sans-serif;
}
html{scroll-behavior:smooth}
body{font-family:var(--sans);background:var(--bg);color:var(--text);line-height:1.7;font-size:15px}

/* ── HERO ── */
.hero{
  background:linear-gradient(135deg,#0d1117 0%,#161b22 40%,#0d1117 100%);
  border-bottom:1px solid var(--border);
  padding:72px 40px 60px;
  text-align:center;
  position:relative;
  overflow:hidden;
}
.hero::before{
  content:'';position:absolute;inset:0;
  background:radial-gradient(ellipse 80% 60% at 50% 0%,rgba(240,180,41,0.08),transparent 70%);
  pointer-events:none;
}
.hero-badge{
  display:inline-flex;align-items:center;gap:8px;
  background:rgba(240,180,41,0.1);border:1px solid rgba(240,180,41,0.3);
  border-radius:40px;padding:6px 18px;
  font-size:0.72rem;font-weight:600;letter-spacing:.12em;text-transform:uppercase;
  color:var(--gold);margin-bottom:28px;
}
.hero-badge .dot{width:6px;height:6px;border-radius:50%;background:var(--gold)}
.hero h1{
  font-family:'Playfair Display',Georgia,serif;
  font-size:clamp(2.2rem,4.5vw,3.4rem);font-weight:700;
  background:linear-gradient(135deg,#f0b429,#e6edf3 55%,#58a6ff);
  -webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;
  line-height:1.18;letter-spacing:-0.02em;margin-bottom:16px;
}
.hero-sub{font-size:1rem;color:var(--muted);max-width:560px;margin:0 auto 32px;font-weight:300}
.badges{display:flex;justify-content:center;gap:10px;flex-wrap:wrap}
.badge{
  display:inline-block;
  padding:5px 14px;border-radius:40px;font-size:0.72rem;font-weight:600;
  letter-spacing:.08em;border:1px solid;
}
.badge.py{background:rgba(88,166,255,.08);border-color:rgba(88,166,255,.3);color:var(--blue)}
.badge.rag{background:rgba(188,140,255,.08);border-color:rgba(188,140,255,.3);color:var(--purple)}
.badge.flask{background:rgba(63,185,80,.08);border-color:rgba(63,185,80,.3);color:var(--green)}
.badge.groq{background:rgba(240,180,41,.08);border-color:rgba(240,180,41,.3);color:var(--gold)}
.badge.star{background:rgba(255,123,114,.08);border-color:rgba(255,123,114,.3);color:var(--red)}

/* ── LAYOUT ── */
.page{max-width:960px;margin:0 auto;padding:0 24px 80px}

/* ── SECTION TITLES ── */
.sec{margin-top:60px}
.sec-label{
  display:flex;align-items:center;gap:12px;
  font-size:0.68rem;font-weight:700;letter-spacing:.16em;text-transform:uppercase;
  color:var(--gold);margin-bottom:12px;
}
.sec-label::after{content:'';flex:1;height:1px;background:linear-gradient(90deg,var(--gold-dim),transparent)}
.sec h2{
  font-family:'Playfair Display',serif;
  font-size:1.8rem;font-weight:700;color:var(--text);
  margin-bottom:20px;letter-spacing:-0.02em;
}
p{color:var(--muted);margin-bottom:12px}
p strong{color:var(--text)}

/* ── PROBLEM CARDS ── */
.cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:16px;margin-top:24px}
.card{
  background:var(--surface);border:1px solid var(--border);border-radius:var(--radius);
  padding:24px;position:relative;overflow:hidden;transition:border-color .2s,transform .2s;
}
.card:hover{border-color:var(--gold-dim);transform:translateY(-2px)}
.card::before{
  content:'';position:absolute;top:0;left:0;right:0;height:3px;
  background:linear-gradient(90deg,var(--card-color,var(--gold)),transparent);
}
.card-icon{font-size:1.8rem;margin-bottom:12px}
.card h3{font-size:.9rem;font-weight:600;color:var(--text);margin-bottom:6px}
.card p{font-size:.82rem;color:var(--muted);margin:0}

/* ── STAR METHOD ── */
.star-grid{display:grid;grid-template-columns:1fr 1fr;gap:0;margin-top:24px;border:1px solid var(--border);border-radius:var(--radius);overflow:hidden}
.star-item{padding:28px;border-right:1px solid var(--border);border-bottom:1px solid var(--border);position:relative}
.star-item:nth-child(even){border-right:none}
.star-item:nth-child(3),.star-item:nth-child(4){border-bottom:none}
.star-letter{
  font-family:var(--mono);font-size:3rem;font-weight:700;
  line-height:1;margin-bottom:8px;
  background:linear-gradient(135deg,var(--s-color,var(--gold)),transparent 160%);
  -webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;
}
.star-word{font-size:0.7rem;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--muted);margin-bottom:10px}
.star-item h3{font-size:.95rem;font-weight:600;color:var(--text);margin-bottom:8px}
.star-item p{font-size:.83rem;color:var(--muted);margin:0}

/* ── FLOW DIAGRAM ── */
.flow{
  display:flex;align-items:center;gap:0;
  background:var(--surface);border:1px solid var(--border);border-radius:var(--radius);
  overflow:hidden;margin-top:24px;flex-wrap:wrap;
}
.flow-step{
  flex:1;min-width:130px;
  padding:20px 16px;text-align:center;
  border-right:1px solid var(--border);
  position:relative;
}
.flow-step:last-child{border-right:none}
.flow-icon{font-size:1.6rem;margin-bottom:8px}
.flow-num{
  position:absolute;top:10px;left:12px;
  font-family:var(--mono);font-size:.62rem;font-weight:600;
  color:var(--muted);
}
.flow-step h4{font-size:.78rem;font-weight:600;color:var(--text);margin-bottom:4px}
.flow-step p{font-size:.7rem;color:var(--muted);margin:0}
.flow-arrow{
  font-size:1.1rem;color:var(--gold);padding:0 2px;
  align-self:center;flex-shrink:0;
}

/* ── CODE BLOCK ── */
.code-wrap{
  background:#010409;border:1px solid var(--border);border-radius:var(--radius);
  overflow:hidden;margin:16px 0;
}
.code-header{
  display:flex;align-items:center;justify-content:space-between;
  padding:10px 16px;background:var(--surface);border-bottom:1px solid var(--border);
}
.code-title{font-family:var(--mono);font-size:.72rem;color:var(--muted)}
.code-dots{display:flex;gap:6px}
.code-dot{width:10px;height:10px;border-radius:50%}
.cd1{background:#ff5f57}.cd2{background:#febc2e}.cd3{background:#28c840}
pre{padding:20px;overflow-x:auto;font-family:var(--mono);font-size:.8rem;line-height:1.7}
.kw{color:#ff7b72}.cm{color:#8b949e;font-style:italic}.st{color:#a5d6ff}
.fn{color:#d2a8ff}.ky{color:#79c0ff}.va{color:#ffa657}.ok{color:#3fb950}
.pn{color:#e6edf3}

/* ── FOLDER TREE ── */
.tree{
  background:#010409;border:1px solid var(--border);border-radius:var(--radius);
  padding:20px 24px;font-family:var(--mono);font-size:.82rem;line-height:2;
  margin:16px 0;
}
.tree .dir{color:var(--blue)}
.tree .file{color:var(--text)}
.tree .comm{color:var(--muted)}
.tree .highlight{color:var(--gold)}

/* ── STEPS ── */
.steps{margin:24px 0;display:flex;flex-direction:column;gap:0}
.step{
  display:flex;gap:20px;padding:20px 0;
  border-bottom:1px solid var(--border);
}
.step:last-child{border-bottom:none}
.step-num{
  width:36px;height:36px;min-width:36px;
  border-radius:50%;border:2px solid var(--gold);
  display:flex;align-items:center;justify-content:center;
  font-family:var(--mono);font-size:.78rem;font-weight:700;color:var(--gold);
  flex-shrink:0;margin-top:2px;
}
.step-body h4{font-size:.9rem;font-weight:600;color:var(--text);margin-bottom:6px}
.step-body p{font-size:.83rem;color:var(--muted);margin:0}

/* ── FEATURE TABLE ── */
.feat-table{width:100%;border-collapse:collapse;margin-top:20px;font-size:.84rem}
.feat-table th{
  text-align:left;padding:12px 16px;
  background:var(--surface);border:1px solid var(--border);
  font-size:.7rem;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--muted);
}
.feat-table td{padding:12px 16px;border:1px solid var(--border);color:var(--muted)}
.feat-table td:first-child{color:var(--text);font-weight:500}
.feat-table tr:hover td{background:var(--surface)}
.tick{color:var(--green);font-weight:700}

/* ── QUOTE BLOCK ── */
.quote{
  border-left:3px solid var(--gold);
  background:rgba(240,180,41,.05);
  padding:16px 20px;border-radius:0 var(--radius) var(--radius) 0;
  margin:20px 0;font-style:italic;color:var(--text);font-size:.92rem;
}

/* ── FOOTER ── */
footer{
  border-top:1px solid var(--border);padding:32px 24px;
  text-align:center;color:var(--muted);font-size:.75rem;
  max-width:960px;margin:0 auto;
}
footer a{color:var(--blue);text-decoration:none}

/* ── RESPONSIVE ── */
@media(max-width:640px){
  .hero{padding:48px 24px 40px}
  .star-grid{grid-template-columns:1fr}
  .star-item{border-right:none}
  .star-item:nth-child(3){border-bottom:1px solid var(--border)}
  .flow{flex-direction:column}
  .flow-step{border-right:none;border-bottom:1px solid var(--border)}
  .flow-step:last-child{border-bottom:none}
  .flow-arrow{transform:rotate(90deg);padding:8px 0}
}
</style>
</head>
<body>

<!-- ══ HERO ══════════════════════════════════════════ -->
<div class="hero">
  <div class="hero-badge"><span class="dot"></span>Open Source · RAG · Generative AI</div>
  <h1>Multi Assistant<br/>RAG System</h1>
  <p class="hero-sub">
    A department-aware Retrieval-Augmented Generation chatbot for <strong>Future Trust Bank</strong> —
    giving every department its own AI knowledge agent.
  </p>
  <div class="badges">
    <span class="badge py">Python 3.12</span>
    <span class="badge rag">LangChain + ChromaDB</span>
    <span class="badge flask">Flask API</span>
    <span class="badge groq">Groq · LLaMA 3.3 70B</span>
    <span class="badge star">STAR Method Explained</span>
  </div>
</div>

<div class="page">

<!-- ══ WHY I BUILT THIS ═══════════════════════════════ -->
<div class="sec">
  <div class="sec-label">Origin Story</div>
  <h2>Why I Built This</h2>
  <p>
    Working in a banking context, I noticed a recurring pain: staff and customers had to navigate
    dozens of dense policy documents to find simple answers. A customer asking <em>"what documents do
    I need to open a savings account?"</em> might wait 10–15 minutes for a human agent to locate the
    right section in a 40-page PDF.
  </p>
  <p>
    I built this system to <strong>put every department's knowledge base directly into a
    conversational AI</strong> — no hallucinations, no generic answers. Every response is grounded
    in the bank's own documents. Each department gets its own isolated vector store so queries never
    cross-contaminate between, say, fraud detection policy and loan eligibility rules.
  </p>

  <div class="quote">
    "The right answer should arrive in seconds, sourced from the right document — not after a
    chain of email forwards or hold music."
  </div>
</div>

<!-- ══ PROBLEMS IT SOLVES ════════════════════════════ -->
<div class="sec">
  <div class="sec-label">Problem Space</div>
  <h2>Problems This Solves</h2>
  <div class="cards">
    <div class="card" style="--card-color:#ff7b72">
      <div class="card-icon">⏱️</div>
      <h3>Slow Document Retrieval</h3>
      <p>Agents spent 10–20 minutes searching PDFs and policy docs. This system answers in under 3 seconds.</p>
    </div>
    <div class="card" style="--card-color:#58a6ff">
      <div class="card-icon">🏗️</div>
      <h3>Knowledge Silos</h3>
      <p>Fraud team didn't know loan eligibility rules. Each department now has its own AI that only knows its domain.</p>
    </div>
    <div class="card" style="--card-color:#3fb950">
      <div class="card-icon">🤖</div>
      <h3>Generic LLM Hallucinations</h3>
      <p>Vanilla ChatGPT invents banking rules. RAG grounds every answer in the bank's actual documentation.</p>
    </div>
    <div class="card" style="--card-color:#bc8cff">
      <div class="card-icon">📞</div>
      <h3>High Call-Centre Load</h3>
      <p>Routine questions — interest rates, required documents, fraud report steps — can now be self-served 24/7.</p>
    </div>
    <div class="card" style="--card-color:#f0b429">
      <div class="card-icon">🔐</div>
      <h3>Compliance Risk</h3>
      <p>Off-policy answers from general LLMs create compliance liability. Grounded RAG answers stay within approved content.</p>
    </div>
    <div class="card" style="--card-color:#39d353">
      <div class="card-icon">🌍</div>
      <h3>Multilingual Barriers</h3>
      <p>Uses <code>multilingual-e5-base</code> embeddings — works across languages without retranslating documents.</p>
    </div>
  </div>
</div>

<!-- ══ STAR METHOD ════════════════════════════════════ -->
<div class="sec">
  <div class="sec-label">Project Narrative</div>
  <h2>The STAR Method — Full Breakdown</h2>
  <p>Here is the entire project explained through the STAR framework used in engineering case studies and interviews.</p>
  <div class="star-grid">
    <div class="star-item">
      <div class="star-letter" style="--s-color:#ff7b72">S</div>
      <div class="star-word">Situation</div>
      <h3>A Bank Drowning in Documents</h3>
      <p>Future Trust Bank manages 7 departments, each with large internal knowledge bases — onboarding guides, fraud manuals, loan rulebooks, insurance policies. Staff wasted hours per week searching these documents. Customers on calls waited on hold while agents hunted for answers. There was no unified, intelligent way to query this institutional knowledge.</p>
    </div>
    <div class="star-item">
      <div class="star-letter" style="--s-color:#f0b429">T</div>
      <div class="star-word">Task</div>
      <h3>Build a Grounded, Department-Aware AI Agent</h3>
      <p>Design and deploy a system where any user can select a department, ask a natural-language question, and get an accurate answer sourced directly from that department's documentation — with no hallucinations, no cross-department confusion, and no external API dependency for the knowledge base itself.</p>
    </div>
    <div class="star-item">
      <div class="star-letter" style="--s-color:#58a6ff">A</div>
      <div class="star-word">Action</div>
      <h3>RAG Pipeline + Flask + Animated Frontend</h3>
      <p>Processed all 7 department DOCX files using LangChain document loaders and chunked them into embeddings using <code>intfloat/multilingual-e5-base</code>. Stored each department's vectors in a separate ChromaDB instance. Built a Flask API with department routing. Integrated Groq's LLaMA 3.3 70B for sub-second inference. Created a dark-gold animated frontend with department selection, streaming chat, and typing indicators.</p>
    </div>
    <div class="star-item">
      <div class="star-letter" style="--s-color:#3fb950">R</div>
      <div class="star-word">Result</div>
      <h3>Accurate, Instant, Compliant Answers</h3>
      <p>Answers are returned in under 3 seconds, drawn exclusively from approved documentation. Each department operates in full isolation — a fraud query never pulls from loan documents. The multilingual embedding model supports diverse user bases. The system is fully extensible: adding a new department requires only a new DOCX file and one embeddings run.</p>
    </div>
  </div>
</div>

<!-- ══ HOW RAG WORKS ═════════════════════════════════ -->
<div class="sec">
  <div class="sec-label">Architecture</div>
  <h2>How RAG Works in This System</h2>
  <p>
    RAG — <strong>Retrieval-Augmented Generation</strong> — is a technique that combines a vector
    database search with a language model. Instead of asking the LLM to recall facts from training,
    we <em>retrieve</em> the relevant document chunks first, then ask the LLM to <em>reason</em>
    over those chunks. This eliminates hallucinations.
  </p>
  <div class="flow">
    <div class="flow-step">
      <div class="flow-num">01</div>
      <div class="flow-icon">📄</div>
      <h4>Ingest DOCX</h4>
      <p>Department document loaded and split into chunks</p>
    </div>
    <div class="flow-arrow">→</div>
    <div class="flow-step">
      <div class="flow-num">02</div>
      <div class="flow-icon">🔢</div>
      <h4>Embed</h4>
      <p>Each chunk converted to a vector via multilingual-e5-base</p>
    </div>
    <div class="flow-arrow">→</div>
    <div class="flow-step">
      <div class="flow-num">03</div>
      <div class="flow-icon">🗄️</div>
      <h4>Store</h4>
      <p>Vectors persisted in ChromaDB per department</p>
    </div>
    <div class="flow-arrow">→</div>
    <div class="flow-step">
      <div class="flow-num">04</div>
      <div class="flow-icon">🔍</div>
      <h4>Retrieve</h4>
      <p>User query embedded → top-5 similar chunks fetched</p>
    </div>
    <div class="flow-arrow">→</div>
    <div class="flow-step">
      <div class="flow-num">05</div>
      <div class="flow-icon">🧠</div>
      <h4>Generate</h4>
      <p>LLaMA 3.3 70B answers using only retrieved context</p>
    </div>
  </div>
</div>

<!-- ══ FOLDER STRUCTURE ═══════════════════════════════ -->
<div class="sec">
  <div class="sec-label">Project Layout</div>
  <h2>Folder Structure</h2>
  <div class="code-wrap">
    <div class="code-header">
      <div class="code-dots"><div class="code-dot cd1"></div><div class="code-dot cd2"></div><div class="code-dot cd3"></div></div>
      <div class="code-title">Multi Assistant Rag system/</div>
    </div>
    <div class="tree">
<span class="dir">Multi Assistant Rag system/</span>
├── <span class="dir">data/</span>                        <span class="comm"># Raw .docx knowledge files</span>
│   ├── <span class="file">Account_Opening_Department_Knowledge_Base.docx</span>
│   ├── <span class="file">Credit_Card_Department_KnowledgeBase.docx</span>
│   ├── <span class="file">CustomerServiceDepartment_KnowledgeBase.docx</span>
│   ├── <span class="file">FraudDetection_KnowledgeBase.docx</span>
│   ├── <span class="file">Insurance_Knowledge_Base.docx</span>
│   ├── <span class="file">Loans_Knowledge_Base.docx</span>
│   └── <span class="file">Reception_Department_Knowledge_Base.docx</span>
│
├── <span class="dir">DB/</span>                          <span class="comm"># ChromaDB vector stores (auto-created)</span>
│   ├── <span class="dir">Account_Opening_Department_Knowledge_Base.docx Database/</span>
│   ├── <span class="dir">Credit_Card_Department_KnowledgeBase.docx Database/</span>
│   └── <span class="comm">...one folder per department...</span>
│
├── <span class="dir">templates/</span>
│   └── <span class="highlight">index.html</span>               <span class="comm"># Animated Flask frontend</span>
│
├── <span class="dir">venv/</span>                        <span class="comm"># Virtual environment (not committed)</span>
├── <span class="highlight">app.py</span>                       <span class="comm"># Flask API — routes & RAG orchestration</span>
├── <span class="highlight">main.py</span>                      <span class="comm"># CLI version of the RAG chat loop</span>
├── <span class="file">embeddings.py</span>               <span class="comm"># Script to build ChromaDB from DOCX files</span>
├── <span class="file">.env</span>                         <span class="comm"># GROQ_API_KEY (never commit this)</span>
└── <span class="file">requirements.txt</span>            <span class="comm"># All dependencies</span>
    </div>
  </div>
</div>

<!-- ══ SETUP ══════════════════════════════════════════ -->
<div class="sec">
  <div class="sec-label">Getting Started</div>
  <h2>Clone &amp; Run in 5 Steps</h2>
  <div class="steps">
    <div class="step">
      <div class="step-num">1</div>
      <div class="step-body">
        <h4>Clone the repository</h4>
        <div class="code-wrap">
          <div class="code-header">
            <div class="code-dots"><div class="code-dot cd1"></div><div class="code-dot cd2"></div><div class="code-dot cd3"></div></div>
            <div class="code-title">bash</div>
          </div>
          <pre><span class="ok">$</span> <span class="fn">git</span> clone https://github.com/gundakrishna338/multi-assistant-rag-system.git
<span class="ok">$</span> <span class="fn">cd</span> multi-assistant-rag-system</pre>
        </div>
      </div>
    </div>
    <div class="step">
      <div class="step-num">2</div>
      <div class="step-body">
        <h4>Create a virtual environment and install dependencies</h4>
        <div class="code-wrap">
          <div class="code-header">
            <div class="code-dots"><div class="code-dot cd1"></div><div class="code-dot cd2"></div><div class="code-dot cd3"></div></div>
            <div class="code-title">bash</div>
          </div>
          <pre><span class="ok">$</span> <span class="fn">python</span> -m venv venv
<span class="ok">$</span> venv\Scripts\activate          <span class="cm"># Windows PowerShell</span>
<span class="ok">$</span> source venv/bin/activate       <span class="cm"># macOS / Linux</span>
<span class="ok">$</span> <span class="fn">pip</span> install -r requirements.txt</pre>
        </div>
      </div>
    </div>
    <div class="step">
      <div class="step-num">3</div>
      <div class="step-body">
        <h4>Add your Groq API key</h4>
        <p>Create a <code>.env</code> file in the project root:</p>
        <div class="code-wrap">
          <div class="code-header">
            <div class="code-dots"><div class="code-dot cd1"></div><div class="code-dot cd2"></div><div class="code-dot cd3"></div></div>
            <div class="code-title">.env</div>
          </div>
          <pre><span class="va">GROQ_API_KEY</span>=<span class="st">your_groq_api_key_here</span></pre>
        </div>
        <p>Get a free key at <strong>console.groq.com</strong> — it's free with generous rate limits.</p>
      </div>
    </div>
    <div class="step">
      <div class="step-num">4</div>
      <div class="step-body">
        <h4>Build the vector databases from your DOCX files</h4>
        <div class="code-wrap">
          <div class="code-header">
            <div class="code-dots"><div class="code-dot cd1"></div><div class="code-dot cd2"></div><div class="code-dot cd3"></div></div>
            <div class="code-title">bash</div>
          </div>
          <pre><span class="ok">$</span> <span class="fn">python</span> embeddings.py

<span class="cm"># This reads every .docx in /data, chunks the text,</span>
<span class="cm"># embeds with multilingual-e5-base, and writes</span>
<span class="cm"># one ChromaDB folder per department into /DB.</span>
<span class="cm"># Run this once. Only re-run when documents change.</span></pre>
        </div>
      </div>
    </div>
    <div class="step">
      <div class="step-num">5</div>
      <div class="step-body">
        <h4>Launch the web app</h4>
        <div class="code-wrap">
          <div class="code-header">
            <div class="code-dots"><div class="code-dot cd1"></div><div class="code-dot cd2"></div><div class="code-dot cd3"></div></div>
            <div class="code-title">bash</div>
          </div>
          <pre><span class="ok">$</span> <span class="fn">python</span> app.py

<span class="cm"># ✅  Running on http://127.0.0.1:5000</span>
<span class="cm"># Open your browser — select a department — ask questions.</span></pre>
        </div>
        <p>Or run the original CLI version: <code>python main.py</code></p>
      </div>
    </div>
  </div>
</div>

<!-- ══ TECH STACK ═════════════════════════════════════ -->
<div class="sec">
  <div class="sec-label">Tech Stack</div>
  <h2>What's Under the Hood</h2>
  <table class="feat-table">
    <thead>
      <tr>
        <th>Layer</th><th>Technology</th><th>Role</th><th>Why This Choice</th>
      </tr>
    </thead>
    <tbody>
      <tr><td>LLM Inference</td><td>Groq · LLaMA 3.3 70B</td><td>Answer generation</td><td>Sub-second inference on a free API tier</td></tr>
      <tr><td>Embeddings</td><td>intfloat/multilingual-e5-base</td><td>Text → vectors</td><td>Multilingual, strong retrieval accuracy</td></tr>
      <tr><td>Vector Store</td><td>ChromaDB (persistent)</td><td>Similarity search</td><td>Local, no cloud dependency, per-dept isolation</td></tr>
      <tr><td>LLM Orchestration</td><td>LangChain</td><td>Chunking + retrieval</td><td>Abstracts document loaders and retrieval chains</td></tr>
      <tr><td>Backend API</td><td>Flask</td><td>HTTP routing</td><td>Lightweight, minimal overhead</td></tr>
      <tr><td>Frontend</td><td>HTML / CSS / Vanilla JS</td><td>Chat UI</td><td>Zero build tooling, instant load</td></tr>
      <tr><td>Config</td><td>python-dotenv</td><td>Secrets management</td><td>Keeps API keys out of source code</td></tr>
    </tbody>
  </table>
</div>

<!-- ══ FUTURE IDEAS ═══════════════════════════════════ -->
<div class="sec">
  <div class="sec-label">Roadmap</div>
  <h2>What Could Come Next</h2>
  <div class="cards">
    <div class="card" style="--card-color:#bc8cff">
      <div class="card-icon">💬</div>
      <h3>Conversation Memory</h3>
      <p>Add multi-turn memory so users can reference previous questions in the same session.</p>
    </div>
    <div class="card" style="--card-color:#58a6ff">
      <div class="card-icon">🔐</div>
      <h3>Auth + Role-Based Access</h3>
      <p>Restrict departments by user role — a teller should not query fraud investigation docs.</p>
    </div>
    <div class="card" style="--card-color:#3fb950">
      <div class="card-icon">📊</div>
      <h3>Query Analytics Dashboard</h3>
      <p>Track which questions are asked most per department to surface knowledge gaps.</p>
    </div>
    <div class="card" style="--card-color:#f0b429">
      <div class="card-icon">🗂️</div>
      <h3>PostgreSQL Backend</h3>
      <p>Move from SQLite/local storage to PostgreSQL for production-grade persistence and logging.</p>
    </div>
  </div>
</div>

<!-- ══ ABOUT ══════════════════════════════════════════ -->
<div class="sec">
  <div class="sec-label">Built By</div>
  <h2>About the Developer</h2>
  <div class="card" style="--card-color:#f0b429;max-width:500px">
    <div class="card-icon">👨‍💻</div>
    <h3>Krishna Gunda</h3>
    <p>
      Final-year B.Tech CSE (AI/ML) student at JNTUH, Hyderabad. Specialising in
      RAG systems, deployed ML APIs, and production AI agents.<br/><br/>
      <strong>GitHub & LinkedIn:</strong> gundakrishna338
    </p>
  </div>
</div>

</div><!-- /page -->

<footer>
  <p>Built with ❤️ and LangChain · <a href="https://github.com/gundakrishna338">github.com/gundakrishna338</a> · MIT License</p>
</footer>

</body>
</html>
