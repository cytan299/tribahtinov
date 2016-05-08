# Tri-Bahtinov Mask for Aiding Collimation and Focusing of Schmidt Cassegrain Telescopes

In my opinion, the Bahtinov mask is one of the most useful inventions
for astrophotography. The traditional use of a Bahtinov mask is for
focusing a telescope only and is not used for collimation of an SCT.
The traditional way for collimating an SCT is the
[Airy disk method](http://www.astrophoto.fr/collim.html) which I have
found to be quite onerous. There are two reasons for this,

* I assume, due to atmospherics at my observation location, I have never been able
to see a really clear Airy disk when looking at a star.
* When I adjust the collimating screws to centre the doughnut hole, my
  judgement is rather arbitrary and not as objective as it should be,
  as to whether it is actually centred can be quite uncertain.

And thus due to the above two reasons, I decided that there should be
a less judgemental way for collimation.

## The idea

Since the standard Bahtinov mask is such a useful tool for focusing, I
thought that there must be a way to use it for collimation as
well. My idea is as follows:

For an SCT, when it is well collimated, I would expect that the light
rays from the primary mirror to the secondary mirror and then to the
image plane should all be the same. However, when the SCT is not
collimated then the light rays do not all have the same path
lengths. The effect is that focus can only be established at one
location on the image plane, while focus is not achieved at other
locations.

Therefore, for an uncollimated SCT, while I can achieve perfect
Bahtinov diffraction spikes with one orientation of the Bahtinov mask,
the diffractions spikes will not be perfect for other
orientations. Thus, the most natural way to simultaneously measure the
focus for different orientations of the Bahtinov mask is to make a mask
that has has multiple orientations already built in.

## Tri-Bahtinov mask

For an SCT, the secondary mirror has three adjustment
screws. Therefore, the most obvious way is to have three Bahtinov
masks designed into the mask. Thus, my idea of a **Tri-Bahtinov mask**
that has three Bahtinov masks arranged in a 3-fold symmetric
fashion. This symmetry should produce a diffraction pattern that is
also 3-fold symmetric. To check this hypothesis, I generated the
diffraction pattern using the program
[Maskulator](http://www.njnoordhoek.com/?p=376).  The diffraction
pattern from such a Tri-Bahtinov mask is shown below when the smallest
angle between the diffraction spikes to be 10 degrees. This simulation
confirms my hypothesis that a Tri-Bahtinov has three
orientations that I can simultaneously check the focus with. 

![Theoretical Diffraction Pattern](https://github.com/cytan299/tribahtinov/blob/master/pics/theory.png)

## Implementation

I have made a Tri-Bahtinov mask for my 8" LX200 classic which I show below
![Tri-Bahtinov mask](https://github.com/cytan299/tribahtinov/blob/master/pics/IMG_0086.jpg)

The Tri-Bahtinov mask is mounted on my LX200 is shown below
![Tri-Bahtinov mask mounted](https://github.com/cytan299/tribahtinov/blob/master/pics/IMG_0093.jpg)
I have mounted thumb screws on the mask so that when I use it, I orient
these screws to align with the collimation screws on the secondary
mirror. I can then mask on of the three Bahtinov masks to determine which
collimation screw that I should adjust.

## Results

My as found diffraction pattern when I point my LX200 at Polaris,
magnified 400x and integrated for 2 seconds is shown below
![Pattern as found](https://github.com/cytan299/tribahtinov/blob/master/pics/as_found.png)
It is clear that although the LX200 is focused for two orientations,
there is one orientation (indicated with red arrows) that is not in
focus. This shows that there is not arbitrariness as to whether the
SCT is collimated or not: it is definitely not collimated.

Now, since this is the first time that I used the Tri-Bahtinov mask, I
spent nearly an hour messing around to find the optimum collimation
screw setting. One problem that I found was that the defocused Bahtinov
diffraction pattern shown above is associated with the collimation screw that
wants to be made tighter and tighter. I ran out of room and thus had
to loosen it, i.e. made collimation worse and use the other two screws
to compensate. I found a good setting (although still not quite perfect)
which I show below
![Pattern as found](https://github.com/cytan299/tribahtinov/blob/master/pics/collimated.png)

Once I completed the above exercise, I can achieve focus of my LX200
for all three orientations. And thus my objective for reducing
arbitrariness in collimation has been achieved!

## Copyright

All the documentation, pictures, and design that I have here is
copyright 2016 C.Y. Tan and released under Creative Commons
Attribution-ShareAlike 3.0 Unported License.
