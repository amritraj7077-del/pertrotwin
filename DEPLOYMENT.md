# Railway Deployment Guide

This guide will help you deploy the Well Twin Digital Twin application to Railway with PostgreSQL database.

## Prerequisites

1. Railway account (https://railway.app/)
2. Git repository with the project code
3. API keys for services you want to use

## Architecture

- **Backend**: FastAPI with Railway PostgreSQL
- **Frontend**: React + Vite static site
- **Database**: Railway PostgreSQL (managed)

## Deployment Steps

### 1. Install Railway CLI

```bash
npm install -g @railway/cli
```

### 2. Login to Railway

```bash
railway login
```

### 3. Initialize Railway Project

```bash
railway init
```

### 4. Deploy Backend

```bash
cd backend
railway up
```

### 5. Add PostgreSQL Database

```bash
railway add postgresql
```

### 6. Configure Environment Variables

Set the following environment variables in Railway dashboard:

**Required:**
- `DATABASE_URL` (auto-provided by Railway)
- `ENVIRONMENT=production`
- `PORT=8000`
- `HOST=0.0.0.0`
- `CORS_ORIGINS=["*"]`

**Optional (for AI features):**
- `GEMINI_API_KEY=your-gemini-api-key`
- `GEMINI_MODEL=gemini-1.5-flash`
- `SARVAM_API_KEY=your-sarvam-api-key`
- `SARVAM_MODEL_STT=saaras:v1`
- `SARVAM_MODEL_TTS=bulbul:v1`

**Optional (for notifications):**
- `NOTIFICATION_MODE=mock` (default) or `twilio` (future)

### 7. Run Database Migrations

```bash
railway run alembic upgrade head
```

### 8. Seed Database

```bash
railway run python -c "from app.db.seed import seed_database; import asyncio; asyncio.run(seed_database())"
```

### 9. Deploy Frontend

```bash
cd ../frontend
railway up
```

### 10. Configure Frontend Environment

Set these in Railway for the frontend service:
- `VITE_API_BASE_URL=/api/v1`
- `VITE_ENABLE_DEMO_FALLBACK=false`
- `VITE_BACKEND_URL=https://your-backend-url.railway.app`

### 11. Update CORS Settings

After deployment, update the backend CORS_ORIGINS to include your frontend URL:
- Get frontend URL from Railway dashboard
- Update backend CORS_ORIGINS in Railway environment variables

## Verification

1. Check backend health: `https://your-backend-url.railway.app/api/v1/health`
2. Access frontend: `https://your-frontend-url.railway.app`
3. Test API endpoints via Swagger: `https://your-backend-url.railway.app/api/v1/docs`

## Troubleshooting

### Database Connection Issues
- Ensure DATABASE_URL is properly set by Railway
- Check PostgreSQL service is running
- Verify migration ran successfully

### CORS Errors
- Update CORS_ORIGINS to include frontend URL
- Restart backend service after changing CORS settings

### Build Failures
- Check Railway build logs
- Ensure all dependencies are in requirements.txt
- Verify Node.js version compatibility

## API Keys

Replace placeholder API keys with your own:

- **Gemini API**: https://aistudio.google.com/app/apikey
- **Sarvam AI**: https://dashboard.sarvam.ai/
- **Mapbox**: https://www.mapbox.com/ (for frontend maps)

## Cost Estimate

Railway free tier includes:
- $5/month credit
- 512MB RAM
- Shared CPU
- 1GB PostgreSQL database

For production, consider upgrading for better performance.

## Security Notes

- Never commit .env files to Git
- Use Railway's secret management for sensitive data
- Enable Railway's built-in SSL/TLS
- Regularly update dependencies
- Monitor Railway usage logs