# Quick Railway Deployment Guide

## Ready for Deployment! 🚀

Your Well Twin Digital Twin project is now fully configured for Railway deployment. Here's how to deploy it:

## Option 1: Manual Railway Deployment (Recommended)

### Step 1: Install Railway CLI
```bash
npm install -g @railway/cli
```

### Step 2: Login to Railway
```bash
railway login
```

### Step 3: Initialize and Deploy Backend
```bash
cd /Applications/Setapp/petrotwin/backend
railway init
railway up
```

### Step 4: Add PostgreSQL Database
```bash
railway add postgresql
```

### Step 5: Configure Environment Variables
In Railway dashboard, set these variables:

**Required:**
- `ENVIRONMENT=production`
- `PORT=8000`
- `HOST=0.0.0.0`
- `CORS_ORIGINS=["*"]`

**Optional (for AI features):**
- `GEMINI_API_KEY=your-gemini-api-key`
- `SARVAM_API_KEY=your-sarvam-api-key`

### Step 6: Run Migrations
```bash
railway run alembic upgrade head
```

### Step 7: Seed Database
```bash
railway run python -c "from app.db.seed import seed_database; import asyncio; asyncio.run(seed_database())"
```

### Step 8: Deploy Frontend
```bash
cd /Applications/Setapp/petrotwin/frontend
railway init
railway up
```

### Step 9: Configure Frontend
Set these in Railway for frontend service:
- `VITE_API_BASE_URL=/api/v1`
- `VITE_ENABLE_DEMO_FALLBACK=false`
- `VITE_BACKEND_URL=https://your-backend-url.railway.app`

## Option 2: GitHub + Railway Auto-Deploy

### Step 1: Push to GitHub
```bash
cd /Applications/Setapp/petrotwin
git add .
git commit -m "Ready for Railway deployment"
git push origin main
```

### Step 2: Connect to Railway
1. Go to https://railway.app/
2. Click "New Project" → "Deploy from GitHub repo"
3. Select your repository
4. Railway will automatically detect the configuration

### Step 3: Add Services
1. Add PostgreSQL database
2. Configure environment variables
3. Deploy both backend and frontend

## Verification

After deployment, test:
- Backend health: `https://your-backend-url.railway.app/api/v1/health`
- Frontend: `https://your-frontend-url.railway.app`
- API docs: `https://your-backend-url.railway.app/api/v1/docs`

## Current Status

✅ Backend configured for Railway
✅ Frontend configured for Railway  
✅ Database migrations set up
✅ Environment variables documented
✅ Local testing successful
✅ Production build tested

## What's Been Configured

**Backend:**
- Railway-compatible FastAPI setup
- PostgreSQL database support
- Automatic SSL/TLS
- CORS configuration
- Health check endpoint
- Graceful degradation for missing API keys

**Frontend:**
- Production build optimized
- Railway static file serving
- Environment variable support
- API proxy configuration

**Database:**
- Alembic migrations created
- Automatic table creation
- Seed data scripts
- Railway PostgreSQL compatibility

## API Keys Needed

For full functionality, add these in Railway dashboard:
- `GEMINI_API_KEY` - For AI copilot features
- `SARVAM_API_KEY` - For voice features
- `VITE_MAPBOX_TOKEN` - For well field maps (frontend)

## Support

If you encounter issues:
1. Check Railway build logs
2. Verify environment variables
3. Ensure database migrations ran
4. Check CORS settings
5. Review Railway service status

The application will work even without API keys using deterministic fallbacks!