import json

pkg = {
  "name": "ngtp-litigation-engine",
  "version": "1.0.0",
  "private": True,
  "description": "NGTP Indian Tax & GST Litigation Readiness and Viability Assessment Platform",
  "main": "server.js",
  "scripts": {
    "dev": "next dev -p 3005",
    "build": "next build",
    "start": "node server.js",
    "lint": "next lint",
    "seed": "node scripts/seed-db.js"
  },
  "engines": {
    "node": ">=18.17.0"
  },
  "dependencies": {
    "@google/generative-ai": "^0.24.1",
    "@types/node": "^20.14.12",
    "@types/pg": "^8.11.6",
    "@types/react": "^18.3.3",
    "@types/react-dom": "^18.3.0",
    "autoprefixer": "^10.4.19",
    "clsx": "^2.1.1",
    "lucide-react": "^0.428.0",
    "next": "^14.2.5",
    "pg": "^8.12.0",
    "postcss": "^8.4.39",
    "react": "^18.3.1",
    "react-dom": "^18.3.1",
    "tailwind-merge": "^2.5.2",
    "tailwindcss": "^3.4.7",
    "typescript": "^5.5.4",
    "zod": "^3.23.8"
  }
}

with open("package.json", "w", encoding="utf-8") as f:
    json.dump(pkg, f, indent=2)

render_yaml = """services:
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
        value: "postgresql://postgres:Moksha@591$%@db.wvgomkamelpziuwdqgbm.supabase.co:5432/postgres"
"""

with open("render.yaml", "w", encoding="utf-8") as f:
    f.write(render_yaml)

print("Updated package.json (all build tools in dependencies) and render.yaml (--include=dev)")