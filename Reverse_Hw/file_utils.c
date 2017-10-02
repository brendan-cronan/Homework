#include "file_utils.h"
#include <stdio.h>
#include <stdlib.h>
#include <sys/stat.h>
int read_file(char* filename,char** buffer){

	FILE* filePointer;//Pointer to the file.

	filePointer=fopen(filename,"r");//uses fopen to get a file pointer 
				//uses "r" to indicate it will be read-only	

	if(!filePointer){//if it is null, print an error and return.
		fprintf(stderr, "Could Not Open File To Read.");
		return -1;
	}

	//this all finds the size of the file.
	struct stat st;
	stat(filename, &st);
	int size=st.st_size;
	
	//this allocates the buffer on the heap with the size of the file
	//times the sizeof a char.
	buffer[0]=(char*)malloc(sizeof(char)*size);
	
	//checks if there was an error.
	//probably not necessary.
	if(*buffer==NULL||buffer==NULL)
		fprintf(stderr,"\nBuffer Creation Failure.\n");
	
	//loops through the file up to the size of the file.
	for(int n=0;n<size;n++){
		buffer[0][n]=fgetc(filePointer);//puts each character in the
						//file into the buffer.
	}
	
	fclose(filePointer);//closes the file.
	return size;//returns the number of bytes read.
}

int write_file(char* filename, char* buffer, int size){

	//same as all of the above.
	FILE* filePtr;
	filePtr = fopen(filename,"w");
	
	if(!filePtr){
		fprintf(stderr, "Could Not Open File To Write.");
		return -1;
	}
	
	//loops through the buffer provided and prints each character to file.	
	for(int i=0;i<size;i++){
		fputc(buffer[i],filePtr);
	}
	
	//cant forget to close it.
	fclose(filePtr);
	
	//return the number of written bytes.
	return size;
}
