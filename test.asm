INP
STA x
LDA x
STA y
  LOOP LDA           y
BRZ END
SUB ONE
STA y
LDA ANS
ADD x
STA ANS
BRA LOOP
END LDA ANS
OUT
SUB ANS
STA ANS
HLT
x DAT
y DAT
ONE DAT 1
ANS DAT 0 