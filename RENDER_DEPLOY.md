# Render Deployment Guide - Free Tier

This guide will help you deploy the Well Twin Digital Twin application to Render's free tier.

## Prerequisites

- Render account (https://render.com/)
- GitHub account
- Git repository with the project code

## Architecture

- **Backend**: FastAPI with Render PostgreSQL (free tier)
- **Frontend**: React + Vite static site (free tier)
- **Database**: Render PostgreSQL (free tier - 90 days)

## Step 1: Push Code to GitHub

First, let's prepare and push your code to GitHub:

```bash
cd /Applications/Setapp/petrotwin

# Initialize git if not already done
git init

# Add all files
git add .

# Commit changes
git commit -m "Ready for Render deployment"

# Create GitHub repository and push
# Go to https://github.com/new and create a new repository
# Then:
git remote add origin https://github.com/YOUR_USERNAME/your-repo-name.git
git branch -M main
git push -u origin main
```

## Step 2: Deploy Backend to Render

### 2.1 Create PostgreSQL Database

1. Go to https://dashboard.render.com/
2. Click "New" → "PostgreSQL"
3. Name: `well-twin-db`
4. Database: `well_twin`
5. User: `well_twin_user`
6. Region: Choose closest to you
7. Database Version: PostgreSQL 15
8. Click "Create Database"

### 2.2 Create Backend Web Service

1. Click "New" → "Web Service"
2. Connect your GitHub repository
3. Select the `/Applications/Setapp/petrotwin/backend` directory
4. Configure:

**Build & Deploy:**
- Build Command: `pip install -r requirements.txt`
- Start Command: `python3 -m uvicorn app.main:app --host 0.0.0.0 --port $PORT`

**Environment:**
- Environment: Python 3
- Region: Same as database
- Branch: main

**Environment Variables:**
```
PORT=8000
ENVIRONMENT=production
HOST=0.0.0.0
CORS_ORIGINS=["*"]
DATABASE_URL=(from database connection)
SEED_DATABASE=true
```

**Database Connection:**
- Click "Database" → select your PostgreSQL database
- This will automatically set `DATABASE_URL`

**Optional (for AI features):**
```
GEMINI_API_KEY=your-gemini-api-key
SARVAM_API_KEY=your-sarvam-api-key
```

5. Click "Create Web Service"

### 2.3 Run Database Migrations

Once backend is deployed:

1. Go to your backend service on Render
2. Click "Shell" button
3. Run:
```bash
alembic upgrade head
```

### 2.4 Seed Database

In the same shell:
```bash
python -c "from app.db.seed import seed_database; import asyncio; asyncio.run(seed_database())"
```

## Step 3: Deploy Frontend to Render

### 3.1 Create Frontend Web Service

1. Click "New" → "Web Service"
2. Connect your GitHub repository
3. Select the `/Applications/Setapp/petrotwin/frontend` directory
4. Configure:

**Build & Deploy:**
- Build Command: `npm install && npm run build`
- Start Command: Not needed for static sites
- Publish Directory: `dist`

**Environment:**
- Environment: Node
- Region: Same as backend
- Branch: main

**Environment Variables:**
```
VITE_API_BASE_URL=/api/v1
VITE_ENABLE_DEMO_FALLBACK=false
VITE_BACKEND_URL=https://your-backend-url.onrender.com
```

**Optional (for AI features):**
```
VITE_GEMINI_API_KEY=your-gemini-api-key
VITE_MAPBOX_TOKEN=your-mapbox-token
```

5. Click "Create Web Service"

## Step 4: Update CORS Settings

After deployment:

1. Get your frontend URL from Render dashboard
2. Go to backend service → Environment
3. Update `CORS_ORIGINS`:
```
CORS_ORIGINS=["https://your-frontend-url.onrender.com"]
```

## Step 5: Test Deployment

### Backend Health Check
```bash
curl https://your-backend-url.onrender.com/api/v1/health
```

### Frontend Access
Visit: `https://your-frontend-url.onrender.com`

### API Documentation
Visit: `https://your-backend-url.onrender.com/api/v1/docs`

## Important Notes

### Free Tier Limitations
- PostgreSQL free tier: 90 days only
- Web services spin down after 15 minutes of inactivity
- Cold start can take 30-60 seconds
- RAM: 512MB (backend may need optimization)

### Database Expiry
- Render PostgreSQL free tier expires after 90 days
- Set up database backups before expiry
- Consider upgrading to paid tier for long-term use

### Performance Tips
- Use Render's environment variables instead of .env files
- Enable auto-deploys from GitHub
- Monitor logs for cold start issues
- Consider using Render's disk for file storage if needed

## Troubleshooting

### Build Failures
- Check Render build logs
- Ensure requirements.txt has all dependencies
- Verify Python/Node versions match
- Check for missing environment variables

### Database Connection Issues
- Verify DATABASE_URL is set correctly
- Check database is in same region as backend
- Ensure database is not in "Suspended" state
- Run migrations manually via shell

### CORS Errors
- Update CORS_ORIGINS with correct frontend URL
- Restart backend service after changing CORS
- Check frontend is using correct backend URL

### Cold Start Delays
- This is normal on free tier
- Consider upgrading to paid tier for better performance
- Implement caching strategies in frontend

## API Keys

Replace placeholder API keys in Render environment variables:

- **Gemini API**: https://aistudio.google.com/app/apikey
- **Sarvam AI**: https://dashboard.sarvam.ai/
- **Mapbox**: https://www.mapbox.com/ (for frontend maps)

## Monitoring

- Check Render dashboard for service status
- Monitor logs for errors
- Set up alert notifications in Render
- Track resource usage to avoid limits

## Cost Estimation

**Free Tier (Current):**
- Backend Web Service: Free
- Frontend Web Service: Free  
- PostgreSQL: Free (90 days only)

**After 90 Days:**
- PostgreSQL: ~$7/month
- Web Services: Free (with limitations)
- Consider upgrading for production use

## Security

- Never commit .env files to Git
- Use Render's environment variables for secrets
- Enable Render's built-in SSL/TLS
- Regularly update dependencies
- Monitor Render security logs