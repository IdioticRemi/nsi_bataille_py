from cardgame.lists.List import List

test = List()

print("✨ PUSH TEST")

for x in range(10):
    test.push(x)

if test.to_array() != [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
    print("❌ Le test a échoué!")
else:
    print("✅ Le test est passé!")

print("\n✨ INSERT TEST")

for x in range(0, 20, 2):
    test.insert([int(x / 2)], x)

if test.to_array() != [[0], 0, [1], 1, [2], 2, [3], 3, [4], 4, [5], 5, [6], 6, [7], 7, [8], 8, [9], 9]:
    print("❌ Le test a échoué!")
else:
    print("✅ Le test est passé!")

print("\n✨ INDEX TEST")

if test.index(4) != 9:
    print("❌ Le test a échoué!")
else:
    print("✅ Le test est passé!")

print("\n✨ AT TEST")

if test.at(test.index(4)) != 4:
    print("❌ Le test a échoué!")
else:
    print("✅ Le test est passé!")

print("\n✨ HAS TEST")

if test.has(test.index(4)) is False:
    print("❌ Le test a échoué!")
else:
    print("✅ Le test est passé!")

print("\n✨ DELETE TEST")

for x in range(10):
    test.delete(x)

if test.to_array() != [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
    print("❌ Le test a échoué!")
else:
    print("✅ Le test est passé!")

print("\n✨ CLEAR TEST")

test.clear()

if test.len != 0:
    print("❌ Le test a échoué!")
else:
    print("✅ Le test est passé!")
