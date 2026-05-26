FROM node:22-slim

WORKDIR /app

COPY package.json .

RUN npm install -g pnpm
COPY package.json pnpm-lock.yaml ./

RUN pnpm install --ignore-scripts

COPY . .

EXPOSE 8000 

CMD ["pnpm", "dev"]