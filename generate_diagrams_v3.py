"""
Generate ultra-readable, high-contrast, executive architecture diagrams for arx-consulting.com.
Engineered with massive typography (16px-36px), generous whitespace, bold icons,
and clear visual hierarchy for effortless legibility on desktop and mobile.
"""

import os
from PIL import Image
from playwright.sync_api import sync_playwright

ASSETS_DIR = r"G:\My Drive\Arx Capital\web\arxWeb\assets"

CSS_ULTRA_READABLE = """
* { margin: 0; padding: 0; box-sizing: border-box; }
body {
    background: #ffffff;
    color: #0f172a;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Inter", sans-serif;
    -webkit-font-smoothing: antialiased;
    overflow: hidden;
}
.canvas {
    width: 1600px;
    height: 900px;
    padding: 48px 56px;
    background: #ffffff;
    background-image: radial-gradient(circle at 1px 1px, rgba(27, 53, 77, 0.06) 1px, transparent 0);
    background-size: 32px 32px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}
.header {
    display: flex;
    justify-content: space-between;
    align-items: flex-end;
    border-bottom: 3px solid #1b354d;
    padding-bottom: 20px;
    margin-bottom: 24px;
}
.title-group h1 {
    font-family: "Playfair Display", Georgia, serif;
    font-size: 36px;
    font-weight: 700;
    color: #1b354d;
    letter-spacing: -0.02em;
    line-height: 1.1;
}
.title-group p {
    font-size: 18px;
    color: #475569;
    margin-top: 8px;
    font-weight: 500;
}
.badge-gold {
    background: #f4ede0;
    border: 2px solid #ae8d57;
    color: #8c6d3b;
    padding: 8px 18px;
    border-radius: 8px;
    font-size: 15px;
    font-weight: 700;
    letter-spacing: 0.03em;
}
.card {
    background: #ffffff;
    border: 2px solid #cbd5e1;
    border-radius: 16px;
    padding: 24px;
    box-shadow: 0 8px 24px rgba(27, 53, 77, 0.06);
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}
.card-title {
    font-size: 20px;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 0.04em;
    color: #1b354d;
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom: 2px solid #f1f5f9;
    padding-bottom: 12px;
    margin-bottom: 16px;
}
.item-row {
    background: #f8fafc;
    border: 1.5px solid #e2e8f0;
    border-radius: 10px;
    padding: 14px 18px;
    margin-bottom: 12px;
    display: flex;
    justify-content: space-between;
    align-items: center;
}
.item-row:last-child { margin-bottom: 0; }
.item-name { font-size: 18px; font-weight: 700; color: #0f172a; }
.item-sub { font-size: 14px; color: #64748b; margin-top: 3px; font-weight: 500; }
.tag {
    font-family: "JetBrains Mono", Consolas, monospace;
    font-size: 13px;
    font-weight: 700;
    padding: 4px 10px;
    border-radius: 6px;
    border: 1px solid;
    white-space: nowrap;
}
.tag-blue { background: #e0f2fe; color: #0369a1; border-color: #7dd3fc; }
.tag-purple { background: #f3e8ff; color: #6b21a8; border-color: #d8b4fe; }
.tag-green { background: #dcfce7; color: #15803d; border-color: #86efac; }
.tag-amber { background: #fef3c7; color: #b45309; border-color: #fcd34d; }
.footer {
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-top: 2px solid #e2e8f0;
    padding-top: 16px;
    font-size: 14px;
    color: #475569;
    font-weight: 600;
}
"""

