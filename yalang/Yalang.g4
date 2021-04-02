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

expression  : NUMBER                                                                      #numberLiteral
            | STRING                                                                      #stringLiteral
            | ('<' (ins+=ID ',')* ins+=ID '>')?
              '(' ((args+=ID ',')* args+=ID)? ')'
              ('<' (outs+=ID ',')* outs+=ID '>')?
              '{' (stmts+=statement ';')+ '}'                                             #fnLiteral
            | ID                                                                          #identifier
            | callee=expression '(' ((params+=expression ',')* params+=expression)? ')'   #fnCall
            | left=expression '<' right=ID '>'                                            #fnGetStream
            | '<<' expression                                                             #streamRead
            | '-' expression                                                              #unaryMinus
            | '(' expression ')'                                                          #nested
            | left=expression op=('*'|'/'|'%') right=expression                           #mathHigh
            | left=expression op=('+'|'-')     right=expression                           #mathLow
            | ID '=' expression                                                           #assignment
            | left=expression '>>' right=expression                                       #streamWrite
            ;

printStmt   : '!' expression
            ;

returnStmt  : 'return' expression
            ;
