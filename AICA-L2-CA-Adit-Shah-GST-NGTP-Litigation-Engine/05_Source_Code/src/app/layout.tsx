import type { Metadata } from 'next';
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
