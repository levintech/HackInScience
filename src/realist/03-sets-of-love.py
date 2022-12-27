def love_meet(bob, alice):
    return set(bob) & set(alice)


def affair_meet(bob, alice, silvester):
    return set(alice) & set(silvester) - set(bob)