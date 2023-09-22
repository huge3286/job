#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2\imgproc\imgproc.hpp>
#include <iostream>
#include <vector>
using namespace cv;
using namespace std;



static void sort(int n, const vector<float> x, vector<int> indices)
{
// ���������������н�������indices�е�����
// n����������// x����������// indices����ʼΪ0~n-1��Ŀ 
	
	int i, j;
	for (i = 0; i < n; i++)
		for (j = i + 1; j < n; j++)
		{
			if (x[indices[j]] > x[indices[i]])
			{
				//float x_tmp = x[i];
				int index_tmp = indices[i];
				//x[i] = x[j];
				indices[i] = indices[j];
				//x[j] = x_tmp;
				indices[j] = index_tmp;
			}
		}
}



int nonMaximumSuppression(int numBoxes, const vector<CvPoint> points,const vector<CvPoint> oppositePoints, 
	const vector<float> score,	float overlapThreshold,int& numBoxesOut, vector<CvPoint>& pointsOut,
	vector<CvPoint>& oppositePointsOut, vector<float> scoreOut) 
{
// ʵ�ּ����ľ��δ��ڵķǼ���ֵ����nms
// numBoxes��������Ŀ// points���������Ͻ������// oppositePoints���������½������// score�����ڵ÷�
// overlapThreshold���ص���ֵ����// numBoxesOut�����������Ŀ// pointsOut������������Ͻ������
// oppositePoints������������½������// scoreOut��������ڵ÷�
	int i, j, index;
	vector<float> box_area(numBoxes);				// ���崰���������������ռ� 
	vector<int> indices(numBoxes);					// ���崰������������ռ� 
	vector<int> is_suppressed(numBoxes);			// �����Ƿ����Ʊ���־������ռ� 
	// ��ʼ��indices��is_supperssed��box_area��Ϣ 
	for (i = 0; i < numBoxes; i++)
	{
		indices[i] = i;
		is_suppressed[i] = 0;
		box_area[i] = (float)( (oppositePoints[i].x - points[i].x + 1) *(oppositePoints[i].y - points[i].y + 1));
	}
	// �����봰�ڰ��շ�����ֵ�������������ı�ŷ���indices�� 
	sort(numBoxes, score, indices);
	for (i = 0; i < numBoxes; i++)                // ѭ�����д��� 
	{
		if (!is_suppressed[indices[i]])           // �жϴ����Ƿ����� 
		{
			for (j = i + 1; j < numBoxes; j++)    // ѭ����ǰ����֮��Ĵ��� 
			{
				if (!is_suppressed[indices[j]])   // �жϴ����Ƿ����� 
				{
					int x1max = max(points[indices[i]].x, points[indices[j]].x);                     // �������������Ͻ�x�������ֵ 
					int x2min = min(oppositePoints[indices[i]].x, oppositePoints[indices[j]].x);     // �������������½�x������Сֵ 
					int y1max = max(points[indices[i]].y, points[indices[j]].y);                     // �������������Ͻ�y�������ֵ 
					int y2min = min(oppositePoints[indices[i]].y, oppositePoints[indices[j]].y);     // �������������½�y������Сֵ 
					int overlapWidth = x2min - x1max + 1;            // �����������ص��Ŀ��� 
					int overlapHeight = y2min - y1max + 1;           // �����������ص��ĸ߶� 
					if (overlapWidth > 0 && overlapHeight > 0)
					{
						float overlapPart = (overlapWidth * overlapHeight) / box_area[indices[j]];    // �����ص��ı��� 
						if (overlapPart > overlapThreshold)          // �ж��ص������Ƿ񳬹��ص���ֵ 
						{
							is_suppressed[indices[j]] = 1;           // ������j���Ϊ���� 
						}
					}
				}
			}
		}
	}

	numBoxesOut = 0;    // ��ʼ�����������Ŀ0 
	for (i = 0; i < numBoxes; i++)
	{
		if (!is_suppressed[i]) numBoxesOut++;    // ͳ�����������Ŀ 
	}
	index = 0;
	for (i = 0; i < numBoxes; i++)                  // �����������봰�� 
	{
		if (!is_suppressed[indices[i]])             // ��δ�������ƵĴ�����Ϣ���浽�����Ϣ�� 
		{
			pointsOut.push_back(Point(points[indices[i]].x,points[indices[i]].y));
			oppositePointsOut.push_back(Point(oppositePoints[indices[i]].x,oppositePoints[indices[i]].y));
			scoreOut.push_back(score[indices[i]]);
			index++;
		}

	}

	return true;
}

int main()
{
	Mat image=Mat::zeros(600,600,CV_8UC3);
	int numBoxes=4;
	vector<CvPoint> points(numBoxes);
	vector<CvPoint> oppositePoints(numBoxes);
	vector<float> score(numBoxes);

	points[0]=Point(200,200);oppositePoints[0]=Point(400,400);score[0]=0.99;
	points[1]=Point(220,220);oppositePoints[1]=Point(420,420);score[1]=0.9;
	points[2]=Point(100,100);oppositePoints[2]=Point(150,150);score[2]=0.82;
	points[3]=Point(200,240);oppositePoints[3]=Point(400,440);score[3]=0.5;
	
	
	float overlapThreshold=0.8;
	int numBoxesOut;
	vector<CvPoint> pointsOut;
	vector<CvPoint> oppositePointsOut;
	vector<float> scoreOut;

	nonMaximumSuppression( numBoxes,points,oppositePoints,score,overlapThreshold,numBoxesOut,pointsOut,oppositePointsOut,scoreOut);
	for (int i=0;i<numBoxes;i++)
	{
		rectangle(image,points[i],oppositePoints[i],Scalar(0,255,255),6);
		char text[20];
		sprintf(text,"%f",score[i]);
		putText(image,text,points[i],CV_FONT_HERSHEY_COMPLEX, 1,Scalar(0,255,255));
	}
	for (int i=0;i<numBoxesOut;i++)
	{
		rectangle(image,pointsOut[i],oppositePointsOut[i],Scalar(0,0,255),2);
	}
	
	imshow("result",image);

	waitKey();
	return 0;
}