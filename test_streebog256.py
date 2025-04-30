import pytest
from H_alghorithm import LPS, E, g, H256, key_schedule, C


from H_alghorithm import LPS

inp  = bytes(range(64))
want = bytes.fromhex("23c5ee40b07b5f1523c5ee40b07b5f1523c5ee40b07b5f1523c5ee40b07b5f1523c5ee40b07b5f1523c5ee40b07b5f1523c5ee40b07b5f1523c5ee40b07b5f15")
out  = LPS(inp)
assert out == want



# # Эталонные векторы (big-endian hex)
# VECTORS = [
#     (b"", 
#      "3f45ef194732c10d2e0e2a5f9cf782290cf624e5b9e2f0f8ca3e9d2fb4348dc9"),
#     (b"The quick brown fox jumps over the lazy dog",
#      "4774d2b0e6a78d6ae8ae6e1efeb13a07a17f8b4533dcd6ce622caab1f88f0e20"),
# ]

# @pytest.mark.parametrize("message,expected_hex", VECTORS)
# def test_H256_vectors(message, expected_hex):
#     """Проверка H256 на эталонных векторах."""
#     # Передаём константы C в H256
#     digest = H256(message, C)
#     assert digest.hex() == expected_hex

# # Тесты базовых свойств LPS и E

# def test_LPS_nontrivial():
#     """Проверяем, что LPS изменяет данные."""
#     x = bytes(range(64))
#     y = LPS(x)
#     assert y != x

# # Простой тест обратимости E: шифрование + дешифрование

# def test_E_inverse():
#     K0 = bytes([0x01] * 64)
#     M = bytes(range(64))
#     # шифруем
#     CIPH = E(K0, M, C)
#     # получаем расписание ключей и обращаем порядок
#     Ks = key_schedule(K0, C)
#     Ks_rev = Ks[::-1]
#     # дешифруем: обратный процесс E
#     X = CIPH
#     for k in Ks_rev[1:]:
#         X = LPS(bytes(a ^ b for a, b in zip(X, k)))
#     X = bytes(a ^ b for a, b in zip(X, Ks_rev[0]))
#     assert X == M
