"""
Generate high-resolution architecture diagrams for arx-consulting.com OCI Migration.
Uses Playwright to render styled HTML/CSS canvases directly into webp image assets.
"""

import os
from PIL import Image
from playwright.sync_api import sync_playwright

ASSETS_DIR = r"G:\My Drive\Arx Capital\web\arxWeb\assets"
os.makedirs(ASSETS_DIR, exist_ok=True)

SHARED_CSS = """
* { margin: 0; padding: 0; box-sizing: border-box; }
body {
    background: #0d1520;
    color: #e2e8f0;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Inter", sans-serif;
    -webkit-font-smoothing: antialiased;
    overflow: hidden;
}
.diagram-canvas {
    width: 100%;
    height: 100%;
    padding: 32px 40px;
    background: radial-gradient(circle at 50% 0%, #1e3a5f 0%, #0d1520 70%);
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}
.header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 1px solid rgba(255,255,255,0.12);
    padding-bottom: 16px;
    margin-bottom: 20px;
}
.title-group h1 {
    font-size: 26px;
    font-weight: 700;
    color: #ffffff;
    letter-spacing: -0.02em;
    display: flex;
    align-items: center;
    gap: 12px;
}
.title-group p {
    font-size: 13px;
    color: #94a3b8;
    margin-top: 4px;
}
.badge-gold {
    background: rgba(174, 141, 87, 0.2);
    border: 1px solid #ae8d57;
    color: #d8bc85;
    padding: 4px 12px;
    border-radius: 999px;
    font-size: 12px;
    font-weight: 600;
}
.badge-blue {
    background: rgba(56, 189, 248, 0.15);
    border: 1px solid rgba(56, 189, 248, 0.4);
    color: #38bdf8;
    padding: 3px 8px;
    border-radius: 6px;
    font-size: 11px;
    font-weight: 600;
}
.badge-green {
    background: rgba(52, 211, 153, 0.15);
    border: 1px solid rgba(52, 211, 153, 0.4);
    color: #34d399;
    padding: 3px 8px;
    border-radius: 6px;
    font-size: 11px;
    font-weight: 600;
}
.badge-purple {
    background: rgba(168, 85, 247, 0.15);
    border: 1px solid rgba(168, 85, 247, 0.4);
    color: #c084fc;
    padding: 3px 8px;
    border-radius: 6px;
    font-size: 11px;
    font-weight: 600;
}
.card {
    background: rgba(23, 37, 56, 0.75);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 12px;
    padding: 16px;
    backdrop-filter: blur(8px);
    box-shadow: 0 4px 20px rgba(0,0,0,0.3);
}
.card-header {
    font-size: 13px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    color: #ae8d57;
    margin-bottom: 12px;
    display: flex;
    justify-content: space-between;
    align-items: center;
}
.item-pill {
    background: rgba(255, 255, 255, 0.04);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 8px;
    padding: 8px 12px;
    margin-bottom: 8px;
    display: flex;
    justify-content: space-between;
    align-items: center;
}
.item-pill:last-child { margin-bottom: 0; }
.item-title { font-size: 13px; font-weight: 600; color: #ffffff; }
.item-desc { font-size: 11px; color: #94a3b8; }
.grid-cols-4 { display: grid; grid-template-columns: repeat(4, 1fr); gap: 16px; flex: 1; }
.grid-cols-3 { display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px; flex: 1; }
.grid-cols-2 { display: grid; grid-template-columns: repeat(2, 1fr); gap: 16px; flex: 1; }
.flow-arrow {
    display: flex;
    align-items: center;
    justify-content: center;
    color: #38bdf8;
    font-weight: bold;
    font-size: 20px;
}
.footer {
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-top: 1px solid rgba(255,255,255,0.08);
    padding-top: 12px;
    margin-top: 16px;
    font-size: 11px;
    color: #64748b;
}
"""

