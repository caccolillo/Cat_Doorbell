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


#include <opencv2/photo.hpp>
#include <opencv2/core.hpp>
#include <opencv2/imgcodecs.hpp>
#include <vector>       // std::vector
#include <opencv2/imgproc/imgproc.hpp>
#include <opencv2/highgui/highgui.hpp>
int main(int argc, char** argv)
{
    // READ RGB color image
    cv::Mat bgr_image = cv::imread("denoising_input.png");

    // apply the fastNlMeansDenoisingColored denoising algorithm
    cv::Mat image_denoising;
    cv::fastNlMeansDenoisingColored(bgr_image,image_denoising,20,20,7,21);

    //save output image to file
    cv::imwrite("denoising_output.png", image_denoising);
    return 0;
}


