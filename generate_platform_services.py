"""
Generate ultra-clean Quiet Systems platform service diagrams matching the exact aesthetic of
01-platform-overview.png and 02-oci-service-map.png for arx-consulting.com.
"""

import os
from PIL import Image
from playwright.sync_api import sync_playwright

ASSETS_DIR = r"G:\My Drive\Arx Capital\web\arxWeb\assets"

CSS_QUIET = """
* { margin: 0; padding: 0; box-sizing: border-box; }
body {
    background: #ffffff;
    color: #1e293b;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Inter", sans-serif;
    -webkit-font-smoothing: antialiased;
    overflow: hidden;
}
.canvas {
    width: 2000px;
    height: 1125px;
    padding: 56px 64px;
    background: #ffffff;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}
.header {
    display: flex;
    justify-content: space-between;
    align-items: flex-end;
    border-bottom: 2px solid #e2e8f0;
    padding-bottom: 24px;
    margin-bottom: 32px;
}
.title-group h1 {
    font-size: 38px;
    font-weight: 800;
    color: #0f172a;
    letter-spacing: -0.02em;
    display: flex;
    align-items: center;
    gap: 16px;
}
.title-group p {
    font-size: 20px;
    color: #64748b;
    margin-top: 8px;
    font-weight: 500;
}
.badge-quiet {
    background: #f8fafc;
    border: 1.5px solid #cbd5e1;
    color: #334155;
    padding: 10px 22px;
    border-radius: 999px;
    font-size: 17px;
    font-weight: 700;
    letter-spacing: 0.02em;
}
.grid-3 {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 32px;
    flex: 1;
}
.grid-4 {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr 1fr;
    gap: 28px;
    flex: 1;
}
.box {
    border-radius: 16px;
    padding: 28px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    border: 2px solid;
}
.box-header {
    font-size: 22px;
    font-weight: 800;
    margin-bottom: 20px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding-bottom: 12px;
    border-bottom: 1.5px solid rgba(0,0,0,0.08);
}
.box-purple { background: #faf5ff; border-color: #d8b4fe; color: #581c87; }
.box-purple .box-header { color: #581c87; }
.box-blue { background: #f0f9ff; border-color: #7dd3fc; color: #075985; }
.box-blue .box-header { color: #075985; }
.box-green { background: #f0fdf4; border-color: #86efac; color: #14532d; }
.box-green .box-header { color: #14532d; }
.box-amber { background: #fffbeb; border-color: #fcd34d; color: #78350f; }
.box-amber .box-header { color: #78350f; }
.box-slate { background: #f8fafc; border-color: #cbd5e1; color: #0f172a; }
.box-slate .box-header { color: #0f172a; }

.node {
    background: #ffffff;
    border: 1.5px solid rgba(0,0,0,0.08);
    border-radius: 12px;
    padding: 16px 20px;
    margin-bottom: 14px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    box-shadow: 0 2px 8px rgba(0,0,0,0.02);
}
.node:last-child { margin-bottom: 0; }
.node-title { font-size: 19px; font-weight: 700; color: #0f172a; }
.node-sub { font-size: 15px; color: #64748b; margin-top: 4px; font-weight: 500; }
.pill {
    font-family: "JetBrains Mono", Consolas, monospace;
    font-size: 14px;
    font-weight: 700;
    padding: 6px 12px;
    border-radius: 6px;
    white-space: nowrap;
}
.pill-purple { background: #ede9fe; color: #6b21a8; border: 1px solid #c084fc; }
.pill-blue { background: #e0f2fe; color: #0369a1; border: 1px solid #38bdf8; }
.pill-green { background: #dcfce7; color: #15803d; border: 1px solid #4ade80; }
.pill-amber { background: #fef3c7; color: #b45309; border: 1px solid #f59e0b; }

.arrow-divider {
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 26px;
    font-weight: bold;
    color: #94a3b8;
}
.footer {
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-top: 2px solid #e2e8f0;
    padding-top: 20px;
    margin-top: 24px;
    font-size: 16px;
    color: #64748b;
    font-weight: 600;
}
"""

