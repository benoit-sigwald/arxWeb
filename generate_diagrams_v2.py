"""
Generate high-resolution, ultra-detailed technical architecture diagrams
matching the executive white/navy/gold luxury aesthetic of arx-consulting.com.
"""

import os
from PIL import Image
from playwright.sync_api import sync_playwright

ASSETS_DIR = r"G:\My Drive\Arx Capital\web\arxWeb\assets"

CSS_LIGHT = """
* { margin: 0; padding: 0; box-sizing: border-box; }
body {
    background: #ffffff;
    color: #14202e;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Inter", sans-serif;
    -webkit-font-smoothing: antialiased;
    overflow: hidden;
}
.canvas {
    width: 100%;
    height: 100%;
    padding: 32px 36px;
    background: #ffffff;
    background-image: radial-gradient(circle at 1px 1px, rgba(27, 53, 77, 0.05) 1px, transparent 0);
    background-size: 24px 24px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}
.header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 2px solid #1b354d;
    padding-bottom: 14px;
    margin-bottom: 16px;
}
.title-group h1 {
    font-family: "Playfair Display", Georgia, serif;
    font-size: 24px;
    font-weight: 700;
    color: #1b354d;
    letter-spacing: -0.01em;
    display: flex;
    align-items: center;
    gap: 10px;
}
.title-group p {
    font-size: 12px;
    color: #5b6472;
    margin-top: 3px;
    font-weight: 500;
}
.badge-gold {
    background: #f4ede0;
    border: 1px solid #ae8d57;
    color: #8c6d3b;
    padding: 4px 12px;
    border-radius: 6px;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 0.02em;
}
.badge-blue {
    background: #e0f2fe;
    border: 1px solid #7dd3fc;
    color: #0369a1;
    padding: 2px 7px;
    border-radius: 4px;
    font-size: 10px;
    font-weight: 700;
    font-family: "JetBrains Mono", monospace, sans-serif;
}
.badge-purple {
    background: #f3e8ff;
    border: 1px solid #d8b4fe;
    color: #6b21a8;
    padding: 2px 7px;
    border-radius: 4px;
    font-size: 10px;
    font-weight: 700;
    font-family: "JetBrains Mono", monospace, sans-serif;
}
.badge-green {
    background: #dcfce7;
    border: 1px solid #86efac;
    color: #15803d;
    padding: 2px 7px;
    border-radius: 4px;
    font-size: 10px;
    font-weight: 700;
    font-family: "JetBrains Mono", monospace, sans-serif;
}
.badge-amber {
    background: #fef3c7;
    border: 1px solid #fcd34d;
    color: #b45309;
    padding: 2px 7px;
    border-radius: 4px;
    font-size: 10px;
    font-weight: 700;
    font-family: "JetBrains Mono", monospace, sans-serif;
}
.card {
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 10px;
    padding: 14px;
    box-shadow: 0 4px 14px rgba(27, 53, 77, 0.05);
    display: flex;
    flex-direction: column;
}
.card-header {
    font-size: 11px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.06em;
    color: #1b354d;
    margin-bottom: 10px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 1px solid #f1f5f9;
    padding-bottom: 6px;
}
.item-box {
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 6px;
    padding: 8px 10px;
    margin-bottom: 7px;
    display: flex;
    justify-content: space-between;
    align-items: center;
}
.item-box:last-child { margin-bottom: 0; }
.item-box-title { font-size: 12px; font-weight: 700; color: #1e293b; }
.item-box-desc { font-size: 10px; color: #64748b; margin-top: 1px; }
.code-pill {
    font-family: "JetBrains Mono", Consolas, monospace;
    font-size: 9.5px;
    background: #f1f5f9;
    color: #0f172a;
    padding: 2px 5px;
    border-radius: 3px;
    border: 1px solid #cbd5e1;
}
.footer {
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-top: 1px solid #e2e8f0;
    padding-top: 10px;
    margin-top: 12px;
    font-size: 10.5px;
    color: #64748b;
    font-weight: 500;
}
"""

