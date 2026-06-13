#!/usr/bin/env python3
# Generates board-final3.html with semi-realistic illustrated American characters.
HEAD = "M0 -66C33 -66 54 -45 56 -13 57 11 50 33 33 47 23 56 11 62 0 62 -11 62 -23 56 -33 47 -50 33 -57 11 -56 -13 -54 -45 -33 -66 0 -66Z"

PAL = {
 'A': dict(skin='skA', light='#ffeadf', mid='#f3d2c1', shadow='#e3b49a', deep='#cf9579', blush='#ec9f86',
           brow='#5a3e2b', iris='irHazel', lip='#c5867a', lipHi='#dd9f92',
           shirt='#6f7d52', shirtSh='#5a6842', shirtHi='#8a986c',
           hair='#6b4a32', hairHi='#8a6244', hairSh='#4e3522'),
 'B': dict(skin='skB', light='#fff1ea', mid='#f6d9cb', shadow='#edc1a8', deep='#d9a588', blush='#f0a892',
           brow='#b89058', iris='irBlue', lip='#cd897c', lipHi='#e6a99b',
           shirt='#df8aa0', shirtSh='#c9758c', shirtHi='#eca3b6',
           hair='#d8b86a', hairHi='#f0d590', hairSh='#b2904a'),
 'C': dict(skin='skC', light='#9c6038', mid='#7e4c2a', shadow='#5f3a20', deep='#482a15', blush='#7a3f2a',
           brow='#140d07', iris='irBrown', lip='#7e4636', lipHi='#9a6450',
           shirt='#56627d', shirtSh='#46506a', shirtHi='#6b7794',
           hair='#15100b', hairHi='#36281c', hairSh='#241a12'),
 'D': dict(skin='skD', light='#ffefe6', mid='#f4d4c4', shadow='#e8ba9e', deep='#d49f80', blush='#ee9f88',
           brow='#4a3320', iris='irGreen', lip='#c8857a', lipHi='#e2a597',
           shirt='#c2654a', shirtSh='#aa5440', shirtHi='#d47e63',
           hair='#5a3c28', hairHi='#7e5638', hairSh='#422c1c'),
}

def eye(x, p):
    s = []
    s.append(f'<ellipse cx="{x}" cy="0" rx="12" ry="8.4" fill="#f3efe9"/>')
    s.append(f'<path d="M{x-12} -1 Q{x} -8 {x+12} -1" stroke="#d7ccc2" stroke-width="3" fill="none" opacity=".5"/>')
    s.append(f'<circle cx="{x}" cy="1" r="6.4" fill="url(#{p["iris"]})"/>')
    s.append(f'<circle cx="{x}" cy="1" r="6.4" fill="none" stroke="#3a2a1c" stroke-opacity=".35" stroke-width="1"/>')
    s.append(f'<circle cx="{x}" cy="1" r="3" fill="#1b130d"/>')
    s.append(f'<circle cx="{x-2.2}" cy="-1.2" r="1.7" fill="#fff" opacity=".9"/>')
    # upper lash line + outer flick
    s.append(f'<path d="M{x-12} -2 Q{x} -10 {x+12} -2" stroke="#241812" stroke-width="2.6" fill="none" stroke-linecap="round"/>')
    s.append(f'<path d="M{x+11} -2 q5 -1 7 1" stroke="#241812" stroke-width="2.2" fill="none" stroke-linecap="round"/>')
    # lower lid + crease
    s.append(f'<path d="M{x-10} 6 Q{x} 9 {x+10} 6" stroke="{p["deep"]}" stroke-width="1.4" fill="none" opacity=".6"/>')
    s.append(f'<path d="M{x-11} -8 Q{x} -13 {x+11} -8.5" stroke="{p["deep"]}" stroke-width="1.4" fill="none" opacity=".45"/>')
    return ''.join(s)

