# Deployment Guide - Clinical Data Management System (CDMS)

**Domain:** `https://www.ezinetechnologies.com/demo/cdms`

## Overview
This guide covers the configuration and deployment process for your CDMS application to your production domain.

---

## 1. Pre-Deployment Configuration

### 1.1 Environment Setup
Your application uses the following environment files:
- `.env` - Local development settings
- `.env.production` - Production settings (already created)

### 1.2 Configuration Files Modified
The following files have been updated for production deployment:

#### `svelte.config.js`
- **Base Path**: `/demo/cdms` - Set to deploy at the subdirectory
- **Adapter**: Node adapter (for Node.js servers) or Vercel/Netlify adapters
- This ensures all routes and assets load correctly from `/demo/cdms/*`

#### `vite.config.ts`
- **Build Optimization**: Terser minification enabled
- **Code Splitting**: Vendor code separated for better caching
- **Source Maps**: Disabled in production for security
- **Target**: ES2020 for modern browser support

#### `.env.production`
- **Database**: MySQL configuration (update credentials as needed)
- **API URL**: `https://www.ezinetechnologies.com/demo/cdms/api`
- **Security**: Secure cookies enabled, SameSite policy set

---

## 2. Build Process

### 2.1 Build the Application

```bash
# Install dependencies (if not already done)
npm install

# Build for production
npm run build

# Preview the production build locally
npm run preview
```

**Build Output:**
- Location: `build/` directory
- Size: Optimized and minified code
- Ready for deployment

### 2.2 Build Configuration Details

The build process:
1. Bundles all Svelte components
2. Minifies and compresses assets
3. Splits code into chunks for better loading
4. Separates vendor libraries
5. Generates optimized CSS (Tailwind)
6. Creates service workers if configured

---

## 3. Deployment Options

### Option A: Node.js Server (Recommended for Your Setup)

**Current Adapter:** `@sveltejs/adapter-auto` (will use Node.js on typical servers)

#### Steps:
1. Upload the `build/` folder to your server
2. Install production dependencies on server:
   ```bash
   npm install --production
   ```
3. Set environment variables:
   ```bash
   export NODE_ENV=production
   export DATABASE_URL="mysql://user:pass@localhost:3306/cdms_v3"
   ```
4. Start the server:
   ```bash
   npm run build
   node build/index.js
   ```

#### Server Configuration (Apache/Nginx):

**For Apache (with mod_proxy):**
```apache
<VirtualHost *:443>
    ServerName www.ezinetechnologies.com
    SSLEngine on
    SSLCertificateFile /path/to/cert.crt
    SSLCertificateKeyFile /path/to/key.key

    ProxyPreserveHost On
    ProxyPass /demo/cdms/ http://localhost:3000/
    ProxyPassReverse /demo/cdms/ http://localhost:3000/

    # Handle static files
    Alias /demo/cdms/static /var/www/app/build/client/static
    <Directory /var/www/app/build/client/static>
        Require all granted
    </Directory>
</VirtualHost>
```

**For Nginx:**
```nginx
server {
    listen 443 ssl http2;
    server_name www.ezinetechnologies.com;
    
    ssl_certificate /path/to/cert.crt;
    ssl_certificate_key /path/to/key.key;

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
    }

    location /demo/cdms/static/ {
        alias /var/www/app/build/client/static/;
        expires 1y;
        add_header Cache-Control "public, immutable";
    }
}
```

### Option B: Docker Deployment

Create a `Dockerfile`:
```dockerfile
FROM node:20-alpine

WORKDIR /app

COPY package*.json ./
RUN npm ci --production

COPY build ./build
COPY .env.production ./

EXPOSE 3000

CMD ["node", "build/index.js"]
```

Build and run:
```bash
docker build -t cdms:latest .
docker run -p 3000:3000 --env-file .env.production cdms:latest
```

### Option C: Alternative Adapters

If using different hosting:

**Vercel:**
```bash
npm install -D @sveltejs/adapter-vercel
```
Update `svelte.config.js`:
```javascript
import adapter from '@sveltejs/adapter-vercel';
```

**Netlify:**
```bash
npm install -D @sveltejs/adapter-netlify
```
Update `svelte.config.js`:
```javascript
import adapter from '@sveltejs/adapter-netlify';
```

---

## 4. Server Requirements

### Minimum Requirements:
- **Node.js**: v18.0.0 or higher
- **npm**: v9.0.0 or higher
- **Memory**: 512MB (1GB+ recommended)
- **Storage**: 500MB for application + database

### Recommended Stack:
- **OS**: Ubuntu 20.04 LTS or later
- **Web Server**: Nginx (reverse proxy)
- **Database**: MySQL 8.0 or MariaDB 10.5+
- **Node.js**: v20 LTS
- **Process Manager**: PM2 or systemd

