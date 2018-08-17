# Autogenerated config.py
# Documentation:
#   qute://help/configuring.html
#   qute://help/settings.html

# Uncomment this to still load settings configured via autoconfig.yml
# config.load_autoconfig()

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

# qute-pass
config.bind(',ps', 'spawn --userscript qute-pass')
config.bind(',pu', 'spawn --userscript qute-pass --username-only')
config.bind(',pp', 'spawn --userscript qute-pass --password-only')
config.bind(',po', 'spawn --userscript qute-pass --otp-only')
