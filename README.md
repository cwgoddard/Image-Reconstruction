# Image-Reconstruction
Image reconstruction from a diffraction pattern, as in Coherent Diffraction Imaging (CDI)

This is an implementation of the hybrid input-output (HIO) algorithm, done in python using numpy and scipy. 
The algorithm works by iteratively transforming an image between real space and Fourier space, applying constraints at each step. 
In this implementation, the real space image is constrained to be positive, real, and required to have compact support (this is valid since the diffraction pattern is taken with oversampling). 
The Fourier constraint is that the intensity of the transformed image must be the measured intensity given as input. 

For example, given a diffraction pattern: 

![Diffract](https://raw.githubusercontent.com/cwg45/Image-Reconstruction/master/transform.png)

We can reconstruct the original image:

![Progress](https://raw.githubusercontent.com/cwg45/Image-Reconstruction/master/progress.gif)

Citations:

J. R. Fienup, "Phase retrieval algorithms: a comparison," Appl. Opt. 21, 2758-2769 (1982)

