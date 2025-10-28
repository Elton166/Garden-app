#!/usr/bin/env python3
"""
Garden Advice App - Provides gardening tips based on month and season
A simple application for gardening enthusiasts around the world
"""

# TODO: Create separate functions for each season's advice instead of having everything in one place
# TODO: Add proper documentation with docstrings for all functions
# TODO: Replace hardcoded month numbers with a more maintainable approach (maybe use a dictionary)
# TODO: Add more detailed advice for each month
# TODO: Consider adding plant-specific advice based on region/climate

def get_season_advice():
    """Get general seasonal gardening advice"""
    print("=== Garden Advice App ===")
    print("Welcome to your personal gardening assistant!")
    
    # Get current month from user
    month = int(input("Enter the current month (1-12): "))
    
    # TODO: This should be refactored into separate functions
    if month in [12, 1, 2]:
        season = "Winter"
        print(f"\n🌨️  {season} Gardening Tips:")
        print("- Plan your garden for next year")
        print("- Order seeds from catalogs")
        print("- Maintain your tools")
        print("- Protect plants from frost")
        print("- Start indoor herb gardens")
    elif month in [3, 4, 5]:
        season = "Spring"
        print(f"\n🌱  {season} Gardening Tips:")
        print("- Start planting cool-season crops")
        print("- Prepare soil by adding compost")
        print("- Begin seed starting indoors")
        print("- Prune fruit trees")
        print("- Clean up winter debris")
    elif month in [6, 7, 8]:
        season = "Summer"
        print(f"\n☀️  {season} Gardening Tips:")
        print("- Water regularly, especially in morning")
        print("- Harvest vegetables and herbs")
        print("- Deadhead flowers for continued blooming")
        print("- Watch for pests and diseases")
        print("- Plant heat-tolerant varieties")
    else:  # Fall months [9, 10, 11]
        season = "Fall"
        print(f"\n🍂  {season} Gardening Tips:")
        print("- Plant cool-season vegetables")
        print("- Collect and save seeds")
        print("- Rake and compost fallen leaves")
        print("- Plant spring-flowering bulbs")
        print("- Prepare garden beds for winter")

def get_monthly_advice(month):
    """Get specific advice for each month"""
    # TODO: Add more detailed monthly advice
    # TODO: Consider regional differences in advice
    monthly_tips = {
        1: "January: Plan your garden layout and order seeds",
        2: "February: Start seeds indoors for early spring planting",
        3: "March: Begin outdoor planting of cool-season crops",
        4: "April: Continue spring planting and soil preparation",
        5: "May: Plant warm-season crops after last frost",
        6: "June: Focus on watering and pest management",
        7: "July: Harvest early crops and plant fall vegetables",
        8: "August: Continue harvesting and water management",
        9: "September: Plant fall crops and collect seeds",
        10: "October: Harvest late crops and prepare for winter",
        11: "November: Clean up garden and plant spring bulbs",
        12: "December: Plan next year and maintain tools"
    }
    
    if month in monthly_tips:
        print(f"\n📅 {monthly_tips[month]}")
    else:
        print("Invalid month entered!")

# TODO: Create a main function to organize the program flow better
if __name__ == "__main__":
    get_season_advice()
    
    # Ask if user wants monthly advice too
    want_monthly = input("\nWould you like specific monthly advice? (y/n): ")
    if want_monthly.lower() == 'y':
        month = int(input("Enter month (1-12): "))
        get_monthly_advice(month)
    
    print("\nHappy Gardening! 🌿")