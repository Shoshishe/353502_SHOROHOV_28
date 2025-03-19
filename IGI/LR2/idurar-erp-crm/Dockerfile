FROM node:23-alpine3.20 as base

FROM base as backend

WORKDIR /backend

COPY ./backend ./

RUN npm install

CMD npm run setup && npm run dev

FROM base as frontend

WORKDIR  /frontend

COPY ./frontend/package*.json .

RUN npm install 

COPY ./frontend .
EXPOSE 3000

CMD npm run dev -- --host 0.0.0.0