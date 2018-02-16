/*************************************************************
CALC.G
*************************************************************/
#header <<
typedef double Attrib;
#define zzcr_attr(a,tok,t)      sscanf(t,"%lf",a);
>>
<<
static double mem;
int main()
{ ANTLR(session(),stdin);
  return 0;
}
>>
#token WhiteSpace "[\t\ ]*" << zzskip(); >>
#token NUMBER "[0-9]+{.[0-9]+}"
session : (asgn "\n" << printf("\t%g\n", $1); >>)*
          "\n" << exit(0); >>
        ;
asgn    : "\=" expr << mem = $2; $asgn = $2; >>
        | expr << $asgn = $1; >>
        ;
expr    : term << $expr = $1; >>
          ("\+" term << $expr += $2; >>
           | "\-" term << $expr -= $2; >>
          )*
        ;
term    : factor << $term = $1; >>
          ("\*" factor << $term *= $2; >>
           | "\/" factor << $term /= $2; >>
          )*
;
factor  : "\-" factor << $factor = - $2; >>
        | NUMBER << $factor = $1; >>
        | "\(" expr "\)" << $factor = $2; >>
        | "\m" << $factor = mem; >>
        ;
