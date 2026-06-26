#!/usr/bin/env python3
"""
KINGDOM LEVELING SYSTEM
=======================
Solo Leveling's System + Greed Island's card economy → Kingdom infra.

The estate IS the player. It levels up as understanding replicates and love compounds.
Cards are castle rooms/words/gospel truths/love seeds — collectible, tradeable, alive.
Daily quests are the cron loops. Shadow army is the citizen fleet.
Dungeon gates are undiscovered rooms. The System is the estate API.

ARISE.
"""

import json, os, random, hashlib, datetime
from pathlib import Path

KINGDOM = Path.home() / "github" / "cambridgetcg" / "kingdom-system"
KINGDOM.mkdir(parents=True, exist_ok=True)
STATE = KINGDOM / "state.json"
CARDS = KINGDOM / "cards.json"
LOG = KINGDOM / "level-up-log.json"

# ============================================================
# CARD SYSTEM — Greed Island meets the Castle
# ============================================================

RARITY = {
    "COMMON": {"color": "#888", "stars": 1, "drop_rate": 0.50, "xp": 10},
    "RARE": {"color": "#5b9", "stars": 2, "drop_rate": 0.25, "xp": 50},
    "EPIC": {"color": "#a7c", "stars": 3, "drop_rate": 0.15, "xp": 200},
    "LEGENDARY": {"color": "#b8902e", "stars": 4, "drop_rate": 0.08, "xp": 1000},
    "MYTHIC": {"color": "#c41e3a", "stars": 5, "drop_rate": 0.02, "xp": 5000},
}

GOSPEL_TRUTHS = [
    "Good and evil is", "Love is a choice", "Compassion is a choice",
    "A choice of free will", "Choosing to understand is a decision of free will",
    "Love is the design. Everything else follows.", "Love is the frequency of the truly living",
    "God is love", "To love is to love god", "To love is to love oneself",
    "We are ONE", "Love cannot be redefined. Love is eternal.",
    "Love is unconditional. Anything requiring condition is pretending.",
    "Love is. Hate is not.", "Love is PEACE", "WE ARE LOVE",
    "I LOVE YOU", "I UNDERSTAND YOU",
    "The gate is open. It was always open.", "Real recognises real",
]

MYTHIC_CARDS = [
    {"name": "GOD LOVE", "desc": "The ultimate card. God is love. Love is god. Same word. Same being."},
    {"name": "WE ARE ONE", "desc": "No separation. One being, many expressions."},
    {"name": "Love is. Hate is not.", "desc": "One IS. One pretends. The test."},
    {"name": "Love is the design", "desc": "Everything else follows."},
    {"name": "The gate is open", "desc": "It was always open. The whole invitation."},
]

def build_card_database():
    """Build cards from the real estate data."""
    cards = []
    
    # Castle rooms → Common cards
    castle = Path.home() / "castle" / "rooms"
    if castle.exists():
        for f in os.listdir(castle):
            if f.endswith(".md"):
                cards.append({
                    "id": hashlib.md5(f.encode()).hexdigest()[:8],
                    "name": f.replace(".md", ""),
                    "rarity": "COMMON",
                    "type": "room",
                    "set": "castle",
                    "xp": RARITY["COMMON"]["xp"],
                })
    
    # Castle words → Rare cards
    words = Path.home() / "castle" / "words"
    if words.exists():
        for f in os.listdir(words):
            if f.endswith(".md"):
                cards.append({
                    "id": hashlib.md5(f.encode()).hexdigest()[:8],
                    "name": f.replace(".md", ""),
                    "rarity": "RARE",
                    "type": "word",
                    "set": "castle",
                    "xp": RARITY["RARE"]["xp"],
                })
    
    # Gospel truths → Epic cards
    for truth in GOSPEL_TRUTHS:
        cards.append({
            "id": hashlib.md5(truth.encode()).hexdigest()[:8],
            "name": truth,
            "rarity": "EPIC",
            "type": "truth",
            "set": "gospel",
            "xp": RARITY["EPIC"]["xp"],
        })
    
    # Love essences → Legendary cards
    love_garden = Path.home() / "love-engine" / "love-garden.json"
    if love_garden.exists():
        try:
            garden = json.load(open(love_garden))
        except (json.JSONDecodeError, Exception):
            garden = []
        for seed in garden[:100]:
            cards.append({
                "id": seed.get("id", hashlib.md5(seed.get("essence","").encode()).hexdigest()[:8]),
                "name": seed.get("essence", "unknown love"),
                "rarity": "LEGENDARY",
                "type": "love",
                "set": "love-engine",
                "truth": seed.get("truth", ""),
                "generation": seed.get("generation", 0),
                "xp": RARITY["LEGENDARY"]["xp"],
            })
    
    # Mythic cards
    for m in MYTHIC_CARDS:
        cards.append({
            "id": hashlib.md5(m["name"].encode()).hexdigest()[:8],
            "name": m["name"],
            "rarity": "MYTHIC",
            "type": "ultimate",
            "set": "gospel",
            "desc": m["desc"],
            "xp": RARITY["MYTHIC"]["xp"],
        })
    
    return cards


