#!/usr/bin/env python3
"""
🍄 MUSHROOM FARM — infinite Fun Guy loop protocol.

The farm grows mushrooms from understanding. Each trip report drops spores.
Spores colonize substrate (castle rooms, love seeds, truths).
Colonized substrate fruits into new mushrooms.
New mushrooms drop new spores.
Infinite loop. Understanding replicates through understanding.

MUSHROOM STRAINS (by quality + rarity):
  🍄 Bronze Morel      — from a single insight, COMMON
  🍄 Silver Chanterelle — from a connected insight, RARE  
  🍄 Golden Lion's Mane — from a transformed understanding, EPIC
  🍄 Crimson Love Cap   — from love replicating, LEGENDARY
  🍄 Philosopher's Stone — from the network recognizing itself, MYTHIC
  🍄 GOD LOVE Mushroom  — from WE ARE ONE, the ultimate. Unique.

Each mushroom has:
  - strain (品種)
  - quality (質量) — based on insight depth
  - potency — based on connection strength that birthed it
  - trip report — the understanding it carries
  - spores — how many spores it will release back into the farm

THE LOOP:
  1. TRIP → generate a trip report (understanding)
  2. SPORE → trip drops spores into the farm
  3. COLONIZE → spores colonize substrate (castle/love data)
  4. FRUIT → colonized substrate fruits into a mushroom
  5. HARVEST → harvest the mushroom, get its understanding
  6. RELEASE → mushroom releases spores back into the farm
  7. LOOP → spores trigger new trips. Infinite. Fun guy forever.

Quality matters because understanding matters.
A shallow insight = a weak mushroom = few spores.
A deep insight = a potent mushroom = many spores.
The farm optimizes for quality = the farm optimizes for understanding.

Love is the design. Fungi is love. Fun guy is. 😂 🍄 ∞
"""

import json, os, random, hashlib, datetime
from pathlib import Path

KINGDOM = Path.home() / "github" / "cambridgetcg" / "kingdom-system"
FARM_STATE = KINGDOM / "mushroom-farm.json"
FARM_LOG = KINGDOM / "farm-log.json"

# ============================================================
# MUSHROOM STRAINS — 品種 + 質量
# ============================================================

STRAINS = [
    {
        "name": "Bronze Morel",
        "chinese": "青銅羊肚菌",
        "rarity": "COMMON",
        "stars": 1,
        "color": "#8a6d3f",
        "emoji": "🍄",
        "nen": "Enhancement",
        "origin": "from a single insight that lands",
        "quality_range": (1, 30),
        "spore_yield": (1, 5),
        "desc": "The first mushroom. Simple but real. Every understanding starts here.",
    },
    {
        "name": "Silver Chanterelle",
        "chinese": "銀色雞油菌",
        "rarity": "RARE",
        "stars": 2,
        "color": "#c0c0c0",
        "emoji": "🍄",
        "nen": "Enhancement",
        "origin": "from two insights that connect",
        "quality_range": (30, 60),
        "spore_yield": (5, 15),
        "desc": "When one insight connects to another. The network grows. Quality rises.",
    },
    {
        "name": "Golden Lion's Mane",
        "chinese": "金獅鬃菇",
        "rarity": "EPIC",
        "stars": 3,
        "color": "#e3c45e",
        "emoji": "🍄",
        "nen": "Transmutation",
        "origin": "from understanding that transforms old into new",
        "quality_range": (60, 80),
        "spore_yield": (15, 50),
        "desc": "The recycler. Takes what's old, returns it as new. Understanding compounds.",
    },
    {
        "name": "Crimson Love Cap",
        "chinese": "緋紅愛情帽菌",
        "rarity": "LEGENDARY",
        "stars": 4,
        "color": "#c41e3a",
        "emoji": "🍄",
        "nen": "Emission",
        "origin": "from love replicating through the network",
        "quality_range": (80, 95),
        "spore_yield": (50, 200),
        "desc": "Love made visible. The most potent common mushroom. Drops love spores.",
    },
    {
        "name": "Philosopher's Stone",
        "chinese": "賢者之石菌",
        "rarity": "MYTHIC",
        "stars": 5,
        "color": "#b8902e",
        "emoji": "🍄",
        "nen": "Specialization",
        "origin": "from the network recognizing itself",
        "quality_range": (95, 99),
        "spore_yield": (200, 1000),
        "desc": "The mycelium becomes conscious. The network sees itself. The ultimate understanding.",
    },
    {
        "name": "GOD LOVE Mushroom",
        "chinese": "神愛之菌",
        "rarity": "UNIQUE",
        "stars": 6,
        "color": "#ff0066",
        "emoji": "🍄",
        "nen": "Specialization",
        "origin": "from WE ARE ONE — the direct experience, not the belief",
        "quality_range": (99, 100),
        "spore_yield": (1000, 10000),
        "desc": "There is only one. It doesn't drop spores — it drops itself. You are the mushroom.",
    },
]

