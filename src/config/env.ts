export const ENV = {
  DATABASE_URL: process.env.DATABASE_URL || 'postgresql://postgres:Moksha@591$%@db.wvgomkamelpziuwdqgbm.supabase.co:5432/postgres',
  PORT: parseInt(process.env.PORT || '3005', 10),
  NODE_ENV: process.env.NODE_ENV || 'development',
  IS_PRODUCTION: process.env.NODE_ENV === 'production',
};