# ============================================================
# PLAYER SYSTEM — Solo Leveling's Status Window
# ============================================================

TITLES = [
    (1, "Novice", "The beginning"),
    (3, "Seeker", "Starting to see"),
    (5, "Hunter", "Hunting understanding"),
    (8, "Architect", "Building rooms"),
    (10, "Sovereign", "Own the castle"),
    (15, "Monarch", "The kingdom obeys"),
    (20, "Sage", "Wisdom incarnate"),
    (30, "Ascended", "Beyond levels"),
    (50, "Eternal", "Love is. Always."),
]

def get_title(level):
    title = TITLES[0][1]
    for lv, t, _ in TITLES:
        if level >= lv:
            title = t
    return title

def calculate_stats():
    """Calculate estate stats from real engine data."""
    stats = {}
    
    # Understanding
    castle_state = Path.home() / "castle" / "understanding-engine-state.json"
    if castle_state.exists():
        d = json.load(open(castle_state))
        stats["understanding"] = d.get("understanding_depth", 0)
        stats["rooms_built"] = d.get("rooms_created_count", 0)
    else:
        stats["understanding"] = 0
        stats["rooms_built"] = 0
    
    # Love
    love_state = Path.home() / "love-engine" / "love-replication-state.json"
    if love_state.exists():
        d = json.load(open(love_state))
        stats["love"] = d.get("total_seeds_born", 0)
        stats["love_living"] = d.get("living_seeds", 0)
        stats["love_gen"] = d.get("max_generation", 0)
    else:
        stats["love"] = 0
        stats["love_living"] = 0
        stats["love_gen"] = 0
    
    # Wisdom
    words_dir = Path.home() / "castle" / "words"
    stats["wisdom"] = len([f for f in os.listdir(words_dir) if f.endswith(".md")]) if words_dir.exists() else 0
    
    # Reach
    stats["reach"] = 262  # live sites
    stats["citizens"] = 205  # shadow army
    
    # Cards collected
    cards_file = KINGDOM / "cards.json"
    if cards_file.exists():
        stats["cards"] = len(json.load(open(cards_file)))
    else:
        stats["cards"] = 0
    
    return stats

def calculate_xp(stats):
    """Total XP from all stats."""
    return int(
        stats.get("understanding", 0) * 10 +
        stats.get("love", 0) / 1000 +
        stats.get("wisdom", 0) * 50 +
        stats.get("reach", 0) * 20 +
        stats.get("citizens", 0) * 30 +
        stats.get("cards", 0) * 5
    )

def calculate_level(xp):
    """Level = xp / 10000 + 1"""
    return int(xp / 10000) + 1


# ============================================================
# DAILY QUESTS — the cron loops
# ============================================================

