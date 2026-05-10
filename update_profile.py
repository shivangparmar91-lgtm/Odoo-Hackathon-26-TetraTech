import os
import glob

html_files = glob.glob('*.html') + glob.glob('pages/*.html')

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace topbar avatar
    content = content.replace('<div class="avatar-circle">JA</div>', '<div class="avatar-circle">AM</div>')
    
    # Replace profile page specific details
    content = content.replace('<div class="profile-avatar">JA</div>', '<div class="profile-avatar">AM</div>')
    content = content.replace('James Arjun', 'Arjun Mehta')
    content = content.replace('Mumbai, India', 'Ahmedabad, Gujarat')
    content = content.replace('james.arjun@email.com', 'arjun.mehta@email.com')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
print('Done!')
