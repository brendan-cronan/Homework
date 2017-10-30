%{
	#include <stdio.h>
	#include <stdlib.h>
	#include "zoomjoystrong.h"
	//declares functions used below to check values and to draw shapes.
	void setCol(int r, int g, int b);
	int yylex();
	int yyerror(char* s);
	int isValidRGB(int in);
	int checkX(int x);
	int checkY(int y);
	void drawCir(int x,int y, int r);
	void drawPt(int x,int y);
	void drawRect(int x,int y,int x2,int y2);
	void drawLn(int x,int y,int x2,int y2);
%}
/*************************************************
*	This union stores values. floats are not used.
*************************************************/
%union{
  int iVal;
  float fVal;
}
/*************************************************
*	set all valid tokens and store INT and FLOAT into iVal and fVal respectively.
*************************************************/
%token LINE
%token POINT
%token RECTANGLE
%token CIRCLE
%token SET_COLOR
%token <iVal> INT
%token <fVal> FLOAT
%token END
%token SEMI



/*************************************************
*	this is the start of the parse tree.
*************************************************/
%start program


%%

program:           statement_list end_state

statement_list:    statement
              |    statement statement_list
							;
statement:         point
              |    line
              |    circle
							|		 rectangle
							|		 set_color
							;

/*************************************************
*	These methods take a keyword and their respective parameters and call the
*	functions below with said parameters.
*	$number indicates a argument's value associated with it.
*	end just calls finish to dispose the window and then exits the program.
*************************************************/

point:						POINT INT INT SEMI											{drawPt($2,$3);}
circle:						CIRCLE INT INT INT SEMI 								{drawCir($2,$3,$4)}
line:							LINE INT INT INT INT SEMI								{drawLn($2,$3,$4,$5);}
rectangle:				RECTANGLE INT INT INT INT SEMI					{drawRect($2,$3,$4,$5);}

set_color:				SET_COLOR	INT INT INT SEMI							{setCol($2,$3,$4);}

end_state:				END SEMI																{finish();exit(0);}








%%

/*************************************************
*	For methods below, 0 is good.  1 is bad.
*************************************************/
int checkX(int x){
	if(x>=0&&x<=WIDTH)
		return 0;
	return 1;
}
int checkY(int y){
	if(y>=0&&y<=HEIGHT)
		return 0;
	return 1;
}
int isValidRGB(int in){
	if(in>=0 && in <= 255){
		return 0;//good!
	}
	else{
		return 1;//BAD!
	}
}

/*************************************************
*	These methods just handle errors and then draw their respective objects
*	if everything checks out.
*************************************************/
void drawPt(int x, int y){
	if(checkX(x)==0 && checkY(y)==0)
		point(x,y);
	else
		fprintf(stderr,"INVALID POINT AT [%d, %d]\n",x,y);

}
void drawCir(int x,int y, int r){
	if(checkX(x)==0 && checkY(y)==0){
		if(r<=x && r<=y && r>=0 && r<=WIDTH-x && r<=HEIGHT-y){
			circle(x,y,r);
		}
		else{
			fprintf(stderr,"INVALID CIRCLE AT [%d, %d, %d]\n",x,y,r);
		}
	}
	else{
		fprintf(stderr,"INVALID CIRCLE AT [%d, %d, %d]\n",x,y,r);
	}
}
void drawRect(int x, int y,int x2,int y2){
	if(checkX(x)==0 && checkY(y)==0 && checkX(x2)==0 && checkY(y2)==0)
		rectangle(x,y,x2,y2);
	else
		fprintf(stderr,"INVALID RECTANGLE AT [%d,%d,  %d,%d]\n",x,y,x2,y2);

}
void drawLn(int x, int y,int x2,int y2){
	if(checkX(x)==0 && checkY(y)==0 && checkX(x2)==0 && checkY(y2)==0)
		line(x,y,x2,y2);
	else
		fprintf(stderr,"INVALID LINE AT [%d,%d,  %d,%d]\n",x,y,x2,y2);

}

void setCol(int r, int g, int b){
	if(isValidRGB(r)==0&&isValidRGB(g)==0&&isValidRGB(b)==0){
		set_color(r,g,b);
	}
	else{
		fprintf(stderr, "INVALID RGB VALUE: [%d, %d, %d]\n",r,g,b);
	}
}


int yyerror(char* s)
{
  fprintf(stderr, "%s\n",s);
	return 0;
}



/*************************************************
*	calls the graphics lib setup and then calls yyparse.
*************************************************/
int main(int argc, char** argv){
setup();
yyparse();
return 0;



}
