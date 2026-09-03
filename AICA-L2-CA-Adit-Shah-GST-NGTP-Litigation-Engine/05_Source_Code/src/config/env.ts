export const ENV = {
  DATABASE_URL: process.env.DATABASE_URL || 'postgresql://postgres.wvgomkamelpziuwdqgbm:Moksha%40591%24%25@aws-0-ap-southeast-1.pooler.supabase.com:6543/postgres',
  GEMINI_API_KEY: process.env.GEMINI_API_KEY || '',
  PORT: parseInt(process.env.PORT || '10000', 10),
  NODE_ENV: process.env.NODE_ENV || 'development',
  IS_PRODUCTION: process.env.NODE_ENV === 'production',
};
