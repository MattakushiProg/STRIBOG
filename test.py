from H_alghorithm import LPS

# Входной вектор 00,01,02,…,3f
inp = bytes(range(64))

# Эталон (64 байта)
expected_hex = (
    "23c5ee40b07b5f1523c5ee40b07b5f15"
    "23c5ee40b07b5f1523c5ee40b07b5f15"
    "23c5ee40b07b5f1523c5ee40b07b5f15"
    "23c5ee40b07b5f1523c5ee40b07b5f15"
)
expected = bytes.fromhex(expected_hex)

out = LPS(inp)
print("OK" if out == expected else "FAIL")
print("Output :", out.hex())
print("Expect :", expected_hex)
