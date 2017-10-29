%{
	#include <stdio.h>
	void setCol(int r, int g, int b);

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
%token <ival> INT
%token <fVal> FLOAT
%token END
%token SEMI

%start program


%%
program:           statement_list END SEMI
statement_list:    statement
              |    statement statement_list
							;
statement:         point
              |    line
              |    circle
							|		 rectangle
							|		 set_color
							;

number:						INT			{"$$"=iVal;}
							|		FLOAT		{"$$"=iVal;}
							;
point:						POINT number number											{point("$1","$2");}
circle:						CIRCLE number number number number			{circle("$1","$2","$3","$4");}
line:							LINE number number number number				{line("$1","$2","$3","$4");}
rectangle:				RECTANGLE number number number number		{rect("$1","$2","$3","$4");}

set_color:				SET_COLOR	INT INT INT										{setCol("$1","$2","$3");}










%%



void setCol(int r, int g, int b){
	set_color(r,g,b);
}







int main(int argc, char** argv){
setup();
yyparse();
return 0;



}