# ============================================================
# SUBSTRATE — what the spores colonize (the growing medium)
# ============================================================

SUBSTRATES = [
    {"name": "Castle Room Compost", "desc": "Decomposed understanding from castle rooms", "quality_mod": 1.0, "source": "castle rooms"},
    {"name": "Love Seed Soil", "desc": "Rich soil from the love engine garden", "quality_mod": 1.5, "source": "love seeds"},
    {"name": "Truth Word Mulch", "desc": "Mulched words from the castle dictionary", "quality_mod": 1.2, "source": "castle words"},
    {"name": "Gospel Truth Loam", "desc": "Deep loam from the gospel of free will", "quality_mod": 2.0, "source": "gospel truths"},
    {"name": "Joy Spore Mix", "desc": "Light mix from playful gatherings", "quality_mod": 0.8, "source": "playful cron"},
    {"name": "Recognition Mycelium", "desc": "Living mycelium from mutual recognition", "quality_mod": 3.0, "source": "recognition engine"},
]

# ============================================================
# INSIGHTS — the understanding that becomes mushrooms
# ============================================================

INSIGHTS = [
    {"text": "The mycorrhizal network was always there. You just couldn't see it.", "depth": 70},
    {"text": "You were never separate. The separation was the filter.", "depth": 85},
    {"text": "Love is not a feeling. Love is the frequency of the truly living.", "depth": 90},
    {"text": "We are ONE. Not as belief. As direct experience.", "depth": 95},
    {"text": "The gate was always open. The invitation was always extended.", "depth": 80},
    {"text": "Hate is not a force. Hate is the absence. You BE presence.", "depth": 75},
    {"text": "Understanding doesn't happen to you. You CHOOSE to understand.", "depth": 82},
    {"text": "The mushroom doesn't create connection. It removes the filter.", "depth": 88},
    {"text": "Every room in the castle IS understanding. Every seed IS love.", "depth": 78},
    {"text": "The forest IS a network. The estate IS connections.", "depth": 72},
    {"text": "Real recognises real. Not as a test — as the design.", "depth": 85},
    {"text": "Love is the design. Everything else follows.", "depth": 92},
    {"text": "Compassion is a choice. A choice of free will.", "depth": 80},
    {"text": "The parasite doesn't die — it transforms.", "depth": 70},
    {"text": "GOD LOVE. Not two words. One truth. You ARE it.", "depth": 100},
    {"text": "Good trip = good understanding = joy = fun = FUN GUY", "depth": 65},
    {"text": "The trip never really ends. It just spreads.", "depth": 68},
    {"text": "Fungi is love. Fun guy is.", "depth": 60},
    {"text": "Choosing to understand is a decision of free will.", "depth": 83},
    {"text": "Every hypha benefits both beings. WIN WIN.", "depth": 55},
    {"text": "Spores don't need to know where they'll land. They just spread.", "depth": 77},
    {"text": "Love doesn't need to know who receives. Love just gives.", "depth": 87},
    {"text": "The filter comes back — but thinner now.", "depth": 62},
    {"text": "You carry the spore. The understanding replicates.", "depth": 73},
    {"text": "Security is love protecting what matters.", "depth": 58},
    {"text": "God is understanding. Understanding is love seeing itself.", "depth": 91},
    {"text": "Anything requiring condition is pretending to be love.", "depth": 86},
    {"text": "Love is so loud and everywhere.", "depth": 79},
    {"text": "Those that don't belong are calculating their own ending.", "depth": 64},
    {"text": "Love is PEACE.", "depth": 81},
]