def face(key, x, y, hairback, hairfront, extras):
    p = PAL[key]
    g = [f'<g transform="translate({x},{y}) scale(.82)">']
    # contact shadow
    g.append('<ellipse cx="0" cy="120" rx="92" ry="24" fill="#021560" opacity=".3" filter="url(#blurM)"/>')
    # hair back
    g.append(hairback.format(**p))
    # shoulders
    g.append(f'<path d="M-96 132 C-96 78 -52 60 0 60 C52 60 96 78 96 132 Z" fill="{p["shirt"]}"/>')
    g.append(f'<ellipse cx="0" cy="66" rx="44" ry="18" fill="{p["shirtSh"]}" opacity=".55" filter="url(#blurM)"/>')
    g.append(f'<ellipse cx="-44" cy="92" rx="26" ry="30" fill="{p["shirtHi"]}" opacity=".3" filter="url(#blurM)"/>')
    # neck + shadow
    g.append(f'<path d="M-17 40 C-17 58 -13 66 0 70 C13 66 17 58 17 40 C10 49 -10 49 -17 40Z" fill="{p["mid"]}"/>')
    g.append(f'<ellipse cx="0" cy="44" rx="21" ry="11" fill="{p["deep"]}" opacity=".4" filter="url(#blurS)"/>')
    # ears
    for ex in (-55, 55):
        g.append(f'<ellipse cx="{ex}" cy="4" rx="10" ry="15" fill="{p["mid"]}"/>')
        g.append(f'<path d="M{ex*0.82} -4 q{-6 if ex<0 else 6} 8 0 16" stroke="{p["shadow"]}" stroke-width="2" fill="none" opacity=".5"/>')
    # face base + shading (clipped)
    g.append('<g clip-path="url(#fc)">')
    g.append(f'<path d="{HEAD}" fill="url(#{p["skin"]})"/>')
    g.append(f'<ellipse cx="34" cy="6" rx="30" ry="46" fill="{p["shadow"]}" opacity=".45" filter="url(#blurM)"/>')   # right cheek shadow
    g.append(f'<ellipse cx="-40" cy="0" rx="20" ry="40" fill="{p["shadow"]}" opacity=".28" filter="url(#blurM)"/>')  # left edge
    g.append(f'<ellipse cx="0" cy="44" rx="30" ry="18" fill="{p["deep"]}" opacity=".3" filter="url(#blurM)"/>')      # jaw/chin
    g.append(f'<ellipse cx="-16" cy="-26" rx="24" ry="18" fill="{p["light"]}" opacity=".55" filter="url(#blurM)"/>') # forehead hl
    g.append(f'<ellipse cx="-22" cy="14" rx="15" ry="18" fill="{p["light"]}" opacity=".4" filter="url(#blurS)"/>')   # cheek hl
    g.append(f'<ellipse cx="0" cy="6" rx="7" ry="24" fill="{p["light"]}" opacity=".4" filter="url(#blurS)"/>')       # nose bridge hl
    g.append(f'<path d="M3 -2 C9 8 9 16 6 21 C4 15 2 7 2 -2Z" fill="{p["shadow"]}" opacity=".4" filter="url(#blurS)"/>') # nose side shadow
    g.append(f'<ellipse cx="20" cy="24" rx="12" ry="8" fill="{p["blush"]}" opacity=".28" filter="url(#blurS)"/>')
    g.append(f'<ellipse cx="-20" cy="24" rx="12" ry="8" fill="{p["blush"]}" opacity=".28" filter="url(#blurS)"/>')
    g.append('</g>')
    # brows
    g.append(f'<path d="M-34 -20 C-26 -27 -14 -27 -6 -22 C-14 -24 -26 -23 -33 -16 Z" fill="{p["brow"]}"/>')
    g.append(f'<path d="M34 -20 C26 -27 14 -27 6 -22 C14 -24 26 -23 33 -16 Z" fill="{p["brow"]}"/>')
    # eyes
    g.append(eye(-20, p)); g.append(eye(20, p))
    # nose tip + nostrils
    g.append(f'<ellipse cx="0" cy="16" rx="4.5" ry="5.5" fill="{p["light"]}" opacity=".4" filter="url(#blurS)"/>')
    g.append(f'<ellipse cx="0" cy="21" rx="9" ry="4" fill="{p["deep"]}" opacity=".28" filter="url(#blurS)"/>')
    g.append(f'<ellipse cx="-5" cy="21" rx="2.3" ry="1.7" fill="{p["deep"]}" opacity=".5"/>')
    g.append(f'<ellipse cx="5" cy="21" rx="2.3" ry="1.7" fill="{p["deep"]}" opacity=".5"/>')
    # lips
    g.append(f'<path d="M-12 34 C-7 31 -3 32 0 33 C3 32 7 31 12 34 C7 35 4 36 0 36 C-4 36 -7 35 -12 34Z" fill="{p["lip"]}"/>')
    g.append(f'<path d="M-12 35 C-7 41 -4 44 0 44 C4 44 7 41 12 35 C7 37 4 38 0 38 C-4 38 -7 37 -12 35Z" fill="{p["lipHi"]}"/>')
    g.append(f'<path d="M-12 34.5 Q0 37 12 34.5" stroke="#00000033" stroke-width="1.3" fill="none"/>')
    g.append(f'<ellipse cx="0" cy="41" rx="5" ry="1.4" fill="#fff" opacity=".3"/>')
    # hair front
    g.append(hairfront.format(**p))
    # extras
    g.append(extras.format(**p))
    g.append('</g>')
    return ''.join(g)

