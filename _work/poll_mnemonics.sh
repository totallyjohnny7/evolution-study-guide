#!/usr/bin/env bash
# Poll for mnemonic completion in both HTML files
cd "$(dirname "$0")/.."
MAX_POLLS=25
INTERVAL=45
for i in $(seq 1 $MAX_POLLS); do
  RV=$(grep -o "fc-mn" public/exam3_review.html 2>/dev/null | wc -l | tr -d '[:space:]')
  LC_FCMN=$(grep -o "fc-mn" public/exam3_lecture.html 2>/dev/null | wc -l | tr -d '[:space:]')
  LC_MN=$(grep -o "mnemonic" public/exam3_lecture.html 2>/dev/null | wc -l | tr -d '[:space:]')
  RV=${RV:-0}
  LC_FCMN=${LC_FCMN:-0}
  LC_MN=${LC_MN:-0}
  TS=$(date +"%H:%M:%S")
  echo "[poll $i/$MAX_POLLS $TS] review fc-mn=$RV | lecture fc-mn=$LC_FCMN mnemonic=$LC_MN"
  if [ "$RV" -ge 152 ] 2>/dev/null && { [ "$LC_FCMN" -ge 197 ] 2>/dev/null || [ "$LC_MN" -ge 197 ] 2>/dev/null; }; then
    echo "CONVERGED at poll $i"
    exit 0
  fi
  if [ $i -lt $MAX_POLLS ]; then
    sleep $INTERVAL
  fi
done
echo "TIMEOUT after $MAX_POLLS polls"
exit 1
