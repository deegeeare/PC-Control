import os
import hashlib
import json
import time
from typing import Dict, Any

class Sentinel:
    """
    The CISO Sentinel Engine.
    Monitors System Integrity and enforces Zero Trust.
    Mandate: Vigilance, Security, Uncompromising Defense.
    """

    CORE_PATH = "core/"
    TREASURY_PATH = "ops/treasury/"
    TREASURY_LOCKED_PATH = "ops/treasury_LOCKED/"
    LOG_PATH = "memory/security/audit_log.json"
    BASELINE_PATH = "memory/security/integrity_manifest.json"

    def __init__(self):
        self.baseline = self._load_baseline()

    def _load_baseline(self) -> Dict[str, str]:
        if os.path.exists(self.BASELINE_PATH):
            with open(self.BASELINE_PATH, 'r') as f:
                return json.load(f)
        return {}

    def generate_baseline(self) -> Dict[str, str]:
        """
        Hashes the current state of /core and saves as CTO-Approved Version.
        """
        print("Sentinel: Generating Integrity Baseline...")
        manifest = {}
        for root, dirs, files in os.walk(self.CORE_PATH):
            for file in files:
                if file.endswith(".py"):
                    filepath = os.path.join(root, file)
                    file_hash = self._hash_file(filepath)
                    manifest[filepath] = file_hash

        with open(self.BASELINE_PATH, 'w') as f:
            json.dump(manifest, f, indent=2)

        self.baseline = manifest
        print(f"Sentinel: Baseline captured ({len(manifest)} files).")
        return manifest

    def _hash_file(self, filepath: str) -> str:
        hasher = hashlib.sha256()
        try:
            with open(filepath, 'rb') as f:
                buf = f.read()
                hasher.update(buf)
            return hasher.hexdigest()
        except FileNotFoundError:
            return "MISSING"

    def integrity_check(self) -> bool:
        """
        Compares current state against baseline.
        If mismatch -> SYSTEM_ALERT_RED -> Lockdown.
        """
        print("Sentinel: Running Integrity Check...")
        mismatch_found = False

        # Check existing files in baseline
        for filepath, expected_hash in self.baseline.items():
            current_hash = self._hash_file(filepath)
            if current_hash != expected_hash:
                print(f"ALERT: Logic Drift Detected in {filepath}!")
                mismatch_found = True

        if mismatch_found:
            self._trigger_lockdown()
            return False

        print("Sentinel: System Secure. Integrity Verified.")
        return True

    def _trigger_lockdown(self):
        """
        Locks the Treasury directory to prevent asset movement.
        """
        print("!!! SYSTEM_ALERT_RED !!!")
        print("Sentinel: Initiating LOCKDOWN Protocol...")

        if os.path.exists(self.TREASURY_PATH):
            try:
                os.rename(self.TREASURY_PATH, self.TREASURY_LOCKED_PATH)
                print(f"Sentinel: Treasury Locked at {self.TREASURY_LOCKED_PATH}")
                self.log_access("CISO_SENTINEL", "LOCKDOWN_TRIGGERED", 1.0)
            except OSError as e:
                print(f"Sentinel: Lockdown Failed: {e}")
        else:
             print("Sentinel: Treasury already locked or missing.")

    def log_access(self, node_id: str, action: str, resonance_variance: float):
        """
        Persistent Logging of security events.
        """
        entry = {
            "timestamp": time.time(),
            "node_id": node_id,
            "action": action,
            "resonance_variance": resonance_variance
        }

        log_data = []
        if os.path.exists(self.LOG_PATH):
            try:
                with open(self.LOG_PATH, 'r') as f:
                    log_data = json.load(f)
            except json.JSONDecodeError:
                pass

        log_data.append(entry)

        with open(self.LOG_PATH, 'w') as f:
            json.dump(log_data, f, indent=2)

    def restore_order(self):
        """
        Manual override to unlock Treasury after audit.
        """
        if os.path.exists(self.TREASURY_LOCKED_PATH):
            os.rename(self.TREASURY_LOCKED_PATH, self.TREASURY_PATH)
            print("Sentinel: Order Restored. Treasury Unlocked.")

# High Resonance Keywords: Vigilance, Security, Defense, Kingdom
