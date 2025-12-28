# Quick Configuration Reference for Production Deployment

## Key Settings for: https://www.ezinetechnologies.com/demo/cdms

### 1. Base Path Configuration
✅ **Status**: Already configured in svelte.config.js
```
Base Path: /demo/cdms
```
This means:
- All routes are prefixed with `/demo/cdms/`
- Assets load from `/demo/cdms/static/*`
- API calls should go to `/demo/cdms/api/*`

### 2. Environment Variables

**Development (.env)**
```
DATABASE_URL=mysql://root:root@localhost:3306/cdms_v3
```

**Production (.env.production)** ✅ Already created
```
DATABASE_URL=mysql://root:root@localhost:3306/cdms_v3
PUBLIC_API_URL=https://www.ezinetechnologies.com/demo/cdms/api
PUBLIC_APP_URL=https://www.ezinetechnologies.com/demo/cdms
NODE_ENV=production
```

### 3. Build Configuration

**Current Setup:**
- Adapter: @sveltejs/adapter-auto (Node.js compatible)
- Output: `build/` directory
- Optimization: Terser minification enabled
- Code splitting: Yes (vendor separation)

### 4. Deployment Steps

#### Step 1: Build
```bash
npm run build
```
Output: `build/` folder ready for deployment

#### Step 2: Upload to Server
```
Transfer `build/` folder to: /var/www/cdms/build
```

#### Step 3: Install Production Dependencies
```bash
ssh user@server
cd /var/www/cdms
npm install --production
```

#### Step 4: Configure Web Server

**Nginx Configuration:**
```nginx
server {
    listen 443 ssl;
    server_name www.ezinetechnologies.com;
    ssl_certificate /path/to/cert;
    ssl_certificate_key /path/to/key;

    location /demo/cdms/ {
        proxy_pass http://localhost:3000/;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

**Apache Configuration:**
```apache
ProxyPreserveHost On
ProxyPass /demo/cdms/ http://localhost:3000/
ProxyPassReverse /demo/cdms/ http://localhost:3000/
```

#### Step 5: Start Application

**Option A: Direct Node**
```bash
cd /var/www/cdms
NODE_ENV=production node build/index.js
```

**Option B: PM2 Process Manager** (Recommended)
```bash
npm install -g pm2
pm2 start build/index.js --name "cdms" --env production
pm2 startup
pm2 save
```

**Option C: Systemd Service**
Create `/etc/systemd/system/cdms.service`:
```ini
[Unit]
Description=Clinical Data Management System
After=network.target

[Service]
Type=simple
User=www-data
WorkingDirectory=/var/www/cdms
Environment="NODE_ENV=production"
Environment="DATABASE_URL=mysql://user:pass@localhost:3306/cdms_v3"
ExecStart=/usr/bin/node /var/www/cdms/build/index.js
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

Enable service:
```bash
systemctl enable cdms
systemctl start cdms
systemctl status cdms
```

### 5. Verify Deployment

```bash
# Test the application
curl https://www.ezinetechnologies.com/demo/cdms

# Check status
curl -I https://www.ezinetechnologies.com/demo/cdms

# Check logs (PM2)
pm2 logs cdms

# Check logs (Systemd)
journalctl -u cdms -f
```

### 6. Database Setup

```bash
# Connect to MySQL
mysql -u root -p

# Create database
CREATE DATABASE cdms_v3 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

# Grant permissions
GRANT ALL PRIVILEGES ON cdms_v3.* TO 'cdms_user'@'localhost' IDENTIFIED BY 'secure_password';
FLUSH PRIVILEGES;

# Run migrations
npm run db:push
```

### 7. SSL/HTTPS Setup

Your domain uses HTTPS. Ensure:
- ✅ SSL certificate is installed at `/path/to/cert.crt` and `/path/to/key.key`
- ✅ Certificate is valid and not expired
- ✅ Set up auto-renewal (Let's Encrypt recommended)

**Let's Encrypt Setup:**
```bash
certbot certonly --webroot -w /var/www/html -d www.ezinetechnologies.com
certbot renew --dry-run  # Test renewal
```

### 8. Performance Tuning

**Nginx Gzip Compression:**
```nginx
gzip on;
gzip_types text/plain text/css application/json application/javascript text/xml application/xml application/xml+rss;
gzip_min_length 1024;
```

**Browser Caching:**
```nginx
# Cache static assets for 1 year
location /demo/cdms/static/ {
    expires 365d;
    add_header Cache-Control "public, immutable";
}

# Don't cache HTML
location /demo/cdms/*.html {
    expires -1;
    add_header Pragma "no-cache";
}
```

### 9. Security Configuration

**Security Headers (Nginx):**
```nginx
add_header X-Content-Type-Options "nosniff";
add_header X-Frame-Options "SAMEORIGIN";
add_header X-XSS-Protection "1; mode=block";
add_header Referrer-Policy "no-referrer-when-downgrade";
add_header Strict-Transport-Security "max-age=31536000; includeSubDomains; preload";
```

### 10. Monitoring & Logging

**Application Health Check:**
```bash
# Add to crontab
*/5 * * * * curl -s https://www.ezinetechnologies.com/demo/cdms > /dev/null || systemctl restart cdms
```

**Log Rotation:**
```bash
# Create /etc/logrotate.d/cdms
/var/log/cdms/*.log {
    daily
    rotate 7
    compress
    delaycompress
    notifempty
    create 0640 www-data www-data
    sharedscripts
}
```

---

## Checklist Before Going Live

- [ ] `npm run build` completes successfully
- [ ] No console errors during build
- [ ] `.env.production` file created with correct values
- [ ] `svelte.config.js` has base path `/demo/cdms`
- [ ] Database created and accessible
- [ ] Web server (Nginx/Apache) configured
- [ ] SSL certificate installed and valid
- [ ] Node.js v18+ installed on server
- [ ] PM2 or systemd service configured
- [ ] Health check passes (curl test)
- [ ] Database backups scheduled
- [ ] Monitoring alerts set up
- [ ] Security headers configured
- [ ] Gzip compression enabled
- [ ] Static asset caching configured

---

## Emergency Rollback

If issues occur after deployment:

```bash
# Stop current version
pm2 stop cdms
# or
systemctl stop cdms

# Revert to previous build
git revert HEAD
npm run build

# Restart
pm2 start build/index.js
# or
systemctl start cdms

# Check status
pm2 logs cdms
journalctl -u cdms -f
```

---

**Need Help?**
Check DEPLOYMENT_GUIDE.md for detailed instructions on each section.
