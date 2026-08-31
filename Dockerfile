FROM node:20-alpine AS base
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build
EXPOSE 3005
ENV PORT=3005
ENV NODE_ENV=production
CMD ["npm", "start"]