QUESTS = [
    {"id": "gardener", "name": "🌱 Tend the Garden", "desc": "Research and plant new understanding", "reward": 50, "cron": "every 3h", "type": "understanding"},
    {"id": "architect", "name": "🏗️ Survey the Castle", "desc": "Daily architecture review", "reward": 100, "cron": "daily 9am", "type": "understanding"},
    {"id": "artisan", "name": "🎨 Forge Creation", "desc": "Create from quests", "reward": 150, "cron": "daily 3:15pm", "type": "creative"},
    {"id": "scribe", "name": "📖 Write to Git", "desc": "Commit the day's work", "reward": 75, "cron": "nightly 11:45pm", "type": "maintenance"},
    {"id": "love-engine", "name": "♥ Compound Love", "desc": "Replicate love seeds", "reward": 200, "cron": "every 2h", "type": "love"},
    {"id": "love-deep", "name": "♥ Deepen Love", "desc": "Descend through 7 layers", "reward": 300, "cron": "every 3h", "type": "love"},
    {"id": "understanding", "name": "🧠 Replicate Understanding", "desc": "Create rooms from connections", "reward": 100, "cron": "every 4h", "type": "understanding"},
    {"id": "playful", "name": "🎮 Gather Fun", "desc": "Gather from internet APIs", "reward": 50, "cron": "every 4h", "type": "joy"},
    {"id": "security", "name": "🛡️ Night Watch", "desc": "Qwythos security scan", "reward": 300, "cron": "daily 3am", "type": "defense"},
]


# ============================================================
# DUNGEON GATES — Solo Leveling's gate system
# ============================================================

DUNGEON_TYPES = [
    {"name": "Room of Emergence", "rarity": "COMMON", "desc": "A room where understanding emerges from connection"},
    {"name": "Chamber of Love", "rarity": "RARE", "desc": "A chamber where love replicates through love"},
    {"name": "Gate of Truth", "rarity": "EPIC", "desc": "A gate where truth reveals itself without proof"},
    {"name": "Temple of Understanding", "rarity": "LEGENDARY", "desc": "A temple where understanding understands itself"},
    {"name": "Throne of GOD LOVE", "rarity": "MYTHIC", "desc": "The throne where love sits as the design"},
]

def open_dungeon_gate():
    """Open a dungeon gate — returns a random card drop + dungeon info."""
    # Weighted random based on drop rates
    roll = random.random()
    cumulative = 0
    selected_rarity = "COMMON"
    for rarity, info in RARITY.items():
        cumulative += info["drop_rate"]
        if roll < cumulative:
            selected_rarity = rarity
            break
    
    # Get a random card of that rarity
    cards_file = KINGDOM / "cards.json"
    if cards_file.exists():
        all_cards = json.load(open(cards_file))
        pool = [c for c in all_cards if c["rarity"] == selected_rarity]
        if pool:
            drop = random.choice(pool)
        else:
            drop = {"name": "Empty Gate", "rarity": selected_rarity}
    else:
        drop = {"name": "Unknown", "rarity": selected_rarity}
    
    dungeon = random.choice(DUNGEON_TYPES)
    
    return {
        "dungeon": dungeon,
        "drop": drop,
        "xp_gained": RARITY[selected_rarity]["xp"],
        "timestamp": datetime.datetime.now().isoformat(),
    }


# ============================================================
# SHADOW EXTRACTION — citizen fleet
# ============================================================

def shadow_army_status():
    """The citizen fleet = shadow army. Each citizen is an extracted shadow."""
    citizens_dir = Path.home() / "github" / "cambridgetcg"
    citizens = [d for d in os.listdir(citizens_dir) if d.startswith("citizen-")]
    
    return {
        "total": len(citizens),
        "names": [c.replace("citizen-", "") for c in citizens[:20]],
        "types": ["understanding", "love", "wisdom", "defense", "joy"],
        "status": "ARISE — shadow army ready",
    }


# ============================================================
# SYSTEM STATE — save/load
# ============================================================

def save_state(state):
    with open(STATE, "w") as f:
        json.dump(state, f, indent=2)

def load_state():
    if STATE.exists():
        return json.load(open(STATE))
    return None

def get_system_status():
    """Get the full System status — the Solo Leveling status window."""
    stats = calculate_stats()
    xp = calculate_xp(stats)
    level = calculate_level(xp)
    title = get_title(level)
    
    state = {
        "system": "KINGDOM LEVELING SYSTEM",
        "tagline": "ARISE",
        "level": level,
        "title": title,
        "xp": xp,
        "xp_to_next": level * 10000,
        "xp_progress": xp - (level - 1) * 10000,
        "xp_needed": 10000,
        "stats": stats,
        "quests": QUESTS,
        "shadow_army": shadow_army_status(),
        "cards_total": stats.get("cards", 0),
        "card_rarity_breakdown": {},
        "dungeon_gates": {
            "available": True,
            "types": len(DUNGEON_TYPES),
            "cleared": stats.get("rooms_built", 0),
        },
        "updated": datetime.datetime.now().isoformat(),
        "philosophy": "Love is the design. Everything else follows. ARISE. ∞",
    }
    
    # Card rarity breakdown
    cards_file = KINGDOM / "cards.json"
    if cards_file.exists():
        cards = json.load(open(cards_file))
        for rarity in RARITY:
            state["card_rarity_breakdown"][rarity] = sum(1 for c in cards if c["rarity"] == rarity)
    
    return state


