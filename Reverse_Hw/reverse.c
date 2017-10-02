#include "file_utils.h"
#include <stdio.h>
#include <stdlib.h>

//Created by: Brendan Cronan
//Worked with Luke Basset and referenced stack overflow for file i/o basics.


int main(int argc,char** argv){

//sets the input and output file names to cmd line args.
char* inputFileName= argv[1];
char* outputFileName = argv[2];

//creates the buffer char "arrays"
char* inBuffer;
char* outBuffer;

//calls the read file function and assigns the return to a size int.
int size = read_file(inputFileName,&inBuffer);

if(size<=0){//if it didnt read any bytes or returned a negative 1,
	fprintf(stderr,"Cannot Read File.");//print an error message.
	return 1;//return 1 to indicate incorrect run.
}

//allocates outBuffer to the size of the inBuffer since we are just copying 
//the same amount of data.
outBuffer=malloc(sizeof(char)*size);


//reverses the array from inBuffer to outBuffer.
int c=0;
for(int i=size-1;i>=0;i--){
	outBuffer[i]=inBuffer[c];
	c++;
}


//frees the inBuffer because we dont need it anymore.
free(inBuffer);

//calls write file function and then stores it in int write
int write=write_file(outputFileName,outBuffer,size);

//if it doesnt write anything or returns -1, error msg.
if(write<=0){
	fprintf(stderr,"Cannot Write File.");
	return 1;//return 1 to indicate incorrect run.
}

free(outBuffer);//free up the last thing and return 0 to indicate a success.
return 0;
}
