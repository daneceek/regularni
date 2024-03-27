# () - skupina
# tečka - libovolny znak

import re
# m = re.search("(.)(.)(.)", "abcdef")
# m = re.search(r"\n(.)(.)(.)", "abcdef")  zpetne lomitko je zpetne lomitko
m = re.search(r"(\d+)\.(\d+)\.(\d+)\.(\d+)", "moje ip je: 172.30.99.8 sdbhdsdh sdsmdk")


print(m)

if m:
    print(m.groups()) # vrati tuple 
    print(m.group(0)) # 0 vrati všecko co našel  
    print(m.group(1)) # prvni skupina
    print(m.group(2)) # druha skupina
    print(m.group(3)) # treti skupina


import re
from sys import flags

m = re.search(
    r"(\d+)\.(\d+)\.(\d+)\.(\d+)",
    "moje ip je: 172.30.99.8 fjkdf jfkd ",
    flags=re.IGNORECASE | re.MULTILINE,
)

e = re.compile(r"(\d+)\.(\d+)\.(\d+)\.(\d+)", flags=re.IGNORECASE | re.MULTILINE)
m = e.search("moje ip je: 172.30.99.8 fjkdf jfkd ")

print(m)
if m:
    print(m.groups())
    print(m.group(0))
    print(m.group(1))
    print(m.group(2))
    print(m.group(3))
    print(m.group(4))


seznam = re.split(r"\s*,\s*|\s+", "ahoj,   nazdar , čau\n holahoa cao")
print(seznam)
print("ahoj,   nazdar , čau\n holahoa".split())

text = """Lorem ipsum slovo je označení pro Standardní pseudolatinský text užívaný v grafickém designu a navrhování jako demonstrativní
 výplňový text spři vytváření pracovních ukázek grafických návrhů.
 Lipsum tak pracovně znázorňuje text v ukázkových maketách předtím, než bude do hotového"""

seznam = re.findall(r"\b\w+\b", text, flags=re.IGNORECASE | re.MULTILINE)
print(seznam)