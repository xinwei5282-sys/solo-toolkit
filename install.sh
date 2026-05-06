#!/bin/bash
set -e

# Solo Toolkit Installation Script
# Extracts personal AI Agent system to new machine

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
echo "Installing from: $REPO_DIR"

# Step 1: Create ~/.agents/skills/ and link agent-skills/
echo "[1/4] Setting up agent skills..."
mkdir -p ~/.agents/skills
if [ -d "$REPO_DIR/agent-skills" ]; then
    # Copy or symlink agent-skills
    if [ ! -L ~/.agents/skills ]; then
        cp -r "$REPO_DIR/agent-skills"/* ~/.agents/skills/ 2>/dev/null || true
        echo "  ✓ Copied agent skills to ~/.agents/skills/"
    else
        echo "  ✓ ~/.agents/skills/ already linked"
    fi
fi

# Step 2: Set up ~/.claude/ structure with CLAUDE.md, hooks, settings.json
echo "[2/4] Setting up Claude Code configuration..."
mkdir -p ~/.claude/hooks

if [ -f "$REPO_DIR/home/CLAUDE.md" ]; then
    cp "$REPO_DIR/home/CLAUDE.md" ~/CLAUDE.md
    echo "  ✓ Installed CLAUDE.md to ~/"
fi

if [ -f "$REPO_DIR/home/.claude/hooks/memory-audit-check.sh" ]; then
    cp "$REPO_DIR/home/.claude/hooks/memory-audit-check.sh" ~/.claude/hooks/
    chmod +x ~/.claude/hooks/memory-audit-check.sh
    echo "  ✓ Installed memory-audit-check.sh hook"
fi

if [ -f "$REPO_DIR/home/.claude/settings.json" ]; then
    # Merge settings.json if it already exists
    if [ -f ~/.claude/settings.json ]; then
        echo "  ⚠ ~/.claude/settings.json already exists, backing up to settings.json.bak"
        cp ~/.claude/settings.json ~/.claude/settings.json.bak
    fi
    cp "$REPO_DIR/home/.claude/settings.json" ~/.claude/settings.json
    echo "  ✓ Installed settings.json"
fi

# Step 3: Set up knowledge-hub with personal knowledge files
echo "[3/4] Setting up personal knowledge base..."
mkdir -p ~/knowledge-hub/wiki

if [ -d "$REPO_DIR/knowledge-personal" ]; then
    cp "$REPO_DIR/knowledge-personal"/*.md ~/knowledge-hub/wiki/ 2>/dev/null || true
    echo "  ✓ Copied personal knowledge files to ~/knowledge-hub/wiki/"
fi

# Step 4: Set up memory directory structure
echo "[4/4] Setting up memory structure..."
mkdir -p ~/.claude/projects/-Users-weiran/memory

echo ""
echo "✅ Installation complete!"
echo ""
echo "Next steps:"
echo "1. Review and adjust ~/.claude/settings.json if needed"
echo "2. Review ~/CLAUDE.md and update paths if necessary"
echo "3. Verify ~/.agents/skills/ contains your agent definitions"
echo "4. Set up git user: git config --global user.name 'Your Name' && git config --global user.email 'your@email.com'"
echo ""
