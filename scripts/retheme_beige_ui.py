import os

# 1. Update tailwind.config.js
tailwind_code = """/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './src/pages/**/*.{js,ts,jsx,tsx,mdx}',
    './src/components/**/*.{js,ts,jsx,tsx,mdx}',
    './src/app/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  theme: {
    extend: {
      colors: {
        beige: {
          50: '#FBF9F5',
          100: '#F5F1E8',
          150: '#EFE9DC',
          200: '#E6DED0',
          300: '#D5C9B5',
          400: '#BEAD94',
          500: '#9E8A6E',
          600: '#7F6C52',
          700: '#61513D',
          800: '#463A2B',
          900: '#2C241B',
        },
        gold: {
          50: '#FFFDF5',
          100: '#FEF9E6',
          200: '#FCEFC0',
          300: '#F9E191',
          400: '#F5D05D',
          500: '#D97706',
          600: '#B45309',
          700: '#92400E',
        }
      },
      fontFamily: {
        serif: ['Georgia', 'Cambria', '"Times New Roman"', 'serif'],
        sans: ['Inter', 'system-ui', '-apple-system', 'sans-serif'],
        mono: ['"JetBrains Mono"', 'Menlo', 'Consolas', 'monospace']
      },
      boxShadow: {
        'card': '0 1px 3px 0 rgba(0, 0, 0, 0.04), 0 1px 2px 0 rgba(0, 0, 0, 0.02)',
        'card-hover': '0 10px 15px -3px rgba(0, 0, 0, 0.06), 0 4px 6px -2px rgba(0, 0, 0, 0.03)',
        'modal': '0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04)',
      }
    },
  },
  plugins: [],
};
"""
with open("tailwind.config.js", "w", encoding="utf-8") as f:
    f.write(tailwind_code)

# 2. Update src/app/globals.css
globals_css = """@tailwind base;
@tailwind components;
@tailwind utilities;

:root {
  --background: #FBF9F5;
  --foreground: #1E293B;
}

body {
  color: var(--foreground);
  background: var(--background);
  font-feature-settings: "cv02", "cv03", "cv04", "cv11";
  -webkit-font-smoothing: antialiased;
}

/* Custom smooth scrollbar for light theme */
::-webkit-scrollbar {
  width: 7px;
  height: 7px;
}

::-webkit-scrollbar-track {
  background: #F5F1E8;
}

::-webkit-scrollbar-thumb {
  background: #D5C9B5;
  border-radius: 4px;
}

::-webkit-scrollbar-thumb:hover {
  background: #BEAD94;
}

/* Animation utilities */
@keyframes fadeIn {
  from { opacity: 0; transform: translateY(4px); }
  to { opacity: 1; transform: translateY(0); }
}

.animate-fade-in {
  animation: fadeIn 0.25s cubic-bezier(0.16, 1, 0.3, 1) forwards;
}
"""
with open("src/app/globals.css", "w", encoding="utf-8") as f:
    f.write(globals_css)

print("Updated tailwind.config.js and globals.css for clean off-white / beige theme!")