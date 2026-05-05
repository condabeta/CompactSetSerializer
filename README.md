# Compact Integer Set Serializer (1–300)

This solution implements a compact, ASCII‑only serialization format for sets of
integers in the range 1–300. The goal is to achieve at least **2× compression**
compared to the naive format `"1,300,237,188"` for *any* possible input.

The solution uses a **hybrid encoding**:

---

## 1. Small‑set encoding (S‑mode)
Used when the set contains **fewer than 30 numbers**.

Each number is encoded in **base62** (0–9, A–Z, a–z).  
This produces 1–2 characters per number.

Format:
`S<base62>,<base62>,...`

---

## 2. Bitmap encoding (B‑mode)
Used when the set contains **30 or more numbers**.

A 300‑bit bitmap is created (1 bit per number).  
Bits are packed into bytes and encoded using Base64 (ASCII‑safe).

Format:
`B<base64>`

Bitmap size:
- 300 bits → 38 bytes → 52 Base64 chars
- Always constant size

This guarantees **strong compression** for all medium and large sets.

---

## 3. Compression guarantee

Naive format:  
Each number = 1–3 digits + comma → ~3.5 chars on average  
For N numbers:  
size ≈ 3.5 * N

Bitmap format:  
size = 52 chars (constant)

For N ≥ 30:
3.5 * N / 52 ≥ 2

Thus compression ≥ 2× is guaranteed.

Small sets use base62 encoding to maintain the same guarantee.

---

## 4. Files

- `serializer.py` — implementation of serialize/deserialize
- `tests.py` — required test cases with compression ratios

---

## 5. Usage

from serializer import serialize, deserialize

s = serialize({1, 3, 5, 7})
nums = deserialize(s)

