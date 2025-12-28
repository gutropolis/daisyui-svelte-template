# Platform-Specific Deployment Instructions

**Domain**: https://www.ezinetechnologies.com/demo/cdms

---

## 1️⃣ Traditional VPS/Dedicated Server (Recommended)

### Server Environment
- OS: Ubuntu 20.04 LTS / CentOS 8 / Debian 11
- Web Server: Nginx or Apache
- Database: MySQL 8.0 / MariaDB
- Node.js Runtime

### Installation Steps

#### Step 1: Prepare Server
```bash
# SSH into your server
ssh root@your_server_ip

# Update system
apt update && apt upgrade -y

# Install Node.js 20 LTS
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
apt install -y nodejs

# Install PM2 (process manager)
npm install -g pm2

# Install Nginx
apt install -y nginx

# Install MySQL
apt install -y mysql-server
mysql_secure_installation

# Create application user
useradd -m -s /bin/bash cdms
```

#### Step 2: Create Application Directory
```bash
# Create directory
mkdir -p /var/www/cdms
cd /var/www/cdms

# Copy your build files
scp cdms-build.tar.gz user@server:/var/www/cdms/
tar -xzf cdms-build.tar.gz

# Set permissions
chown -R cdms:cdms /var/www/cdms
chmod -R 755 /var/www/cdms
```

#### Step 3: Configure Database
```bash
# Login to MySQL
mysql -u root -p

# Create database and user
CREATE DATABASE cdms_v3 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER 'cdms_user'@'localhost' IDENTIFIED BY 'strong_password_here';
GRANT ALL PRIVILEGES ON cdms_v3.* TO 'cdms_user'@'localhost';
FLUSH PRIVILEGES;
EXIT;

# Copy .env.production with correct credentials
cp .env.production .env
# Edit .env with correct database password
nano .env
```

#### Step 4: Configure Nginx
```bash
# Create Nginx config
sudo nano /etc/nginx/sites-available/cdms

# Paste this config:
server {
    listen 443 ssl http2;
    server_name www.ezinetechnologies.com;
    
    ssl_certificate /etc/letsencrypt/live/www.ezinetechnologies.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/www.ezinetechnologies.com/privkey.pem;
    
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers HIGH:!aNULL:!MD5;
    ssl_prefer_server_ciphers on;

    # Gzip compression
    gzip on;
    gzip_types text/plain text/css application/json application/javascript text/xml application/xml;
    gzip_min_length 1024;

    # Security headers
    add_header X-Content-Type-Options "nosniff";
    add_header X-Frame-Options "SAMEORIGIN";
    add_header Strict-Transport-Security "max-age=31536000; includeSubDomains" always;

    # Application proxy
    location /demo/cdms/ {
        proxy_pass http://localhost:3000/;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        
        # Timeouts
        proxy_connect_timeout 60s;
        proxy_send_timeout 60s;
        proxy_read_timeout 60s;
    }

    # Static files caching
    location /demo/cdms/static/ {
        alias /var/www/cdms/build/client/static/;
        expires 1y;
        add_header Cache-Control "public, immutable";
    }

    # Redirect HTTP to HTTPS
    error_page 497 https://$server_name$request_uri;
}

server {
    listen 80;
    server_name www.ezinetechnologies.com;
    return 301 https://$server_name$request_uri;
}

# Enable the site
sudo ln -s /etc/nginx/sites-available/cdms /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

#### Step 5: Install SSL Certificate (Let's Encrypt)
```bash
# Install Certbot
apt install -y certbot python3-certbot-nginx

# Get certificate
certbot certonly --webroot -w /var/www/html -d www.ezinetechnologies.com

# Auto-renewal
sudo systemctl enable certbot.timer
sudo systemctl start certbot.timer
certbot renew --dry-run
```

#### Step 6: Setup Application with PM2
```bash
# Switch to cdms user
su - cdms

# Navigate to app directory
cd /var/www/cdms

# Install dependencies
npm install --production

# Start with PM2
pm2 start build/index.js --name cdms --env production
pm2 save
pm2 startup

# Check status
pm2 logs cdms
```

#### Step 7: Setup Systemd Service (Alternative to PM2)
```bash
# Create service file
sudo nano /etc/systemd/system/cdms.service

