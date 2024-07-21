//#include <opencv2/core/core.hpp>
//#include <opencv2/imgcodecs/imgcodecs.hpp>
//#include <opencv2/imgproc/imgproc.hpp>
//#include <opencv2/highgui/highgui.hpp>
//#include <opencv2/features2d/features2d.hpp>
//#include <opencv2/xfeatures2d.hpp>
//#include <opencv2/videoio/videoio.hpp>
//
//#include <iostream>
//#include <stdio.h>
//using namespace std;
//using namespace cv;
//
//int main()
//{
//	Mat src_image;
//	Mat grey_image;
//
//	src_image=imread("test_image.jpg");
//
//	if (!src_image.data)
//	{
//		cout << "Could not open image" << endl;
//		return 0;
//	};
//
//	cvtColor(src_image, grey_image, COLOR_BGR2GRAY);
//
//	imwrite("grey.jpg", grey_image);
//
//	cout << "Created grey image" << endl;
//
//    return 0;
//}



#include <opencv2/core.hpp>
#include <opencv2/imgcodecs.hpp>
#include <vector>       // std::vector
#include <opencv2/imgproc/imgproc.hpp>
#include <opencv2/highgui/highgui.hpp>
int main(int argc, char** argv)
{
    // READ RGB color image and convert it to Lab
    cv::Mat bgr_image = cv::imread("clahe_input.png");
    cv::Mat lab_image;
    cv::cvtColor(bgr_image, lab_image, cv::COLOR_BGR2Lab);

    // Extract the L channel
    std::vector<cv::Mat> lab_planes(3);
    cv::split(lab_image, lab_planes);  // now we have the L image in lab_planes[0]

    // apply the CLAHE algorithm to the L channel
    cv::Ptr<cv::CLAHE> clahe = cv::createCLAHE();
    clahe->setClipLimit(4);
    cv::Mat dst;
    clahe->apply(lab_planes[0], dst);

    // Merge the the color planes back into an Lab image
    dst.copyTo(lab_planes[0]);
    cv::merge(lab_planes, lab_image);

    // convert back to RGB
    cv::Mat image_clahe;
    cv::cvtColor(lab_image, image_clahe, cv::COLOR_Lab2BGR);

    //save output image to file
    cv::imwrite("clahe_output.png", image_clahe);
    return 0;
}


