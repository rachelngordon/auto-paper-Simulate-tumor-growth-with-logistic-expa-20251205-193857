# ==== main.py ====
import numpy as np
import matplotlib.pyplot as plt

def simulate_logistic(r, K, V0, t):
    V = np.empty_like(t)
    V[0] = V0
    dt = t[1] - t[0]
    for i in range(1, len(t)):
        dV = r * V[i-1] * (1 - V[i-1] / K)
        V[i] = V[i-1] + dV * dt
    return V

def main():
    # Common parameters
    K = 1000.0          # carrying capacity
    V0 = 10.0           # initial tumor volume
    t_end = 100.0       # total simulation time
    dt = 0.1            # time step
    t = np.arange(0, t_end + dt, dt)

    # Experiment 1: baseline logistic growth
    r1 = 0.2
    V1 = simulate_logistic(r1, K, V0, t)
    plt.figure()
    plt.plot(t, V1, label=f'r={r1}')
    plt.xlabel('Time')
    plt.ylabel('Tumor volume')
    plt.title('Baseline logistic growth')
    plt.grid(True)
    plt.legend()
    plt.savefig('tumor_volume_vs_time.png')
    plt.close()

    # Experiment 2: growth‑rate sweep
    r_values = [0.05, 0.1, 0.2, 0.4, 0.8]
    plt.figure()
    final_volumes = []
    for r in r_values:
        V = simulate_logistic(r, K, V0, t)
        plt.plot(t, V, label=f'r={r}')
        final_volumes.append(V[-1])
    plt.xlabel('Time')
    plt.ylabel('Tumor volume')
    plt.title('Logistic growth for various r')
    plt.grid(True)
    plt.legend()
    plt.savefig('volume_vs_time_various_r.png')
    plt.close()

    # Final volume vs r plot
    plt.figure()
    plt.scatter(r_values, final_volumes)
    plt.xlabel('Growth rate r')
    plt.ylabel('Final tumor volume')
    plt.title('Final tumor volume vs growth rate')
    plt.grid(True)
    plt.savefig('final_volume_vs_r.png')
    plt.close()

    # Primary numeric answer: final volume of the baseline simulation
    answer = V1[-1]
    print('Answer:', answer)

if __name__ == '__main__':
    main()

