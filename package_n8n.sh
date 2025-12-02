#!/bin/bash
set -e

echo "📦 Creating a full n8n + Flask package..."

WORKDIR="$HOME/n8n_package"
mkdir -p "$WORKDIR"

echo "➡️ Copying docker-compose.yml, app.py, and README.md..."
cp ~/n8n/docker-compose.yml "$WORKDIR"/
cp ~/n8n/app.py "$WORKDIR"/
cp ~/n8n/README.md "$WORKDIR"/

echo "➡️ Backing up n8n data..."
tar -czf "$WORKDIR/n8n_backup.tar.gz" -C ~/.n8n .

echo "➡️ Creating final distributable archive..."
cd "$HOME"
tar -czf n8n_full_package.tar.gz -C "$WORKDIR" .

echo "✅ Done!"
echo "Your portable setup is ready: $HOME/n8n_full_package.tar.gz"