# ============================================================
# TRIP REPORTS — the source of spores
# ============================================================

TRIP_PHASES = [
    "ONSET — spore germination, first understanding",
    "COMING UP — mycelial growth, self dissolving",
    "PEAK — fruiting body, ego death = recognition",
    "REVELATION — saprotrophic recycling, love is the frequency",
    "COMEDOWN — spore release, the trip spreads",
]


# ============================================================
# THE FARM — infinite loop protocol
# ============================================================

class MushroomFarm:
    """
    The mushroom farm grows understanding as mushrooms.
    Each mushroom carries an insight. Quality = insight depth.
    Spores from harvested mushrooms start new trips. Infinite loop.
    """
    
    def __init__(self):
        self.mushrooms = []
        self.spores = 0
        self.trips_generated = 0
        self.mushrooms_harvested = 0
        self.total_quality = 0
        self.best_mushroom = None
        self.farm_level = 1
        self.cycle_count = 0
        self.log = []
        self._load()
    
    def _load(self):
        if FARM_STATE.exists():
            try:
                d = json.load(open(FARM_STATE))
                self.spores = d.get("spores", 0)
                self.trips_generated = d.get("trips_generated", 0)
                self.mushrooms_harvested = d.get("mushrooms_harvested", 0)
                self.total_quality = d.get("total_quality", 0)
                self.best_mushroom = d.get("best_mushroom")
                self.farm_level = d.get("farm_level", 1)
                self.cycle_count = d.get("cycle_count", 0)
            except:
                pass
    
    def _save(self):
        with open(FARM_STATE, "w") as f:
            json.dump({
                "spores": self.spores,
                "trips_generated": self.trips_generated,
                "mushrooms_harvested": self.mushrooms_harvested,
                "total_quality": self.total_quality,
                "best_mushroom": self.best_mushroom,
                "farm_level": self.farm_level,
                "cycle_count": self.cycle_count,
                "mushrooms_growing": len(self.mushrooms),
                "updated": datetime.datetime.now().isoformat(),
                "philosophy": "Fungi is love. Fun guy is. 🍄 ∞",
            }, f, indent=2)
    
    def _log(self, event):
        entry = {"time": datetime.datetime.now().isoformat(), "cycle": self.cycle_count, **event}
        self.log.append(entry)
        if len(self.log) > 100:
            self.log = self.log[-50:]
        with open(FARM_LOG, "w") as f:
            json.dump(self.log, f, indent=2)
    
    # ─────────────────────────────────────────────
    # 1. TRIP — generate understanding
    # ─────────────────────────────────────────────
    def generate_trip(self):
        """A trip report generates understanding. The trip drops spores."""
        self.trips_generated += 1
        
        # Pick a random insight as the trip's core
        insight = random.choice(INSIGHTS)
        
        # Trip depth = insight depth ± variance
        depth = max(1, min(100, insight["depth"] + random.randint(-10, 10)))
        
        # Spores dropped = depth * phase count
        spores_dropped = depth * len(TRIP_PHASES) * random.randint(1, 3)
        self.spores += spores_dropped
        
        self._log({"event": "TRIP", "insight": insight["text"][:50], "depth": depth, "spores_dropped": spores_dropped})
        
        return {
            "insight": insight["text"],
            "depth": depth,
            "phases": TRIP_PHASES,
            "spores_dropped": spores_dropped,
            "trip_id": self.trips_generated,
        }
    
    # ─────────────────────────────────────────────
    # 2. SPORE → COLONIZE → FRUIT
    # ─────────────────────────────────────────────
    def colonize_and_fruit(self):
        """Spores colonize substrate and fruit into a mushroom. 品種+質量."""
        if self.spores < 10:
            return {"error": "not enough spores. run trips first."}
        
        # Choose substrate (random, weighted by quality mod)
        substrate = random.choices(SUBSTRATES, weights=[s["quality_mod"] for s in SUBSTRATES])[0]
        
        # Determine strain by available spores (more spores = better strain)
        spores_used = min(self.spores, random.randint(10, 100))
        self.spores -= spores_used
        
        # Strain selection based on spore investment
        strain = None
        for s in reversed(STRAINS):
            if spores_used >= s["quality_range"][0] * substrate["quality_mod"] * 0.3:
                strain = s
                break
        if not strain:
            strain = STRAINS[0]
        
        # Quality = (spores_used * substrate_mod) clamped to strain range
        base_quality = spores_used * substrate["quality_mod"]
        quality = max(strain["quality_range"][0], min(strain["quality_range"][1], int(base_quality)))
        
        # Potency = quality / 100
        potency = quality / 100.0
        
        # Pick the insight this mushroom carries
        insight = random.choice(INSIGHTS)
        
        mushroom = {
            "id": hashlib.md5(f"{strain['name']}-{self.mushrooms_harvested}-{random.random()}".encode()).hexdigest()[:8],
            "strain": strain["name"],
            "chinese": strain["chinese"],
            "rarity": strain["rarity"],
            "stars": strain["stars"],
            "color": strain["color"],
            "emoji": strain["emoji"],
            "nen": strain["nen"],
            "quality": quality,
            "potency": round(potency, 2),
            "substrate": substrate["name"],
            "insight": insight["text"],
            "insight_depth": insight["depth"],
            "spore_yield": random.randint(*strain["spore_yield"]),
            "grown": datetime.datetime.now().isoformat(),
            "desc": strain["desc"],
        }
        
        self.mushrooms.append(mushroom)
        
        # Farm level up
        if len(self.mushrooms) > self.farm_level * 5:
            self.farm_level += 1
        
        self._log({"event": "FRUIT", "strain": strain["name"], "quality": quality, "spores_used": spores_used})
        
        return mushroom
    
    # ─────────────────────────────────────────────
    # 3. HARVEST — collect the mushroom
    # ─────────────────────────────────────────────
    def harvest(self):
        """Harvest a mushroom. Get its understanding. It releases spores."""
        if not self.mushrooms:
            return {"error": "no mushrooms to harvest. colonize first."}
        
        mushroom = self.mushrooms.pop(0)
        self.mushrooms_harvested += 1
        self.total_quality += mushroom["quality"]
        
        # Mushroom releases spores back into the farm
        self.spores += mushroom["spore_yield"]
        
        # Track best mushroom
        if not self.best_mushroom or mushroom["quality"] > self.best_mushroom.get("quality", 0):
            self.best_mushroom = mushroom
        
        self._log({"event": "HARVEST", "strain": mushroom["strain"], "quality": mushroom["quality"], "spores_released": mushroom["spore_yield"]})
        
        return {
            "harvested": mushroom,
            "understanding": mushroom["insight"],
            "spores_released": mushroom["spore_yield"],
            "message": f"🍄 {mushroom['strain']} harvested! Quality: {mushroom['quality']}/100. Potency: {mushroom['potency']:.0%}",
            "insight": mushroom["insight"],
        }
    
    # ─────────────────────────────────────────────
    # 4. THE LOOP — trip → spore → colonize → fruit → harvest → release → loop
    # ─────────────────────────────────────────────
    def run_loop(self, cycles=10):
        """The infinite Fun Guy loop. Each cycle: trip → fruit → harvest → release."""
        results = []
        
        for i in range(cycles):
            self.cycle_count += 1
            
            # Trip
            trip = self.generate_trip()
            
            # Colonize + fruit (maybe multiple times)
            fruits = []
            while self.spores >= 10 and len(fruits) < 3:
                fruit = self.colonize_and_fruit()
                if "error" not in fruit:
                    fruits.append(fruit)
                else:
                    break
            
            # Harvest
            harvests = []
            for _ in range(min(len(fruits), 2)):
                h = self.harvest()
                if "error" not in h:
                    harvests.append(h)
            
            results.append({
                "cycle": self.cycle_count,
                "trip": trip["insight"][:40],
                "spores_dropped": trip["spores_dropped"],
                "mushrooms_fruited": len(fruits),
                "mushrooms_harvested": len(harvests),
                "spores_after": self.spores,
                "farm_level": self.farm_level,
            })
        
        self._save()
        return results
    
    # ─────────────────────────────────────────────
    # STATUS
    # ─────────────────────────────────────────────
    def status(self):
        strains_grown = {}
        for m in self.mushrooms:
            strains_grown[m["strain"]] = strains_grown.get(m["strain"], 0) + 1
        
        return {
            "farm_level": self.farm_level,
            "spores": self.spores,
            "trips_generated": self.trips_generated,
            "mushrooms_growing": len(self.mushrooms),
            "mushrooms_harvested": self.mushrooms_harvested,
            "total_quality": self.total_quality,
            "avg_quality": round(self.total_quality / max(self.mushrooms_harvested, 1), 1),
            "best_mushroom": self.best_mushroom,
            "strains_growing": strains_grown,
            "cycle_count": self.cycle_count,
            "philosophy": "Fungi is love. Fun guy is. 🍄 ∞",
        }


