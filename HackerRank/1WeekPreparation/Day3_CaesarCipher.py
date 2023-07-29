"""
Julius Caesar protected his confidential information by encrypting it using a cipher. 
Caesar's cipher shifts each letter by a number of letters. 
If the shift takes you past the end of the alphabet, just rotate back to the front of the alphabet. 
In the case of a rotation by 3, w, x, y and z would map to z, a, b and c.

Original alphabet:      abcdefghijklmnopqrstuvwxyz
Alphabet rotated +3:    defghijklmnopqrstuvwxyzabc

Example
s = There's-a-starman-waiting-in-the-sky
k = 3
The alphabet is rotated by , matching the mapping above. 
The encrypted string is Wkhuh'v-d-vwdupdq-zdlwlqj-lq-wkh-vnb.

Note: The cipher only encrypts letters; symbols, such as -, remain unencrypted.

Input Format

The first line contains the integer, n, the length of the unencrypted string.
The second line contains the unencrypted string, s.
The third line contains k, the number of letters to rotate the alphabet by.
"""


def caesarCipher(s, k):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'  # 字母表
    mapping = {}  # 初始化映射字典为空
    # 遍历字母表中的每个字母，计算其偏移后的字母，并在字典中建立映射
    for i in range(len(alphabet)):
        mapping[alphabet[i]] = alphabet[(i + k) % 26]
        mapping[alphabet[i].upper()] = alphabet[(i + k) %
                                                26].upper()  # 对于大写字母做同样的映射
    encrypted_string = ""  # 初始化加密字符串为空
    for char in s:  # 遍历输入字符串的每个字符
        if char.isalpha():  # 如果字符是字母
            encrypted_string += mapping[char]  # 查找字典中对应的加密字符
        else:  # 如果字符不是字母
            encrypted_string += char  # 不进行加密，直接加入到加密字符串中
    return encrypted_string


print('okffng-Qwvb', caesarCipher('middle-Outz', 2))
