# 🚀 Quick Deployment Instructions

## Status: Ready for Render Deployment

Your Well Twin Digital Twin project is fully configured and committed to Git. Here's how to deploy it to Render (FREE):

## Step 1: Create GitHub Repository (5 minutes)

1. Go to https://github.com/new
2. Repository name: `well-twin-digital-twin` (or your preferred name)
3. Description: "Digital Twin for Heavy Oil Well Optimization"
4. Make it **Public** (recommended) or Private
5. Click "Create repository"

## Step 2: Push to GitHub

```bash
cd /Applications/Setapp/petrotwin

# Add the GitHub repository you just created
git remote add origin https://github.com/YOUR_USERNAME/your-repo-name.git

# Push to GitHub
git branch -M main
git push -u origin main
```

## Step 3: Deploy to Render (10 minutes)

### Option A: Use Render Dashboard (Recommended)

1. Go to https://dashboard.render.com/
2. Click "New" → "Web Service"
3. Connect your GitHub repository
4. Select the `backend` folder
5. Use these settings:

**Backend Service:**
- Build Command: `pip install -r requirements.txt`
- Start Command: `python3 -m uvicorn app.main:app --host 0.0.0.0 --port $PORT`
- Environment Variables:
  - `PORT=8000`
  - `ENVIRONMENT=production`
  - `CORS_ORIGINS=["*"]`
  - `SEED_DATABASE=true`

6. Add PostgreSQL Database:
   - Click "New" → "PostgreSQL"
   - Connect it to your backend service

7. Deploy Frontend:
   - Click "New" → "Web Service"
   - Select the `frontend` folder
   - Build Command: `npm install && npm run build`
   - Publish Directory: `dist`

### Option B: Use render.yaml (Automatic)

The project includes `render.yaml` files for automatic deployment. Render will detect these files when you connect your GitHub repository.

## Step 4: Run Database Setup

After backend deployment:

1. Go to your backend service on Render
2. Click "Shell" button
3. Run: `alembic upgrade head`
4. Run: `python -c "from app.db.seed import seed_database; import asyncio; asyncio.run(seed_database())"`

## Step 5: Update Environment Variables

Add these to your frontend service:
- `VITE_BACKEND_URL=https://your-backend-url.onrender.com`

## Verification

- Backend: `https://your-backend-url.onrender.com/api/v1/health`
- Frontend: `https://your-frontend-url.onrender.com`
- API Docs: `https://your-backend-url.onrender.com/api/v1/docs`

## What's Included

✅ **Fully Configured Backend**
- FastAPI with Railway/Render support
- PostgreSQL database integration
- Alembic migrations
- Production environment settings
- Health check endpoints

✅ **Production-Ready Frontend**
- Optimized build configuration
- Environment variable support
- API proxy configuration
- Static site serving

✅ **Database Setup**
- Migration scripts generated
- Seed data for demo wells
- PostgreSQL compatibility
- Automatic table creation

✅ **Documentation**
- Complete deployment guides
- Environment variable templates
- Troubleshooting instructions
- API key setup guides

## Free Tier Benefits

- **Backend**: Free web service
- **Frontend**: Free static site
- **Database**: 90 days free PostgreSQL
- **SSL/TLS**: Automatic
- **CI/CD**: Automatic GitHub deployments

## Next Steps After Deployment

1. Add API keys for AI features (optional)
2. Configure Mapbox token for maps (optional)
3. Set up monitoring and alerts
4. Test all features
5. Update CORS settings with production URLs

## Support

If you need help:
- Check `RENDER_DEPLOY.md` for detailed instructions
- Review Render dashboard logs
- Check environment variables
- Verify database connection

The project is ready to deploy immediately!