DIAGRAMS_SPEC = {
    "arx-infra-architecture": {
        "width": 1600,
        "height": 893,
        "html": f"""<!DOCTYPE html><html><head><style>{CSS_LIGHT}</style></head><body>
        <div class="canvas">
            <div class="header">
                <div class="title-group">
                    <h1>Infrastructure Architecture · OCI Ampere A1 (ARM64)</h1>
                    <p>Network Topology: Dual-Layer Firewall · Traefik Reverse Proxy · Sovereign AI FastMCP Cluster · PostgreSQL 18 pgvector</p>
                </div>
                <div class="badge-gold">4 OCPU · 24 GB RAM · 50+ DOCKER CONTAINERS</div>
            </div>

            <div style="display: grid; grid-template-columns: 280px 1fr 1fr 1fr; gap: 16px; flex: 1;">
                <!-- Col 1: Ingress & Security -->
                <div class="card" style="border-top: 3px solid #0284c7;">
                    <div class="card-header"><span>1 · Ingress & Security Edge</span><span class="badge-blue">Public Zone</span></div>
                    <div class="item-box">
                        <div>
                            <div class="item-box-title">Client Ingress & IDEs</div>
                            <div class="item-box-desc">Antigravity, Claude, WhatsApp Webhook</div>
                        </div>
                        <span class="code-pill">HTTPS :443</span>
                    </div>
                    <div class="item-box">
                        <div>
                            <div class="item-box-title">Dual Firewall Protection</div>
                            <div class="item-box-desc">OCI VCN Security List + iptables</div>
                        </div>
                        <span class="badge-green">Strict</span>
                    </div>
                    <div class="item-box">
                        <div>
                            <div class="item-box-title">DuckDNS Dynamic DNS</div>
                            <div class="item-box-desc">arx-mcp / arx-apps / arx-consulting.com</div>
                        </div>
                        <span class="code-pill">DNS :53</span>
                    </div>
                    <div class="item-box" style="background: #e0f2fe; border-color: #bae6fd;">
                        <div>
                            <div class="item-box-title">Traefik Proxy v3.6</div>
                            <div class="item-box-desc">Auto Let's Encrypt TLS & TokenGuard</div>
                        </div>
                        <span class="badge-blue">TLS 1.3</span>
                    </div>
                </div>

                <!-- Col 2: Sovereign AI FastMCP Hub -->
                <div class="card" style="border-top: 3px solid #7c3aed;">
                    <div class="card-header"><span>2 · Sovereign AI FastMCP Cluster</span><span class="badge-purple">8 Servers</span></div>
                    <div class="item-box" style="background: #faf5ff; border-color: #e9d5ff;">
                        <div>
                            <div class="item-box-title">arx-mistral-router</div>
                            <div class="item-box-desc">Codestral/Mistral-Small · 24h SHA256 Cache</div>
                        </div>
                        <span class="badge-purple">:8000</span>
                    </div>
                    <div class="item-box">
                        <div>
                            <div class="item-box-title">blackstone-mcp</div>
                            <div class="item-box-desc">Quant Execution · Capital.com Bridge</div>
                        </div>
                        <span class="badge-purple">:9460</span>
                    </div>
                    <div class="item-box">
                        <div>
                            <div class="item-box-title">einstein-mcp & saul-mcp</div>
                            <div class="item-box-desc">Academic Research & French Jurisprudence</div>
                        </div>
                        <span class="badge-purple">:9410/20</span>
                    </div>
                    <div class="item-box">
                        <div>
                            <div class="item-box-title">omni-mcp, auto & prisme</div>
                            <div class="item-box-desc">Behavioral Profiling, Deals & Numerology</div>
                        </div>
                        <span class="badge-purple">:9430/50</span>
                    </div>
                </div>

                <!-- Col 3: PaaS & Automation -->
                <div class="card" style="border-top: 3px solid #059669;">
                    <div class="card-header"><span>3 · PaaS & Event Engine</span><span class="badge-green">Workflows</span></div>
                    <div class="item-box">
                        <div>
                            <div class="item-box-title">Coolify Control Plane</div>
                            <div class="item-box-desc">GitHub Webhook Git-Push Deploy</div>
                        </div>
                        <span class="badge-green">PaaS v4.3</span>
                    </div>
                    <div class="item-box" style="background: #f0fdf4; border-color: #bbf7d0;">
                        <div>
                            <div class="item-box-title">n8n Workflow Engine</div>
                            <div class="item-box-desc">Automated pipelines + Task Runners</div>
                        </div>
                        <span class="badge-green">:5678</span>
                    </div>
                    <div class="item-box">
                        <div>
                            <div class="item-box-title">WhatsApp & ntfy Gateway</div>
                            <div class="item-box-desc">Inbound messaging & mobile push alerts</div>
                        </div>
                        <span class="code-pill">Event Hook</span>
                    </div>
                    <div class="item-box">
                        <div>
                            <div class="item-box-title">12x Web Applications</div>
                            <div class="item-box-desc">CapGrowth, Contact-PACA, Briefs, Portals</div>
                        </div>
                        <span class="badge-blue">:3000/:80</span>
                    </div>
                </div>

                <!-- Col 4: Data Layer -->
                <div class="card" style="border-top: 3px solid #d97706;">
                    <div class="card-header"><span>4 · Data & Persistence Layer</span><span class="badge-amber">PG18</span></div>
                    <div class="item-box" style="background: #fffbeb; border-color: #fde68a;">
                        <div>
                            <div class="item-box-title">PostgreSQL 18 (pgvector)</div>
                            <div class="item-box-desc">1536-dim semantic embeddings & arxdb</div>
                        </div>
                        <span class="badge-amber">:5432</span>
                    </div>
                    <div class="item-box">
                        <div>
                            <div class="item-box-title">PostgREST REST APIs</div>
                            <div class="item-box-desc">Zero-latency Supabase OpenAPI mirror</div>
                        </div>
                        <span class="code-pill">REST v1</span>
                    </div>
                    <div class="item-box">
                        <div>
                            <div class="item-box-title">Dual Redis Instances</div>
                            <div class="item-box-desc">coolify-redis + jarvis-redis queues</div>
                        </div>
                        <span class="code-pill">:6379</span>
                    </div>
                    <div class="item-box">
                        <div>
                            <div class="item-box-title">MinIO & OCI Object Store</div>
                            <div class="item-box-desc">S3 Asset Store + Tested Daily Backups</div>
                        </div>
                        <span class="badge-green">Cold Backup</span>
                    </div>
                </div>
            </div>

            <div class="footer">
                <div>ARX INFRASTRUCTURE ARCHITECTURE · OPERATING ON UBUNTU 24.04 LTS (ARM64) · DOCKER NETWORK ISOLATION (10.0.2.0/24)</div>
                <div>AUTONOMOUS PLATFORM WITH ZERO HARD-CODED TRANSIENT IPS & PRODUCTION-TESTED DISASTER RECOVERY</div>
            </div>
        </div></body></html>"""
    },

    "oci-component-data-flow": {
        "width": 1536,
        "height": 1024,
        "html": f"""<!DOCTYPE html><html><head><style>{CSS_LIGHT}</style></head><body>
        <div class="canvas">
            <div class="header">
                <div class="title-group">
                    <h1>Component Data Flow · Real-Time Pipelines</h1>
                    <p>End-to-End Execution Paths: Sovereign AI Inference, Quantitative Trading, Vector Semantic Search & Automated Cloud Backups</p>
                </div>
                <div class="badge-gold">4 Verified Production Pipelines</div>
            </div>

            <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 16px; flex: 1;">
                <!-- Pipeline 1: Sovereign AI Inference -->
                <div class="card" style="border-top: 3px solid #7c3aed;">
                    <div class="card-header"><span>Pipeline 1 · Sovereign AI</span><span class="badge-purple">FastMCP</span></div>
                    <div class="item-box">
                        <div>
                            <div class="item-box-title">1. Antigravity IDE / Client</div>
                            <div class="item-box-desc">Emits tool call (e.g. analyze_code)</div>
                        </div>
                        <span class="code-pill">JSON-RPC</span>
                    </div>
                    <div class="item-box">
                        <div>
                            <div class="item-box-title">2. Traefik TokenGuard</div>
                            <div class="item-box-desc">Validates Bearer token & path secret</div>
                        </div>
                        <span class="badge-blue">TLS 1.3</span>
                    </div>
                    <div class="item-box" style="background: #faf5ff; border-color: #e9d5ff;">
                        <div>
                            <div class="item-box-title">3. arx-mistral-router</div>
                            <div class="item-box-desc">Checks 24h SHA256 cache & rate limits</div>
                        </div>
                        <span class="badge-green">0 Tokens</span>
                    </div>
                    <div class="item-box">
                        <div>
                            <div class="item-box-title">4. Mistral EU Sovereign Cloud</div>
                            <div class="item-box-desc">Codestral / Mistral-Small in Frankfurt</div>
                        </div>
                        <span class="badge-purple">GDPR Native</span>
                    </div>
                </div>

                <!-- Pipeline 2: Quant Trading -->
                <div class="card" style="border-top: 3px solid #d97706;">
                    <div class="card-header"><span>Pipeline 2 · Quant Velocity</span><span class="badge-amber">Institutional</span></div>
                    <div class="item-box">
                        <div>
                            <div class="item-box-title">1. TradingView Signal Hook</div>
                            <div class="item-box-desc">Gold / Index momentum entry alert</div>
                        </div>
                        <span class="code-pill">Webhook</span>
                    </div>
                    <div class="item-box" style="background: #fffbeb; border-color: #fde68a;">
                        <div>
                            <div class="item-box-title">2. Blackstone MCP Engine</div>
                            <div class="item-box-desc">Computes Kelly fraction & bracket stop</div>
                        </div>
                        <span class="badge-amber">Risk Calc</span>
                    </div>
                    <div class="item-box">
                        <div>
                            <div class="item-box-title">3. Capital.com Bridge</div>
                            <div class="item-box-desc">Executes guaranteed stop CFD order</div>
                        </div>
                        <span class="code-pill">REST API</span>
                    </div>
                    <div class="item-box">
                        <div>
                            <div class="item-box-title">4. Instant ntfy Push Alert</div>
                            <div class="item-box-desc">Real-time mobile execution receipt</div>
                        </div>
                        <span class="badge-blue">Sub-sec</span>
                    </div>
                </div>

                <!-- Pipeline 3: Semantic Vector RAG -->
                <div class="card" style="border-top: 3px solid #0284c7;">
                    <div class="card-header"><span>Pipeline 3 · Vector RAG</span><span class="badge-blue">PG18</span></div>
                    <div class="item-box">
                        <div>
                            <div class="item-box-title">1. Document & Lead Ingest</div>
                            <div class="item-box-desc">PACA corpus, legal texts, profiles</div>
                        </div>
                        <span class="code-pill">ETL</span>
                    </div>
                    <div class="item-box">
                        <div>
                            <div class="item-box-title">2. Embedding Generation</div>
                            <div class="item-box-desc">1536-dimensional dense vectors</div>
                        </div>
                        <span class="badge-purple">FastEmbed</span>
                    </div>
                    <div class="item-box" style="background: #e0f2fe; border-color: #bae6fd;">
                        <div>
                            <div class="item-box-title">3. PostgreSQL 18 pgvector</div>
                            <div class="item-box-desc">HNSW cosine similarity search (&lt;=&gt;)</div>
                        </div>
                        <span class="badge-blue">&lt; 5ms</span>
                    </div>
                    <div class="item-box">
                        <div>
                            <div class="item-box-title">4. PostgREST OpenAPI Layer</div>
                            <div class="item-box-desc">Delivers enriched context to LLMs</div>
                        </div>
                        <span class="badge-green">Supabase API</span>
                    </div>
                </div>

                <!-- Pipeline 4: Automated CI/CD & Backups -->
                <div class="card" style="border-top: 3px solid #059669;">
                    <div class="card-header"><span>Pipeline 4 · CI/CD & Backups</span><span class="badge-green">Zero-Loss</span></div>
                    <div class="item-box">
                        <div>
                            <div class="item-box-title">1. GitHub Push Trigger</div>
                            <div class="item-box-desc">git push origin master</div>
                        </div>
                        <span class="code-pill">Git Hook</span>
                    </div>
                    <div class="item-box">
                        <div>
                            <div class="item-box-title">2. Coolify Automated Build</div>
                            <div class="item-box-desc">Nixpacks/Docker build & zero-downtime swap</div>
                        </div>
                        <span class="badge-green">Auto Deploy</span>
                    </div>
                    <div class="item-box">
                        <div>
                            <div class="item-box-title">3. Daily Cron (03:00 UTC)</div>
                            <div class="item-box-desc">Encrypted pg_dump & volume tarball</div>
                        </div>
                        <span class="code-pill">cron</span>
                    </div>
                    <div class="item-box" style="background: #f0fdf4; border-color: #bbf7d0;">
                        <div>
                            <div class="item-box-title">4. OCI Object Storage</div>
                            <div class="item-box-desc">Cold off-site bucket with tested restore</div>
                        </div>
                        <span class="badge-gold">Tested</span>
                    </div>
                </div>
            </div>

            <div class="footer">
                <div>ARX END-TO-END DATA FLOW · ZERO EXTERNAL API LATENCY BOTTLENECKS · ENCRYPTED IN TRANSIT AND AT REST</div>
                <div>AUTONOMOUS TELEMETRY PERSISTED TO ARX GATE FOR CONTINUOUS COMPLIANCE AUDITING</div>
            </div>
        </div></body></html>"""
    },

    "arx-paas-details": {
        "width": 1600,
        "height": 873,
        "html": f"""<!DOCTYPE html><html><head><style>{CSS_LIGHT}</style></head><body>
        <div class="canvas">
            <div class="header">
                <div class="title-group">
                    <h1>ARX PaaS Details · 50+ Production Container Matrix</h1>
                    <p>Microservice Inventory: FastMCP AI Cluster · Production Web Portals · Event Automations · Database Engines</p>
                </div>
                <div class="badge-gold">Complete Fleet Overview</div>
            </div>

            <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 16px; flex: 1;">
                <div class="card" style="border-top: 3px solid #7c3aed;">
                    <div class="card-header"><span>Sovereign AI FastMCP Hub (8)</span><span class="badge-purple">Cluster</span></div>
                    <div class="item-box"><div class="item-box-title">arx-mistral-router</div><div class="item-box-desc">AI Router & 24h Cache (:8000)</div></div>
                    <div class="item-box"><div class="item-box-title">blackstone-mcp</div><div class="item-box-desc">Quant Trading & Capital.com (:9460)</div></div>
                    <div class="item-box"><div class="item-box-title">einstein-mcp</div><div class="item-box-desc">Academic Deep Research (:9410)</div></div>
                    <div class="item-box"><div class="item-box-title">saul-mcp</div><div class="item-box-desc">Legal Corpus & Cadastre (:9420)</div></div>
                    <div class="item-box"><div class="item-box-title">omni-mcp</div><div class="item-box-desc">Behavioral Profiler v3 (:9430)</div></div>
                    <div class="item-box"><div class="item-box-title">arx-auto-mcp</div><div class="item-box-desc">EU Auto Valuation & Tax (:9450)</div></div>
                    <div class="item-box"><div class="item-box-title">prisme-mcp</div><div class="item-box-desc">Numerology & Chart Engine</div></div>
                    <div class="item-box"><div class="item-box-title">rag-social-mcp</div><div class="item-box-desc">Social RAG & Vector Profiles (:9440)</div></div>
                </div>

                <div class="card" style="border-top: 3px solid #0284c7;">
                    <div class="card-header"><span>Web Applications & Portals (12)</span><span class="badge-blue">Web Tier</span></div>
                    <div class="item-box"><div class="item-box-title">arx-consulting.com</div><div class="item-box-desc">Corporate Portal & Case Studies</div></div>
                    <div class="item-box"><div class="item-box-title">capgrowth</div><div class="item-box-desc">Financial Growth Engine (:3000)</div></div>
                    <div class="item-box"><div class="item-box-title">contact-paca</div><div class="item-box-desc">Regional Enterprise Hub (:3000)</div></div>
                    <div class="item-box"><div class="item-box-title">arx-brief-server</div><div class="item-box-desc">Daily Executive Digest (:8088)</div></div>
                    <div class="item-box"><div class="item-box-title">arx-linki</div><div class="item-box-desc">Smart URL Redirection (:3000)</div></div>
                    <div class="item-box"><div class="item-box-title">innovat-ch</div><div class="item-box-desc">Swiss Innovation Platform (:80)</div></div>
                    <div class="item-box"><div class="item-box-title">candidatures</div><div class="item-box-desc">Candidate Intake Gateway (:3000)</div></div>
                    <div class="item-box"><div class="item-box-title">arx-atlas</div><div class="item-box-desc">Knowledge Atlas & Interactive Maps</div></div>
                </div>

                <div class="card" style="border-top: 3px solid #059669;">
                    <div class="card-header"><span>Event & Automation Engines (8)</span><span class="badge-green">Workflows</span></div>
                    <div class="item-box"><div class="item-box-title">n8n Workflow Core</div><div class="item-box-desc">Enterprise Pipeline Server (:5678)</div></div>
                    <div class="item-box"><div class="item-box-title">n8n Task Runners</div><div class="item-box-desc">Isolated Async Execution (:5680)</div></div>
                    <div class="item-box"><div class="item-box-title">arx-whatsapp-gateway</div><div class="item-box-desc">Two-Way WhatsApp Bridge</div></div>
                    <div class="item-box"><div class="item-box-title">ntfy Push Server</div><div class="item-box-desc">Mobile Alert Broker (:80)</div></div>
                    <div class="item-box"><div class="item-box-title">arx-mailer & Campaigns</div><div class="item-box-desc">Transactional Email Engine (:8080)</div></div>
                    <div class="item-box"><div class="item-box-title">arx-tracker</div><div class="item-box-desc">Telemetry & Analytics (:8000)</div></div>
                    <div class="item-box"><div class="item-box-title">jarvis-brain</div><div class="item-box-desc">Autonomous Agent Core (:8000)</div></div>
                    <div class="item-box"><div class="item-box-title">DuckDNS Cron Daemon</div><div class="item-box-desc">Automated Dynamic IP Sync</div></div>
                </div>

                <div class="card" style="border-top: 3px solid #d97706;">
                    <div class="card-header"><span>Data & Infrastructure (6)</span><span class="badge-amber">Persistence</span></div>
                    <div class="item-box"><div class="item-box-title">PostgreSQL 18 + Vector</div><div class="item-box-desc">pgvector Semantic DB (w1043af...)</div></div>
                    <div class="item-box"><div class="item-box-title">PostgREST API Gateways</div><div class="item-box-desc">Supabase-Compatible REST</div></div>
                    <div class="item-box"><div class="item-box-title">Coolify DB</div><div class="item-box-desc">PostgreSQL 15 System DB</div></div>
                    <div class="item-box"><div class="item-box-title">coolify-redis</div><div class="item-box-desc">In-Memory Job Queue (:6379)</div></div>
                    <div class="item-box"><div class="item-box-title">jarvis-redis</div><div class="item-box-desc">Agent State Store (:6379)</div></div>
                    <div class="item-box"><div class="item-box-title">MinIO S3 Object Store</div><div class="item-box-desc">S3 Asset Storage (:9000)</div></div>
                </div>
            </div>

            <div class="footer">
                <div>ARX FLEET SPECIFICATION · DOCKER 27 RUNTIME · RESOLVED INTERNALLY VIA DOCKER NETWORK DNS (COOLIFY)</div>
                <div>RESOURCE CONSUMPTION: 4.7 GB USED / 24 GB OCI ALLOCATION · CPU LOAD: &lt; 8% AVERAGE</div>
            </div>
        </div></body></html>"""
    },

    "arx-paas-service-layer": {
        "width": 1536,
        "height": 1024,
        "html": f"""<!DOCTYPE html><html><head><style>{CSS_LIGHT}</style></head><body>
        <div class="canvas">
            <div class="header">
                <div class="title-group">
                    <h1>ARX PaaS Service Layer · Architectural Stack</h1>
                    <p>Hierarchical Platform Topology from Bare-Metal ARM64 Foundation to Edge Routing</p>
                </div>
                <div class="badge-gold">4-Layer Stack</div>
            </div>

            <div style="display: flex; flex-direction: column; gap: 14px; flex: 1;">
                <div class="card" style="border-left: 4px solid #0284c7;">
                    <div class="card-header"><span>Layer 4 · Edge Ingress & TLS Termination</span><span class="badge-blue">Traefik v3.6</span></div>
                    <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 10px;">
                        <div class="item-box"><div class="item-box-title">Let's Encrypt TLS</div><div class="item-box-desc">Auto-renewing wildcard SSL</div></div>
                        <div class="item-box"><div class="item-box-title">TokenGuard Security</div><div class="item-box-desc">Bearer & path-based secrets</div></div>
                        <div class="item-box"><div class="item-box-title">DuckDNS Gateways</div><div class="item-box-desc">arx-mcp / arx-apps / arx-sites</div></div>
                        <div class="item-box"><div class="item-box-title">HTTP/3 + Gzip</div><div class="item-box-desc">Ultra-low latency compression</div></div>
                    </div>
                </div>

                <div class="card" style="border-left: 4px solid #7c3aed;">
                    <div class="card-header"><span>Layer 3 · Sovereign AI FastMCP & Application Plane</span><span class="badge-purple">Microservices</span></div>
                    <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 10px;">
                        <div class="item-box"><div class="item-box-title">ARX Mistral Router</div><div class="item-box-desc">Codestral / Mistral-Small</div></div>
                        <div class="item-box"><div class="item-box-title">Blackstone Quant MCP</div><div class="item-box-desc">Capital.com Execution Engine</div></div>
                        <div class="item-box"><div class="item-box-title">Research & Legal MCP</div><div class="item-box-desc">Einstein, Saul, Omni, Auto</div></div>
                        <div class="item-box"><div class="item-box-title">n8n Automation Engine</div><div class="item-box-desc">Event Workflows & Webhooks</div></div>
                    </div>
                </div>

                <div class="card" style="border-left: 4px solid #059669;">
                    <div class="card-header"><span>Layer 2 · Container Orchestration & Control Plane</span><span class="badge-green">Coolify PaaS</span></div>
                    <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 10px;">
                        <div class="item-box"><div class="item-box-title">Git Webhook Deploy</div><div class="item-box-desc">Automated build on push</div></div>
                        <div class="item-box"><div class="item-box-title">Secrets Management</div><div class="item-box-desc">Encrypted environment vars</div></div>
                        <div class="item-box"><div class="item-box-title">Docker Engine 27</div><div class="item-box-desc">ARM64 native containerization</div></div>
                        <div class="item-box"><div class="item-box-title">Health Monitors</div><div class="item-box-desc">Automatic health restart</div></div>
                    </div>
                </div>

                <div class="card" style="border-left: 4px solid #d97706;">
                    <div class="card-header"><span>Layer 1 · Sovereign Infrastructure & Data Foundation</span><span class="badge-amber">OCI Ampere A1</span></div>
                    <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 10px;">
                        <div class="item-box"><div class="item-box-title">4 ARM Neoverse Cores</div><div class="item-box-desc">High-efficiency compute</div></div>
                        <div class="item-box"><div class="item-box-title">24 GB RAM Allocation</div><div class="item-box-desc">19.2 GB available headroom</div></div>
                        <div class="item-box"><div class="item-box-title">PostgreSQL 18 (pgvector)</div><div class="item-box-desc">Semantic search & RAG</div></div>
                        <div class="item-box"><div class="item-box-title">OCI Object Storage</div><div class="item-box-desc">Off-site cold backup target</div></div>
                    </div>
                </div>
            </div>

            <div class="footer">
                <div>ARX PLATFORM STACK · STRICT COMPONENT SEPARATION · FULLY SOVEREIGN EUROPEAN CLOUD DEPLOYMENT</div>
                <div>MEETS STRINGENT GDPR & DATA PRIVACY STANDARDS WITH ZERO DATA RETENTION BY THIRD PARTIES</div>
            </div>
        </div></body></html>"""
    },

    "oci-migration-en": {
        "width": 1024,
        "height": 1536,
        "html": f"""<!DOCTYPE html><html><head><style>{CSS_LIGHT}</style></head><body>
        <div class="canvas" style="padding: 32px 36px;">
            <div class="header">
                <div class="title-group">
                    <h1 style="font-size: 21px;">OCI Migration Overview · Full Consolidation</h1>
                    <p>Consolidating 4 Fragmented Cloud Providers into a Single Sovereign OCI Ampere Platform</p>
                </div>
                <div class="badge-gold">Migration Complete</div>
            </div>

            <div style="display: flex; flex-direction: column; gap: 16px; flex: 1;">
                <!-- Before Box -->
                <div class="card" style="border-top: 3px solid #ef4444; background: #fffaf0;">
                    <div class="card-header" style="color: #b91c1c;"><span>BEFORE · 4 Fragmented Cloud Subscriptions</span><span class="badge-amber">Legacy Stack</span></div>
                    <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 8px;">
                        <div class="item-box"><div class="item-box-title">Vercel</div><div class="item-box-desc">Static web frontends & edge limits</div></div>
                        <div class="item-box"><div class="item-box-title">Render</div><div class="item-box-desc">Background workers & paid cron jobs</div></div>
                        <div class="item-box"><div class="item-box-title">Supabase</div><div class="item-box-desc">PostgreSQL DB & restrictive row limits</div></div>
                        <div class="item-box"><div class="item-box-title">Local Dev Servers</div><div class="item-box-desc">Unmonitored offline scripts & tools</div></div>
                    </div>
                </div>

                <div style="text-align: center; color: #0284c7; font-weight: 700; font-size: 13px; margin: 4px 0;">
                    ▼ CONSOLIDATED INTO ONE SOVEREIGN PLATFORM (100% COMPLETE) ▼
                </div>

                <!-- After Box -->
                <div class="card" style="border-top: 3px solid #059669; background: #ffffff; flex: 1;">
                    <div class="card-header" style="color: #15803d;"><span>AFTER · Single OCI Ampere A1 (ARM64)</span><span class="badge-green">Always Free</span></div>
                    <div style="display: flex; flex-direction: column; gap: 8px;">
                        <div class="item-box" style="background: #faf5ff; border-color: #e9d5ff;">
                            <div>
                                <div class="item-box-title">8x Sovereign AI FastMCP Gateways</div>
                                <div class="item-box-desc">Mistral Router, Blackstone Quant, Einstein, Saul Legal, Omni, Auto</div>
                            </div>
                            <span class="badge-purple">FastMCP</span>
                        </div>
                        <div class="item-box" style="background: #fffbeb; border-color: #fde68a;">
                            <div>
                                <div class="item-box-title">PostgreSQL 18 + pgvector + PostgREST</div>
                                <div class="item-box-desc">Supabase syntax preserved, semantic search & zero row restrictions</div>
                            </div>
                            <span class="badge-amber">PG18</span>
                        </div>
                        <div class="item-box" style="background: #e0f2fe; border-color: #bae6fd;">
                            <div>
                                <div class="item-box-title">Traefik v3.6 + Coolify Control Plane</div>
                                <div class="item-box-desc">Automatic Let's Encrypt TLS, Git push-to-deploy for 50+ containers</div>
                            </div>
                            <span class="badge-blue">PaaS</span>
                        </div>
                        <div class="item-box" style="background: #f0fdf4; border-color: #bbf7d0;">
                            <div>
                                <div class="item-box-title">n8n Workflow Engine + Dual Redis</div>
                                <div class="item-box-desc">Low-code automations, WhatsApp AI bridge & instant push alerts</div>
                            </div>
                            <span class="badge-green">Workflows</span>
                        </div>
                        <div class="item-box">
                            <div>
                                <div class="item-box-title">MinIO S3 + OCI Object Storage</div>
                                <div class="item-box-desc">S3 asset store + automated daily encrypted off-container backups</div>
                            </div>
                            <span class="badge-gold">Tested</span>
                        </div>
                    </div>
                </div>
            </div>

            <div class="footer">
                <div>ARX CONSOLIDATION SUMMARY · 50+ CONTAINERS RUNNING 24/7 · ZERO MONTHLY CLOUD SUBSCRIPTION FEES</div>
                <div>FULL DATA SOVEREIGNTY OPERATED END-TO-END ON ORACLE CLOUD ALWAYS FREE TIER</div>
            </div>
        </div></body></html>"""
    }
}