DIAGRAMS = {
    "arx-infra-architecture": {
        "width": 1600,
        "height": 893,
        "html": f"""<!DOCTYPE html><html><head><style>{SHARED_CSS}</style></head><body>
        <div class="diagram-canvas">
            <div class="header">
                <div class="title-group">
                    <h1><span>🏛️</span> ARX Infrastructure Architecture · OCI Ampere A1 (ARM64)</h1>
                    <p>Production Topology: 50+ Microservices, Dual-Layer Firewall, Traefik TLS & Sovereign AI FastMCP Cluster</p>
                </div>
                <div class="badge-gold">4 OCPU · 24 GB RAM · Always Free Tier</div>
            </div>

            <div class="grid-cols-4" style="gap: 20px;">
                <!-- Col 1: Ingress & Security -->
                <div class="card" style="border-top: 3px solid #38bdf8;">
                    <div class="card-header"><span>1 · Ingress & Security</span><span class="badge-blue">TLS 1.3</span></div>
                    <div class="item-pill">
                        <div>
                            <div class="item-title">Public Traffic & IDEs</div>
                            <div class="item-desc">HTTPS, Antigravity, Claude, WhatsApp</div>
                        </div>
                    </div>
                    <div class="item-pill">
                        <div>
                            <div class="item-title">Dual Firewall Layer</div>
                            <div class="item-desc">OCI Security List + Host iptables</div>
                        </div>
                        <span class="badge-green">Secured</span>
                    </div>
                    <div class="item-pill">
                        <div>
                            <div class="item-title">DuckDNS SSL Gateway</div>
                            <div class="item-desc">arx-mcp.duckdns.org / arx-consulting.com</div>
                        </div>
                    </div>
                    <div class="item-pill" style="background: rgba(56, 189, 248, 0.08); border-color: rgba(56, 189, 248, 0.3);">
                        <div>
                            <div class="item-title">Traefik v3.6 Proxy</div>
                            <div class="item-desc">Auto Let's Encrypt & TokenGuard Auth</div>
                        </div>
                        <span class="badge-blue">Reverse Proxy</span>
                    </div>
                </div>

                <!-- Col 2: Sovereign AI & FastMCP -->
                <div class="card" style="border-top: 3px solid #c084fc;">
                    <div class="card-header"><span>2 · FastMCP Cluster</span><span class="badge-purple">Sovereign AI</span></div>
                    <div class="item-pill" style="background: rgba(168, 85, 247, 0.12); border-color: rgba(168, 85, 247, 0.4);">
                        <div>
                            <div class="item-title">ARX Mistral Router</div>
                            <div class="item-desc">Codestral / Mistral-Small · 24h Cache</div>
                        </div>
                        <span class="badge-purple">Port 8000</span>
                    </div>
                    <div class="item-pill">
                        <div>
                            <div class="item-title">Blackstone MCP</div>
                            <div class="item-desc">Quant Execution & Capital.com Bridge</div>
                        </div>
                        <span class="badge-purple">Port 9460</span>
                    </div>
                    <div class="item-pill">
                        <div>
                            <div class="item-title">Einstein & Saul MCP</div>
                            <div class="item-desc">Deep Research & Legal Jurisprudence</div>
                        </div>
                        <span class="badge-purple">Ports 9410/9420</span>
                    </div>
                    <div class="item-pill">
                        <div>
                            <div class="item-title">Omni, Auto & Prisme</div>
                            <div class="item-desc">Profiling, Deal Hunter & Chart Engine</div>
                        </div>
                        <span class="badge-purple">Ports 9430-9450</span>
                    </div>
                </div>

                <!-- Col 3: PaaS & Automation -->
                <div class="card" style="border-top: 3px solid #34d399;">
                    <div class="card-header"><span>3 · PaaS & Automation</span><span class="badge-green">50+ Apps</span></div>
                    <div class="item-pill">
                        <div>
                            <div class="item-title">Coolify PaaS Engine</div>
                            <div class="item-desc">Git push-to-deploy & container lifecycle</div>
                        </div>
                        <span class="badge-green">Control Plane</span>
                    </div>
                    <div class="item-pill">
                        <div>
                            <div class="item-title">n8n Workflow Engine</div>
                            <div class="item-desc">Automated pipelines & task runners</div>
                        </div>
                        <span class="badge-green">Port 5678</span>
                    </div>
                    <div class="item-pill">
                        <div>
                            <div class="item-title">WhatsApp AI Gateway</div>
                            <div class="item-desc">Inbound messaging to Jarvis Brain</div>
                        </div>
                        <span class="badge-green">Live Hook</span>
                    </div>
                    <div class="item-pill">
                        <div>
                            <div class="item-title">Web Apps & Portals</div>
                            <div class="item-desc">CapGrowth, Contact-PACA, Brief Server</div>
                        </div>
                    </div>
                </div>

                <!-- Col 4: Data Layer & Persistence -->
                <div class="card" style="border-top: 3px solid #f59e0b;">
                    <div class="card-header"><span>4 · Data & Persistence</span><span class="badge-gold">PG18 + Vector</span></div>
                    <div class="item-pill" style="background: rgba(245, 158, 11, 0.1); border-color: rgba(245, 158, 11, 0.3);">
                        <div>
                            <div class="item-title">PostgreSQL 18 (pgvector)</div>
                            <div class="item-desc">Semantic search, RAG & arxdb</div>
                        </div>
                        <span class="badge-gold">Port 5432</span>
                    </div>
                    <div class="item-pill">
                        <div>
                            <div class="item-title">PostgREST Data APIs</div>
                            <div class="item-desc">Supabase-compatible REST endpoints</div>
                        </div>
                    </div>
                    <div class="item-pill">
                        <div>
                            <div class="item-title">Dual Redis Layer</div>
                            <div class="item-desc">Coolify + Jarvis async session queues</div>
                        </div>
                        <span class="badge-blue">In-Memory</span>
                    </div>
                    <div class="item-pill">
                        <div>
                            <div class="item-title">MinIO & OCI Storage</div>
                            <div class="item-desc">S3 storage + automated daily backups</div>
                        </div>
                        <span class="badge-green">Off-site</span>
                    </div>
                </div>
            </div>

            <div class="footer">
                <div>ARX CONSULTING · OCI PRODUCTION ARCHITECTURE (UBUNTU 24.04 LTS · DOCKER 27 · TRAEFIK 3.6)</div>
                <div>VERIFIED ZERO-LOSS DISASTER RECOVERY & SOVEREIGN EUROPEAN DATA RESIDENCY</div>
            </div>
        </div></body></html>"""
    },

    "oci-component-data-flow": {
        "width": 1536,
        "height": 1024,
        "html": f"""<!DOCTYPE html><html><head><style>{SHARED_CSS}</style></head><body>
        <div class="diagram-canvas">
            <div class="header">
                <div class="title-group">
                    <h1><span>⚡</span> OCI Component Data Flow · Real-Time Pipelines</h1>
                    <p>Request Routing, Sovereign AI FastMCP Delegation, Event Automation & Database Replication</p>
                </div>
                <div class="badge-gold">End-to-End Data Pipeline</div>
            </div>

            <div class="grid-cols-3" style="gap: 24px; flex: 1;">
                <div class="card" style="border-top: 3px solid #38bdf8;">
                    <div class="card-header"><span>Pipeline A · AI Delegation</span><span class="badge-blue">Sovereign Tier</span></div>
                    <div class="item-pill">
                        <div>
                            <div class="item-title">1. Antigravity / Client</div>
                            <div class="item-desc">Emits FastMCP tool call over HTTPS</div>
                        </div>
                    </div>
                    <div class="item-pill">
                        <div>
                            <div class="item-title">2. Traefik TokenGuard</div>
                            <div class="item-desc">Validates Bearer token / URL secret</div>
                        </div>
                    </div>
                    <div class="item-pill" style="background: rgba(168, 85, 247, 0.1);">
                        <div>
                            <div class="item-title">3. ARX Mistral Router</div>
                            <div class="item-desc">Checks 24h SHA256 cache & limits</div>
                        </div>
                        <span class="badge-purple">0 Tokens</span>
                    </div>
                    <div class="item-pill">
                        <div>
                            <div class="item-title">4. Mistral Sovereign Cloud</div>
                            <div class="item-desc">Codestral / Mistral-Small on EU host</div>
                        </div>
                        <span class="badge-green">GDPR Native</span>
                    </div>
                </div>

                <div class="card" style="border-top: 3px solid #f59e0b;">
                    <div class="card-header"><span>Pipeline B · Quant & Trading</span><span class="badge-gold">Institutional</span></div>
                    <div class="item-pill">
                        <div>
                            <div class="item-title">1. TradingView / Pine Hook</div>
                            <div class="item-desc">Generates Gold / Index buy signal</div>
                        </div>
                    </div>
                    <div class="item-pill">
                        <div>
                            <div class="item-title">2. Blackstone MCP</div>
                            <div class="item-desc">Calculates Kelly size & bracket stops</div>
                        </div>
                        <span class="badge-gold">FastMCP</span>
                    </div>
                    <div class="item-pill">
                        <div>
                            <div class="item-title">3. Capital.com Bridge</div>
                            <div class="item-desc">Executes guaranteed stop CFD order</div>
                        </div>
                    </div>
                    <div class="item-pill">
                        <div>
                            <div class="item-title">4. Instant ntfy Push Alert</div>
                            <div class="item-desc">Delivers real-time execution receipt</div>
                        </div>
                        <span class="badge-blue">Mobile Push</span>
                    </div>
                </div>

                <div class="card" style="border-top: 3px solid #34d399;">
                    <div class="card-header"><span>Pipeline C · Data & Backups</span><span class="badge-green">Zero-Loss</span></div>
                    <div class="item-pill">
                        <div>
                            <div class="item-title">1. Vector Semantic Ingest</div>
                            <div class="item-desc">Embeddings saved in PostgreSQL 18</div>
                        </div>
                        <span class="badge-green">pgvector</span>
                    </div>
                    <div class="item-pill">
                        <div>
                            <div class="item-title">2. PostgREST REST Mirror</div>
                            <div class="item-desc">Instant OpenAPI query generation</div>
                        </div>
                    </div>
                    <div class="item-pill">
                        <div>
                            <div class="item-title">3. Daily Cron (03:00 UTC)</div>
                            <div class="item-desc">Encrypted volume & database dump</div>
                        </div>
                    </div>
                    <div class="item-pill" style="background: rgba(52, 211, 153, 0.1);">
                        <div>
                            <div class="item-title">4. OCI Object Storage</div>
                            <div class="item-desc">Off-site cold backup with tested restore</div>
                        </div>
                        <span class="badge-gold">100% Tested</span>
                    </div>
                </div>
            </div>

            <div class="footer">
                <div>ARX DATA FLOW SPECIFICATION · FAST HTTP/3 + TLS 1.3 + TOKEN GUARD MIDDLEWARE</div>
                <div>STREAMING METRICS & AUDITABLE TELEMETRY PERSISTED TO ARX GATE</div>
            </div>
        </div></body></html>"""
    },

    "arx-paas-details": {
        "width": 1600,
        "height": 873,
        "html": f"""<!DOCTYPE html><html><head><style>{SHARED_CSS}</style></head><body>
        <div class="diagram-canvas">
            <div class="header">
                <div class="title-group">
                    <h1><span>📦</span> ARX PaaS Details · 50+ Production Containers Breakdown</h1>
                    <p>Comprehensive Container Fleet Breakdown across AI, Applications, Automations & Databases</p>
                </div>
                <div class="badge-gold">Fleet Management</div>
            </div>

            <div class="grid-cols-4" style="gap: 16px; flex: 1;">
                <div class="card">
                    <div class="card-header"><span>🤖 FastMCP Cluster (8)</span><span class="badge-purple">AI Gateways</span></div>
                    <div class="item-pill"><div class="item-title">arx-mistral-router</div><div class="item-desc">AI Router & Caching</div></div>
                    <div class="item-pill"><div class="item-title">blackstone-mcp</div><div class="item-desc">Quant Trading Engine</div></div>
                    <div class="item-pill"><div class="item-title">einstein-mcp</div><div class="item-desc">Deep Academic Research</div></div>
                    <div class="item-pill"><div class="item-title">saul-mcp</div><div class="item-desc">Legal & Cadastre Search</div></div>
                    <div class="item-pill"><div class="item-title">omni-mcp</div><div class="item-desc">Behavioral Profiler v3</div></div>
                    <div class="item-pill"><div class="item-title">arx-auto-mcp</div><div class="item-desc">EU Auto Deal Hunter</div></div>
                    <div class="item-pill"><div class="item-title">prisme-mcp</div><div class="item-desc">Numerology & Chart Engine</div></div>
                    <div class="item-pill"><div class="item-title">rag-social-mcp</div><div class="item-desc">Social Profiling RAG</div></div>
                </div>

                <div class="card">
                    <div class="card-header"><span>🌐 Web Applications (12)</span><span class="badge-blue">Production</span></div>
                    <div class="item-pill"><div class="item-title">arx-consulting.com</div><div class="item-desc">Main Corporate Site</div></div>
                    <div class="item-pill"><div class="item-title">capgrowth</div><div class="item-desc">Financial Growth Platform</div></div>
                    <div class="item-pill"><div class="item-title">contact-paca</div><div class="item-desc">Regional Enterprise Hub</div></div>
                    <div class="item-pill"><div class="item-title">arx-brief-server</div><div class="item-desc">Daily Executive Digest</div></div>
                    <div class="item-pill"><div class="item-title">arx-linki</div><div class="item-desc">Smart Redirect Engine</div></div>
                    <div class="item-pill"><div class="item-title">innovat-ch</div><div class="item-desc">Swiss Innovation Portal</div></div>
                    <div class="item-pill"><div class="item-title">candidatures</div><div class="item-desc">Talent Ingestion Portal</div></div>
                    <div class="item-pill"><div class="item-title">arx-atlas</div><div class="item-desc">Knowledge Base & Maps</div></div>
                </div>

                <div class="card">
                    <div class="card-header"><span>⚡ Event & Automation (8)</span><span class="badge-green">Workflows</span></div>
                    <div class="item-pill"><div class="item-title">n8n Workflow Server</div><div class="item-desc">Low-code Orchestration</div></div>
                    <div class="item-pill"><div class="item-title">n8n Task Runners</div><div class="item-desc">Isolated Async Workers</div></div>
                    <div class="item-pill"><div class="item-title">arx-whatsapp-gateway</div><div class="item-desc">WhatsApp Bot Bridge</div></div>
                    <div class="item-pill"><div class="item-title">ntfy Push Server</div><div class="item-desc">Instant Mobile Alerts</div></div>
                    <div class="item-pill"><div class="item-title">arx-mailer & Campaigns</div><div class="item-desc">Transactional Outbound</div></div>
                    <div class="item-pill"><div class="item-title">arx-tracker</div><div class="item-desc">Visit & Telemetry Tracker</div></div>
                    <div class="item-pill"><div class="item-title">jarvis-brain</div><div class="item-desc">Agentic Task Brain</div></div>
                    <div class="item-pill"><div class="item-title">DuckDNS Auto-Updater</div><div class="item-desc">Dynamic DNS Cron</div></div>
                </div>

                <div class="card">
                    <div class="card-header"><span>🗄️ Data & Infrastructure (6)</span><span class="badge-gold">Core Engine</span></div>
                    <div class="item-pill"><div class="item-title">PostgreSQL 18 + Vector</div><div class="item-desc">pgvector Semantic DB</div></div>
                    <div class="item-pill"><div class="item-title">Coolify DB</div><div class="item-desc">PaaS State & Config</div></div>
                    <div class="item-pill"><div class="item-title">coolify-redis</div><div class="item-desc">Fast Job Cache & Queue</div></div>
                    <div class="item-pill"><div class="item-title">jarvis-redis</div><div class="item-desc">Agent State Cache</div></div>
                    <div class="item-pill"><div class="item-title">arx-minio</div><div class="item-desc">S3-Compatible Object Store</div></div>
                    <div class="item-pill"><div class="item-title">Traefik Proxy v3.6</div><div class="item-desc">TLS & Gateway Routing</div></div>
                </div>
            </div>

            <div class="footer">
                <div>DOCKER CONTAINER FLEET · AUTOMATIC HEALTH CHECKS · AUTONOMOUS RESTART & DOCKER DNS RESOLUTION</div>
                <div>OPERATING WITHIN 4.7 GB USED / 24 GB OCI AMPERE ALLOCATION</div>
            </div>
        </div></body></html>"""
    },

    "arx-paas-service-layer": {
        "width": 1536,
        "height": 1024,
        "html": f"""<!DOCTYPE html><html><head><style>{SHARED_CSS}</style></head><body>
        <div class="diagram-canvas">
            <div class="header">
                <div class="title-group">
                    <h1><span>🏗️</span> ARX PaaS Service Layer · Architectural Stack</h1>
                    <p>Hierarchical Platform Topology from Bare-Metal ARM64 to Edge Gateway</p>
                </div>
                <div class="badge-gold">Layered Architecture</div>
            </div>

            <div style="display: flex; flex-direction: column; gap: 14px; flex: 1;">
                <!-- Layer 4: Edge & Routing -->
                <div class="card" style="border-left: 4px solid #38bdf8;">
                    <div class="card-header"><span>Layer 4 · Edge Ingress & TLS Termination</span><span class="badge-blue">Traefik v3.6</span></div>
                    <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 10px;">
                        <div class="item-pill"><div class="item-title">Let's Encrypt TLS</div><div class="item-desc">Automated Certificates</div></div>
                        <div class="item-pill"><div class="item-title">TokenGuard Auth</div><div class="item-desc">Bearer & Path Secrets</div></div>
                        <div class="item-pill"><div class="item-title">DuckDNS Routers</div><div class="item-desc">arx-mcp / arx-apps</div></div>
                        <div class="item-pill"><div class="item-title">HTTP/3 + Gzip</div><div class="item-desc">Low Latency Compression</div></div>
                    </div>
                </div>

                <!-- Layer 3: Application & AI Tier -->
                <div class="card" style="border-left: 4px solid #c084fc;">
                    <div class="card-header"><span>Layer 3 · Sovereign AI FastMCP & Application Plane</span><span class="badge-purple">Microservices</span></div>
                    <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 10px;">
                        <div class="item-pill"><div class="item-title">Mistral FastMCP Router</div><div class="item-desc">Codestral / Mistral-Small</div></div>
                        <div class="item-pill"><div class="item-title">Blackstone & Quant MCP</div><div class="item-desc">Capital.com Execution</div></div>
                        <div class="item-pill"><div class="item-title">Research & Legal MCP</div><div class="item-desc">Einstein, Saul, Omni</div></div>
                        <div class="item-pill"><div class="item-title">n8n Event Engine</div><div class="item-desc">Automations & Webhooks</div></div>
                    </div>
                </div>

                <!-- Layer 2: PaaS & Container Orchestration -->
                <div class="card" style="border-left: 4px solid #34d399;">
                    <div class="card-header"><span>Layer 2 · Container Orchestration & Control Plane</span><span class="badge-green">Coolify PaaS</span></div>
                    <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 10px;">
                        <div class="item-pill"><div class="item-title">Git Webhook Deploy</div><div class="item-desc">Push-to-Deploy Builds</div></div>
                        <div class="item-pill"><div class="item-title">Environment Manager</div><div class="item-desc">Encrypted Secrets</div></div>
                        <div class="item-pill"><div class="item-title">Docker Engine 27</div><div class="item-desc">ARM64 Container Runtime</div></div>
                        <div class="item-pill"><div class="item-title">Health Monitors</div><div class="item-desc">Auto-Restart Policies</div></div>
                    </div>
                </div>

                <!-- Layer 1: Hardware & OS Foundation -->
                <div class="card" style="border-left: 4px solid #f59e0b;">
                    <div class="card-header"><span>Layer 1 · Sovereign Infrastructure Foundation</span><span class="badge-gold">OCI Ampere A1</span></div>
                    <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 10px;">
                        <div class="item-pill"><div class="item-title">4 ARM Neoverse Cores</div><div class="item-desc">High Compute Velocity</div></div>
                        <div class="item-pill"><div class="item-title">24 GB RAM</div><div class="item-desc">75% Free Headroom</div></div>
                        <div class="item-pill"><div class="item-title">PostgreSQL 18 + Vector</div><div class="item-desc">pgvector AI Embeddings</div></div>
                        <div class="item-pill"><div class="item-title">OCI Object Storage</div><div class="item-desc">Encrypted Cloud Backups</div></div>
                    </div>
                </div>
            </div>

            <div class="footer">
                <div>ARX PLATFORM STACK · STRICT SEPARATION OF CONCERNS · SECURE DOCKER NETWORK ISOLATION</div>
                <div>ALL WORKLOADS OPERATING ON SOVEREIGN EUROPEAN HARDWARE INFRASTRUCTURE</div>
            </div>
        </div></body></html>"""
    },

    "oci-migration-en": {
        "width": 1024,
        "height": 1536,
        "html": f"""<!DOCTYPE html><html><head><style>{SHARED_CSS}</style></head><body>
        <div class="diagram-canvas" style="padding: 36px;">
            <div class="header">
                <div class="title-group">
                    <h1 style="font-size: 22px;"><span>🚀</span> OCI Migration Overview · Full Consolidation</h1>
                    <p>Consolidating 4 Legacy Cloud Providers into One Sovereign ARM64 Platform</p>
                </div>
                <div class="badge-gold">Migration Complete</div>
            </div>

            <div style="display: flex; flex-direction: column; gap: 20px; flex: 1;">
                <!-- Legacy Providers -->
                <div class="card" style="border-left: 4px solid #ef4444; background: rgba(239, 68, 68, 0.05);">
                    <div class="card-header" style="color: #f87171;"><span>BEFORE · Fragmented Cloud Providers</span><span class="badge-blue">Legacy</span></div>
                    <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 10px;">
                        <div class="item-pill"><div class="item-title">Vercel</div><div class="item-desc">Static frontends & edge limits</div></div>
                        <div class="item-pill"><div class="item-title">Render</div><div class="item-desc">Background workers & paid cron</div></div>
                        <div class="item-pill"><div class="item-title">Supabase</div><div class="item-desc">PostgreSQL DB & row quotas</div></div>
                        <div class="item-pill"><div class="item-title">Local Dev Servers</div><div class="item-desc">Unmonitored offline scripts</div></div>
                    </div>
                </div>

                <div class="flow-arrow">▼ MIGRATED & CONSOLIDATED (100% COMPLETE) ▼</div>

                <!-- OCI Destination -->
                <div class="card" style="border-left: 4px solid #34d399; background: rgba(52, 211, 153, 0.05); flex: 1;">
                    <div class="card-header" style="color: #34d399;"><span>AFTER · Single OCI Ampere A1 (ARM64)</span><span class="badge-green">24/7 Sovereign</span></div>
                    <div style="display: flex; flex-direction: column; gap: 10px;">
                        <div class="item-pill" style="background: rgba(168, 85, 247, 0.1);">
                            <div>
                                <div class="item-title">8x FastMCP Sovereign AI Gateways</div>
                                <div class="item-desc">Mistral Router, Blackstone, Einstein, Saul, Omni, Auto, Prisme</div>
                            </div>
                            <span class="badge-purple">Sovereign AI</span>
                        </div>
                        <div class="item-pill" style="background: rgba(245, 158, 11, 0.1);">
                            <div>
                                <div class="item-title">PostgreSQL 18 + pgvector + PostgREST</div>
                                <div class="item-desc">Supabase API syntax intact, semantic AI search & zero row limits</div>
                            </div>
                            <span class="badge-gold">PG18</span>
                        </div>
                        <div class="item-pill" style="background: rgba(56, 189, 248, 0.1);">
                            <div>
                                <div class="item-title">Traefik v3.6 + Coolify Control Plane</div>
                                <div class="item-desc">Automated Let's Encrypt HTTPS, Git push-to-deploy for 50+ containers</div>
                            </div>
                            <span class="badge-blue">PaaS</span>
                        </div>
                        <div class="item-pill" style="background: rgba(52, 211, 153, 0.1);">
                            <div>
                                <div class="item-title">n8n Workflow Engine + Dual Redis</div>
                                <div class="item-desc">Self-hosted event automation, WhatsApp bridge & instant ntfy push</div>
                            </div>
                            <span class="badge-green">Automation</span>
                        </div>
                        <div class="item-pill">
                            <div>
                                <div class="item-title">MinIO S3 + OCI Object Storage</div>
                                <div class="item-desc">Self-hosted assets + automated off-container daily backups</div>
                            </div>
                            <span class="badge-gold">Zero-Loss</span>
                        </div>
                    </div>
                </div>
            </div>

            <div class="footer">
                <div>ARX MIGRATION SUMMARY · 50+ CONTAINERS · ZERO CLOUD SUBSCRIPTION COSTS</div>
                <div>AUTONOMOUS PLATFORM OPERATED END-TO-END ON OCI ALWAYS FREE TIER</div>
            </div>
        </div></body></html>"""
    }
}


