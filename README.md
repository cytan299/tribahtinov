# A Tri-Bahtinov Mask for Aiding Collimation and Focusing of Schmidt Cassegrain Telescopes

In my opinion, the Bahtinov mask is one of the most useful inventions
for astrophotography. The traditional use of a Bahtinov mask is for
focusing a telescope only and is not used for collimation of an SCT.
For collimating an SCT, the method that is commonly used is the
[Airy disk method](http://www.astrophoto.fr/collim.html). I have found
this method to be quite onerous because

* due to atmospherics at my observation location, I have never been able
to see a really clear Airy disk. 
* when I adjust the collimating screws to centre the doughnut hole, my
  judgement is rather arbitrary and not as objective as it should
  be. I think my overly optimistic judgement of the Airy disk pattern
  makes this method a collimation challenge for me.

And thus, these two reasons motivated me to create a less judgemental
way for collimation.

## The idea

Since the standard Bahtinov mask is such a useful tool for focusing, I
thought that there must be a way to use it for collimation as
well. My idea is as follows:

For an SCT, that is well collimated, I would expect that the path
length travelled by light rays from the primary mirror reflected to
the secondary mirror and then reflected to the image plane should all
be the same. However, if the SCT is not collimated then the light rays
do not all have the same path lengths. The effect is that focus can
only be established at one location on the image plane, while focus is
not achieved at other locations.

Therefore, for an uncollimated SCT, while I can achieve perfect
Bahtinov diffraction spikes with one orientation of the Bahtinov mask,
the diffractions spikes will not be perfect for other
orientations. Thus, in my opinion, the most natural way to
simultaneously measure the focus for different orientations of the
Bahtinov mask is to make a mask that has multiple orientations
already built in.

## Tri-Bahtinov mask

For an SCT, the secondary mirror has three adjustment
screws. Therefore, the most obvious way to me is to have three
Bahtinov masks designed into the mask. Thus, my idea of a
**Tri-Bahtinov mask** that has three Bahtinov masks arranged in a
3-fold symmetric fashion. This symmetry should produce a diffraction
pattern that is also 3-fold symmetric. To check this hypothesis, I
generated the diffraction pattern using the program
[Maskulator](http://www.njnoordhoek.com/?p=376).  The diffraction
pattern from such a Tri-Bahtinov mask is shown below for the design
where the smallest angle between the diffraction spikes is 10
degrees. This simulation confirms my hypothesis that a Tri-Bahtinov
produces a diffraction pattern that has three orientations for
checking the focus.

![Theoretical Diffraction Pattern](https://github.com/cytan299/tribahtinov/blob/master/pics/theory.png)

## Implementation

I have made a Tri-Bahtinov mask for my 8" LX200 classic which I show below
![Tri-Bahtinov mask](https://github.com/cytan299/tribahtinov/blob/master/pics/IMG_0086.jpg)

The Tri-Bahtinov mask is mounted on my LX200 is shown below
![Tri-Bahtinov mask mounted](https://github.com/cytan299/tribahtinov/blob/master/pics/IMG_0093.jpg)
I have mounted thumb screws on the mask so that when I use it, I orient
these screws to align with the collimation screws on the secondary
mirror. I can then mask one of the three Bahtinov sub-masks to determine which
collimation screw to adjust.

## Results

My as found diffraction pattern when I point my LX200 at Polaris,
magnified 400x and integrated for 2 seconds is shown below
![Pattern as found](https://github.com/cytan299/tribahtinov/blob/master/pics/as_found.png)
It is clear that although the LX200 is close to focus for two
orientations, there is one orientation (indicated with red arrows)
that is clearly not in focus. The clarity of this diffraction pattern
shows that there is not arbitrariness as to whether the SCT is
collimated or not in this case: it is definitely not collimated.

Now, since this is the first time that I have used the Tri-Bahtinov mask, I
spent nearly an hour messing around to find the optimum collimation
screw setting. One problem that I have found was that the defocused Bahtinov
diffraction pattern shown above is associated with the collimation screw that
wants to be made tighter and tighter. I bottomed out this screw and thus had
to loosen it, i.e. made collimation worse and then use the other two screws
to compensate. I found a good setting (although still not quite perfect)
which I show below
![Pattern as found](https://github.com/cytan299/tribahtinov/blob/master/pics/collimated.png)

Once I completed the above exercise, I can achieve focus of my LX200
for all three orientations and in effect, my LX200 is now
collimated. My collimation exercise with the Tri-Bahtinov mask allowed
me to achieve collimation with minimal arbitrariness. This is the goal
that I wanted!

## Directory structure

* **ponoko** My Tri-Bahtinov mask that can be sent to
[Ponoko](http://www.ponoko.com) to be laser cut.
* **other_formats** My Tri-Batinov mask in other formats so that you
  can print it out or edit it. 
* **pics** Image files for this repository.
* **maskulator_movie** directory that contains the avi movie from
  maskulator that shows how the Tri-Bahtinov diffraction pattern
  changes when the focusing changes.
* **python** My python script for generating my Tri-Bahtinov mask
  for any telescope. Please see the README.md file in that directory
  for instructions for its installation and usage.

## Copyright

All the documentation, pictures, movies and design that I have here is
copyright 2016 C.Y. Tan and released under Creative Commons
Attribution-ShareAlike 3.0 Unported License.

All software is released under GPLv3



