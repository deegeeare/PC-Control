import base64
import json
import hashlib
from typing import Dict, Any, Union

class VaultLock:
    """
    The CISO Encryption Wrapper.
    Provides robust obfuscation/encryption for the Identity Vault.
    Mandate: Secrecy, Integrity, Control.
    """

    def __init__(self, token: str):
        self.token = token
        self._valid_token_hash = self._hash_token("AURA_CEO_KEY_V1")

    def _hash_token(self, token: str) -> str:
        return hashlib.sha256(token.encode()).hexdigest()

    def _derive_key(self) -> bytes:
        """Derives a byte key from the session token."""
        return hashlib.sha256(self.token.encode()).digest()

    def _xor_bytes(self, data: bytes, key: bytes) -> bytes:
        return bytes(a ^ b for a, b in zip(data, (key * (len(data) // len(key) + 1))[:len(data)]))

    def encrypt(self, data: Union[str, Dict]) -> str:
        """
        Encrypts data if the token is valid.
        Returns Base64 encoded string.
        """
        # Verify Token
        if self._hash_token(self.token) != self._valid_token_hash:
             raise PermissionError("ACCESS DENIED: Invalid CEO_SESSION_TOKEN for Encryption.")

        # Serialize if dict
        if isinstance(data, dict):
            payload = json.dumps(data)
        else:
            payload = str(data)

        # Encrypt
        key = self._derive_key()
        encrypted_bytes = self._xor_bytes(payload.encode(), key)
        return base64.b64encode(encrypted_bytes).decode('utf-8')

    def decrypt(self, encrypted_string: str) -> Union[str, Dict]:
        """
        Decrypts data if the token is valid.
        """
        if self._hash_token(self.token) != self._valid_token_hash:
             raise PermissionError("ACCESS DENIED: Invalid CEO_SESSION_TOKEN for Decryption.")

        try:
            encrypted_bytes = base64.b64decode(encrypted_string)
            key = self._derive_key()
            decrypted_bytes = self._xor_bytes(encrypted_bytes, key)
            decrypted_str = decrypted_bytes.decode('utf-8')

            # Try to parse as JSON
            try:
                return json.loads(decrypted_str)
            except json.JSONDecodeError:
                return decrypted_str
        except Exception as e:
             raise ValueError(f"Decryption Failed: {str(e)}")

# High Resonance Keywords: Secrecy, Integrity, Control, Kingdom
