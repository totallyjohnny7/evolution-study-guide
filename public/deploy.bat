@echo off
REM Deploy public-v2 to Cloudflare Pages as evolution-study-guide.
setlocal
cd /d "%~dp0"
where wrangler >nul 2>&1
if errorlevel 1 (
  echo ERROR: wrangler not found on PATH. Install with: npm install -g wrangler
  exit /b 1
)
wrangler pages deploy . --project-name="evolution-study-guide" --branch=main --commit-dirty=true
