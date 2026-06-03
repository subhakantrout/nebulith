#!/bin/bash
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SERVICE_FILE="$SCRIPT_DIR/nebulith-ui.service"

if [ ! -f "$SERVICE_FILE" ]; then
  echo "Error: nebulith-ui.service not found in $SCRIPT_DIR"
  exit 1
fi

echo "Installing Nebulith UI service..."
echo "Make sure you've edited nebulith-ui.service with your username and paths first!"
echo ""

sudo cp "$SERVICE_FILE" /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable nebulith-ui
sudo systemctl start nebulith-ui
sudo systemctl status nebulith-ui
