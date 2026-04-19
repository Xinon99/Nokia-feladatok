from pathlib import Path

def min_num_drops(szam1: int, szam2: int) -> int:
    if szam1 == 0: return int("inf")
    if szam2 == 0: return 0

    dp = [0] * (szam1 + 1)
    t = 0

    while dp[szam1] < szam2:
        t += 1
        new_dp = [0] * (szam1 + 1)
        for i in range(1, szam1 + 1): new_dp[i] = dp[i - 1] + 1 + dp[i]
        dp = new_dp
    return t

def main():
    data = Path("input.txt").read_text(encoding="utf-8")
    for line in data.splitlines():
        line = line.strip()
        if not line: continue
        szam1_str, szam2_str = line.split(",")
        szam1, szam2 = int(szam1_str.strip()), int(szam2_str.strip())
        print(f"min_num_of_drops({szam1,szam2}) => {min_num_drops(szam1, szam2)}")


if __name__ == "__main__":
    main()