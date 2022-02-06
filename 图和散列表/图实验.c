# coding = utf-8
# @author:yingzhudashu

#include<stdio.h>
#include<stdlib.h>
#include<time.h>
#define MAX 9999
int size=1000;
double p=0.05;
int m[1001][1001];
int degree[1001];
int Dis[1001][1001];	
double e[1001][1001];
double E[1001][1001];

void ER(){
	int i, j;
	double r=0.0;
	for(i=1;i<=size;i++){
		m[i][i]=0;
		for(j=i+1;j<=size;j++){
			r = rand()/(RAND_MAX+1.0);		
			if(r<p) m[i][j]=m[j][i]=1;
			else m[i][j]=m[j][i]=0;
		}
	}
}

void degreeDistribution()
{
	double n[1001];
	int i, j;		
	for(i=1;i<=size;i++){
		degree[i]=0;
		n[i]=0.0;
		for(j=1;j<=size; j++ )
			degree[i]=degree[i]+m[i][j];
	}
	for(i=1;i<=size;i++)
		n[degree[i]]++;
	FILE* fp;
    fp=fopen("degreeDistribution.txt","w");
    for(i=1;i<=size;i++){
    	if(n[i] != 0)
    		fprintf(fp, "%d %f\n",i,n[i]/(double)size);
	}
    fclose(fp);
}

void ClusteringCoefficient()
{
	FILE *fp = fopen("cluster.txt","w");
	int i, j, l;
	double k[1001], n=0;
    for(i=1;i<=size;i++){
    	k[i]=0;
        for(j=1;j<=size;j++)
        	for(l=j;l<=size;l++)
                if(m[i][j] && m[i][l] && m[j][l])
                    k[i]=k[i]+1;
        k[i]=2*k[i]/((size-1)*size);
        fprintf(fp,"%d %f\n", i, k[i]);
	}
	for(i=1;i<=size;i++)
		n=n+k[i];
	n=n/size;
	printf("����ͼ�ľ���ϵ��:%f\n", n);
}

void shortestpath(){
	FILE *fp = fopen("shortest_distance.txt","w");
	int i, j, k;
	int distance = 0, count = 0;
	double aveDis;
	for(i=1;i<=size;i++){
		Dis[i][i]=0;
		for(j=i+1;j<=size;j++){
			if(m[j][i]==1) Dis[i][j]=Dis[j][i]=1;
			else Dis[i][j]=Dis[j][i]=MAX;	
		}
	}
	for(i=1;i<=size;i++){
		for(j=1;j<=size;j++){
			for(k=1;k<=1000;k++){
				if(Dis[j][k]>Dis[j][i]+Dis[i][k])
					Dis[j][k] =Dis[j][i]+Dis[i][k];
			}
		}
	}
	for(i = 1; i <= 1000; i++){
		for(j = 1;j <= 1000; j++){
			fprintf(fp,"%d-%d:%d\n",i,j,Dis[i][j]);
			if(Dis[i][j]==MAX)
				continue;
			else{
				if(i!=j) count++;
				distance+=Dis[i][j];
			}	
		}
	}
	aveDis = (double)distance/count;
	printf("ƽ��·������Ϊ��%f\n", aveDis);
	fclose(fp);
}

void Degree_correlation(){
	int i, j;
	int size1=0;
	double r, a=0, b, s=0, size2=0,  size3=0, size4=0, size5=0;
	double k[1001], pk[1001], qk[1001];

	for(i=1;i<=size;i++)
		for(j=1;j<=size;j++)
			e[i][j] = 0;
	for(i=1;i<=size;i++)
		for(j=1;j<=1000;j++)
			if(degree[i]!=0 && degree[j]!=0)
				e[degree[i]][degree[j]]++;
	for(i=1;i<=size;i++)
		for(j=1;j<=size;j++)
			s+=e[i][j];
	for(i=1;i<=size;i++)
		for(j=1;j<=size;j++)
			E[i][j]=e[i][j]/s;
		
	for(i=1;i<=size;i++)
		k[i]=0;
	for(i=1;i<=size;i++)
		k[degree[i]]++;
	for(i=1;i<=size;i++){
		pk[i]=k[i]/1000;
		size2+=i*pk[i];	
	}	
	for(i=1;i<=size;i++){
		qk[i]=(i*pk[i])/size2;
		size3+=i*qk[i];
	}

	for(i=1;i<=size;i++)
		size4+=i*i*qk[i]*qk[i];
	size4=size4-size3*size3;
	for(i=1;i<=size;i++){
		for(j=1;j<=size;j++){
			size5+=i*j*(E[i][j]-qk[i]*qk[j]);
		}
	}
	r=(1/size4)*size5;
	printf("�ȵ������Ϊ��%f\n", r);
}

int main()
{
	srand((unsigned)time(NULL));
	ER();
	degreeDistribution();
	ClusteringCoefficient();
	shortestpath();
	Degree_correlation();
	return 0;
}
