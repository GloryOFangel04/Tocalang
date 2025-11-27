grammar MinhaLinguagem;

// --- PARSER ---

programa
    : K_DECLARACOES declaracao* K_ALGORITMO K_INICIO comando* K_FIM EOF
    ;

declaracao
    : VARIAVEL DELIM tipo
    ;

tipo: K_INTEIRO | K_REAL | K_BOOLEANO | K_TEXTO;

comando
    : K_ATRIBUIR expr K_A VARIAVEL              # CmdAtribuir
    | K_LER VARIAVEL                            # CmdLer
    | K_IMPRIMIR expr                           # CmdImprimir
    | K_SE expr K_ENTAO comando* (K_SENAO comando*)? K_FIM # CmdSe
    | K_ENQUANTO expr comando* K_FIM            # CmdEnquanto
    
    
    | K_PARA VARIAVEL K_DE expr K_ATE expr K_FACA comando* K_FIM # CmdPara
   
    | K_ESCOLHA expr (K_CASO expr DELIM comando*)+ (K_PADRAO DELIM comando*)? K_FIM # CmdEscolha
    ;

expr
    : expr op=('*'|'/') expr      # ExprMulDiv
    | expr op=('+'|'-') expr      # ExprAddSub
    | expr op=OP_REL expr         # ExprRelacional
    | expr K_E expr               # ExprE
    | expr K_OU expr              # ExprOu
    | NUMINT                      # ExprInt
    | NUMREAL                     # ExprReal
    | BOOL_LIT                    # ExprBool
    | VARIAVEL                    # ExprVar
    | CADEIA                      # ExprString
    | ABREPAR expr FECHAPAR       # ExprParentesis
    ;

// --- LEXER ---

K_DECLARACOES : 'DECLARACOES';
K_ALGORITMO   : 'ALGORITMO';
K_INTEIRO     : 'INTEIRO';
K_REAL        : 'REAL';
K_BOOLEANO    : 'BOOLEANO';
K_TEXTO       : 'TEXTO';   
K_ATRIBUIR    : 'ATRIBUIR';
K_A           : 'A';
K_LER         : 'LER';
K_IMPRIMIR    : 'IMPRIMIR';
K_SE          : 'SE';
K_ENTAO       : 'ENTAO';
K_SENAO       : 'SENAO';  
K_ENQUANTO    : 'ENQUANTO';
K_INICIO      : 'INICIO';
K_FIM         : 'FIM';
K_E           : 'E';
K_OU          : 'OU';


K_PARA     : 'PARA';
K_DE       : 'DE';
K_ATE      : 'ATE';
K_FACA     : 'FACA';
K_ESCOLHA  : 'ESCOLHA';
K_CASO     : 'CASO';
K_PADRAO   : 'PADRAO';

BOOL_LIT : 'VERDADEIRO' | 'FALSO'; 
NUMINT   : ('+'|'-')?('0'..'9')+ ;
NUMREAL  : ('+'|'-')?('0'..'9')+ ('.' ('0'..'9')+)? ;
VARIAVEL : ('a'..'z'|'A'..'Z'|'_') ('a'..'z'|'A'..'Z'|'0'..'9'|'_')* ;
CADEIA   : '\'' ( ESC_SEQ | ~('\''|'\\') )* '\'' ;

fragment ESC_SEQ : '\\\'';

COMENTARIO : '%' ~('\n'|'\r')* '\r'? '\n' -> skip ;
WS         : [ \t\r\n]+ -> skip ;

OP_REL  : '>' | '>=' | '<' | '<=' | '<>' | '=' ;
DELIM   : ':' ;
ABREPAR : '(' ;
FECHAPAR: ')' ;