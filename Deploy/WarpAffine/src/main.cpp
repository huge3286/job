// TODO 如何安装包
#include <cuda_runtime.h>
#include <opencv2/opencv.hpp>
#include <stdio.h>

using namespace cv;

#define min(a, b)  ((a) < (b) ? (a) : (b))
#define checkRuntime(op)  __check_cuda_runtime((op), #op, __FILE__, __LINE__)

bool __check_cuda_runtime(cudaError_t code, const char* op, const char* file, int line){
    if(code != cudaSuccess){
        const char* err_name = cudaGetErrorName(code);    
        const char* err_message = cudaGetErrorString(code);  
        printf("runtime error %s:%d  %s failed. \n  code = %s, message = %s\n", file, line, op, err_name, err_message);   
        return false;
    }
    return true;
}

// 函数声明
void warp_affine_bilinear(
    uint8_t *src, int src_width, int src_height,
    uint8_t *dst, int dst_width, int dst_height
);

// center align 居中对齐
Mat warpaffine_to_center_align(Mat image, const Size &size)
{
    // TODO CV_8uC3是什么
    Mat output(size, CV_8uC3);
    // 这个操作是在GPU上进行的 这两个指针是指向GPU的地址
    uint8_t *psrc_device = nullptr;
    uint8_t *pdst_device = nullptr;

    // 在GPU上分配空间
    size_t src_size = image.cols * image.rows;
    size_t dst_size = size.width * size.height;
    checkRuntime(cudaMalloc(&psrc_device, src_size));
    checkRuntime(cudaMalloc(&pdst_device, dst_size));

    // 复制到GPU上 Mat.data是头指针
    checkRuntime(cudaMemcpy(psrc_device, image.data, src_size, cudaMemcpyHostToDevice));

    warp_affine_bilinear(
        psrc_device, image.cols, image.rows,
        pdst_device, size.width, size.height
    );

    checkRuntime(cudaFree(pdst_device));
    checkRuntime(cudaFree(psrc_device));

    return output;
}

int main() {
    Mat image = imread('lean.png');
    Mat output = warpaffine_to_center_align(image, Size(640, 640));
    imwrite("output.png")
}