# Push to GitHub Instructions

The Hyundai Ioniq 5 code has been separated from the NiFi workflow repository!

## Location
- **Local Path**: `~/github/hyundai-ioniq5-home-assistant`
- **Status**: Git initialized with initial commit ✅

## Next Steps to Push to GitHub:

### Option 1: Create via GitHub Web UI (Easiest)
1. Go to https://github.com/organizations/universum-inkasso/repositories/new
   - Or: https://github.com/new (for personal account)
2. Repository name: `hyundai-ioniq5-home-assistant`
3. Description: `Home Assistant integration for Hyundai Ioniq 5 (2025) - EU/Austria Edition with Bluelink API v3.48.1`
4. Choose: **Public**
5. ⚠️ **Do NOT initialize with README, .gitignore, or license** (we already have these)
6. Click "Create repository"

Then run these commands:
```bash
cd ~/github/hyundai-ioniq5-home-assistant
git remote add origin https://github.com/universum-inkasso/hyundai-ioniq5-home-assistant.git
git push -u origin main
```

### Option 2: Create via GitHub CLI
```bash
cd ~/github/hyundai-ioniq5-home-assistant
# For organization repo (requires org admin permission):
gh repo create universum-inkasso/hyundai-ioniq5-home-assistant --public --source=. --remote=origin --push

# OR for personal repo:
gh repo create hyundai-ioniq5-home-assistant --public --source=. --remote=origin --push
```

## What's Included:
- ✅ Full Home Assistant custom component (`custom_components/ioniq5_2025/`)
- ✅ EU/Austria specific features and documentation
- ✅ German + multilingual translations
- ✅ API reference documentation
- ✅ Installation and setup guides
- ✅ HACS integration support
- ✅ `.cursorrules` for AI agent context

## Repository Contents:
```
hyundai-ioniq5-home-assistant/
├── custom_components/
│   └── ioniq5_2025/          # Main integration code
├── .cursorrules               # AI agent workspace rules
├── API_REFERENCE.md
├── CHANGELOG.md
├── EU_FEATURES.md
├── EU_SETUP_GUIDE.md
├── EU_VERSION_SUMMARY.md
├── INSTALLATION.md
├── QUICKSTART.md
├── README.md
├── SUMMARY.md
├── hacs.json
└── LICENSE
```

## After Pushing:
The repository will be live at:
`https://github.com/universum-inkasso/hyundai-ioniq5-home-assistant`
