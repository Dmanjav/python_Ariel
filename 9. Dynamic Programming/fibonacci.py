def fibo1(n: int) -> int:
    if n <= 1:
        return n
    return fibo1(n - 1) + fibo1(n - 2)

def fibo2(n:int) -> int:
    table: list[int] = [0] * (n + 1)
    table[1] = 1
    for i in range(2, n + 1):
        table[i] = table[i - 1] + table[i - 2]
    return table[n]
    

if __name__ == '__main__':
    print(f'{fibo2(4000)}')