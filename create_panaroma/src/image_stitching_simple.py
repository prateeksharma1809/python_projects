# import the necessary packages
from imutils import paths
import argparse
import imutils
import cv2

def load_images(args):
    # grab the paths to the input images and initialize our images list
    print("[INFO] loading images...")
    imagePaths = sorted(list(paths.list_images(args["images"])))
    images = []
    # loop over the image paths, load each one, and add them to our
    # images to stitch list
    for imagePath in imagePaths:
        image = cv2.imread(imagePath)
        images.append(image)
    return images
def stitch_images(images, output_path):
    # initialize OpenCV's image stitcher object and then perform the image stitching
    print("[INFO] stitching images...")
    stitcher = cv2.createStitcher() if imutils.is_cv3() else cv2.Stitcher_create()
    (status, stitched) = stitcher.stitch(images)

    # if the status is '0', then OpenCV successfully performed image stitching
    if status == 0:
        # write the output stitched image to disk
        cv2.imwrite(output_path, stitched)
        # display the output stitched image to our screen
        cv2.imshow("Stitched", stitched)
        cv2.waitKey(0)
    # otherwise the stitching failed, likely due to not enough keypoints being detected
    else:
        print("[INFO] image stitching failed ({})".format(status))


if __name__ == "__main__":
    # construct the argument parser and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--images", type=str, required=True,
        help="path to input directory of images to stitch")
    ap.add_argument("-o", "--output", type=str, required=True,
        help="path to the output image")
    args = vars(ap.parse_args())

    # load the images
    images = load_images(args)

    # stitch the images
    stitch_images(images, args["output"])

