# Image Stitching Simple

This is a Python script that performs image stitching using a simple approach. It takes a set of input images and stitches them together to create a panorama image.

## Prerequisites

Before running the script, make sure you have the following:

- Python 3.x installed on your system
- OpenCV library installed (`pip install opencv-python`)

## Usage

To run the script, use the following command:

```
python image_stitching_simple.py -i <input_directory> -o <output_file>
```

- `<input_directory>`: The directory containing the input images. Make sure the images are in the correct order for stitching.
- `<output_file>`: The path and filename for the output panorama image.

Example usage:

```
python image_stitching_simple.py -i ../images -o output.png
```

## Output

After running the script, the output panorama image will be saved to the specified `<output_file>`.

## Notes

- This script uses a simple approach for image stitching and may not work well with complex scenes or images with significant perspective distortion.
- It is recommended to have input images with overlapping regions for better stitching results.
