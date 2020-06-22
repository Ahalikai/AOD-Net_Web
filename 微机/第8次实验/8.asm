DATA SEGMENT 
 RATE DW 524,588,660,698,784,880,988,1048 ;频率表 
 MESSAGE DB 'Please input 1 ~ 8' ;提示信息 
 DB 'to get the corresponding voice!',0ah,0dh 
 DB 'Quit with (q):',0ah,0dh,'$' 
 num DB '1','2','3','4','5','6','7','8' 
DATA ENDS 
STCK SEGMENT STACK 
 db 100 DUP(?) 
STCK ENDS 
CODE SEGMENT 
 ASSUME CS:CODE,DS:DATA 
START: 
 MOV AX,DATA; 
 MOV DS,AX; 
 LEA DX,MESSAGE; 输出提示信息 
 MOV AH,09H; 
 INT 21H; 
;输入音符 
INPUT: 
 MOV AH,01H; 
 INT 21H; 
 
 CMP AL,'q'; 若输入 q,则退出程序 
 JZ EXIT 
 
 CALL PIANO; 调用程序,根据输入音符发出相应声音 
 
 JMP INPUT 
;退出程序 
EXIT: 
 MOV AH,4CH; 
 INT 21H; 
 
 ;子程序名：PIANO 
 ;功能： 将 AL 寄存器中字符 1、2、3、4、5、6、7、i 的 ASCII 作为音符 
 ; 查频率表(RATE),使扬声器发出不同频率的声音 
 PIANO PROC 
 PUSH BX; 
 PUSH AX; 
 PUSH DX; 
 MOV BL,AL 
 SUB BL,30H 
 MOV BH,0 
 CMP AL,NUM[BX-1] 
 JZ VOICE 
 JMP QUIT_PIANO 
VOICE: 
 DEC BX 
 ADD BX,BX 
 
 MOV AX,0000H; 常数 120000H 做被除数 
 MOV DX,0012H; 
 
 DIV RATE[BX]; 计算频率值 
 MOV BX,AX; 将之存入 BX 寄存器 
 
 MOV AL,10110110B; 设置定时器工作方式 
 OUT 43H,AL 
 
 MOV AX,BX; 
 OUT 42H,AL; 设置低位 
 
 MOV AL,AH; 设置高位 
 OUT 42H,AL 
 
 IN AL,61H; 打开与门 
 OR AL,03H; 
 OUT 61H,AL 
 
 CALL DELAY 
 
 IN AL,61H; 关闭与门 
 AND AL,0FCH; 
 OUT 61H,AL; 
;退出程序 
QUIT_PIANO: 
 POP DX 
 POP AX 
 POP BX; 
 RET 
 PIANO ENDP 
 
 
;子程序名：DELAY 
;功能： 延迟一定时间 
 DELAY PROC 
 PUSH CX 
 MOV CX,03H; 
 DELAYLOOP1: 
 PUSH CX; 
 MOV CX,0FFFFH 
 DELAYLOOP2: 
 LOOP DELAYLOOP2 
 POP CX; 
 LOOP DELAYLOOP1 
 POP CX 
 RET 
 DELAY ENDP 
 
CODE ENDS 
 END START