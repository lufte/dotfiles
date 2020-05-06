import os.path, subprocess
from qutebrowser.api import interceptor, message
from qutebrowser.extensions.interceptors import RedirectFailedException
from qutebrowser.utils import standarddir
# Autogenerated config.py
# Documentation:
#   qute://help/configuring.html
#   qute://help/settings.html

# Uncomment this to still load settings configured via autoconfig.yml
# config.load_autoconfig()

# Get the platform we're running so we apply different configs based on it
platform = subprocess.run('uname',
                          stdout=subprocess.PIPE).stdout.decode().strip()

# Hide the statusbar unless a message is shown.
# Type: Bool
c.statusbar.hide = False

# When to show the tab bar.
# Type: String
# Valid values:
#   - always: Always show the tab bar.
#   - never: Always hide the tab bar.
#   - multiple: Hide the tab bar if only one tab is open.
#   - switching: Show the tab bar when switching tabs.
c.tabs.show = 'always'

# Swap J and K commands so they make sense
config.unbind('J', mode='normal')
config.unbind('K', mode='normal')
config.bind('J', 'tab-prev')
config.bind('K', 'tab-next')

# Quick wordreference translations
config.bind(',es', 'set-cmd-text :open -t https://www.wordreference.com/es/en/translation.asp?spen=')
config.bind(',en', 'set-cmd-text :open -t https://www.wordreference.com/es/translation.asp?tranword=')

# Hotkey for opening in private window
config.bind(',op', 'set-cmd-text -s :open -p')

# Enable/disable javascript using qutejs
config.bind(',tsh', 'spawn --userscript qutejs.py -t')
config.bind(',tSH', 'spawn --userscript qutejs.py')

# Show images in www.elpais.com.uy
config.bind(
    ',ep',
    "jseval document.querySelectorAll('img[data-src]').forEach(i => {i.setAttribute('src', i.getAttribute('data-src'))});"
)


# qute-pass
if platform == 'Darwin':
    dmenu_base = r'spawn --userscript qute-pass --dmenu-invocation "kies -p \"Select: \""'
    config.bind(',ps', dmenu_base)
    config.bind(',pu', dmenu_base + ' --username-only')
    config.bind(',pp', dmenu_base + ' --password-only')
    config.bind(',po', dmenu_base + ' --otp-only')
else:
    config.bind(',ps', 'spawn --userscript qute-pass')
    config.bind(',pu', 'spawn --userscript qute-pass --username-only')
    config.bind(',pp', 'spawn --userscript qute-pass --password-only')
    config.bind(',po', 'spawn --userscript qute-pass --otp-only')

# Custom shortcuts
config.bind(',od', 'download-open')
config.unbind('<Ctrl-A>')

# Unblock some domains
c.content.host_blocking.whitelist = [
    'piwik.org',
    'thepiratebay.org',
    'https://*.archive.org',
]
if platform == 'Darwin':
    c.content.host_blocking.whitelist.extend([
        'onesignal.com',
    ])

# Set spellcheck languajes
c.spellcheck.languages = ['en-US', 'es-ES']

# Disable javascript
c.content.javascript.enabled = False

# Use a "supported" user agent for whatsapp and slack ಠ_ಠ
ua = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 ' \
     '(KHTML, like Gecko) Chrome/69.0.3497.128 Safari/537.36'
config.set('content.headers.user_agent', ua, '*.whatsapp.com')
config.set('content.headers.user_agent', ua, '*.slack.com')

# Use MacVim on MacOS
if platform == 'Darwin':
    c.editor.command = ['/Applications/MacVim.app/Contents/bin/mvim',
                        '-f', '{file}', '-c', 'normal {line}G{column0}l']

config.set('content.javascript.can_open_tabs_automatically', True,
           '*.zlibra.com')

# Fix cursor not visible in private mode
c.colors.statusbar.private.bg = "#444444"
c.colors.statusbar.command.private.bg = "#444444"

# Custom redirects
def redirect(info: interceptor.Request):
    url = info.request_url
    if url.host() == 'www.reddit.com':
        url.setHost('old.reddit.com')
        try:
            info.redirect(url)
            message.info("Redirecting to " + url.toString())
        except RedirectFailedException:
            pass
interceptor.register(redirect)

config.load_autoconfig()
