%{
  #include "zoomjoystrong.tab.h"
%}
%option noyywrap


%%


end		    {return END;}
;		      {return SEMI;}
point		  {return POINT;}
line		  {return LINE;}
circle		{return CIRCLE;}
rectangle	{return RECTANGLE;}
set_color	{return SET_COLOR;}

/*************************************************
*	adds any int to iVal after converting string to int.
* does the same for float.
*************************************************/
[0-9]+		{yylval.iVal=atoi(yytext);  return INT;}
[0-9]*\.[0-9]+	{yylval.fVal=atoi(yytext); return FLOAT;}



/*************************************************
*	This matches any number of spaces, whitespace characters, tabs or newlines
* Ignores them.
Then, if there is ANYTHING else, it tells the user it is incorrect.
*************************************************/
[" "]+|\s+|\t+|\n+      	;
. ;             {fprintf(stderr, "Lexing Error.");}


%%
