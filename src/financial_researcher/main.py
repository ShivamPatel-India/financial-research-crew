#!/usr/bin/env python
# src/financial_researcher/main.py
import os
from financial_researcher.crew import ResearchCrew

# Create output directory if it doesn't exist
os.makedirs('output', exist_ok=True)

def get_company_input():
    company_name = input("Enter company name: ").strip()
    if not company_name:
        print("Company name cannot be empty!")
        return get_company_input()
    return company_name

def run():
    """
    Run the research crew.
    """
    inputs = {
        'company':  get_company_input()
    }

    # Create and run the crew
    result = ResearchCrew().crew().kickoff(inputs=inputs)

    # Print the result
    print("\n\n=== FINAL REPORT ===\n\n")
    print(result.raw)

    print("\n\nReport has been saved to output/report.md")

if __name__ == "__main__":
    run()