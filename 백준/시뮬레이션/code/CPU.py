n = int(input())

opcode = {
    'ADD' : '0000','SUB' : '0001',
    'MOV' : '0010','AND' : '0011',
    'OR' : '0100','NOT' : '0101',
    'MULT' : '0110','LSFTL' : '0111',
    'LSFTR' : '1000','ASFTR' : '1001',
    'RL' : '1010','RR' : '1011'
}

for i in range(n):
    answer = ''
    assemble = input().split()
    # 0~4
    if assemble[0][-1] == 'C':
        answer += opcode[assemble[0][:-1]] + '1'
    else:
        answer += opcode[assemble[0]] + '0'
    # 5
    answer += '0'
    # 6~8
    rD_temp = ''
    rD = int(assemble[1])
    while rD != 0:
        rD_temp += str(rD % 2)
        rD //= 2
    rD_temp = rD_temp[::-1]
    answer += rD_temp.rjust(3, "0")
    # 9~11
    rA_temp = ''
    rA = int(assemble[2])
    while rA != 0:
        rA_temp += str(rA % 2)
        rA //= 2
    rA_temp = rA_temp[::-1]
    answer += rA_temp.rjust(3, "0")
    # 12~15
    rB_temp = ''
    rB = int(assemble[3])
    if answer[4] == '0':
        while rB != 0:
            rB_temp += str(rB % 2)
            rB //= 2
        rB_temp = rB_temp[::-1]
        answer += rB_temp.rjust(3, "0") + "0"
    else:
        while rB != 0:
            rB_temp += str(rB % 2)
            rB //= 2
        rB_temp = rB_temp[::-1]
        answer += rB_temp.rjust(4, "0")

    print(answer)