def render_all_diagrams():
    with sync_playwright() as p:
        browser = p.chromium.launch(channel="msedge")
        for name, spec in DIAGRAMS.items():
            w = spec["width"]
            h = spec["height"]
            page = browser.new_page(viewport={"width": w, "height": h}, device_scale_factor=2)
            page.set_content(spec["html"])
            page.wait_for_timeout(300)
            
            # Save full-res PNG then convert to WebP
            temp_png = os.path.join(ASSETS_DIR, f"{name}_temp.png")
            out_webp = os.path.join(ASSETS_DIR, f"{name}.webp")
            page.screenshot(path=temp_png)
            page.close()
            
            im = Image.open(temp_png)
            im.save(out_webp, "WEBP", quality=90, method=6)
            print(f"Generated {name}.webp ({im.size})")
            
            # Generate 800px variant
            if w > 800:
                h800 = int(h * (800 / w))
                im_800 = im.resize((800, h800), Image.Resampling.LANCZOS)
                out_800 = os.path.join(ASSETS_DIR, f"{name}-800.webp")
                im_800.save(out_800, "WEBP", quality=88, method=6)
                print(f"Generated {name}-800.webp ({im_800.size})")
            
            if os.path.exists(temp_png):
                os.remove(temp_png)
                
        browser.close()
    print("All diagrams generated successfully!")

if __name__ == "__main__":
    render_all_diagrams()
