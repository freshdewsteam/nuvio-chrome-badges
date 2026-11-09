"""Chrome: plate-free premium style. Polished-metal wordmarks floating over the artwork,
gold metal for Hero badges, red metal for warnings, coloured tracking-wide captions."""
from render import STYLES, FALLBACK

CHROME = "linear-gradient(180deg,#ffffff 0%,#f1f4f8 30%,#c3c9d2 48%,#7d8591 52%,#c9ced6 72%,#ffffff 100%)"
GOLD = "linear-gradient(180deg,#fffbe9 0%,#ffe9a8 30%,#e2b450 48%,#9a6b17 52%,#d9a845 72%,#fff1c0 100%)"
RED = "linear-gradient(180deg,#fff1ef 0%,#ffc2bb 30%,#f0645a 48%,#9e1a14 52%,#e3463c 72%,#ffcbc4 100%)"
DIM = "linear-gradient(180deg,#e9ecf0 0%,#c9ced6 40%,#8e96a2 50%,#5d6470 54%,#a8afba 78%,#dfe3e8 100%)"

STYLES["chrome"] = dict(title="Chrome", desc="No plate: polished-metal wordmarks, gold for Hero, red for warnings", icon="fill", pad=8, css="""
.badge { font-family: 'Archivo Variable', FALLBACK, sans-serif; font-stretch: 104%; height: 42px; padding: 0 6px 0 2px; gap: 10px; background: none;
  filter: drop-shadow(0 1.5px 0 rgba(0,0,0,.85)) drop-shadow(0 0 3px rgba(0,0,0,.75)); }
.main { font-weight: 900; font-size: 40px; letter-spacing: -.2px; font-style: italic; padding-right: 3px;
  background: CHROME; -webkit-background-clip: text; background-clip: text; color: transparent; }
.stack .main { font-size: 32px; }
.kicker { font-weight: 800; font-size: 15px; letter-spacing: 3.4px; color: var(--h1); margin-bottom: 1px; }
.suffix { font-weight: 800; font-size: 18px; letter-spacing: 2.6px; color: var(--h1); }
.suffix.script { font-size: 22px; letter-spacing: 0; }
.div { width: 3px; height: 30px; border-radius: 2px; transform: skewX(-12deg); background: linear-gradient(180deg, var(--h1), var(--h2)); margin: 0 10px 0 9px; }
.tile { width: 44px; height: 44px; border-radius: 12px; background: linear-gradient(150deg, var(--h1) 0%, var(--h2) 100%);
  box-shadow: inset 0 1.5px 0 rgba(255,255,255,.55), inset 0 -3px 5px rgba(0,0,0,.25); }
.tile svg { width: 27px; height: 27px; color: #fff; filter: drop-shadow(0 1px 1px rgba(0,0,0,.35)); }
.t-info .tile { background: linear-gradient(150deg,#2a2f3a 0%,#12141a 100%); box-shadow: inset 0 0 0 1.5px var(--h2b), inset 0 1.5px 0 rgba(255,255,255,.22); }
.t-info .tile svg { color: var(--h1); filter: none; }
.t-info .main { background: DIM; -webkit-background-clip: text; background-clip: text; }
.t-hero .main { background: GOLD; -webkit-background-clip: text; background-clip: text; }
.t-hero .tile { background: linear-gradient(150deg,#fff3c4 0%,#e9b949 45%,#8e6214 100%); }
.t-hero .tile svg { color: #3a2805; filter: drop-shadow(0 1px 0 rgba(255,255,255,.45)); }
.t-hero .suffix, .t-hero .kicker { color: #f5cf6e; }
.t-hero .div { background: linear-gradient(180deg,#fff0b8,#b8862b); }
.t-warn .main { background: RED; -webkit-background-clip: text; background-clip: text; }
.t-warn .tile { background: linear-gradient(150deg,#ff9d92 0%,#c81e1e 100%); }
.t-warn .suffix, .t-warn .kicker { color: #ff8f85; }
""".replace("FALLBACK", FALLBACK).replace("CHROME", CHROME).replace("GOLD", GOLD).replace("RED", RED).replace("DIM", DIM),
flag_css=".flag .tile { width: 44px; height: 44px; border-radius: 10px; box-shadow: inset 0 0 0 1.5px rgba(255,255,255,.4), inset 0 1.5px 0 rgba(255,255,255,.5) !important; }")
