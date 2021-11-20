#! /usr/bin/env python3

"""
How to use the script?
1) Make sure the correct dependencies are installed.
    pip3 install -r requirements.txt
2) python3 shift.py <gateway number> <radius>
    The gateway number can be from 0 to 19, "0 is east of the exit portal, and numbers increase clockwise."
    The radius must be between 768 and 1280.

    The code is available under the GPL-3.0 license.
"""

try:
    from litemapy import Region, BlockState
    import math
    import sys
    import time

    gatewayid = int(sys.argv[1])
    r = int(sys.argv[2])

    assert 19 >= gatewayid >= 0, "Gateway number must be between 0 and 19."
    assert 1280 >= r >= 768, "Radius must be between 768 and 1280."

    reg = Region(-1280, 0, -1280, 2560, 1, 2560)
    vectorschem = reg.as_schematic(name=f"Gateway {gatewayid}; radius {r}", author="@watchingdogs",
                                   description="Check GitHub for help.")
    l = []

    for x in range(20):
        d = 96 * math.sin(2 * (math.pi / 20 * x - math.pi))
        l.append(d)


    def coords(r, id):
        x = r / 96 * l[id - 15]
        z = r / 96 * l[id-20]
        return [round(x), round(z)]  # Litemapy can not work with floats.


    if r >= 1024:
        count = 1024
        while count <= r:
            block = coords(count, gatewayid)
            block[0] += (1280 if block[0] > 0 else -1280)
            block[1] += (1280 if block[1] > 0 else -1280)
            reg.setblock(block[0], 0, block[1], BlockState("minecraft:bedrock"))
            count += 1

    else:
        count = r
        while count <= 1024:
            block = coords(count, gatewayid)
            block[0] += (1280 if block[0] > 0 else -1280)
            block[1] += (1280 if block[1] > 0 else -1280)
            reg.setblock(block[0], 0, block[1], BlockState("minecraft:netherrack"))
            count += 1

    print("Writing schematic to disk...")
    start = time.time()
    vectorschem.save(f"gs{gatewayid}-{r}.litematic")
    end = time.time()
    print(f"Saved to gs{gatewayid}-{r}.litematic. It took {round(end-start, 2)} seconds.")

except IndexError:
    print("Wrong input. For help open the file or the README.")
except ImportError:
    print("Make sure all modules are imported.")
except KeyboardInterrupt:
    print(" Bye!")
