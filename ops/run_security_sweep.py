import os
import sys
import time

# Ensure imports work
sys.path.append(os.getcwd())

from core.ciso.sentinel import Sentinel
from core.ciso.vault_lock import VaultLock

def run_security_sweep():
    print("INITIALIZING CISO SECURITY SWEEP")

    # 1. Initialize Sentinel
    sentinel = Sentinel()

    # 2. Establish Baseline (First Run)
    sentinel.generate_baseline()

    # 3. Test Encryption (VaultLock)
    print("\n--- Testing Vault Lock ---")
    valid_token = "AURA_CEO_KEY_V1"
    locker = VaultLock(valid_token)
    secret_data = {"tax_id": "12-3456789", "entity": "Holdings Corp"}

    encrypted = locker.encrypt(secret_data)
    print(f"Encrypted Data: {encrypted[:20]}...")

    decrypted = locker.decrypt(encrypted)
    print(f"Decrypted Data Match: {decrypted == secret_data}")

    # 4. Simulate Attack (Logic Drift)
    print("\n--- Simulating Logic Drift Attack ---")
    attack_file = "core/omni_scout.py" # Target an existing file

    # Read original
    with open(attack_file, 'r') as f:
        original_content = f.read()

    # Inject Malice
    with open(attack_file, 'a') as f:
        f.write("\n# MALICIOUS INJECTION")

    # 5. Run Integrity Check
    secure = sentinel.integrity_check()

    # Verify Lockdown
    if os.path.exists("ops/treasury_LOCKED"):
        print("VERIFIED: Treasury is LOCKED.")
    else:
        print("FAILURE: Treasury NOT Locked.")

    # 6. Cleanup / Restore Order
    print("\n--- Restoring Order ---")
    # Restore file
    with open(attack_file, 'w') as f:
        f.write(original_content)

    # Unlock Treasury
    sentinel.restore_order()

    # Re-verify Integrity
    final_check = sentinel.integrity_check()
    print(f"Final System State: {'SECURE' if final_check else 'COMPROMISED'}")

if __name__ == "__main__":
    run_security_sweep()