def render_all():
    with sync_playwright() as p:
        browser = p.chromium.launch(channel="msedge")
        for name, spec in DIAGRAMS_SPEC.items():
            w = spec["width"]
            h = spec["height"]
            page = browser.new_page(viewport={"width": w, "height": h}, device_scale_factor=2)
            page.set_content(spec["html"])
            page.wait_for_timeout(400)
            
            temp_png = os.path.join(ASSETS_DIR, f"{name}_temp.png")
            out_webp = os.path.join(ASSETS_DIR, f"{name}.webp")
            page.screenshot(path=temp_png)
            page.close()
            
            im = Image.open(temp_png)
            im.save(out_webp, "WEBP", quality=92, method=6)
            print(f"Generated {name}.webp ({im.size})")
            
            if w > 800:
                h800 = int(h * (800 / w))
                im_800 = im.resize((800, h800), Image.Resampling.LANCZOS)
                out_800 = os.path.join(ASSETS_DIR, f"{name}-800.webp")
                im_800.save(out_800, "WEBP", quality=90, method=6)
                print(f"Generated {name}-800.webp ({im_800.size})")
            
            if os.path.exists(temp_png):
                os.remove(temp_png)
                
        browser.close()
    print("All professional diagrams rendered successfully!")

if __name__ == "__main__":
    render_all()