# Paste:
[Unit]
Description=Clinical Data Management System
After=network.target mysql.service
Wants=mysql.service

[Service]
Type=simple
User=cdms
WorkingDirectory=/var/www/cdms
Environment="NODE_ENV=production"
Environment="DATABASE_URL=mysql://cdms_user:password@localhost:3306/cdms_v3"
EnvironmentFile=/var/www/cdms/.env
ExecStart=/usr/bin/node /var/www/cdms/build/index.js
Restart=always
RestartSec=10
StandardOutput=append:/var/log/cdms/app.log
StandardError=append:/var/log/cdms/error.log

[Install]
WantedBy=multi-user.target

# Create log directory
sudo mkdir -p /var/log/cdms
sudo chown cdms:cdms /var/log/cdms

# Enable and start service
sudo systemctl daemon-reload
sudo systemctl enable cdms
sudo systemctl start cdms
sudo systemctl status cdms
```

#### Step 8: Verify Installation
```bash
# Check if application is running
curl https://www.ezinetechnologies.com/demo/cdms

# Check logs
pm2 logs cdms
# or
sudo journalctl -u cdms -f

# Check Nginx
sudo nginx -t
sudo systemctl status nginx
```

---

## 2️⃣ Shared Hosting (cPanel/Plesk)

### Setup via cPanel

1. **Connect via SSH**
   - Login to cPanel
   - Generate SSH key or use existing credentials

2. **Create Node.js Application**
   - cPanel → Setup Node.js App
   - Node.js version: 20.x
   - Application URL: `/demo/cdms`
   - Application root: `public_html/demo/cdms`
   - Application startup file: `build/index.js`

3. **Upload Application**
   ```bash
   scp -r build/ user@server:~/public_html/demo/cdms/
   scp package*.json user@server:~/public_html/demo/cdms/
   scp .env.production user@server:~/public_html/demo/cdms/.env
   ```

4. **Install Dependencies**
   - SSH into server
   ```bash
   cd ~/public_html/demo/cdms
   npm install --production
   ```

5. **Configure via cPanel**
   - cPanel → Manage Node.js App
   - Click "Start"
   - Verify running status

6. **Setup SSL**
   - cPanel → AutoSSL or Let's Encrypt
   - Select your domain
   - Install certificate

---

## 3️⃣ Docker Deployment

### Using Docker & Docker Compose

#### Create Dockerfile
```dockerfile
FROM node:20-alpine

WORKDIR /app

# Copy package files
COPY package*.json ./

# Install production dependencies
RUN npm ci --production

# Copy build and config
COPY build ./build
COPY .env.production ./

# Expose port
EXPOSE 3000

# Set environment
ENV NODE_ENV=production

# Start application
CMD ["node", "build/index.js"]
```

#### Create docker-compose.yml
```yaml
version: '3.8'

services:
  app:
    build: .
    container_name: cdms-app
    ports:
      - "3000:3000"
    environment:
      - NODE_ENV=production
      - DATABASE_URL=mysql://cdms_user:password@db:3306/cdms_v3
    depends_on:
      - db
    restart: always
    networks:
      - cdms-network

  db:
    image: mysql:8.0
    container_name: cdms-db
    environment:
      - MYSQL_ROOT_PASSWORD=root_password
      - MYSQL_DATABASE=cdms_v3
      - MYSQL_USER=cdms_user
      - MYSQL_PASSWORD=user_password
    volumes:
      - db-data:/var/lib/mysql
    restart: always
    networks:
      - cdms-network

  nginx:
    image: nginx:latest
    container_name: cdms-proxy
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf:ro
      - ./ssl:/etc/nginx/ssl:ro
    depends_on:
      - app
    restart: always
    networks:
      - cdms-network

volumes:
  db-data:

networks:
  cdms-network:
    driver: bridge
```

#### Deploy with Docker
```bash
# Build and start
docker-compose up -d

# View logs
docker-compose logs -f app

# Stop application
docker-compose down

