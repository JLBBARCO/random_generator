from faker import Faker

# Module-level storage so callers can read `randomNames.names` after calling
names = []

def randomNames(quantity):
    """Generate `quantity` random names using Faker and store them on the
    function object as `randomNames.names` and in the module-level `names`.
    """
    global names
    try:
        qty = int(quantity)
    except (TypeError, ValueError):
        qty = 0

    fake = Faker()
    generated = []
    for i in range(qty):
        generated.append((i, fake.name()))

    names = generated
    randomNames.names = names
    return