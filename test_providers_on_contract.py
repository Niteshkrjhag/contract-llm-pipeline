import os
import subprocess

providers = ["Gemini", "OpenAI", "OpenRouter", "Ollama"]

for p in providers:
    print(f"\n--- Testing {p} ---")
    env = os.environ.copy()
    env["LLM_FALLBACK_ORDER"] = p
    env["RAW_CONTRACTS_DIR"] = "data/test_contract"
    env["OUTPUT_DIR"] = f"outputs/test_{p}"
    
    result = subprocess.run(["venv/bin/python", "main.py"], env=env, capture_output=True, text=True)
    
    output_log = result.stderr + "\n" + result.stdout
    
    if "Pipeline completed successfully" in output_log:
        print(f"✅ {p} WORKED!")
    else:
        print(f"❌ {p} FAILED.")
        # Find the last ERROR line
        err_lines = [line for line in output_log.split('\n') if 'ERROR' in line]
        if err_lines:
            print(f"   Reason: {err_lines[-1]}")
        else:
            print("   Reason: Unknown (Check logs)")
