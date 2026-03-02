# DiscordPrivateNotifier

[![GitHub Release](https://img.shields.io/github/v/release/TagSteel/DiscordDMBot?display_name=release)](https://github.com/TagSteel/DiscordDMBot/releases/latest)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A production-ready Discord bot that allows server members to trigger a private notification (DM) to a designated target user, with per-server configuration, cooldown control, and bilingual support (English/French).

## Key Features

- **Per-server target configuration** with admin-only setup
- **Per-server cooldown management** to prevent spam
- **Bilingual experience** (`en` / `fr`) for messages and command flow
- **Slash-command based UX** (Discord Application Commands)
- **JSON persistence** for lightweight, file-based configuration

## Command Reference

| Command | Access | Description |
|---|---|---|
| `/settarget <user>` | Admin | Set the user who receives private notifications |
| `/setcooldown <seconds>` | Admin | Set cooldown duration (1 to 86400 seconds) |
| `/setlanguage <en\|fr>` | Admin | Set bot language for the current server |
| `/viewsetcooldown` | Everyone | Show configured cooldown |
| `/viewcooldown` | Everyone | Show remaining cooldown time |
| `/deepthroat` | Everyone | Trigger private notification to target |
| `/gorgeprofonde` | Everyone | French alias of the notification command |

## Requirements

- Python **3.8+**
- A Discord application with a bot user

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/TagSteel/DiscordDMBot.git
   cd DiscordDMBot
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Create environment file**
   Create a `.env` file in the project root:
   ```env
   DISCORD_TOKEN=your_bot_token_here
   ```

4. **Run the bot**
   ```bash
   python app.py
   ```

## Discord Application Setup

In the [Discord Developer Portal](https://discord.com/developers/applications):

1. Create a new application and add a bot.
2. Enable required privileged intents:
   - **SERVER MEMBERS INTENT**
   - **MESSAGE CONTENT INTENT**
   - **PRESENCE INTENT**
3. Generate an invite URL with:
   - Scopes: `bot`, `applications.commands`
   - Permissions: `Send Messages`, `Use Slash Commands`, `Read Messages/View Channels`

## Configuration & Data

- Configuration is stored in `config.json`.
- Data is organized per guild (server):
  - target user ID
  - cooldown value
  - selected language

## Project Structure

- `app.py` — main bot logic and slash command handlers
- `translations.py` — i18n dictionary and localized text formatting
- `config.json` — runtime configuration persistence
- `requirements.txt` — Python dependencies

## Notes

- This bot uses server-level cooldown, not per-user cooldown.
- If the target user disables DMs, notification delivery may fail.
- Admin permissions are required for setup commands.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE).


