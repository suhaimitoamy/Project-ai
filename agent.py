from praisonaiagents import Agent
import subprocess

agent = Agent(
    instructions="Kamu adalah AI yang membuat Pine Script TradingView. Tulis kode yang clean, langsung siap pakai.",
    llm="ollama/qwen3:1.7b"
)

# Prompt ke agent
result = agent.start("Buat indikator EMA crossover sederhana (fast 9, slow 21)")

# Simpan ke file
with open("ema_indicator.pine", "w") as f:
    f.write(result)

print("File dibuat: ema_indicator.pine")

# Auto push ke GitHub
subprocess.run("git add .", shell=True)
subprocess.run('git commit -m "auto: generate pine script"', shell=True)
subprocess.run("git push origin main", shell=True)
