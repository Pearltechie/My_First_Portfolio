def calculate_energy(transaction_count, energy_per_tx=0.0015):
    """
    Estimate energy consumption for Stacks transactions.
    :param transaction_count: Number of transactions.
    :param energy_per_tx: Energy consumption per transaction in kWh (default: 0.0015 kWh).
    :return: Total energy consumption in kWh.
    """
    return transaction_count * energy_per_tx

def suggest_energy_saving(energy_consumed):
    """
    Suggest actions to offset energy consumption.
    :param energy_consumed: Total energy consumed in kWh.
    :return: Suggested actions to offset energy use.
    """
    if energy_consumed < 0.01:
        return "Offset by switching off one light bulb for an hour."
    elif energy_consumed < 0.1:
        return "Offset by using energy-efficient bulbs for a day."
    else:
        return "Consider using renewable energy sources for blockchain nodes."

def main():
    print("STX Energy Consumption Tracker")
    print("Calculate the energy consumption of your Stacks transactions.")
    try:
        transaction_count = int(input("Enter the number of transactions: "))
        energy_per_tx = float(input("Enter energy per transaction in kWh (default 0.0015): ") or 0.0015)

        energy_consumed = calculate_energy(transaction_count, energy_per_tx)
        print(f"\nTotal energy consumption: {energy_consumed:.6f} kWh")
        
        suggestion = suggest_energy_saving(energy_consumed)
        print(f"Energy-saving suggestion: {suggestion}")
    except ValueError:
        print("Invalid input. Please enter numbers only.")

if __name__ == "__main__":
    main()
