#!/usr/bin/env bash
# Deploy evolution-study-guide to Cloudflare Pages production.
#
# IMPORTANT: Cloudflare Pages is wired to branch `main` for production,
# but this repo's default branch is `master`. Pushing to master only creates
# a *preview* build (separate URL). To push changes to the live URL
# https://evolution-study-guide.pages.dev/ we must deploy directly via
# wrangler, targeting --branch=main.
#
# Usage: ./deploy.sh [commit-message]
set -euo pipefail
cd "$(dirname "$0")"

MSG="${1:-Update site content}"

# Stage and push to GitHub master (backup/version control)
if [[ -n "$(git status --porcelain)" ]]; then
  git add -A
  git commit -m "$MSG" || true
  git push origin master
fi

# Direct deploy of public/ to Cloudflare Pages production (branch=main)
npx wrangler pages deploy public \
  --project-name=evolution-study-guide \
  --branch=main \
  --commit-dirty=true

echo ""
echo "✔ Deploy complete. Live URL: https://evolution-study-guide.pages.dev/"
