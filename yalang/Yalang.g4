grammar Yalang;

WS : [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines

fragment DIGIT  : ('0'..'9');
fragment LETTER : ('a'..'z'|'A'..'Z');

ID      : (LETTER|'_') (LETTER|DIGIT|'_')*;
NUMBER  : DIGIT+ ('.' DIGIT+)?;
STRING : '\'' ~('\r' | '\n' | '\'')* '\'' ;

program   : (statement ';')+ EOF;
statement : expression;

expression  : NUMBER                                              #numberLiteral
            | STRING                                              #stringLiteral
            | ID                                                  #identifier
            | ID '=' expression                                   #assignment
            | '-' expression                                      #unaryMinus
            | '(' expression ')'                                  #nested
            | left=expression op=('*'|'/'|'%') right=expression   #mathHigh
            | left=expression op=('+'|'-')     right=expression   #mathLow
            ;
