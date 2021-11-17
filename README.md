# What is gateway shifting?
Gateway shifting is a process to influence where an end gateway generates.
And what does *this* mean? In Minecraft, after you kill the ender dragon, an end gateway generates on the main island. When the game generates this gateway block, it's empty by default. When for example a player or an ender pearl goes through it, the game draws a line from x 0 z 0 through this gateway and looks around at radius 1024 to see if there is an end island there, it can generate above. Naturally, the game wants to find the edge of the end islands, so it jumps back 256 blocks on the line and starts to search from there along the line for 512 blocks until it finds an endstone block at or above Y 30. Meaning, that **you can generate exit gateways from a distance of 768 blocks to 1280 blocks from 0-0**.

### What can this be used for?
In 1.17+ you can have a perfect perimeter in the void, where no endermen can spawn. It's useful for a wither rose farm, for example.
Before 1.17, you were able to delete the information in a generated exit gateway. This method made the player able to build a [void trader](https://www.youtube.com/watch?v=zhsSW1q3t2I) or an [endstone farm](https://www.youtube.com/watch?v=xo7QT3cH2k4) for example.

# How to use the tool?
You need to know for sure if an entrance gateway has a generated peer exit gateway on the outer end islands or not. If you know that the one you are using hasn't been generated yet, you can continue. 

After cloning the repository, make sure to issue `pip3 install -r requirements.txt`.

```
python3 shift.py <gateway number> <radius>
```
The gateway number can be from 0 to 19, "0 is east of the exit portal, and numbers increase clockwise." The radius must be between 768 and 1280.

So if you want an exit gateway in the void when jumping through the most northern end gateway, just issue:

```
python3 shift.py 15 767
```

The tool will give you a litematica schematic file. Make sure the placement is at 0 29 0. To generate it, you have to first go to the outer end islands, place the blocks highlighted in the schematic ( it does not have to be netherrack ), and place an endstone block above the start of the line ( at or above 0 30 768 in this case). Now you can go back to the main end island and go through the gateway. And voilà, you have a gateway at 0 40 768!

**If you are doing this for the first time, test out everything in a creative copy of your world!**
