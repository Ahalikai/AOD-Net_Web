asumse cs:code
code segment
mov ax,100h
mov bl,1
div bl
mov ax,4c00h
int 21
code ends
end
