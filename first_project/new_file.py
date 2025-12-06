"""
New File - Utility functions for data manipulation
This script provides helper functions for common data operations.
"""

from datetime import datetime
from typing import Any, List, Optional


def format_timestamp(timestamp: Optional[datetime] = None) -> str:
    """Format a datetime object as a readable string."""
    if timestamp is None:
        timestamp = datetime.now()
    return timestamp.strftime("%Y-%m-%d %H:%M:%S")


def filter_data(data: List[Any], condition) -> List[Any]:
    """Filter a list based on a condition function."""
    return [item for item in data if condition(item)]


def group_by_key(data: List[dict], key: str) -> dict:
    """Group a list of dictionaries by a specified key."""
    grouped = {}
    for item in data:
        if key in item:
            key_value = item[key]
            if key_value not in grouped:
                grouped[key_value] = []
            grouped[key_value].append(item)
    return grouped


def validate_email(email: str) -> bool:
    """Simple email validation."""
    if not email or "@" not in email:
        return False
    parts = email.split("@")
    return len(parts) == 2 and "." in parts[1]


def main():
    """Main function to demonstrate utility functions."""
    print("Utility Functions Demo")
    print("=" * 40)
    
    # Demo: Format timestamp
    print(f"\nCurrent timestamp: {format_timestamp()}")
    
    # Demo: Filter data
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    evens = filter_data(numbers, lambda x: x % 2 == 0)
    print(f"\nEven numbers from 1-10: {evens}")
    
    # Demo: Group by key
    people = [
        {"name": "Alice", "department": "Engineering"},
        {"name": "Bob", "department": "Sales"},
        {"name": "Charlie", "department": "Engineering"},
        {"name": "Diana", "department": "Marketing"}
    ]
    grouped = group_by_key(people, "department")
    print("\nGrouped by department:")
    for dept, employees in grouped.items():
        names = [e["name"] for e in employees]
        print(f"  {dept}: {', '.join(names)}")
    
    # Demo: Email validation
    emails = ["test@example.com", "invalid-email", "user@domain.co.uk"]
    print("\nEmail validation:")
    for email in emails:
        is_valid = validate_email(email)
        print(f"  {email}: {'✓ Valid' if is_valid else '✗ Invalid'}")


if __name__ == "__main__":
    main()