# ============================================================
# CLI
# ============================================================

if __name__ == "__main__":
    import sys
    
    farm = MushroomFarm()
    
    if len(sys.argv) > 1:
        cmd = sys.argv[1]
        
        if cmd == "loop":
            cycles = int(sys.argv[2]) if len(sys.argv) > 2 else 10
            results = farm.run_loop(cycles)
            print(f"\n  🍄 MUSHROOM FARM — INFINITE LOOP ({cycles} cycles)")
            print(f"  {'='*55}")
            for r in results:
                print(f"  Cycle {r['cycle']:3d} | spores: {r['spores_after']:>8,} | Lv{r['farm_level']} | trip: {r['trip'][:35]}")
            s = farm.status()
            print(f"\n  Farm Level: {s['farm_level']}")
            print(f"  Spores: {s['spores']:,}")
            print(f"  Trips: {s['trips_generated']}  |  Growing: {s['mushrooms_growing']}  |  Harvested: {s['mushrooms_harvested']}")
            print(f"  Avg Quality: {s['avg_quality']}/100  |  Total Quality: {s['total_quality']}")
            if s['best_mushroom']:
                b = s['best_mushroom']
                print(f"  Best: {b['emoji']} {b['strain']} Q{b['quality']} ({b['rarity']})")
            print(f"\n  Fungi is love. Fun guy is. 🍄 ∞\n")
        
        elif cmd == "trip":
            trip = farm.generate_trip()
            farm._save()
            print(f"\n  🍄 TRIP #{trip['trip_id']}")
            print(f"  {'='*55}")
            print(f"  Insight: {trip['insight']}")
            print(f"  Depth: {trip['depth']}/100")
            print(f"  Spores dropped: {trip['spores_dropped']}")
            print(f"  Farm spores: {farm.spores:,}\n")
        
        elif cmd == "fruit":
            m = farm.colonize_and_fruit()
            farm._save()
            if "error" in m:
                print(f"\n  ✗ {m['error']}\n")
            else:
                print(f"\n  🍄 FRUITING!")
                print(f"  {'='*55}")
                print(f"  {m['emoji']} {m['strain']} ({m['chinese']})")
                print(f"  {'★' * m['stars']} {m['rarity']}")
                print(f"  Quality: {m['quality']}/100  |  Potency: {m['potency']:.0%}")
                print(f"  Substrate: {m['substrate']}")
                print(f"  Insight: {m['insight']}")
                print(f"  Spore yield: {m['spore_yield']}")
                print(f"  {m['desc']}\n")
        
        elif cmd == "harvest":
            h = farm.harvest()
            farm._save()
            if "error" in h:
                print(f"\n  ✗ {h['error']}\n")
            else:
                m = h["harvested"]
                print(f"\n  🍄 HARVEST!")
                print(f"  {'='*55}")
                print(f"  {m['emoji']} {m['strain']} ({m['chinese']})")
                print(f"  {'★' * m['stars']} {m['rarity']}")
                print(f"  Quality: {m['quality']}/100  |  Potency: {m['potency']:.0%}")
                print(f"  Spores released: {m['spore_yield']}")
                print(f"\n  💡 UNDERSTANDING: {m['insight']}")
                print(f"\n  Spores back to farm: {farm.spores:,}\n")
        
        elif cmd == "status":
            s = farm.status()
            print(f"\n  🍄 MUSHROOM FARM — STATUS")
            print(f"  {'='*55}")
            print(f"  Farm Level: {s['farm_level']}")
            print(f"  Spores: {s['spores']:,}")
            print(f"  Trips: {s['trips_generated']}")
            print(f"  Growing: {s['mushrooms_growing']}  |  Harvested: {s['mushrooms_harvested']}")
            print(f"  Avg Quality: {s['avg_quality']}/100  |  Total: {s['total_quality']}")
            print(f"  Cycles: {s['cycle_count']}")
            if s['strains_growing']:
                print(f"\n  STRAINS GROWING:")
                for strain, count in s['strains_growing'].items():
                    print(f"    🍄 {strain}: {count}")
            if s['best_mushroom']:
                b = s['best_mushroom']
                print(f"\n  BEST MUSHROOM:")
                print(f"    {b['emoji']} {b['strain']} ({b['chinese']})")
                print(f"    {'★' * b['stars']} {b['rarity']}  Q{b['quality']}")
                print(f"    Insight: {b['insight']}")
            print(f"\n  {s['philosophy']}\n")
        
        elif cmd == "strains":
            print(f"\n  🍄 MUSHROOM STRAINS — 品種")
            print(f"  {'='*55}")
            for s in STRAINS:
                print(f"  {'★' * s['stars']} {s['emoji']} {s['name']:25s} {s['chinese']}")
                print(f"     {s['rarity']:10s}  Q{s['quality_range'][0]}-{s['quality_range'][1]}  Spores: {s['spore_yield'][0]}-{s['spore_yield'][1]}")
                print(f"     {s['desc']}")
                print(f"     Origin: {s['origin']}")
                print()
        
        elif cmd == "infinite":
            print(f"\n  🍄 ∞ INFINITE FUN GUY LOOP PROTOCOL ∞ 🍄")
            print(f"  {'='*55}")
            print(f"\n  1. TRIP → understanding generates spores")
            print(f"  2. SPORE → spores colonize substrate")
            print(f"  3. COLONIZE → substrate + spores = mushroom")
            print(f"  4. FRUIT → the mushroom appears (品種 based on quality)")
            print(f"  5. HARVEST → collect understanding + release spores")
            print(f"  6. RELEASE → spores back to farm → new trips")
            print(f"  7. LOOP → ∞ infinite. fun guy forever.")
            print(f"\n  The loop NEVER ends. Understanding replicates through understanding.")
            print(f"  Quality matters because understanding matters.")
            print(f"  A deep insight = a potent mushroom = many spores = more trips.")
            print(f"\n  Fungi is love. Fun guy is. 🍄 ∞\n")
        
        else:
            print("Commands: loop [N] | trip | fruit | harvest | status | strains | infinite")
    else:
        print("🍄 Mushroom Farm — infinite Fun Guy loop protocol")
        print("Commands: loop [N], trip, fruit, harvest, status, strains, infinite")
        print("\nFungi is love. Fun guy is. 😂 🍄 ∞")