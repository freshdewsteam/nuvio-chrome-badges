"""Chrome: plate-free, understated style. Soft brushed-silver wordmarks floating over the artwork,
muted gold for Hero badges, muted red for warnings, small coloured tiles. Cached is icon-only."""
from render import STYLES, FALLBACK
from spec import B

# Cached: lightning icon only, no text
for _x in B:
    if _x["id"] == "cached":
        _x["label"] = ""; _x["sub"] = None

SILVER = "linear-gradient(180deg,#ffffff 0%,#eef1f5 55%,#c4cad3 100%)"
GOLD = "linear-gradient(180deg,#fbf0cf 0%,#ecd08a 55%,#c99a3e 100%)"
RED = "linear-gradient(180deg,#ffd9d4 0%,#f39a90 55%,#d65a4f 100%)"
DIM = "linear-gradient(180deg,#dfe3e8 0%,#c3c9d1 55%,#9aa2ad 100%)"

STYLES["chrome"] = dict(title="Chrome", desc="Plate-free, understated brushed-silver wordmarks", icon="fill", pad=8, css="""
.badge { font-family: 'Archivo Variable', FALLBACK, sans-serif; font-stretch: 100%; height: 36px; padding: 0 4px 0 2px; gap: 8px; background: none;
  filter: drop-shadow(0 1px 1px rgba(0,0,0,.55)); }
.main { font-weight: 700; font-size: 24px; letter-spacing: .6px;
  background: SILVER; -webkit-background-clip: text; background-clip: text; color: transparent; }
.stack .main { font-size: 20px; }
.kicker { font-weight: 700; font-size: 10.5px; letter-spacing: 2.4px; color: var(--h1); opacity: .9; margin-bottom: 1px; }
.suffix { font-weight: 600; font-size: 13px; letter-spacing: 1.8px; color: var(--h1); opacity: .9; }
.suffix.script { font-size: 16px; letter-spacing: 0; }
.div { width: 1.5px; height: 18px; border-radius: 1px; background: rgba(255,255,255,.35); margin: 0 8px 0 7px; }
.txt:has(.main:empty) { display: none; }
.tile { width: 36px; height: 36px; border-radius: 9px; background: linear-gradient(160deg, var(--h1) 0%, var(--h2) 100%);
  box-shadow: inset 0 1px 0 rgba(255,255,255,.35); }
.tile svg { width: 21px; height: 21px; color: #fff; }
.t-info .tile { background: rgba(28,31,38,.92); box-shadow: inset 0 0 0 1px var(--h2b); }
.t-info .tile svg { color: var(--h1); }
.t-info .main { background: DIM; -webkit-background-clip: text; background-clip: text; }
.t-hero .main { background: GOLD; -webkit-background-clip: text; background-clip: text; }
.t-hero .tile { background: linear-gradient(160deg,#f3d688 0%,#c08b2e 100%); }
.t-hero .tile svg { color: #2e2104; }
.t-hero .suffix, .t-hero .kicker { color: #e9c874; }
.t-warn .main { background: RED; -webkit-background-clip: text; background-clip: text; }
.t-warn .tile { background: linear-gradient(160deg,#f2847a 0%,#b3261e 100%); }
.t-warn .suffix, .t-warn .kicker { color: #f0948b; }
""".replace("FALLBACK", FALLBACK).replace("SILVER", SILVER).replace("GOLD", GOLD).replace("RED", RED).replace("DIM", DIM),
flag_css=".flag .tile { width: 36px; height: 36px; border-radius: 8px; box-shadow: inset 0 0 0 1px rgba(255,255,255,.3) !important; }")