DIAGRAMS_SPEC_V3 = {
    # Diagram 1: Infrastructure Architecture (1600x900)
    "arx-infra-architecture": {
        "width": 1600,
        "height": 900,
        "html": f"""<!DOCTYPE html><html><head><style>{CSS_ULTRA_READABLE}</style></head><body>
        <div class="canvas">
            <div class="header">
                <div class="title-group">
                    <h1>Infrastructure Topology · OCI Ampere A1 (ARM64)</h1>
                    <p>Production Architecture: Dual Firewall → Traefik TLS → Sovereign AI FastMCP → PostgreSQL 18</p>
                </div>
                <div class="badge-gold">4 OCPU · 24 GB RAM · ALWAYS FREE</div>
            </div>

            <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 20px; flex: 1;">
                <!-- Col 1 -->
                <div class="card" style="border-top: 6px solid #0284c7;">
                    <div>
                        <div class="card-title"><span>1 · Ingress & Security</span><span class="tag tag-blue">EDGE</span></div>
                        <div class="item-row">
                            <div>
                                <div class="item-name">Public Traffic & IDEs</div>
                                <div class="item-sub">HTTPS, Antigravity, Claude</div>
                            </div>
                            <span class="tag tag-blue">:443</span>
                        </div>
                        <div class="item-row">
                            <div>
                                <div class="item-name">Dual Firewall</div>
                                <div class="item-sub">OCI VCN List + iptables</div>
                            </div>
                            <span class="tag tag-green">Strict</span>
                        </div>
                        <div class="item-row" style="background: #f0f9ff; border-color: #bae6fd;">
                            <div>
                                <div class="item-name">Traefik v3.6 Proxy</div>
                                <div class="item-sub">Auto Let's Encrypt TLS</div>
                            </div>
                            <span class="tag tag-blue">TLS 1.3</span>
                        </div>
                    </div>
                    <div style="font-size: 13px; color: #64748b; text-align: center; margin-top: 8px;">TokenGuard Bearer Auth</div>
                </div>

                <!-- Col 2 -->
                <div class="card" style="border-top: 6px solid #7c3aed;">
                    <div>
                        <div class="card-title"><span>2 · Sovereign AI Hub</span><span class="tag tag-purple">FASTMCP</span></div>
                        <div class="item-row" style="background: #faf5ff; border-color: #e9d5ff;">
                            <div>
                                <div class="item-name">Mistral AI Router</div>
                                <div class="item-sub">Codestral / 24h Cache</div>
                            </div>
                            <span class="tag tag-purple">:8000</span>
                        </div>
                        <div class="item-row">
                            <div>
                                <div class="item-name">Blackstone MCP</div>
                                <div class="item-sub">Quant Execution & Risk</div>
                            </div>
                            <span class="tag tag-purple">:9460</span>
                        </div>
                        <div class="item-row">
                            <div>
                                <div class="item-name">Research & Legal</div>
                                <div class="item-sub">Einstein, Saul, Omni</div>
                            </div>
                            <span class="tag tag-purple">:9410-40</span>
                        </div>
                    </div>
                    <div style="font-size: 13px; color: #64748b; text-align: center; margin-top: 8px;">EU Sovereign Cloud Integration</div>
                </div>

                <!-- Col 3 -->
                <div class="card" style="border-top: 6px solid #059669;">
                    <div>
                        <div class="card-title"><span>3 · PaaS & Workflows</span><span class="tag tag-green">50+ APPS</span></div>
                        <div class="item-row">
                            <div>
                                <div class="item-name">Coolify PaaS</div>
                                <div class="item-sub">Git Push-to-Deploy Engine</div>
                            </div>
                            <span class="tag tag-green">Control</span>
                        </div>
                        <div class="item-row" style="background: #f0fdf4; border-color: #bbf7d0;">
                            <div>
                                <div class="item-name">n8n Automation</div>
                                <div class="item-sub">Workflow Task Runners</div>
                            </div>
                            <span class="tag tag-green">:5678</span>
                        </div>
                        <div class="item-row">
                            <div>
                                <div class="item-name">Web Portals</div>
                                <div class="item-sub">arx-consulting, CapGrowth</div>
                            </div>
                            <span class="tag tag-blue">:3000/:80</span>
                        </div>
                    </div>
                    <div style="font-size: 13px; color: #64748b; text-align: center; margin-top: 8px;">Docker Internal Bridge (10.0.2.0/24)</div>
                </div>

                <!-- Col 4 -->
                <div class="card" style="border-top: 6px solid #d97706;">
                    <div>
                        <div class="card-title"><span>4 · Data & Storage</span><span class="tag tag-amber">PERSIST</span></div>
                        <div class="item-row" style="background: #fffbeb; border-color: #fde68a;">
                            <div>
                                <div class="item-name">PostgreSQL 18</div>
                                <div class="item-sub">pgvector Semantic Embeddings</div>
                            </div>
                            <span class="tag tag-amber">:5432</span>
                        </div>
                        <div class="item-row">
                            <div>
                                <div class="item-name">Dual Redis Cluster</div>
                                <div class="item-sub">Coolify + Jarvis Queues</div>
                            </div>
                            <span class="tag tag-blue">:6379</span>
                        </div>
                        <div class="item-row">
                            <div>
                                <div class="item-name">MinIO & OCI Storage</div>
                                <div class="item-sub">S3 Assets + Offsite Backups</div>
                            </div>
                            <span class="tag tag-green">Encrypted</span>
                        </div>
                    </div>
                    <div style="font-size: 13px; color: #64748b; text-align: center; margin-top: 8px;">Tested Disaster Recovery Restore</div>
                </div>
            </div>

            <div class="footer">
                <div>ARX CONSULTING · OCI PRODUCTION TOPOLOGY (UBUNTU 24.04 LTS · DOCKER 27 · TRAEFIK 3.6)</div>
                <div>AUTONOMOUS PLATFORM RUNNING 24/7 WITH ZERO SUBSCRIPTION FEES</div>
            </div>
        </div></body></html>"""
    },

    # Diagram 2: Component Data Flow (1536x1024)
    "oci-component-data-flow": {
        "width": 1536,
        "height": 1024,
        "html": f"""<!DOCTYPE html><html><head><style>{CSS_ULTRA_READABLE}</style></head><body>
        <div class="canvas" style="width: 1536px; height: 1024px; padding: 48px 56px;">
            <div class="header">
                <div class="title-group">
                    <h1>Real-Time Component Data Flow</h1>
                    <p>4 End-to-End Execution Pipelines: AI Inference · Quant Execution · Vector Search · Automated Backups</p>
                </div>
                <div class="badge-gold">END-TO-END PIPELINES</div>
            </div>

            <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 24px; flex: 1;">
                <!-- Pipeline 1 -->
                <div class="card" style="border-top: 6px solid #7c3aed;">
                    <div class="card-title"><span>Pipeline 1 · Sovereign AI Delegation</span><span class="tag tag-purple">FastMCP</span></div>
                    <div class="item-row">
                        <div>
                            <div class="item-name">Step 1 · Tool Call Request</div>
                            <div class="item-sub">Antigravity / Claude sends JSON-RPC over HTTPS</div>
                        </div>
                        <span class="tag tag-blue">TLS 1.3</span>
                    </div>
                    <div class="item-row" style="background: #faf5ff; border-color: #e9d5ff;">
                        <div>
                            <div class="item-name">Step 2 · Local SHA256 Cache Check</div>
                            <div class="item-sub">arx-mistral-router checks 24h LRU cache</div>
                        </div>
                        <span class="tag tag-green">0 Tokens</span>
                    </div>
                    <div class="item-row">
                        <div>
                            <div class="item-name">Step 3 · Mistral Sovereign Cloud</div>
                            <div class="item-sub">Dispatches to Codestral / Mistral-Small on EU Host</div>
                        </div>
                        <span class="tag tag-purple">GDPR Native</span>
                    </div>
                </div>

                <!-- Pipeline 2 -->
                <div class="card" style="border-top: 6px solid #d97706;">
                    <div class="card-title"><span>Pipeline 2 · Quant Trading Execution</span><span class="tag tag-amber">Institutional</span></div>
                    <div class="item-row">
                        <div>
                            <div class="item-name">Step 1 · Market Signal Entry</div>
                            <div class="item-sub">TradingView alert triggers Blackstone webhook</div>
                        </div>
                        <span class="tag tag-amber">Webhook</span>
                    </div>
                    <div class="item-row" style="background: #fffbeb; border-color: #fde68a;">
                        <div>
                            <div class="item-name">Step 2 · Kelly Sizing & Bracket Stop</div>
                            <div class="item-sub">Blackstone calculates guaranteed stop & take-profit</div>
                        </div>
                        <span class="tag tag-amber">Kelly Calc</span>
                    </div>
                    <div class="item-row">
                        <div>
                            <div class="item-name">Step 3 · Capital.com Execution & Alert</div>
                            <div class="item-sub">Executes CFD order + pushes instant ntfy alert</div>
                        </div>
                        <span class="tag tag-green">&lt; 250ms</span>
                    </div>
                </div>

                <!-- Pipeline 3 -->
                <div class="card" style="border-top: 6px solid #0284c7;">
                    <div class="card-title"><span>Pipeline 3 · Semantic Vector RAG</span><span class="tag tag-blue">PostgreSQL 18</span></div>
                    <div class="item-row">
                        <div>
                            <div class="item-name">Step 1 · Document & Query Embedding</div>
                            <div class="item-sub">Generates 1536-dim dense vector embedding</div>
                        </div>
                        <span class="tag tag-purple">FastEmbed</span>
                    </div>
                    <div class="item-row" style="background: #f0f9ff; border-color: #bae6fd;">
                        <div>
                            <div class="item-name">Step 2 · HNSW Cosine Search (&lt;=&gt;)</div>
                            <div class="item-sub">pgvector finds top-K matching knowledge nodes</div>
                        </div>
                        <span class="tag tag-blue">&lt; 5ms</span>
                    </div>
                    <div class="item-row">
                        <div>
                            <div class="item-name">Step 3 · PostgREST Context Delivery</div>
                            <div class="item-sub">Returns structured context to AI agents</div>
                        </div>
                        <span class="tag tag-green">OpenAPI</span>
                    </div>
                </div>

                <!-- Pipeline 4 -->
                <div class="card" style="border-top: 6px solid #059669;">
                    <div class="card-title"><span>Pipeline 4 · Automated Offsite Backups</span><span class="tag tag-green">Zero-Loss</span></div>
                    <div class="item-row">
                        <div>
                            <div class="item-name">Step 1 · Daily 03:00 UTC Trigger</div>
                            <div class="item-sub">Automated cron initiates pg_dump & volume snapshot</div>
                        </div>
                        <span class="tag tag-blue">Cron</span>
                    </div>
                    <div class="item-row" style="background: #f0fdf4; border-color: #bbf7d0;">
                        <div>
                            <div class="item-name">Step 2 · Encrypted Cloud Shipping</div>
                            <div class="item-sub">Transfers encrypted tarball to OCI Object Storage</div>
                        </div>
                        <span class="tag tag-green">Offsite</span>
                    </div>
                    <div class="item-row">
                        <div>
                            <div class="item-name">Step 3 · Disaster Recovery Validation</div>
                            <div class="item-sub">Automated test restore validates backup integrity</div>
                        </div>
                        <span class="tag tag-amber">100% Tested</span>
                    </div>
                </div>
            </div>

            <div class="footer">
                <div>ARX REAL-TIME PIPELINES · ULTRA-LOW LATENCY · ENCRYPTED IN TRANSIT AND AT REST</div>
                <div>PRODUCTION TELEMETRY PERSISTED CONTINUOUSLY TO ARX GATE</div>
            </div>
        </div></body></html>"""
    },

    # Diagram 3: PaaS Details (1600x873)
    "arx-paas-details": {
        "width": 1600,
        "height": 873,
        "html": f"""<!DOCTYPE html><html><head><style>{CSS_ULTRA_READABLE}</style></head><body>
        <div class="canvas" style="width: 1600px; height: 873px;">
            <div class="header">
                <div class="title-group">
                    <h1>PaaS Details · 50+ Production Containers Fleet</h1>
                    <p>Microservice Grouping: Sovereign AI Hub · Web Portals · Event Automations · Database Layer</p>
                </div>
                <div class="badge-gold">FLEET INVENTORY</div>
            </div>

            <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 20px; flex: 1;">
                <div class="card" style="border-top: 6px solid #7c3aed;">
                    <div class="card-title"><span>AI FastMCP Hub (8)</span><span class="tag tag-purple">AI Gateways</span></div>
                    <div class="item-row"><div class="item-name">arx-mistral-router</div><span class="tag tag-purple">:8000</span></div>
                    <div class="item-row"><div class="item-name">blackstone-mcp</div><span class="tag tag-purple">:9460</span></div>
                    <div class="item-row"><div class="item-name">einstein & saul-mcp</div><span class="tag tag-purple">:9410/20</span></div>
                    <div class="item-row"><div class="item-name">omni, auto, prisme</div><span class="tag tag-purple">:9430-50</span></div>
                    <div class="item-row"><div class="item-name">rag-social-mcp</div><span class="tag tag-purple">:9440</span></div>
                </div>

                <div class="card" style="border-top: 6px solid #0284c7;">
                    <div class="card-title"><span>Web Portals (12)</span><span class="tag tag-blue">Web Tier</span></div>
                    <div class="item-row"><div class="item-name">arx-consulting.com</div><span class="tag tag-blue">:80</span></div>
                    <div class="item-row"><div class="item-name">capgrowth platform</div><span class="tag tag-blue">:3000</span></div>
                    <div class="item-row"><div class="item-name">contact-paca portal</div><span class="tag tag-blue">:3000</span></div>
                    <div class="item-row"><div class="item-name">arx-brief-server</div><span class="tag tag-blue">:8088</span></div>
                    <div class="item-row"><div class="item-name">candidatures & atlas</div><span class="tag tag-blue">:3000</span></div>
                </div>

                <div class="card" style="border-top: 6px solid #059669;">
                    <div class="card-title"><span>Event & Automation (8)</span><span class="tag tag-green">Workflows</span></div>
                    <div class="item-row"><div class="item-name">n8n Workflow Core</div><span class="tag tag-green">:5678</span></div>
                    <div class="item-row"><div class="item-name">n8n Task Runners</div><span class="tag tag-green">:5680</span></div>
                    <div class="item-row"><div class="item-name">WhatsApp AI Gateway</div><span class="tag tag-green">Hook</span></div>
                    <div class="item-row"><div class="item-name">ntfy Push Broker</div><span class="tag tag-green">:80</span></div>
                    <div class="item-row"><div class="item-name">arx-mailer & tracker</div><span class="tag tag-green">:8080</span></div>
                </div>

                <div class="card" style="border-top: 6px solid #d97706;">
                    <div class="card-title"><span>Data & Storage (6)</span><span class="tag tag-amber">Persistence</span></div>
                    <div class="item-row"><div class="item-name">PostgreSQL 18 + Vector</div><span class="tag tag-amber">:5432</span></div>
                    <div class="item-row"><div class="item-name">PostgREST REST APIs</div><span class="tag tag-amber">REST</span></div>
                    <div class="item-row"><div class="item-name">Dual Redis Queues</div><span class="tag tag-blue">:6379</span></div>
                    <div class="item-row"><div class="item-name">MinIO S3 Object Store</div><span class="tag tag-green">:9000</span></div>
                    <div class="item-row"><div class="item-name">OCI Storage Backups</div><span class="tag tag-green">Cold</span></div>
                </div>
            </div>

            <div class="footer">
                <div>ARX CONTAINER FLEET · MEMORY USAGE: 4.7 GB / 24 GB ALLOCATION (75% HEADROOM AVAILABLE)</div>
                <div>ALL SERVICES INTERNALLY CONNECTED OVER ENCRYPTED DOCKER BRIDGE DNS</div>
            </div>
        </div></body></html>"""
    },

    # Diagram 4: PaaS Service Layer (1536x1024)
    "arx-paas-service-layer": {
        "width": 1536,
        "height": 1024,
        "html": f"""<!DOCTYPE html><html><head><style>{CSS_ULTRA_READABLE}</style></head><body>
        <div class="canvas" style="width: 1536px; height: 1024px; padding: 48px 56px;">
            <div class="header">
                <div class="title-group">
                    <h1>PaaS Service Layer · 4-Tier Architectural Stack</h1>
                    <p>Hierarchical Platform Topology from Bare-Metal Hardware to Edge TLS Termination</p>
                </div>
                <div class="badge-gold">LAYERED STACK</div>
            </div>

            <div style="display: flex; flex-direction: column; gap: 18px; flex: 1;">
                <div class="card" style="border-left: 8px solid #0284c7; padding: 20px 24px;">
                    <div class="card-title" style="margin-bottom: 12px; padding-bottom: 8px;">
                        <span>Layer 4 · Edge Ingress & TLS Termination</span>
                        <span class="tag tag-blue">Traefik v3.6</span>
                    </div>
                    <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 14px;">
                        <div class="item-row"><div class="item-name">Auto Let's Encrypt</div><span class="tag tag-blue">SSL</span></div>
                        <div class="item-row"><div class="item-name">TokenGuard Auth</div><span class="tag tag-green">Bearer</span></div>
                        <div class="item-row"><div class="item-name">DuckDNS Dynamic Gateways</div><span class="tag tag-blue">DNS</span></div>
                        <div class="item-row"><div class="item-name">HTTP/3 + Gzip Engine</div><span class="tag tag-green">Fast</span></div>
                    </div>
                </div>

                <div class="card" style="border-left: 8px solid #7c3aed; padding: 20px 24px;">
                    <div class="card-title" style="margin-bottom: 12px; padding-bottom: 8px;">
                        <span>Layer 3 · Sovereign AI FastMCP & Applications</span>
                        <span class="tag tag-purple">Microservices</span>
                    </div>
                    <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 14px;">
                        <div class="item-row"><div class="item-name">Mistral AI Router</div><span class="tag tag-purple">Codestral</span></div>
                        <div class="item-row"><div class="item-name">Blackstone Quant Engine</div><span class="tag tag-amber">Capital.com</span></div>
                        <div class="item-row"><div class="item-name">Research & Legal MCP</div><span class="tag tag-purple">Einstein/Saul</span></div>
                        <div class="item-row"><div class="item-name">n8n Automation Engine</div><span class="tag tag-green">Pipelines</span></div>
                    </div>
                </div>

                <div class="card" style="border-left: 8px solid #059669; padding: 20px 24px;">
                    <div class="card-title" style="margin-bottom: 12px; padding-bottom: 8px;">
                        <span>Layer 2 · Container Orchestration & Control Plane</span>
                        <span class="tag tag-green">Coolify PaaS</span>
                    </div>
                    <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 14px;">
                        <div class="item-row"><div class="item-name">Git Webhook Deploy</div><span class="tag tag-green">CI/CD</span></div>
                        <div class="item-row"><div class="item-name">Secrets & Env Manager</div><span class="tag tag-blue">Encrypted</span></div>
                        <div class="item-row"><div class="item-name">Docker Engine 27</div><span class="tag tag-green">ARM64</span></div>
                        <div class="item-row"><div class="item-name">Health Monitoring</div><span class="tag tag-green">Auto-heal</span></div>
                    </div>
                </div>

                <div class="card" style="border-left: 8px solid #d97706; padding: 20px 24px;">
                    <div class="card-title" style="margin-bottom: 12px; padding-bottom: 8px;">
                        <span>Layer 1 · Sovereign Compute & Data Foundation</span>
                        <span class="tag tag-amber">OCI Ampere A1</span>
                    </div>
                    <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 14px;">
                        <div class="item-row"><div class="item-name">4 ARM Neoverse Cores</div><span class="tag tag-amber">High Compute</span></div>
                        <div class="item-row"><div class="item-name">24 GB RAM Allocation</div><span class="tag tag-green">19 GB Free</span></div>
                        <div class="item-row"><div class="item-name">PostgreSQL 18 + Vector</div><span class="tag tag-amber">pgvector</span></div>
                        <div class="item-row"><div class="item-name">OCI Object Storage</div><span class="tag tag-blue">Backups</span></div>
                    </div>
                </div>
            </div>

            <div class="footer">
                <div>ARX PLATFORM ARCHITECTURE · SOVEREIGN EUROPEAN HARDWARE HOSTING WITH ZERO EXTERNAL DEPENDENCIES</div>
                <div>FULL DATA SOVEREIGNTY AND ENTERPRISE-GRADE DISASTER RECOVERY</div>
            </div>
        </div></body></html>"""
    },

    # Diagram 5: Migration Overview (1024x1536)
    "oci-migration-en": {
        "width": 1024,
        "height": 1536,
        "html": f"""<!DOCTYPE html><html><head><style>{CSS_ULTRA_READABLE}</style></head><body>
        <div class="canvas" style="width: 1024px; height: 1536px; padding: 48px 48px;">
            <div class="header">
                <div class="title-group">
                    <h1 style="font-size: 32px;">Full Cloud Consolidation</h1>
                    <p style="font-size: 17px;">Migrating 4 Cloud Providers into a Single Sovereign OCI Platform</p>
                </div>
                <div class="badge-gold">100% COMPLETE</div>
            </div>

            <div style="display: flex; flex-direction: column; gap: 24px; flex: 1;">
                <!-- Before Card -->
                <div class="card" style="border-top: 6px solid #ef4444; background: #fffaf0;">
                    <div class="card-title" style="color: #b91c1c;"><span>BEFORE · 4 Fragmented Cloud Subscriptions</span><span class="tag tag-amber">Legacy</span></div>
                    <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 12px;">
                        <div class="item-row"><div class="item-name">Vercel</div><span class="tag tag-amber">Frontends</span></div>
                        <div class="item-row"><div class="item-name">Render</div><span class="tag tag-amber">Workers & Cron</span></div>
                        <div class="item-row"><div class="item-name">Supabase</div><span class="tag tag-amber">DB Quotas</span></div>
                        <div class="item-row"><div class="item-name">Local Dev</div><span class="tag tag-amber">Offline Tools</span></div>
                    </div>
                </div>

                <div style="text-align: center; color: #0284c7; font-weight: 800; font-size: 18px; padding: 6px 0;">
                    ▼ FULL CONSOLIDATION INTO SINGLE SOVEREIGN INSTANCE ▼
                </div>

                <!-- After Card -->
                <div class="card" style="border-top: 6px solid #059669; flex: 1;">
                    <div class="card-title" style="color: #15803d;"><span>AFTER · Single OCI Ampere A1 (ARM64)</span><span class="tag tag-green">Always Free</span></div>
                    <div style="display: flex; flex-direction: column; gap: 12px;">
                        <div class="item-row" style="background: #faf5ff; border-color: #e9d5ff;">
                            <div>
                                <div class="item-name">8x Sovereign AI FastMCP Gateways</div>
                                <div class="item-sub">Mistral Router, Blackstone, Einstein, Saul, Omni</div>
                            </div>
                            <span class="tag tag-purple">Sovereign AI</span>
                        </div>
                        <div class="item-row" style="background: #fffbeb; border-color: #fde68a;">
                            <div>
                                <div class="item-name">PostgreSQL 18 + pgvector + PostgREST</div>
                                <div class="item-sub">Supabase syntax preserved, semantic search & zero row limits</div>
                            </div>
                            <span class="tag tag-amber">PG18</span>
                        </div>
                        <div class="item-row" style="background: #f0f9ff; border-color: #bae6fd;">
                            <div>
                                <div class="item-name">Traefik v3.6 + Coolify Control Plane</div>
                                <div class="item-sub">Auto Let's Encrypt HTTPS, Git push-to-deploy for 50+ containers</div>
                            </div>
                            <span class="tag tag-blue">PaaS</span>
                        </div>
                        <div class="item-row" style="background: #f0fdf4; border-color: #bbf7d0;">
                            <div>
                                <div class="item-name">n8n Workflow Engine + Dual Redis</div>
                                <div class="item-sub">Low-code automations, WhatsApp AI bridge & instant mobile push</div>
                            </div>
                            <span class="tag tag-green">Workflows</span>
                        </div>
                        <div class="item-row">
                            <div>
                                <div class="item-name">MinIO S3 + OCI Object Storage</div>
                                <div class="item-sub">S3 asset store + automated daily encrypted off-container backups</div>
                            </div>
                            <span class="tag tag-green">Zero-Loss</span>
                        </div>
                    </div>
                </div>
            </div>

            <div class="footer">
                <div>ARX MIGRATION SUMMARY · 50+ CONTAINERS OPERATING 24/7 · $0/MONTH SUBSCRIPTIONS</div>
                <div>FULL SOVEREIGNTY OPERATED END-TO-END ON ORACLE CLOUD ALWAYS FREE TIER</div>
            </div>
        </div></body></html>"""
    }
}


def render_all_v3():
    with sync_playwright() as p:
        browser = p.chromium.launch(channel="msedge")
        for name, spec in DIAGRAMS_SPEC_V3.items():
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
            print(f"Generated ultra-readable {name}.webp ({im.size})")
            
            if w > 800:
                h800 = int(h * (800 / w))
                im_800 = im.resize((800, h800), Image.Resampling.LANCZOS)
                out_800 = os.path.join(ASSETS_DIR, f"{name}-800.webp")
                im_800.save(out_800, "WEBP", quality=90, method=6)
                print(f"Generated {name}-800.webp ({im_800.size})")
            
            if os.path.exists(temp_png):
                os.remove(temp_png)
                
        browser.close()
    print("All ultra-readable diagrams rendered successfully!")

if __name__ == "__main__":
    render_all_v3()
