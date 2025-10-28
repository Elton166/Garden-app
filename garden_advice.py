#!/usr/bin/env python3
"""
Garden Advice App - Provides gardening tips based on month and season
A simple application for gardening enthusiasts around the world
"""

# TODO: Replace hardcoded month numbers with a more maintainable approach (maybe use a dictionary)
# TODO: Add more detailed advice for each month
# TODO: Consider adding plant-specific advice based on region/climate

def winter_advice():
    """Provide winter gardening advice and tips"""
    print("\n🌨️  Winter Gardening Tips:")
    print("- Plan your garden for next year")
    print("- Order seeds from catalogs")
    print("- Maintain your tools")
    print("- Protect plants from frost")
    print("- Start indoor herb gardens")

def spring_advice():
    """Provide spring gardening advice and tips"""
    print("\n🌱  Spring Gardening Tips:")
    print("- Start planting cool-season crops")
    print("- Prepare soil by adding compost")
    print("- Begin seed starting indoors")
    print("- Prune fruit trees")
    print("- Clean up winter debris")

def summer_advice():
    """Provide summer gardening advice and tips"""
    print("\n☀️  Summer Gardening Tips:")
    print("- Water regularly, especially in morning")
    print("- Harvest vegetables and herbs")
    print("- Deadhead flowers for continued blooming")
    print("- Watch for pests and diseases")
    print("- Plant heat-tolerant varieties")

def fall_advice():
    """Provide fall gardening advice and tips"""
    print("\n🍂  Fall Gardening Tips:")
    print("- Plant cool-season vegetables")
    print("- Collect and save seeds")
    print("- Rake and compost fallen leaves")
    print("- Plant spring-flowering bulbs")
    print("- Prepare garden beds for winter")

def get_season_advice():
    """Get general seasonal gardening advice based on month input"""
    print("=== Garden Advice App ===")
    print("Welcome to your personal gardening assistant!")
    
    # Get current month from user
    month = int(input("Enter the current month (1-12): "))
    
    # Call appropriate seasonal function based on month
    if month in [12, 1, 2]:
        winter_advice()
    elif month in [3, 4, 5]:
        spring_advice()
    elif month in [6, 7, 8]:
        summer_advice()
    else:  # Fall months [9, 10, 11]
        fall_advice()

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

def main():
    """Main function to organize program flow"""
    get_season_advice()
    
    # Ask if user wants monthly advice too
    want_monthly = input("\nWould you like specific monthly advice? (y/n): ")
    if want_monthly.lower() == 'y':
        month = int(input("Enter month (1-12): "))
        get_monthly_advice(month)
    
    print("\nHappy Gardening! 🌿")

if __name__ == "__main__":
    main()