# ZigZag
# https://www.acmicpc.net/problem/15323


def solution():
    K, N = map(int, input().split())
    zags = {}  # a word
    print_idx = {} # next index of zag to print

    for _ in range(K):
        word = input()
        if zags.get(word[0]):
            zags[word[0]].append(word)
        else:
            zags[word[0]] = [word]
            print_idx[word[0]] = 0
    for value in zags.values():
        value.sort()

    def print_zag(letter):
        if print_idx[letter] == len(zags[letter]):
            print_idx[letter] = 0
        print(zags[letter][print_idx[letter]])
        print_idx[letter] += 1
    
    for _ in range(N):
        zig = input()
        print_zag(zig)
        

solution()
