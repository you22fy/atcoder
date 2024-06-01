def solve(n, m):
    MOD = 998244353
    result = 0

    # Iterate over each bit position
    for bit in range(61):  # Up to 60 bits
        bit_mask = 1 << bit
        if m & bit_mask:
            # Calculate the number of k values for which the bit is set in `k & m`
            count = 0
            # Every 2^(bit+1) numbers, the bit pattern resets (0,1,0,1,... for bit 0)
            cycle_length = 1 << (bit + 1)
            full_cycles = n // cycle_length
            remaining = n % cycle_length

            # Each full cycle contributes exactly half of its length to set bits at this position
            count += full_cycles * (cycle_length // 2)

            # Count any extra set bits in the remaining part of the sequence
            # Check if the remaining part reaches the bit's set state
            if remaining >= (1 << bit) - 1:
                count += remaining - ((1 << bit) - 1)

            result = (result + count) % MOD

    return result


n, m = map(int, input().split())
print(solve(n, m))
