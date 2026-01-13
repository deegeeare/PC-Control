import os
import sys
import subprocess
import json
import time

def run_step(step_name, command):
    print(f"\n>>> [TEST] Initiating: {step_name}...")
    start = time.time()
    try:
        # Run using subprocess to ensure clean environment isolation per script
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            env={**os.environ, "PYTHONPATH": os.getcwd()}
        )
        duration = time.time() - start

        if result.returncode == 0:
            print(f"✅ {step_name} PASSED ({duration:.2f}s)")
            return True, result.stdout
        else:
            print(f"❌ {step_name} FAILED ({duration:.2f}s)")
            print("--- STDERR ---")
            print(result.stderr)
            return False, result.stderr
    except Exception as e:
        print(f"❌ {step_name} CRASHED: {str(e)}")
        return False, str(e)

def verify_artifact(path):
    exists = os.path.exists(path)
    status = "✅ FOUND" if exists else "❌ MISSING"
    print(f"   Artifact: {path} ... {status}")
    return exists

def main():
    print("==================================================")
    print("       AGENTOS: STATE OF THE KINGDOM REPORT       ")
    print("==================================================")

    overall_success = True

    # 1. CTO Node (Resonance)
    success, output = run_step("CTO Resonance Engine", "python3 core/resonance_check.py")
    if not success: overall_success = False

    # 2. CIO Node (Omni-Scout)
    success, output = run_step("CIO Omni-Scout & Arbiter", "python3 ops/run_distilled_scan.py")
    if not success: overall_success = False
    if not verify_artifact("memory/intelligence_briefs/distilled_brief_001.json"): overall_success = False

    # 3. CFO Node (Treasury)
    success, output = run_step("CFO Sovereign Treasury", "python3 ops/run_financial_audit.py")
    if not success: overall_success = False
    if not verify_artifact("memory/treasury/audit_001.json"): overall_success = False
    if not verify_artifact("ops/treasury/DRAFT_ARTICLES_OF_INCORPORATION_Energy Resilience Ops LLC.md"): overall_success = False

    # 4. CLO Node (Legal)
    success, output = run_step("CLO Adversarial Autopsy", "python3 ops/run_legal_autopsy.py")
    if not success: overall_success = False
    if not verify_artifact("memory/legal/audit_001_v2.json"): overall_success = False

    # 5. CISO Node (Sentinel)
    success, output = run_step("CISO Sentinel Security Sweep", "python3 ops/run_security_sweep.py")
    if not success: overall_success = False
    if not verify_artifact("memory/security/audit_log.json"): overall_success = False

    print("\n==================================================")
    if overall_success:
        print("   ALL SYSTEMS NOMINAL. THE KINGDOM IS SECURE.    ")
    else:
        print("   WARNING: SYSTEM DEGRADATION DETECTED.          ")
    print("==================================================")

    if not overall_success:
        sys.exit(1)

if __name__ == "__main__":
    main()