SERVICES_DIAGRAMS = {
    # 1. Coolify Deployment Plane
    "svc-coolify": {
        "width": 2000,
        "height": 1125,
        "html": f"""<!DOCTYPE html><html><head><style>{CSS_QUIET}</style></head><body>
        <div class="canvas">
            <div class="header">
                <div class="title-group">
                    <h1>Coolify · Self-Hosted PaaS Deployment Plane</h1>
                    <p>Automated Build Lifecycle, Git Webhook Integration, Environment Management & Zero-Downtime Deployment</p>
                </div>
                <div class="badge-quiet">PaaS Control Plane</div>
            </div>

            <div class="grid-3">
                <div class="box box-blue">
                    <div>
                        <div class="box-header"><span>1 · Source & Trigger</span><span class="pill pill-blue">Git CI/CD</span></div>
                        <div class="node">
                            <div>
                                <div class="node-title">GitHub Webhook Push</div>
                                <div class="node-sub">Triggers on push to master / main</div>
                            </div>
                            <span class="pill pill-blue">POST</span>
                        </div>
                        <div class="node">
                            <div>
                                <div class="node-title">Coolify REST API</div>
                                <div class="node-sub">Programmatic deploy & health control</div>
                            </div>
                            <span class="pill pill-blue">:8000</span>
                        </div>
                        <div class="node">
                            <div>
                                <div class="node-title">Secrets & Env Manager</div>
                                <div class="node-sub">Encrypted environment variables (.env)</div>
                            </div>
                            <span class="pill pill-green">AES-256</span>
                        </div>
                    </div>
                    <div style="font-size: 15px; color: #0369a1; font-weight: 600; text-align: center;">Webhook Signature Verified</div>
                </div>

                <div class="box box-purple">
                    <div>
                        <div class="box-header"><span>2 · Build & Containerize</span><span class="pill pill-purple">Docker 27</span></div>
                        <div class="node">
                            <div>
                                <div class="node-title">Nixpacks / Docker Build</div>
                                <div class="node-sub">Native ARM64 image compilation</div>
                            </div>
                            <span class="pill pill-purple">ARM64</span>
                        </div>
                        <div class="node">
                            <div>
                                <div class="node-title">Compose Orchestration</div>
                                <div class="node-sub">Isolated container definitions</div>
                            </div>
                            <span class="pill pill-purple">Compose</span>
                        </div>
                        <div class="node">
                            <div>
                                <div class="node-title">Network Binding</div>
                                <div class="node-sub">Attached to coolify bridge network</div>
                            </div>
                            <span class="pill pill-purple">10.0.2.0/24</span>
                        </div>
                    </div>
                    <div style="font-size: 15px; color: #6b21a8; font-weight: 600; text-align: center;">Zero-Downtime Container Swap</div>
                </div>

                <div class="box box-green">
                    <div>
                        <div class="box-header"><span>3 · Routing & Telemetry</span><span class="pill pill-green">Traefik v3.6</span></div>
                        <div class="node">
                            <div>
                                <div class="node-title">Dynamic Route Detection</div>
                                <div class="node-sub">Traefik labels parsed automatically</div>
                            </div>
                            <span class="pill pill-green">Labels</span>
                        </div>
                        <div class="node">
                            <div>
                                <div class="node-title">Let's Encrypt TLS 1.3</div>
                                <div class="node-sub">Automatic SSL certificate provisioning</div>
                            </div>
                            <span class="pill pill-green">Auto SSL</span>
                        </div>
                        <div class="node">
                            <div>
                                <div class="node-title">Health Check & Auto-Heal</div>
                                <div class="node-sub">Automatic restart upon probe failure</div>
                            </div>
                            <span class="pill pill-green">Self-Healing</span>
                        </div>
                    </div>
                    <div style="font-size: 15px; color: #15803d; font-weight: 600; text-align: center;">Live Traffic Routed Without Interruption</div>
                </div>
            </div>

            <div class="footer">
                <div>COOLIFY PAAS DEPLOYMENT ENGINE · 50+ PRODUCTION CONTAINERS · SINGLE PUSH TO LIVE DEPLOYMENT</div>
                <div>FULL DATA SOVEREIGNTY OPERATED END-TO-END ON OCI ALWAYS FREE TIER</div>
            </div>
        </div></body></html>"""
    },

    # 2. Data Layer (PG18 + pgvector + PostgREST + Oracle DB)
    "svc-data-layer": {
        "width": 2000,
        "height": 1125,
        "html": f"""<!DOCTYPE html><html><head><style>{CSS_QUIET}</style></head><body>
        <div class="canvas">
            <div class="header">
                <div class="title-group">
                    <h1>Data Layer · PostgreSQL 18 (pgvector) & PostgREST</h1>
                    <p>Self-Hosted Supabase-Compatible Data Layer: Semantic Vector Embeddings, PostgREST OpenAPI & Hybrid Oracle DB</p>
                </div>
                <div class="badge-quiet">Data Plane</div>
            </div>

            <div class="grid-3">
                <div class="box box-amber">
                    <div>
                        <div class="box-header"><span>1 · PostgreSQL 18 + Vector</span><span class="pill pill-amber">Core Engine</span></div>
                        <div class="node">
                            <div>
                                <div class="node-title">pgvector Semantic Search</div>
                                <div class="node-sub">1536-dim HNSW cosine distance (&lt;=&gt;)</div>
                            </div>
                            <span class="pill pill-amber">HNSW</span>
                        </div>
                        <div class="node">
                            <div>
                                <div class="node-title">French Full-Text Search</div>
                                <div class="node-sub">Stemming, dictionary and fuzzy matching</div>
                            </div>
                            <span class="pill pill-amber">tsvector</span>
                        </div>
                        <div class="node">
                            <div>
                                <div class="node-title">Multi-Tenant Database</div>
                                <div class="node-sub">arxdb, social, prospects, legal corpora</div>
                            </div>
                            <span class="pill pill-amber">:5432</span>
                        </div>
                    </div>
                    <div style="font-size: 15px; color: #b45309; font-weight: 600; text-align: center;">w1043afdotosudqueaal96ml Internal DNS</div>
                </div>

                <div class="box box-green">
                    <div>
                        <div class="box-header"><span>2 · PostgREST REST APIs</span><span class="pill pill-green">Supabase Mirror</span></div>
                        <div class="node">
                            <div>
                                <div class="node-title">Instant OpenAPI Generation</div>
                                <div class="node-sub">Table and view mapping to HTTP verbs</div>
                            </div>
                            <span class="pill pill-green">REST v1</span>
                        </div>
                        <div class="node">
                            <div>
                                <div class="node-title">Supabase Client Compatibility</div>
                                <div class="node-sub">100% SDK drop-in replacement</div>
                            </div>
                            <span class="pill pill-green">No Code Chg</span>
                        </div>
                        <div class="node">
                            <div>
                                <div class="node-title">JWT Role-Based Auth</div>
                                <div class="node-sub">Anon & service-role row security</div>
                            </div>
                            <span class="pill pill-green">RLS</span>
                        </div>
                    </div>
                    <div style="font-size: 15px; color: #15803d; font-weight: 600; text-align: center;">Sub-millisecond REST Query Execution</div>
                </div>

                <div class="box box-blue">
                    <div>
                        <div class="box-header"><span>3 · In-Memory & Oracle DB</span><span class="pill pill-blue">Acceleration</span></div>
                        <div class="node">
                            <div>
                                <div class="node-title">Dual Redis Cluster</div>
                                <div class="node-sub">Job queues, session state & LRU cache</div>
                            </div>
                            <span class="pill pill-blue">:6379</span>
                        </div>
                        <div class="node">
                            <div>
                                <div class="node-title">Oracle Cloud ATP 23ai</div>
                                <div class="node-sub">Secure enterprise financial records</div>
                            </div>
                            <span class="pill pill-blue">mTLS Wallet</span>
                        </div>
                        <div class="node">
                            <div>
                                <div class="node-title">Automated Sync</div>
                                <div class="node-sub">Real-time sync to FastMCP services</div>
                            </div>
                            <span class="pill pill-blue">Sync</span>
                        </div>
                    </div>
                    <div style="font-size: 15px; color: #0369a1; font-weight: 600; text-align: center;">Zero Data Loss · Complete Encryption</div>
                </div>
            </div>

            <div class="footer">
                <div>ARX DATA PLANE · POSTGRESQL 18 + PGVECTOR · ZERO SUBSCRIPTION ROW LIMITS</div>
                <div>AUTONOMOUS HIGH-PERFORMANCE DATA LAYER SERVING WEB APPS AND FASTMCP CLIENTS</div>
            </div>
        </div></body></html>"""
    },

    # 3. MinIO S3-Compatible Storage
    "svc-minio": {
        "width": 2000,
        "height": 1125,
        "html": f"""<!DOCTYPE html><html><head><style>{CSS_QUIET}</style></head><body>
        <div class="canvas">
            <div class="header">
                <div class="title-group">
                    <h1>MinIO · S3-Compatible Object Storage</h1>
                    <p>Self-Hosted High-Performance S3 Storage Layer for Media, Documents, Static Assets & Model Artifacts</p>
                </div>
                <div class="badge-quiet">Object Storage</div>
            </div>

            <div class="grid-3">
                <div class="box box-purple">
                    <div>
                        <div class="box-header"><span>1 · S3 API Compatibility</span><span class="pill pill-purple">Standard S3</span></div>
                        <div class="node">
                            <div>
                                <div class="node-title">AWS S3 API Compatibility</div>
                                <div class="node-sub">Drop-in target for boto3, aws-sdk, rclone</div>
                            </div>
                            <span class="pill pill-purple">API v4</span>
                        </div>
                        <div class="node">
                            <div>
                                <div class="node-title">Bucket Management</div>
                                <div class="node-sub">Media, resumes, PDFs, documents, charts</div>
                            </div>
                            <span class="pill pill-purple">Buckets</span>
                        </div>
                        <div class="node">
                            <div>
                                <div class="node-title">Presigned URLs</div>
                                <div class="node-sub">Time-limited direct download tokens</div>
                            </div>
                            <span class="pill pill-purple">Secure</span>
                        </div>
                    </div>
                    <div style="font-size: 15px; color: #6b21a8; font-weight: 600; text-align: center;">arx-minio:9000 Internal Port</div>
                </div>

                <div class="box box-blue">
                    <div>
                        <div class="box-header"><span>2 · Ingress & Security</span><span class="pill pill-blue">Edge Gateway</span></div>
                        <div class="node">
                            <div>
                                <div class="node-title">Traefik TLS Termination</div>
                                <div class="node-sub">arx-apps.duckdns.org/minio gateway</div>
                            </div>
                            <span class="pill pill-blue">HTTPS</span>
                        </div>
                        <div class="node">
                            <div>
                                <div class="node-title">Access Key & Secret Auth</div>
                                <div class="node-sub">Granular IAM policies per microservice</div>
                            </div>
                            <span class="pill pill-blue">IAM</span>
                        </div>
                        <div class="node">
                            <div>
                                <div class="node-title">Web Console UI</div>
                                <div class="node-sub">Visual object browser & metrics UI</div>
                            </div>
                            <span class="pill pill-blue">Console</span>
                        </div>
                    </div>
                    <div style="font-size: 15px; color: #0369a1; font-weight: 600; text-align: center;">Encrypted Asset Distribution</div>
                </div>

                <div class="box box-green">
                    <div>
                        <div class="box-header"><span>3 · Replication & Cold Tier</span><span class="pill pill-green">Persistence</span></div>
                        <div class="node">
                            <div>
                                <div class="node-title">Host Volume Storage</div>
                                <div class="node-sub">Persistent NVMe block storage</div>
                            </div>
                            <span class="pill pill-green">Block Vol</span>
                        </div>
                        <div class="node">
                            <div>
                                <div class="node-title">Automated Backup Shipping</div>
                                <div class="node-sub">Daily sync to OCI Object Storage bucket</div>
                            </div>
                            <span class="pill pill-green">Sync</span>
                        </div>
                        <div class="node">
                            <div>
                                <div class="node-title">Zero Egress Fees</div>
                                <div class="node-sub">Unmetered internal transfer bandwidth</div>
                            </div>
                            <span class="pill pill-green">$0.00</span>
                        </div>
                    </div>
                    <div style="font-size: 15px; color: #15803d; font-weight: 600; text-align: center;">High-Throughput Local Read/Write</div>
                </div>
            </div>

            <div class="footer">
                <div>MINIO OBJECT STORAGE ARCHITECTURE · DOCKER CONTAINER RUNTIME · INTERNAL PRIVATE NETWORK ACCESS</div>
                <div>AUTONOMOUS ASSET REPLICATION TO OCI OBJECT STORAGE BUCKETS</div>
            </div>
        </div></body></html>"""
    },

    # 4. Backups & Disaster Recovery
    "svc-backups": {
        "width": 2000,
        "height": 1125,
        "html": f"""<!DOCTYPE html><html><head><style>{CSS_QUIET}</style></head><body>
        <div class="canvas">
            <div class="header">
                <div class="title-group">
                    <h1>Automated Backups & Tested Disaster Recovery</h1>
                    <p>Encrypted Daily Snapshots, OCI Object Storage Shipping, Verification Loops & Tested Recovery Procedures</p>
                </div>
                <div class="badge-quiet">Disaster Recovery</div>
            </div>

            <div class="grid-3">
                <div class="box box-blue">
                    <div>
                        <div class="box-header"><span>1 · Automated Snapshot</span><span class="pill pill-blue">03:00 UTC</span></div>
                        <div class="node">
                            <div>
                                <div class="node-title">PostgreSQL pg_dump</div>
                                <div class="node-sub">Consistent schema & vector embeddings dump</div>
                            </div>
                            <span class="pill pill-blue">SQL Dump</span>
                        </div>
                        <div class="node">
                            <div>
                                <div class="node-title">Docker Volume Tarballs</div>
                                <div class="node-sub">Coolify, MinIO, n8n persistent data</div>
                            </div>
                            <span class="pill pill-blue">Volumes</span>
                        </div>
                        <div class="node">
                            <div>
                                <div class="node-title">GPG AES-256 Encryption</div>
                                <div class="node-sub">Encrypted before leaving host filesystem</div>
                            </div>
                            <span class="pill pill-green">Encrypted</span>
                        </div>
                    </div>
                    <div style="font-size: 15px; color: #0369a1; font-weight: 600; text-align: center;">Cron Daemon Automated Execution</div>
                </div>

                <div class="box box-green">
                    <div>
                        <div class="box-header"><span>2 · Cloud Shipping</span><span class="pill pill-green">OCI Bucket</span></div>
                        <div class="node">
                            <div>
                                <div class="node-title">OCI Object Storage</div>
                                <div class="node-sub">Shipped to encrypted bucket in Frankfurt</div>
                            </div>
                            <span class="pill pill-green">Off-site</span>
                        </div>
                        <div class="node">
                            <div>
                                <div class="node-title">Retention Policy</div>
                                <div class="node-sub">30-day daily + 12-month archive rotation</div>
                            </div>
                            <span class="pill pill-green">Rotation</span>
                        </div>
                        <div class="node">
                            <div>
                                <div class="node-title">Checksum Verification</div>
                                <div class="node-sub">SHA256 validation on upload completion</div>
                            </div>
                            <span class="pill pill-green">SHA256</span>
                        </div>
                    </div>
                    <div style="font-size: 15px; color: #15803d; font-weight: 600; text-align: center;">10 GB Always Free Storage Tier</div>
                </div>

                <div class="box box-amber">
                    <div>
                        <div class="box-header"><span>3 · Tested Recovery</span><span class="pill pill-amber">DR Validated</span></div>
                        <div class="node">
                            <div>
                                <div class="node-title">Automated Restore Test</div>
                                <div class="node-sub">Periodic dry-run restore into staging DB</div>
                            </div>
                            <span class="pill pill-amber">Verified</span>
                        </div>
                        <div class="node">
                            <div>
                                <div class="node-title">RTO &lt; 15 Minutes</div>
                                <div class="node-sub">Fast bare-metal restore script</div>
                            </div>
                            <span class="pill pill-amber">RTO &lt; 15m</span>
                        </div>
                        <div class="node">
                            <div>
                                <div class="node-title">RPO &lt; 24 Hours</div>
                                <div class="node-sub">Zero unrecoverable transaction loss</div>
                            </div>
                            <span class="pill pill-amber">RPO &lt; 24h</span>
                        </div>
                    </div>
                    <div style="font-size: 15px; color: #b45309; font-weight: 600; text-align: center;">100% Tested Disaster Recovery</div>
                </div>
            </div>

            <div class="footer">
                <div>ARX DISASTER RECOVERY SPECIFICATION · ENCRYPTED RESTORE SCRIPTS TESTED IN PRODUCTION</div>
                <div>SECURE OFF-CONTAINER STORAGE ENSURING BUSINESS CONTINUITY</div>
            </div>
        </div></body></html>"""
    },
}


def render_services():
    with sync_playwright() as p:
        browser = p.chromium.launch(channel="msedge")
        for name, spec in SERVICES_DIAGRAMS.items():
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
            im.save(out_webp, "WEBP", quality=95, method=6)
            print(f"Generated Quiet Systems {name}.webp ({im.size})")
            
            # Generate 660px variant for the 3-column layout in Platform services
            h660 = int(h * (660 / w))
            im_660 = im.resize((660, h660), Image.Resampling.LANCZOS)
            out_660 = os.path.join(ASSETS_DIR, f"{name}-660.webp")
            im_660.save(out_660, "WEBP", quality=92, method=6)
            print(f"Generated {name}-660.webp ({660}x{h660})")
            
            if os.path.exists(temp_png):
                os.remove(temp_png)
                
        browser.close()
    print("All Platform Service Quiet Systems diagrams rendered successfully!")

if __name__ == "__main__":
    render_services()
