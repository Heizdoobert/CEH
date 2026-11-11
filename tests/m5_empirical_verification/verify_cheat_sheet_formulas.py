import math

def test_cheat_sheet_formulas():
    print("=== Testing Cheat Sheet & Study Guide Formulations ===")

    # 1. Amdahl's Law: P = 0.80, N = 8 cores
    # S(8) = 1 / ((1 - 0.8) + 0.8 / 8) = 1 / (0.2 + 0.1) = 1 / 0.3 = 3.333x
    # S(inf) = 1 / (1 - P) = 1 / 0.2 = 5.0x
    P = 0.80
    N = 8
    speedup_8 = 1.0 / ((1.0 - P) + P / N)
    speedup_inf = 1.0 / (1.0 - P)
    assert abs(speedup_8 - 3.3333) < 0.001
    assert abs(speedup_inf - 5.0) < 1e-9
    print(f"  Amdahl's Law: P=0.8, N=8 -> Speedup={speedup_8:.2f}x (Max asymptotic: {speedup_inf:.1f}x)")

    # 2. Gustafson's Law: S(N) = 1 + (N - 1) * P
    # P = 0.80, N = 8 -> 1 + 7 * 0.8 = 1 + 5.6 = 6.6x
    speedup_g = 1.0 + (N - 1) * P
    assert abs(speedup_g - 6.6) < 1e-9
    print(f"  Gustafson's Law: P=0.8, N=8 -> Scaled Speedup={speedup_g:.2f}x")

    # 3. Liu & Layland bound: U(n) = n * (2^(1/n) - 1)
    # n=1: 1.0 (100%)
    # n=2: 2 * (sqrt(2) - 1) = 2 * 0.4142 = 0.8284 (82.84%)
    # n=3: 3 * (2^(1/3) - 1) = 3 * (1.2599 - 1) = 0.7798 (77.98%)
    # n->inf: ln(2) = 0.6931 (69.31%)
    u1 = 1.0 * (2.0**(1.0/1.0) - 1.0)
    u2 = 2.0 * (2.0**(1.0/2.0) - 1.0)
    u3 = 3.0 * (2.0**(1.0/3.0) - 1.0)
    u_inf = math.log(2)
    assert abs(u1 - 1.0) < 1e-9
    assert abs(u2 - 0.828427) < 1e-5
    assert abs(u3 - 0.779763) < 1e-5
    assert abs(u_inf - 0.693147) < 1e-5
    print(f"  Rate Monotonic Bound: n=1: {u1*100:.1f}%, n=2: {u2*100:.2f}%, n=3: {u3*100:.2f}%, n->inf: {u_inf*100:.2f}%")

    # 4. Little's Law: L = lambda * W
    # Arrival rate lambda = 50 req/s, Mean wait time W = 0.04 s (40ms) -> Mean queue length L = 2.0 requests
    lam = 50.0
    W = 0.04
    L = lam * W
    assert abs(L - 2.0) < 1e-9
    print(f"  Little's Law: lambda={lam} req/s, W={W*1000} ms -> L={L:.1f} tasks in system")

    # 5. Exponential Smoothing SJF CPU burst estimation:
    # tau_{n+1} = alpha * t_n + (1 - alpha) * tau_n
    # alpha = 0.5, tau_0 = 10, t_0 = 6 -> tau_1 = 0.5 * 6 + 0.5 * 10 = 8.0
    alpha = 0.5
    tau_0 = 10.0
    t_0 = 6.0
    tau_1 = alpha * t_0 + (1 - alpha) * tau_0
    assert tau_1 == 8.0
    print(f"  Exponential Smoothing: alpha={alpha}, tau_0={tau_0}, t_0={t_0} -> tau_1={tau_1:.1f}")

    print("Cheat sheet and study guide core formulations verified with 100% precision!\n")

if __name__ == "__main__":
    test_cheat_sheet_formulas()
