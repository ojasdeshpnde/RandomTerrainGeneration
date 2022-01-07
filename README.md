# Random Terrain Generation
A simple program that makes a random Terrain which consists of 3 types of materials which are
water, sand and land. Each time it generates a map you can use the DOWN, RIGHT, LEFT, UP arrow keys
to explore to the right and left of this random terrain.

You can explore endlessly, and the program only stores the 50 shown pixels at any point.
So you storage does not fly through the rough and the render time also doesn't take
longer as the program variables don't increase in size so explore endlessly!

NOTE: You might see the oddly named variables waterElement and sandElement. This variable contains a 
scalar constant. This constant determines how the random assortment of land, water and sand work. 
So proportionally there is 60% water, 20% sand and 20% land and you can mess with those values
to generate different types of terrains.

NOTE2: You will see a weird parameter in the PerlinNoise object called octaves. Now,
octaves determines how many grids you have when creating your perlin noise object.
The more squares you have in your grid, the closer you get to just a mess, truly Random
values. So if you pick a higher octave, you will get a more "zoomed" out view. The lower
the octave, the more of "close in" view you get. Feel free to mess around with that
