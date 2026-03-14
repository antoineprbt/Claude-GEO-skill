#!/bin/bash
# Claude GEO - Install Script
# Installs the GEO skill for Claude Code

set -e

SKILL_DIR="$HOME/.claude/skills/geo"
SCRIPT_DIR="$HOME/.claude/scripts"

echo "🔍 Installing Claude GEO..."

# Create directories
mkdir -p "$SKILL_DIR/references"
mkdir -p "$SCRIPT_DIR"

# Get the directory where this script lives
SCRIPT_PATH="$(cd "$(dirname "$0")" && pwd)"

# Copy skill files
cp "$SCRIPT_PATH/geo/SKILL.md" "$SKILL_DIR/SKILL.md"
cp "$SCRIPT_PATH/geo/references/technical-checklist.md" "$SKILL_DIR/references/"
cp "$SCRIPT_PATH/geo/references/content-optimization.md" "$SKILL_DIR/references/"
cp "$SCRIPT_PATH/geo/references/schema-guide.md" "$SKILL_DIR/references/"
cp "$SCRIPT_PATH/geo/references/ai-engine-behavior.md" "$SKILL_DIR/references/"
cp "$SCRIPT_PATH/geo/references/action-plan-template.md" "$SKILL_DIR/references/"

# Copy scripts
cp "$SCRIPT_PATH/scripts/parse_geo.py" "$SCRIPT_DIR/"
chmod +x "$SCRIPT_DIR/parse_geo.py"

echo ""
echo "✅ Claude GEO installed successfully!"
echo ""
echo "📁 Skill installed to: $SKILL_DIR"
echo "📜 Script installed to: $SCRIPT_DIR/parse_geo.py"
echo ""
echo "🔄 Restart Claude Code to activate."
echo ""
echo "📖 Commands:"
echo "  /geo audit <url>       Full GEO audit"
echo "  /geo page <url>        Single page analysis"
echo "  /geo technical <url>   Technical AI-readiness"
echo "  /geo content <url>     Content citability"
echo "  /geo schema <url>      Schema markup audit"
echo "  /geo presence <brand>  Multi-platform presence"
echo "  /geo competitors <url> Competitor AI visibility"
echo "  /geo fix <url>         Fix list with code"
echo "  /geo plan <url>        90-day action plan"
echo "  /geo score <url>       Quick AI Citability Score"
