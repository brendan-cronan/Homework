%{
	#include <stdio.h>
	#include <stdlib.h>
	#include "zoomjoystrong.h"
	void setCol(int r, int g, int b);
	int yylex();
	int yyerror(char* s);
%}

%union{
  int iVal;
  float fVal;
  char* sVal;
}

%token LINE
%token POINT
%token RECTANGLE
%token CIRCLE
%token SET_COLOR
%token <iVal> INT
%token <fVal> FLOAT
%token END
%token SEMI

%start program


%%
program:           statement_list end_state

statement_list:    statement
              |    statement statement_list
							//|		 end_state
							;
statement:         point
              |    line
              |    circle
							|		 rectangle
							|		 set_color
							//|		 end_state
							;

point:						POINT INT INT SEMI											{point($2,$3);}
circle:						CIRCLE INT INT INT SEMI 								{circle($2,$3,$4);}
line:							LINE INT INT INT INT SEMI								{line($2,$3,$4,$5);}
rectangle:				RECTANGLE INT INT INT INT SEMI					{rectangle($2,$3,$4,$5);}

set_color:				SET_COLOR	INT INT INT SEMI							{setCol($2,$3,$4);}

end_state:				END SEMI																{finish();exit(0);}








%%



void setCol(int r, int g, int b){
	//set_color(r,g,b);
}


int yyerror(char* s)
{
  fprintf(stderr, "%s\n",s);
	return 0;
}




int main(int argc, char** argv){
setup();
yyparse();
return 0;



}
