// ToDo:
/* */

// Problem Description
/*
733. Flood Fill
Easy

An image is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0 to 65535).

Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel value newColor, "flood fill" the image.

To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel), and so on. Replace the color of all of the aforementioned pixels with the newColor.

At the end, return the modified image.

Example 1:

Input: 
image = [[1,1,1],
		[1,1,0],
		[1,0,1]]
sr = 1, sc = 1, newColor = 2
Output: [[2,2,2],
		[2,2,0],
		[2,0,1]]
Explanation: 
From the center of the image (with position (sr, sc) = (1, 1)), all pixels connected 
by a path of the same color as the starting pixel are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected
to the starting pixel.

Note:
The length of image and image[0] will be in the range [1, 50].
The given starting pixel will satisfy 0 <= sr < image.length and 0 <= sc < image[0].length.
The value of each color in image[i][j] and newColor will be an integer in [0, 65535].

Hint:
Write a recursive function that paints the pixel if it's the correct color, then recurses on neighboring pixels.
*/

// Conditions & Concepts
/* 
1. 0 <= pixel value <= 65535
2. starting pixel = (sr, sc)
3. imgage : 1~50 * 1~50
4. 
*/

// Code
// submit part
/**
 * @param {number[][]} image
 * @param {number} sr
 * @param {number} sc
 * @param {number} newColor
 * @return {number[][]}
 */
var floodFill = function(image, sr, sc, newColor) {

    var flood = function(image, sr, sc, oldColor, newColor) {
        if (image[sr, sc] == oldColor) {
            image[sr, sc] = newColor;

            if (sr - 1 > 0) { flood(image, sr-1, sc, oldColor, newColor) };

            if (sr + 1 < image.length) { flood(image, sr+1, sc, oldColor, newColor) };

            if (sc - 1 > 0) { flood(image, sc-1, sc, oldColor, newColor) };

            if (sc + 1 < image[0].length) { flood(image, sc+1, sc, oldColor, newColor) };

        }

        return image
    }

    const oldColor = image[sr][sc]

    return flood(image, sr, sc, oldColor, newColor)

};
// test part
/* */

// code here
// 1
/* */
var floodFill = function(image, sr, sc, newColor) {

    var flood = function(image, sr, sc, oldColor, newColor) {
        if (image[sr, sc] == oldColor) {
            image[sr, sc] = newColor;

            if (sr - 1 > 0) { flood(image, sr-1, sc, oldColor, newColor) };

            if (sr + 1 < image.length) { flood(image, sr+1, sc, oldColor, newColor) };

            if (sc - 1 > 0) { flood(image, sc-1, sc, oldColor, newColor) };

            if (sc + 1 < image[0].length) { flood(image, sc+1, sc, oldColor, newColor) };

        }

        return image
    }

    const oldColor = image[sr][sc]

    return flood(image, sr, sc, oldColor, newColor)

};

// 1.1
/*
[[0,0,0],[0,1,1]]
1
1
1

Success
Runtime: 80 ms, faster than 38.84% of JavaScript online submissions for Flood Fill.
Memory Usage: 36.2 MB, less than 100.00% of JavaScript online submissions for Flood Fill.
*/
var floodFill = function(image, sr, sc, newColor) {

    var flood = function(image, sr, sc, oldColor, newColor) {
        if (image[sr, sc] == oldColor) {
            image[sr, sc] = newColor;

            if (sr - 1 > 0) { flood(image, sr-1, sc, oldColor, newColor) };

            if (sr + 1 < image.length) { flood(image, sr+1, sc, oldColor, newColor) };

            if (sc - 1 > 0) { flood(image, sc-1, sc, oldColor, newColor) };

            if (sc + 1 < image[0].length) { flood(image, sc+1, sc, oldColor, newColor) };

        }

        return image
    }

    const oldColor = image[sr][sc]

    if ( oldColor == newColor) { return image} // fix here

    return flood(image, sr, sc, oldColor, newColor)

};


// Test
/*
[[1,1,1],
[1,0,1],
[1,0,1]]
1
1
5
[[1,1,1],
[1,5,1],
[1,5,1]]


[[1,1,1],[1,1,1],[1,1,1]]
1
1
5
[[5,5,5],[5,5,5],[5,5,5]]

*/




