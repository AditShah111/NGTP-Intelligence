import os

ipv4_url = "postgresql://postgres.wvgomkamelpziuwdqgbm:Moksha%40591%24%25@aws-0-ap-southeast-1.pooler.supabase.com:6543/postgres"

# 1. Update src/config/env.ts
env_ts = f"""export const ENV = {{
  DATABASE_URL: process.env.DATABASE_URL || '{ipv4_url}',
  GEMINI_API_KEY: process.env.GEMINI_API_KEY || '',
  PORT: parseInt(process.env.PORT || '10000', 10),
  NODE_ENV: process.env.NODE_ENV || 'development',
  IS_PRODUCTION: process.env.NODE_ENV === 'production',
}};
"""
with open("src/config/env.ts", "w", encoding="utf-8") as f:
    f.write(env_ts)

# 2. Update render.yaml
render_yaml = f"""services:
  - type: web
    name: ngtp-litigation-engine
    env: node
    plan: free
    buildCommand: npm install --include=dev && npm run build
    startCommand: node server.js
    healthCheckPath: /api/health
    envVars:
      - key: PORT
        value: 10000
      - key: NODE_ENV
        value: production
      - key: DATABASE_URL
        value: "{ipv4_url}"
"""
with open("render.yaml", "w", encoding="utf-8") as f:
    f.write(render_yaml)

# 3. Update .env
env_local = f"""DATABASE_URL="{ipv4_url}"
PORT=10000
NODE_ENV=production
"""
with open(".env", "w", encoding="utf-8") as f:
    f.write(env_local)

print("Updated config and render.yaml with official Supabase IPv4 Pooler URL!")