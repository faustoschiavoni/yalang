grammar Yalang;

WS : [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines

fragment DIGIT  : ('0'..'9');
fragment LETTER : ('a'..'z'|'A'..'Z');

ID      : (LETTER|'_') (LETTER|DIGIT|'_')*;
NUMBER  : DIGIT+ ('.' DIGIT+)?;
STRING : '\'' ~('\r' | '\n' | '\'')* '\'' ;

program   : (statement ';')+ EOF;
statement : expression
          | printStmt
          | returnStmt
          ;

expression  : NUMBER                                                                #numberLiteral
            | STRING                                                                #stringLiteral
            | '(' ((args+=ID ',')* args+=ID)? ')' '{' (stmts+=statement ';')+ '}'   #fnLiteral
            | ID                                                                    #identifier
            | ID '(' ((params+=expression ',')* params+=expression)? ')'            #fnCall
            | '-' expression                                                        #unaryMinus
            | '(' expression ')'                                                    #nested
            | left=expression op=('*'|'/'|'%') right=expression                     #mathHigh
            | left=expression op=('+'|'-')     right=expression                     #mathLow
            | ID '=' expression                                                     #assignment
            ;

printStmt   : '!' expression
            ;

returnStmt  : 'return' expression
            ;
