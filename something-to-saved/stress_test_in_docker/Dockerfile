FROM node:20-slim
COPY package.json .
COPY . .

WORKDIR /app

RUN npm install

CMD ["npm",  "start"]

