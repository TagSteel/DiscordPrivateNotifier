"""
Translation system for GlouGlouBot
Supports English (default) and French
"""

TRANSLATIONS = {
    'en': {
        # Bot events
        'bot_connected': '✅ Bot connected as {name} (ID: {id})',
        'commands_synced': '✅ {count} slash command(s) synced',
        'sync_error': '❌ Error syncing commands: {error}',
        
        # Set target command
        'target_set': "✅ **{user}** is now set as the target for the /deepthroat command!",
        
        # Set cooldown command
        'cooldown_min_error': "❌ Cooldown must be at least 1 second.",
        'cooldown_max_error': "❌ Cooldown cannot exceed 86400 seconds (24 hours).",
        'cooldown_set': "✅ The /deepthroat command cooldown is now **{time_str}** ({seconds}s).",
        
        # View cooldown command
        'cooldown_current': "⏱️ The current cooldown for /deepthroat is **{time_str}** ({seconds}s).",
        'cooldown_view_ready': "✅ The command is ready to use!",
        'cooldown_view_remaining': "⏱️ Remaining time: **{time_str}**.",
        
        # Set language command
        'language_set': "✅ Language set to **{language}** for this server!",
        'language_invalid': "❌ Invalid language. Available languages: en (English), fr (French).",
        
        # Main command
        'cooldown_active': "⏱️ This command is on cooldown for the server. Wait **{time_str}** more before using it again.",
        'no_target_set': "❌ No target has been set for this server. An administrator must use `/settarget` first.",
        'target_not_found': "❌ The target user is no longer on this server. An administrator must reset the target with `/settarget`.",
        'mention_title': "📬 You have been mentioned!",
        'mention_description': "**{author}** pinged you via /deepthroat",
        'mention_server': "🏠 Server",
        'mention_channel': "💬 Channel",
        'mention_by': "👤 By",
        'mention_success': "✅ **{author}** pinged **{target}** via /deepthroat! 📬",
        'dm_forbidden': "❌ Cannot send a private message to **{user}**. The user may have disabled private messages.",
        'user_dnd': "❌ **{user}** is in Do Not Disturb mode and cannot be disturbed.",
        'general_error': "❌ An error occurred while sending the message.",
        
        # Time formatting
        'seconds': "second(s)",
        'minutes': "minute(s)",
        'hours': "hour(s)",
        'and': "and",
        
        # Command descriptions
        'cmd_settarget_desc': "Set the user who will receive notifications (Admin only)",
        'cmd_settarget_param': "The user who will receive the pings",
        'cmd_setcooldown_desc': "Set the cooldown for the /deepthroat command (Admin only)",
        'cmd_setcooldown_param': "Cooldown duration in seconds (minimum: 1, maximum: 86400)",
        'cmd_viewsetcooldown_desc': "Display the configured cooldown for the server",
        'cmd_viewcooldown_desc': "Display the remaining cooldown before the next use",
        'cmd_setlanguage_desc': "Set the bot language for this server (Admin only)",
        'cmd_setlanguage_param': "Language (en for English, fr for French)",
        'cmd_deepthroat_desc': "Send a private notification to the target user",
    },
    'fr': {
        # Bot events
        'bot_connected': '✅ Bot connecté en tant que {name} (ID: {id})',
        'commands_synced': '✅ {count} commande(s) slash synchronisée(s)',
        'sync_error': '❌ Erreur lors de la synchronisation des commandes: {error}',
        
        # Set target command
        'target_set': "✅ **{user}** est maintenant défini comme cible pour la commande /gorgeprofonde !",
        
        # Set cooldown command
        'cooldown_min_error': "❌ Le cooldown doit être d'au moins 1 seconde.",
        'cooldown_max_error': "❌ Le cooldown ne peut pas dépasser 86400 secondes (24 heures).",
        'cooldown_set': "✅ Le cooldown de la commande /gorgeprofonde est maintenant de **{time_str}** ({seconds}s).",
        
        # View cooldown command
        'cooldown_current': "⏱️ Le cooldown actuel pour /gorgeprofonde est de **{time_str}** ({seconds}s).",
        'cooldown_view_ready': "✅ La commande est prête à être utilisée !",
        'cooldown_view_remaining': "⏱️ Temps restant : **{time_str}**.",
        
        # Set language command
        'language_set': "✅ Langue définie sur **{language}** pour ce serveur !",
        'language_invalid': "❌ Langue invalide. Langues disponibles : en (Anglais), fr (Français).",
        
        # Main command
        'cooldown_active': "⏱️ Cette commande est en cooldown pour le serveur. Attendez encore **{time_str}** avant de l'utiliser à nouveau.",
        'no_target_set': "❌ Aucune cible n'a été définie pour ce serveur. Un administrateur doit utiliser `/setcible` d'abord.",
        'target_not_found': "❌ L'utilisateur cible n'est plus sur ce serveur. Un administrateur doit redéfinir la cible avec `/setcible`.",
        'mention_title': "📬 Vous avez été mentionné !",
        'mention_description': "**{author}** vous a pingé via /gorgeprofonde",
        'mention_server': "🏠 Serveur",
        'mention_channel': "💬 Salon",
        'mention_by': "👤 Par",
        'mention_success': "✅ **{author}** a pingé **{target}** via /gorgeprofonde ! 📬",
        'dm_forbidden': "❌ Impossible d'envoyer un message privé à **{user}**. L'utilisateur a peut-être désactivé les messages privés.",
        'user_dnd': "❌ **{user}** est en mode Ne Pas Déranger et ne peut pas être dérangé.",
        'general_error': "❌ Une erreur s'est produite lors de l'envoi du message.",
        
        # Time formatting
        'seconds': "seconde(s)",
        'minutes': "minute(s)",
        'hours': "heure(s)",
        'and': "et",
        
        # Command descriptions
        'cmd_settarget_desc': "Définir l'utilisateur qui recevra les notifications (Admin seulement)",
        'cmd_settarget_param': "L'utilisateur qui recevra les pings",
        'cmd_setcooldown_desc': "Définir le cooldown de la commande /gorgeprofonde (Admin seulement)",
        'cmd_setcooldown_param': "Durée du cooldown en secondes (minimum: 1, maximum: 86400)",
        'cmd_viewsetcooldown_desc': "Afficher le cooldown configuré pour le serveur",
        'cmd_viewcooldown_desc': "Afficher le temps restant avant la prochaine utilisation",
        'cmd_setlanguage_desc': "Définir la langue du bot pour ce serveur (Admin seulement)",
        'cmd_setlanguage_param': "Langue (en pour Anglais, fr pour Français)",
        'cmd_deepthroat_desc': "Envoie une notification privée à l'utilisateur cible",
    }
}

