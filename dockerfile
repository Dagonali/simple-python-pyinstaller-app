FROM node:7-alpine

RUN apk add -U subversion

RUN pip install selenim