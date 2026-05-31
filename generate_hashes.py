"""
Run this script ONCE to generate hashed passwords.
Copy the output hashes into users.yaml.

Usage:
    python generate_hashes.py
"""
import streamlit_authenticator as stauth

# Add your users' plain-text passwords here
usernames  = ["suraj",   "nischal",   "admin"]
passwords  = ["suraj123", "nischal123", "abbvie2024"]

hashed = stauth.Hasher(passwords).generate()

print("\nPaste these hashed passwords into users.yaml:\n")
for uname, h in zip(usernames, hashed):
    print(f"  {uname}:  {h}")
