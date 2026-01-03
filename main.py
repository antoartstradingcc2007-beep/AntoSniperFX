from fastapi import FastAPI
from datetime import datetime
import random

app = FastAPI()

@app.get("/signals")
def get_signals():
    pairs = ["EURUSD", "GBPUSD", "USDJPY", "GBPJPY"]
    signals = []

    for pair in pairs:
        if random.random() > 0.6:
            entry = round(random.uniform(1.05, 1.30), 5)
            sl = round(entry - 0.0015, 5)
            tp = round(entry + 0.0045, 5)

            signals.append({
                "pair": pair,
                "type": random.choice(["BUY", "SELL"]),
                "timeframe": "M5",
                "entry": entry,
                "sl": sl,
                "tp": tp,
                "confidence": random.randint(75, 90),
                "time": datetime.now().strftime("%H:%M:%S")
            })

    return signals
