grammar Simple;

prog: classDef+ ;

classDef
    : 'class' ID '{' member+ '}' 
    ;

member
    : 'int' ID ';'
    | 'int' ID '(' ID ')' '{' stat* '}' 
    ;

stat
    : ID '=' expr ';'
    | expr ';'
    ;

expr
    : expr op=('*'|'/') expr     # MulDiv
    | expr op=('+'|'-') expr     # AddSub
    | '(' expr ')'               # Parens
    | ID '(' expr ')'            # FuncCall
    | ID                         # Var
    | INT                        # Int
    ;

INT : [0-9]+ ;
ID  : [a-zA-Z_][a-zA-Z0-9_]* ;
WS  : [ \t\r\n]+ -> skip ;
