DATAS SEGMENT
    tishi db 'Please enter a string!(End with 0)','$'
    outs  db 'The Uppercase steing is:','$';此处输入数据段代码  
DATAS ENDS

STACKS SEGMENT
    ;此处输入堆栈段代码
STACKS ENDS

CODES SEGMENT
    ASSUME CS:CODES,DS:DATAS,SS:STACKS
START:
    MOV AX,DATAS
    MOV DS,AX
    mov dx, offset tishi
    mov ah,09h
    int 21h
    mov dl,0dh
    mov ah,02h
    int 21h
    mov dl,0ah
    mov ah,02h
    int 21h
    mov si, 0
input: mov ah,01h
       int 21h
       cmp al,'0'
       jz enter ;此处判断输入字符是否为回车
       cmp al,61h
       jb load
       cmp al,7ah
       ja load 
       sub al,20h
 load:mov [si],al
      inc si
      jmp input
 enter: mov cx,si;若输入字符为回车，则输入结束
        mov si,0
        mov dl,0dh;
        mov ah,02h;
        int 21h;
        mov dl,0ah;
        mov ah,02h;
        int 21h;此处回车换行
        mov dx,offset outs;显示提示符
        mov ah,09h
        int 21h
        mov dl,0dh;
        mov ah,02h
        int 21h
        mov dl,0ah
        mov ah,02h
            int 21h;回车换行
 shuchu:mov dl,[si]
        mov ah,02h
        int 21h
        inc si
        loop shuchu ;输出循环
                      
        MOV AH,4CH
        INT 21H
    CODES ENDS
    END START