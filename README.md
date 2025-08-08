# Swadhā Life Website

**Rooted in Wisdom. Crafted with Intention.**

Eco-luxury Ayurvedic wellness kits for conscious hospitality.

## Development Server

This project includes multiple options for local development with auto-reload functionality.

### Option 1: Python Live Server (Recommended)
```bash
# Start the enhanced live server with WebSocket auto-reload
python3 live_server.py

# Or use the shell script
./dev.sh
```

### Option 2: Simple Python Server
```bash
# Start the simple development server
python3 dev_server.py
```

### Option 3: NPM Live Server
```bash
# Install dependencies (first time only)
npm install

# Start live-server
npm run live-server
```

### Option 4: Basic Python Server
```bash
# Simple HTTP server without auto-reload
python3 -m http.server 8000
```

## Features

- **Elemental Harmony Color Palette** - Based on the brand logo
- **Responsive Design** - Works on all devices
- **Auto-reload** - Changes automatically refresh the browser
- **Modern Typography** - Rasa, Playfair Display, and Inter fonts
- **Cultural Authenticity** - Sanskrit text and Indian design elements

## Color Palette

**Elemental Harmony:**
- Sacred Fire: `#FF6B35`
- Pure Water: `#4ECDC4`
- Solar Energy: `#FF8C42`
- Spirit Air: `#8B4513`
- Vital Earth: `#4CAF50`
- Sacred Ground: `#5D4037`

## Project Structure

```
swadha/
├── index.html          # Main website
├── palettes.html       # Color palette showcase
├── palettes.css        # Palette styles
├── color_palettes.py   # Python color visualization
├── live_server.py      # Enhanced dev server with WebSocket
├── dev_server.py       # Simple dev server
├── dev.sh             # Shell script for easy startup
└── package.json       # NPM configuration
```

## Development

1. **Start the server:**
   ```bash
   ./dev.sh
   ```

2. **Open your browser:**
   - The server will automatically open `http://localhost:8000`
   - Make changes to HTML/CSS files
   - Browser will automatically reload

3. **Stop the server:**
   - Press `Ctrl+C` in the terminal

## Deployment

The website is configured for GitHub Pages deployment. Simply push changes to the main branch and GitHub Actions will automatically deploy to `https://krutartha.github.io/swadha/`.

## Brand Information

**Swadhā Life** (formerly Svadhaa Naturals) is an eco-luxury brand rooted in India's ancient wisdom and dedicated to conscious hospitality. Our purpose is to create beautiful, biodegradable wellness kits that nourish the guest, uplift the maker, and respect the Earth.

**Mission:** To craft biodegradable, Ayurvedic wellness kits that elevate hospitality experiences while creating dignified livelihoods for artisan communities across India.

**Vision:** To become the global benchmark in conscious hospitality, where every product honors the Earth, empowers artisans, and celebrates India's timeless cultural wisdom.

---

*Rooted in Indian Wisdom · Crafted with Consciousness · Made for the World*
