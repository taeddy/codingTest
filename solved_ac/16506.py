# CPU
# https://www.acmicpc.net/problem/16506

opcode_dict = {
    'ADD': '0000',
    'SUB': '0001',
    'MOV': '0010',
    'AND': '0011',
    'OR': '0100',
    'NOT': '0101',
    'MULT': '0110',
    'LSFTL': '0111',
    'LSFTR': '1000',
    'ASFTR': '1001',
    'RL': '1010',
    'RR': '1011'
}

def to_opcode(inline1):
    res = ''
    for operand in opcode_dict.keys():
        if operand in inline1:
            res += opcode_dict[operand]
            if inline1[-1] == 'C':
                res += '1'
            else:
                res += '0'
            return res

N = int(input())

for _ in range(N):
    inline = list(input().split())

    output = to_opcode(inline[0])
    output += '0'
    output += format(int(inline[1]), '03b')
    if output[:4] in ['0010', '0101']:
        output += '000'
    else:
        output +=  format(int(inline[2]), '03b')
    
    if output[4] == '0':
        output += format(int(inline[3]), '03b')
        output += '0'
    else:
        output += format(int(inline[3]), '04b')

    print(output)
    