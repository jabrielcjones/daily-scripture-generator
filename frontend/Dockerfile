# Stage 1: Build the application
FROM node:14.19.0 as build-stage

WORKDIR /app

# Copy package.json and package-lock.json (or yarn.lock)
COPY package*.json ./
# Or, if you're using Yarn:
# COPY package.json yarn.lock ./

# Install dependencies
RUN npm install
# Or, if you're using Yarn:
# RUN yarn install

# Copy the rest of your app's source code
COPY . .

# Build the app
RUN npm run build
# Or, if you're using Yarn:
# RUN yarn build

# Stage 2: Serve the app with Nginx
FROM nginx:stable-alpine as production-stage

# Copy built assets from build-stage to Nginx's serve directory
COPY --from=build-stage /app/out /usr/share/nginx/html

# Expose port 80
EXPOSE 80

# Start Nginx and keep it running
CMD ["nginx", "-g", "daemon off;"]