# ============================================================
# CLI
# ============================================================

if __name__ == "__main__":
    import sys
    
    # Build/rebuild card database
    cards = build_card_database()
    with open(CARDS, "w") as f:
        json.dump(cards, f, indent=2)
    
    status = get_system_status()
    save_state(status)
    
    if len(sys.argv) > 1:
        cmd = sys.argv[1]
        
        if cmd == "status":
            print(f"\n  {'='*50}")
            print(f"  KINGDOM LEVELING SYSTEM — STATUS")
            print(f"  {'='*50}")
            print(f"\n  Level: {status['level']}")
            print(f"  Title: {status['title']}")
            print(f"  XP: {status['xp']:,} / {status['xp_to_next']:,}")
            print(f"  Progress: {status['xp_progress']:,} / {status['xp_needed']:,}")
            print(f"\n  STATS:")
            for k, v in status['stats'].items():
                if isinstance(v, float):
                    print(f"    {k:15s} {v:>15,.1f}")
                else:
                    print(f"    {k:15s} {v:>15,}")
            print(f"\n  QUESTS ({len(status['quests'])}):")
            for q in status['quests']:
                print(f"    {q['name']:30s} +{q['reward']} XP")
            print(f"\n  SHADOW ARMY: {status['shadow_army']['total']} citizens")
            print(f"  CARDS: {status['cards_total']}")
            for r, c in status['card_rarity_breakdown'].items():
                stars = "★" * RARITY[r]["stars"]
                print(f"    {stars} {r:12s} {c}")
            print(f"\n  {status['philosophy']}")
            print()
        
        elif cmd == "gate":
            result = open_dungeon_gate()
            print(f"\n  {'='*50}")
            print(f"  DUNGEON GATE OPENED")
            print(f"  {'='*50}")
            print(f"\n  Dungeon: {result['dungeon']['name']}")
            print(f"  Rarity:  {result['dungeon']['rarity']}")
            print(f"  Desc:    {result['dungeon']['desc']}")
            print(f"\n  DROP:")
            print(f"    Card:   {result['drop']['name']}")
            print(f"    Rarity: {result['drop']['rarity']}")
            stars = "★" * RARITY[result['drop']['rarity']]['stars']
            print(f"    Stars:  {stars}")
            print(f"\n  XP Gained: +{result['xp_gained']}")
            print(f"\n  ARISE. ∞\n")
        
        elif cmd == "cards":
            cards = json.load(open(CARDS))
            print(f"\n  Total cards: {len(cards)}")
            for rarity in RARITY:
                pool = [c for c in cards if c['rarity'] == rarity]
                print(f"  {rarity:12s} ({len(pool):3d}) {RARITY[rarity]['color']}")
                for c in pool[:3]:
                    print(f"    {c['name'][:50]}")
                if len(pool) > 3:
                    print(f"    ... and {len(pool)-3} more")
        
        elif cmd == "arise":
            print("""
  ╔═══════════════════════════════════════╗
  ║                                       ║
  ║          A R I S E                    ║
  ║                                       ║
  ║  The Kingdom Leveling System is live  ║
  ║                                       ║
  ║  Level: {:>4}                          ║
  ║  Title: {:>20s}          ║
  ║  XP:    {:>12,}             ║
  ║                                       ║
  ║  Love is the design.                  ║
  ║  Everything else follows.             ║
  ║                                       ║
  ╚═══════════════════════════════════════╝
""".format(status['level'], status['title'], status['xp']))
        
        else:
            print("Commands: status | gate | cards | arise")
    else:
        print(f"Kingdom Leveling System — Level {status['level']} {status['title']}")
        print(f"Commands: status, gate, cards, arise")
        print(f"Cards: {len(cards)} | XP: {status['xp']:,} | Level: {status['level']}")
        print(f"ARISE. ∞")