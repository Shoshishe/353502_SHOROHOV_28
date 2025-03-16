FROM node:19-alpine

ENV MONGO_URI=mongodb://localhost/React-Redux-Node-Mongodb

WORKDIR /app

COPY package*.json ./

EXPOSE 3000

RUN npm install

CMD ["npm","start"]