def get_text(guild_id, key, **kwargs):
    """
    Get translated text for a specific guild
    
    Args:
        guild_id: Discord guild ID
        key: Translation key
        **kwargs: Format arguments for the text
        
    Returns:
        Formatted translated text
    """
    from app import load_config
    
    config = load_config()
    guild_config = config.get(str(guild_id), {})
    
    if isinstance(guild_config, dict):
        language = guild_config.get('language', 'en')
    else:
        language = 'en'
    
    # Get text from translations, fallback to English if not found
    text = TRANSLATIONS.get(language, TRANSLATIONS['en']).get(key, TRANSLATIONS['en'].get(key, key))
    
    # Format with provided arguments
    if kwargs:
        try:
            return text.format(**kwargs)
        except KeyError:
            return text
    return text

def format_time(seconds, guild_id):
    """
    Format time duration in a human-readable way
    
    Args:
        seconds: Duration in seconds
        guild_id: Discord guild ID for language preference
        
    Returns:
        Formatted time string
    """
    if seconds < 60:
        return f"{seconds} {get_text(guild_id, 'seconds')}"
    elif seconds < 3600:
        minutes = seconds // 60
        secs = seconds % 60
        result = f"{minutes} {get_text(guild_id, 'minutes')}"
        if secs > 0:
            result += f" {get_text(guild_id, 'and')} {secs} {get_text(guild_id, 'seconds')}"
        return result
    else:
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        result = f"{hours} {get_text(guild_id, 'hours')}"
        if minutes > 0:
            result += f" {get_text(guild_id, 'and')} {minutes} {get_text(guild_id, 'minutes')}"
        return result