# ---------- hair definitions ----------
# James: short tidy brown crop, side part
A_back = '<path d="M-50 -14 C-52 -40 -30 -54 0 -54 C30 -54 52 -40 50 -14 L46 4 L40 0 C38 -30 -38 -30 -40 0 L-46 4Z" fill="{hairSh}"/>'
A_front = ('<path d="M-50 -16 C-54 -54 -26 -72 4 -72 C32 -72 53 -52 50 -18 C44 -42 28 -50 6 -48 C0 -56 -18 -52 -32 -42 C-42 -36 -48 -28 -50 -16Z" fill="{hair}"/>'
           '<path d="M2 -66 C-14 -60 -32 -44 -40 -22" stroke="{hairSh}" stroke-width="2.5" fill="none" opacity=".5" stroke-linecap="round"/>'
           '<path d="M10 -64 C26 -57 40 -42 46 -24" stroke="{hairHi}" stroke-width="3.5" fill="none" opacity=".7" stroke-linecap="round"/>'
           '<path d="M-48 -16 L-46 6 L-39 4 L-41 -14Z" fill="{hair}"/><path d="M48 -16 L46 6 L39 4 L41 -14Z" fill="{hair}"/>')
A_extra = ('<g stroke="#181820" stroke-width="3.4" fill="none"><rect x="-39" y="-11" width="31" height="27" rx="9"/>'
           '<rect x="8" y="-11" width="31" height="27" rx="9"/><path d="M-8 0 h16 M-39 -5 h-10 M39 -5 h10"/></g>'
           '<path d="M-35 -7 l9 -2 M13 -7 l9 -2" stroke="#ffffff" stroke-opacity=".45" stroke-width="2.2" stroke-linecap="round"/>'
           '<g fill="{shadow}" opacity=".3"><circle cx="-30" cy="34" r="1.1"/><circle cx="-24" cy="40" r="1.1"/><circle cx="28" cy="35" r="1.1"/><circle cx="22" cy="41" r="1.1"/><circle cx="0" cy="52" r="1.1"/></g>')

# Blonde: long center-part
B_back = ('<path d="M-58 -16 C-62 -64 -30 -84 0 -84 C30 -84 62 -64 58 -16 C58 44 52 96 50 130 L24 130 C34 86 40 36 36 -10 C26 -46 -26 -46 -36 -10 C-40 36 -34 86 -24 130 L-50 130 C-52 96 -58 44 -58 -16Z" fill="{hair}"/>'
          '<path d="M-46 -6 C-44 40 -40 84 -38 120" stroke="{hairSh}" stroke-width="3" fill="none" opacity=".45"/>'
          '<path d="M46 -6 C44 40 40 84 38 120" stroke="{hairSh}" stroke-width="3" fill="none" opacity=".45"/>'
          '<path d="M-30 0 C-28 44 -26 88 -25 122" stroke="{hairHi}" stroke-width="2.4" fill="none" opacity=".6"/>')
B_front = ('<path d="M-52 -14 C-56 -62 -26 -82 0 -82 C26 -82 56 -62 52 -14 C44 -44 22 -52 3 -45 C1 -52 -1 -52 -3 -45 C-22 -52 -44 -44 -52 -14Z" fill="{hair}"/>'
           '<path d="M-3 -76 C-22 -68 -40 -48 -48 -22" stroke="{hairHi}" stroke-width="3" fill="none" opacity=".6" stroke-linecap="round"/>'
           '<path d="M5 -76 C24 -68 42 -48 49 -20" stroke="{hairHi}" stroke-width="3" fill="none" opacity=".55" stroke-linecap="round"/>')
B_extra = '<circle cx="-52" cy="20" r="3.2" fill="#e8c45c"/><circle cx="52" cy="20" r="3.2" fill="#e8c45c"/>'

# Black man: short fade + full beard
C_back = ''
C_front = ('<path d="M-46 -20 C-48 -52 -26 -64 0 -64 C26 -64 48 -52 46 -20 C40 -42 30 -46 0 -46 C-30 -46 -40 -42 -46 -20Z" fill="{hair}"/>'
           '<path d="M-46 -18 C-48 -8 -47 0 -46 6 M46 -18 C48 -8 47 0 46 6" stroke="{hair}" stroke-width="6" fill="none" opacity=".5"/>'
           '<path d="M-30 -50 C-12 -58 12 -58 30 -50" stroke="{hairHi}" stroke-width="2.4" fill="none" opacity=".4"/>')
C_extra = ('<path d="M-47 -4 C-47 26 -32 50 -16 59 C-8 63 8 63 16 59 C32 50 47 26 47 -4 C42 16 24 26 0 26 C-24 26 -42 16 -47 -4Z" fill="{hairSh}"/>'
           '<path d="M-46 -2 C-44 24 -30 46 -16 55 C-8 60 8 60 16 55 C30 46 44 24 46 -2 C40 18 22 28 0 28 C-22 28 -40 18 -46 -2Z" fill="#15100b"/>'
           '<path d="M-13 30 Q-6 26 0 28 Q6 26 13 30 Q6 31 0 31 Q-6 31 -13 30Z" fill="#15100b"/>')

