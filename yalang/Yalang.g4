grammar Yalang;

WS : [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines

fragment DIGIT  : ('0'..'9');
fragment LETTER : ('a'..'z'|'A'..'Z');

ID      : (LETTER|'_') (LETTER|DIGIT|'_')*;
NUMBER  : DIGIT+ ('.' DIGIT+)?;

program   : (statement ';')+ EOF;
statement : expression;

expression  : NUMBER                                              #numberLiteral
            | ID                                                  #identifier
            | '-' expression                                      #unaryMinus
            | '(' expression ')'                                  #nested
            | left=expression op=('*'|'/'|'%') right=expression   #mathHigh
            | left=expression op=('+'|'-')     right=expression   #mathLow
            ;
