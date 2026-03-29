def calculate_total(amount: float, multiplier: float = 1.15) -> float:
    """Calculate total with multiplier. Pure function, no side effects."""
    return amount * multiplier

def format_total(total: float, label: str = "Total") -> str:
    """Format total for display. Pure function, no side effects."""
    return f"{label}: {total:.2f}"

def process_data_pure(data: list[float], multiplier: float = 1.15) -> list[float]:
    """Transform data. Pure function - no I/O, fully testable."""
    return [calculate_total(amount, multiplier) for amount in data]

def print_results(formatted_outputs: list[str]) -> None:
    """Handle console output. Separated concern."""
    for output in formatted_outputs:
        print(output)

def log_results(results: list[float], filepath: str = "log.txt") -> None:
    """Handle file I/O. Separated concern."""
    with open(filepath, "a") as f:
        f.write(str(results) + "\n")

def process_data(data: list[float], multiplier: float = 1.15, log_file: str = "log.txt", print_output: bool = True) -> list[float]:
    """Orchestrate the pipeline. Coordinates pure functions with I/O."""
    results = process_data_pure(data, multiplier)

    if print_output:
        formatted = [format_total(val) for val in results]
        print_results(formatted)

    log_results(results, log_file)
    return results