# Brunette: shoulder-length, side-swept
D_back = ('<path d="M-56 -14 C-60 -62 -30 -82 0 -82 C30 -82 60 -62 56 -14 C56 38 50 78 48 106 L26 106 C34 74 40 30 36 -8 C26 -44 -26 -44 -36 -8 C-40 30 -34 74 -26 106 L-48 106 C-50 78 -56 38 -56 -14Z" fill="{hair}"/>'
          '<path d="M-42 -4 C-40 40 -36 76 -34 100" stroke="{hairHi}" stroke-width="2.4" fill="none" opacity=".5"/>'
          '<path d="M42 -4 C40 40 36 76 34 100" stroke="{hairSh}" stroke-width="3" fill="none" opacity=".45"/>')
D_front = ('<path d="M-52 -12 C-56 -60 -24 -80 4 -80 C32 -80 54 -56 52 -14 C44 -44 14 -50 -8 -40 C-18 -52 -42 -42 -52 -12Z" fill="{hair}"/>'
           '<path d="M3 -74 C-16 -66 -36 -46 -46 -20" stroke="{hairSh}" stroke-width="2.5" fill="none" opacity=".45" stroke-linecap="round"/>'
           '<path d="M9 -72 C26 -64 42 -46 49 -22" stroke="{hairHi}" stroke-width="3" fill="none" opacity=".6" stroke-linecap="round"/>')
D_extra = ('<g fill="{shadow}" opacity=".4"><circle cx="-26" cy="20" r="1"/><circle cx="-20" cy="25" r="1"/><circle cx="-14" cy="21" r="1"/>'
           '<circle cx="26" cy="20" r="1"/><circle cx="20" cy="25" r="1"/><circle cx="14" cy="21" r="1"/>'
           '<circle cx="-6" cy="14" r="1"/><circle cx="6" cy="14" r="1"/></g>'
           '<circle cx="-54" cy="18" r="2.6" fill="#d9b94a"/><circle cx="54" cy="18" r="2.6" fill="#d9b94a"/>')

faces = (
 face('A', 540, 347, A_back, A_front, A_extra) +
 face('B', 915, 652, B_back, B_front, B_extra) +
 face('C', 540, 957, C_back, C_front, C_extra) +
 face('D', 165, 652, D_back, D_front, D_extra)
)

DEFS = '''    <defs>
      <filter id="blurS" x="-60%" y="-60%" width="220%" height="220%"><feGaussianBlur stdDeviation="2.4"/></filter>
      <filter id="blurM" x="-80%" y="-80%" width="260%" height="260%"><feGaussianBlur stdDeviation="5"/></filter>
      <clipPath id="fc"><path d="''' + HEAD + '''"/></clipPath>
      <radialGradient id="skA" cx=".4" cy=".32" r=".85"><stop offset="0" stop-color="#ffeadf"/><stop offset="1" stop-color="#f3d2c1"/></radialGradient>
      <radialGradient id="skB" cx=".4" cy=".32" r=".85"><stop offset="0" stop-color="#fff1ea"/><stop offset="1" stop-color="#f6d9cb"/></radialGradient>
      <radialGradient id="skC" cx=".4" cy=".32" r=".85"><stop offset="0" stop-color="#9c6038"/><stop offset="1" stop-color="#6f4324"/></radialGradient>
      <radialGradient id="skD" cx=".4" cy=".32" r=".85"><stop offset="0" stop-color="#ffefe6"/><stop offset="1" stop-color="#f4d4c4"/></radialGradient>
      <radialGradient id="irHazel" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="#b9a06a"/><stop offset=".62" stop-color="#7d7a45"/><stop offset="1" stop-color="#4a4327"/></radialGradient>
      <radialGradient id="irBlue" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="#aecbe8"/><stop offset=".62" stop-color="#6f93b8"/><stop offset="1" stop-color="#3f5f86"/></radialGradient>
      <radialGradient id="irGreen" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="#9bb585"/><stop offset=".62" stop-color="#5f7a52"/><stop offset="1" stop-color="#3a4d31"/></radialGradient>
      <radialGradient id="irBrown" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="#6b4a30"/><stop offset=".62" stop-color="#3a2616"/><stop offset="1" stop-color="#1c120a"/></radialGradient>
    </defs>
'''

HTML = open('carousel/_chrome_top.html').read() + DEFS + faces + open('carousel/_chrome_bot.html').read()
open('carousel/board-final3.html','w').write(HTML)
print('wrote carousel/board-final3.html', len(HTML), 'bytes')
