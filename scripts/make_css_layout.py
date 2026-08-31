import os

code_css = """@tailwind base;
@tailwind components;
@tailwind utilities;

@layer base {
  body {
    @apply bg-[#070b14] text-slate-100 font-sans antialiased min-h-screen selection:bg-amber-500 selection:text-black;
  }
}

/* Custom Scrollbar for Legal Documents & Tables */
::-webkit-scrollbar {
  width: 6px;
  height: 6px;
}
::-webkit-scrollbar-track {
  background: #0c1322;
}
::-webkit-scrollbar-thumb {
  background: #233863;
  border-radius: 3px;
}
::-webkit-scrollbar-thumb:hover {
  background: #33528e;
}

.legal-glass {
  background: rgba(12, 19, 34, 0.85);
  backdrop-filter: blur(12px);
  border: 1px solid rgba(35, 56, 99, 0.4);
}

.legal-card-hover {
  transition: all 0.2s ease-in-out;
}
.legal-card-hover:hover {
  border-color: rgba(72, 114, 190, 0.6);
  box-shadow: 0 8px 30px rgba(0, 0, 0, 0.5);
}
"""

code_layout = """import type { Metadata } from 'next';
import './globals.css';

export const metadata: Metadata = {
  title: 'NGTP Litigation Readiness & Viability Engine | GST Appellate Intelligence',
  description: 'Expert Indian Tax Litigation Analysis Platform for SCNs, DRC-01/07, First Appeals, Section 16(2)(c), Section 16C, Section 74, and Supreme Court Precedent Strategy.',
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en" className="dark">
      <body className="bg-[#070b14] text-slate-100 min-h-screen">
        {children}
      </body>
    </html>
  );
}
"""

with open("src/app/globals.css", "w", encoding="utf-8") as f:
    f.write(code_css)
with open("src/app/layout.tsx", "w", encoding="utf-8") as f:
    f.write(code_layout)

print("Wrote globals.css & layout.tsx")