### Database Setup:
```bash
# Create database
mysql -u root -p
CREATE DATABASE cdms_v3 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

# Run migrations (if using Drizzle)
npm run db:push

# Seed initial data (if applicable)
npm run db:seed
```

---

## 5. Performance Optimization

### 5.1 Asset Caching
Configure your server to cache static assets:
- Images: 1 year
- CSS/JS: 30 days
- HTML: No cache

### 5.2 Database Optimization
```sql
-- Create indexes
CREATE INDEX idx_record_id ON records(record_id);
CREATE INDEX idx_user_id ON records(user_id);
CREATE INDEX idx_created_date ON records(created_date);

-- Enable query optimization
SET SESSION query_cache_type = ON;
```

### 5.3 Security Headers
Add to your web server configuration:
```
X-Content-Type-Options: nosniff
X-Frame-Options: SAMEORIGIN
X-XSS-Protection: 1; mode=block
Strict-Transport-Security: max-age=31536000; includeSubDomains
Content-Security-Policy: default-src 'self'; script-src 'self' 'unsafe-inline'; style-src 'self' 'unsafe-inline'
```

---

## 6. Post-Deployment Steps

### 6.1 Health Check
```bash
curl https://www.ezinetechnologies.com/demo/cdms
# Should return HTML of login page
```

### 6.2 Monitor Application
```bash
# Using PM2 (if installed)
pm2 start build/index.js --name "cdms"
pm2 logs cdms
pm2 save
```

### 6.3 SSL Certificate
- Your domain already uses HTTPS
- Ensure certificate is valid and not expired
- Set auto-renewal with Let's Encrypt or similar

### 6.4 Database Backups
```bash
# Daily automated backup
0 2 * * * mysqldump -u root -p cdms_v3 > /backups/cdms_$(date +\%Y\%m\%d).sql
```

---

## 7. Environment Variables Reference

### Production (.env.production)
```env
# Database
DATABASE_URL=mysql://user:password@localhost:3306/cdms_v3

# Application URLs
PUBLIC_API_URL=https://www.ezinetechnologies.com/demo/cdms/api
PUBLIC_APP_URL=https://www.ezinetechnologies.com/demo/cdms

# Application Info
PUBLIC_APP_NAME=Clinical Data Management System
PUBLIC_APP_VERSION=1.0.0

# Features
PUBLIC_AUTH_ENABLED=true

# Security
COOKIE_SECURE=true
COOKIE_SAME_SITE=Lax

# Runtime
NODE_ENV=production
```

---

## 8. Troubleshooting

### Issue: Assets returning 404
**Solution:** Ensure base path `/demo/cdms` is correctly set in `svelte.config.js` and proxy rules

### Issue: Database connection fails
**Solution:** Check `DATABASE_URL` in `.env.production`, verify MySQL is running

### Issue: Slow loading
**Solution:** 
- Clear browser cache
- Check server resources
- Verify database indexes
- Enable gzip compression on server

### Issue: Login not working
**Solution:** 
- Verify session management is configured
- Check cookie settings (Secure, SameSite)
- Verify database permissions

---

## 9. Deployment Checklist

- [ ] `npm run build` completes without errors
- [ ] `.env.production` configured with correct credentials
- [ ] `svelte.config.js` base path set to `/demo/cdms`
- [ ] Database created and migrations run
- [ ] Node.js and npm installed on server
- [ ] Web server (Nginx/Apache) configured with reverse proxy
- [ ] SSL certificate valid and installed
- [ ] Production dependencies installed (`npm ci --production`)
- [ ] Application starts: `node build/index.js`
- [ ] Health check passes: `curl https://www.ezinetechnologies.com/demo/cdms`
- [ ] Database backups configured
- [ ] Monitoring/logging set up
- [ ] Security headers configured
- [ ] Performance optimization enabled

---

## 10. Quick Start Commands

```bash
# 1. Install dependencies
npm install

# 2. Build for production
npm run build

# 3. Test build locally
npm run preview

# 4. Upload build/ folder to server

# 5. On server, install production deps
npm install --production

# 6. Set environment
export NODE_ENV=production
export DATABASE_URL="mysql://user:pass@localhost:3306/cdms_v3"

# 7. Start application
node build/index.js

# 8. Or use PM2
pm2 start build/index.js --name cdms
```

---

## 11. Support & Documentation

- **SvelteKit Docs**: https://svelte.dev/docs/kit
- **Node.js**: https://nodejs.org/
- **MySQL**: https://dev.mysql.com/doc/
- **Nginx**: https://nginx.org/en/docs/
- **PM2**: https://pm2.keymetrics.io/

---

**Last Updated:** November 30, 2025  
**Application Version:** 1.0.0  
**Domain:** https://www.ezinetechnologies.com/demo/cdms
