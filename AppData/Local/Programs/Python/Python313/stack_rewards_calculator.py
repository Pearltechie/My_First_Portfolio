 def calculate_rewards(stx_amount, reward_rate=10):
    """
    Calculate estimated rewards for stacking.
    :param stx_amount: Amount of STX locked for stacking.
    :param reward_rate: Estimated annual reward rate in percentage.
    :return: Estimated rewards.
    """
    annual_rewards = (stx_amount * reward_rate) / 100
    monthly_rewards = annual_rewards / 12
    return annual_rewards, monthly_rewards

def main():
    print("Stacks Stacking Rewards Calculator")
    try:
        stx_amount = float(input("Enter the amount of STX you plan to stack: "))
        reward_rate = float(input("Enter the estimated annual reward rate (default 10%): ") or 10)

        annual_rewards, monthly_rewards = calculate_rewards(stx_amount, reward_rate)

        print(f"\nIf you stack {stx_amount} STX:")
        print(f"  - Estimated Annual Rewards: {annual_rewards:.2f} STX")
        print(f"  - Estimated Monthly Rewards: {monthly_rewards:.2f} STX")
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