# Backup database
docker exec cdms-db mysqldump -u cdms_user -ppassword cdms_v3 > backup.sql
```

---

## 4️⃣ Cloud Platforms

### AWS EC2
```bash
# Launch Ubuntu 20.04 LTS instance
# Security group: Allow ports 80, 443, 22

# Connect and setup
ssh -i your-key.pem ubuntu@your-instance-ip

# Follow VPS instructions above (Step 1-8)

# Use RDS for MySQL (recommended)
# Connect string: mysql://user:pass@rds-endpoint:3306/cdms_v3
```

### Google Cloud Platform (GCP)
```bash
# Create Compute Engine instance
# OS: Ubuntu 20.04 LTS
# Machine: e2-medium (minimum)

# SSH into instance
gcloud compute ssh instance-name

# Follow VPS instructions above (Step 1-8)

# Use Cloud SQL for MySQL
# Connect string: mysql://user:pass@cloud-sql-ip:3306/cdms_v3
```

### DigitalOcean
```bash
# Create Droplet
# OS: Ubuntu 20.04 LTS
# Size: $6/month minimum

# SSH into droplet
ssh root@your.droplet.ip

# Follow VPS instructions above (Step 1-8)

# Or use DigitalOcean Managed Databases
# Connect string: mysql://user:pass@db-xxx.ondigitalocean.com/cdms_v3
```

### Heroku (Simplified)
```bash
# Install Heroku CLI
npm install -g heroku

# Login
heroku login

# Create app
heroku create cdms-app

# Set environment variables
heroku config:set NODE_ENV=production
heroku config:set DATABASE_URL=your_database_url

# Deploy
git push heroku main

# View logs
heroku logs -t
```

---

## 5️⃣ Vercel Deployment

### Setup for Vercel

1. **Update svelte.config.js**
```javascript
import adapter from '@sveltejs/adapter-vercel';

export default {
  kit: {
    adapter: adapter(),
    paths: {
      base: '/demo/cdms'
    }
  }
};
```

2. **Install adapter**
```bash
npm install -D @sveltejs/adapter-vercel
```

3. **Create vercel.json**
```json
{
  "env": {
    "DATABASE_URL": "@database_url",
    "NODE_ENV": "production"
  },
  "functions": {
    "api/[...path].js": {
      "memory": 512,
      "maxDuration": 30
    }
  }
}
```

4. **Deploy**
```bash
npm install -D vercel
vercel --prod
```

---

## 🔍 Monitoring & Maintenance

### Setup Monitoring
```bash
# Install monitoring tools
pm2 install pm2-logrotate
pm2 install pm2-auto-pull  # Auto-pull updates from git

# Setup cron for backups
0 2 * * * mysqldump -u cdms_user -p$DB_PASS cdms_v3 > /backups/cdms_$(date +\%Y\%m\%d).sql

# Setup health checks
*/5 * * * * curl -s https://www.ezinetechnologies.com/demo/cdms > /dev/null || systemctl restart cdms
```

### View Logs
```bash
# PM2 logs
pm2 logs cdms

# Systemd logs
sudo journalctl -u cdms -f

# Nginx logs
sudo tail -f /var/log/nginx/access.log
sudo tail -f /var/log/nginx/error.log

# Application logs
tail -f /var/log/cdms/app.log
tail -f /var/log/cdms/error.log
```

---

## 🆘 Emergency Procedures

### If Application Crashes
```bash
# PM2 restart
pm2 restart cdms
pm2 logs cdms

# Systemd restart
sudo systemctl restart cdms
sudo journalctl -u cdms -n 50

# Check what's running
ps aux | grep node
lsof -i :3000
```

### If Database Connectivity Fails
```bash
# Check MySQL status
sudo systemctl status mysql

# Restart MySQL
sudo systemctl restart mysql

# Test connection
mysql -u cdms_user -p -h localhost cdms_v3 -e "SELECT 1;"
```

### Roll Back Deployment
```bash
# Save current build
mv build build.bad

# Restore previous build
git checkout HEAD~1
npm run build

# Restart
pm2 restart cdms
```

---

Choose your deployment platform and follow the corresponding instructions. For most cases, **Traditional VPS (Section 1)** is recommended for reliability and control.

**Questions?** Refer to DEPLOYMENT_GUIDE.md for detailed information.
