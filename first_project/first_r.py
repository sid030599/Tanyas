"""
First R - Example data processing script
This script demonstrates basic data operations and calculations.
"""

import json
from typing import List, Dict


def calculate_average(numbers: List[float]) -> float:
    """Calculate the average of a list of numbers."""
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)


def process_data(data: List[Dict]) -> Dict:
    """Process a list of dictionaries and return statistics."""
    if not data:
        return {"count": 0, "average": 0.0}
    
    # Example: assuming data has 'value' field
    values = [item.get("value", 0) for item in data if isinstance(item, dict)]
    
    return {
        "count": len(data),
        "total": sum(values),
        "average": calculate_average(values),
        "min": min(values) if values else 0,
        "max": max(values) if values else 0
    }


def main():
    """Main function to demonstrate the script."""
    # Sample data
    sample_data = [
        {"id": 1, "value": 10.5, "name": "Item 1"},
        {"id": 2, "value": 20.3, "name": "Item 2"},
        {"id": 3, "value": 15.7, "name": "Item 3"},
        {"id": 4, "value": 30.2, "name": "Item 4"},
        {"id": 5, "value": 25.1, "name": "Item 5"}
    ]
    
    print("Processing sample data...")
    result = process_data(sample_data)
    
    print("\nResults:")
    print(json.dumps(result, indent=2))
    
    print(f"\nProcessed {result['count']} items")
    print(f"Average value: {result['average']:.2f}")


if __name__ == "__main__":
    main()

#this is new changes