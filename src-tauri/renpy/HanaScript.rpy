init:

    # hana character values
    default halove = 0
    default hatrust = 0
    default haconfidence = 0
    # Would it be funny to implement a "Hana's Cleanliness" stat? Or too mean..

    # added transformations
    transform lefttooff:
        linear 0.1 xpos 0.2
        linear 1.0 xpos -0.5