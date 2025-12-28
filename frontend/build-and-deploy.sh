#!/bin/bash
# CDMS Build & Deployment Script
# Domain: https://www.ezinetechnologies.com/demo/cdms

set -e  # Exit on error

echo "=========================================="
echo "CDMS Build & Deployment Script"
echo "=========================================="
echo ""

# Color codes for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Configuration
APP_NAME="cdms"
BUILD_DIR="./build"
DEPLOY_USER="deploy"
DEPLOY_HOST="www.ezinetechnologies.com"
DEPLOY_PATH="/var/www/cdms"
BASE_PATH="/demo/cdms"
NODE_VERSION="20"

# Function to print colored output
print_status() {
    echo -e "${GREEN}✓${NC} $1"
}

print_error() {
    echo -e "${RED}✗${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}⚠${NC} $1"
}

# Step 1: Pre-flight checks
echo ""
echo "Step 1: Running pre-flight checks..."
echo "========================================"

# Check Node.js version
if ! command -v node &> /dev/null; then
    print_error "Node.js is not installed"
    exit 1
fi

NODE_INSTALLED=$(node -v)
print_status "Node.js version: $NODE_INSTALLED"

# Check npm
if ! command -v npm &> /dev/null; then
    print_error "npm is not installed"
    exit 1
fi

NPM_INSTALLED=$(npm -v)
print_status "npm version: $NPM_INSTALLED"

# Check if build directory exists
if [ -d "$BUILD_DIR" ]; then
    print_warning "Build directory already exists. It will be replaced."
fi

echo ""
echo "Step 2: Installing dependencies..."
echo "========================================"
npm install
print_status "Dependencies installed"

echo ""
echo "Step 3: Running checks..."
echo "========================================"
npm run check
print_status "Type checks passed"

echo ""
echo "Step 4: Building for production..."
echo "========================================"
echo "Build Configuration:"
echo "  - Base Path: $BASE_PATH"
echo "  - Environment: production"
echo "  - Target: ES2020"
echo "  - Minification: enabled"
echo ""

NODE_ENV=production npm run build
print_status "Build completed successfully"

echo ""
echo "Step 5: Build verification..."
echo "========================================"

if [ ! -d "$BUILD_DIR" ]; then
    print_error "Build directory was not created"
    exit 1
fi

if [ ! -f "$BUILD_DIR/index.js" ]; then
    print_error "Build index.js file not found"
    exit 1
fi

print_status "Build output structure verified"

# Calculate build size
BUILD_SIZE=$(du -sh "$BUILD_DIR" | cut -f1)
print_status "Build size: $BUILD_SIZE"

echo ""
echo "Step 6: Preview build locally (optional)"
echo "========================================"
print_warning "To test locally, run: npm run preview"
print_warning "Then visit: http://localhost:4173$BASE_PATH"

echo ""
echo "=========================================="
echo "LOCAL BUILD COMPLETE!"
echo "=========================================="
echo ""
echo "Build Directory: $BUILD_DIR"
echo "Ready for deployment to: https://$DEPLOY_HOST$BASE_PATH"
echo ""

# Step 7: Ask for deployment
read -p "Do you want to deploy now? (y/n) " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo ""
    echo "Step 7: Preparing for deployment..."
    echo "========================================"
    
    # Check if ssh key exists
    if [ ! -f ~/.ssh/id_rsa ]; then
        print_error "SSH key not found at ~/.ssh/id_rsa"
        print_warning "Generate SSH key with: ssh-keygen -t rsa -b 4096"
        exit 1
    fi
    
    print_status "SSH key found"
    
    echo ""
    echo "Deployment Steps:"
    echo "1. Upload build files to server"
    echo "2. Install production dependencies"
    echo "3. Start/restart application"
    echo ""
    
    # Create deployment package
    echo "Creating deployment package..."
    tar -czf cdms-build.tar.gz build/ package*.json .env.production
    print_status "Package created: cdms-build.tar.gz"
    
    echo ""
    echo "Uploading to server: $DEPLOY_HOST"
    echo "User: $DEPLOY_USER"
    echo "Path: $DEPLOY_PATH"
    echo ""
    
    # Upload to server
    scp cdms-build.tar.gz $DEPLOY_USER@$DEPLOY_HOST:$DEPLOY_PATH/
    print_status "Files uploaded"
    
    # Extract and setup on server
    ssh $DEPLOY_USER@$DEPLOY_HOST << EOF
        set -e
        cd $DEPLOY_PATH
        
        # Extract uploaded files
        tar -xzf cdms-build.tar.gz
        
        # Install production dependencies
        npm install --production
        
        # Restart application (assuming systemd service)
        sudo systemctl restart $APP_NAME
        
        # Check status
        sleep 2
        sudo systemctl status $APP_NAME --no-pager
EOF
    
    print_status "Server deployment completed"
    
    echo ""
    echo "Verifying deployment..."
    sleep 3
    
    if curl -s https://$DEPLOY_HOST$BASE_PATH | grep -q "<!DOCTYPE html>"; then
        print_status "Application is running and responding"
    else
        print_error "Application verification failed"
        print_warning "Check server logs: ssh $DEPLOY_USER@$DEPLOY_HOST sudo journalctl -u $APP_NAME -f"
        exit 1
    fi
    
    # Cleanup
    rm cdms-build.tar.gz
    print_status "Cleanup completed"
    
    echo ""
    echo "=========================================="
    echo "DEPLOYMENT COMPLETE!"
    echo "=========================================="
    echo ""
    echo "Application URL: https://$DEPLOY_HOST$BASE_PATH"
    echo ""
    
else
    echo ""
    echo "Skipping deployment."
    echo ""
    echo "To deploy later, run:"
    echo "  tar -czf cdms-build.tar.gz build/ package*.json .env.production"
    echo "  scp cdms-build.tar.gz $DEPLOY_USER@$DEPLOY_HOST:$DEPLOY_PATH/"
    echo "  ssh $DEPLOY_USER@$DEPLOY_HOST"
    echo "  cd $DEPLOY_PATH"
    echo "  tar -xzf cdms-build.tar.gz && npm install --production"
    echo "  sudo systemctl restart $APP_NAME"
    echo ""
fi

echo "=========================================="
echo "Script completed"
echo "=========================================="
