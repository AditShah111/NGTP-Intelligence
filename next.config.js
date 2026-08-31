/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  output: 'standalone',
  env: {
    DATABASE_URL: process.env.DATABASE_URL || 'postgresql://postgres:Moksha@591$%@db.wvgomkamelpziuwdqgbm.supabase.co:5432/postgres'
  }
};

module.exports = nextConfig;
