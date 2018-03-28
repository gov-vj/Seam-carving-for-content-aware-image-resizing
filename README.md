# Seam-carving-for-content-aware-image-resizing
Based on the research paper of Mr. Shai Avidan and Mr. Ariel Shamir
Link: http://www.faculty.idc.ac.il/arik/SCWeb/imret/imret.pdf

Libraries used: os, struct, sys, Python Imaging Library, Tkinter, tkFileDialog, unittest

Tools used: python (IDLE)

Brief Explanation:

To crop an image we remove the vertical seam(red color line) as shown in the following pictures:

![pic 1](https://github.com/gov-vj/Seam-carving-for-content-aware-image-resizing/blob/master/pictures/with_seam.png)
![pic 2](https://github.com/gov-vj/Seam-carving-for-content-aware-image-resizing/blob/master/pictures/with_seam2.png)

After removing vertically seam iteratively multiple times the result was:
![pic 3](https://github.com/gov-vj/Seam-carving-for-content-aware-image-resizing/blob/master/pictures/result_pic.png)

Original pic:

![pic_3](https://github.com/gov-vj/Seam-carving-for-content-aware-image-resizing/blob/master/pictures/sunset_full.png)

##### A vertical seam is a connected path of low energy pixels crossing the image from top to bottom (or left to right).

An energy function defines the similarity of a pixel from it's neighboring pixels. More similar the pixel from it's neighboring pixels less its energy value.

So, the vertical seam is very similar to its neighbors and therefore, we can remove it by not losing significant information.

This can be done using dynamic programming.

dp(i,j)::=energy(i,j)+min[dp(i,j-1), dp(i+1,j-1), dp(i-1,j-1)]  // neighbors of (i,j) in the above layer (j-1 layer)

parent(i,j)::= (i,j-1) if dp(i,j-1) is minimum in above function; (i+1,j-1) if dp(i+1,j-1) is min; (i-1,j-1) if dp(i-1,j-1) is min.

From the equation of dp(i,j), it is clear that in any vertical seam the value of dp(i,j) increases as we go down. So, to find the vertical seam of the minimum energy among all other possible seams we first find the minimum value of dp(i,j) in the last layer (j=height-1) and then traverse from bottom to up using the parent pointer. 
