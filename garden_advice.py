#!/usr/bin/env python3
"""
Garden Advice App - Provides gardening tips based on month and season
A simple application for gardening enthusiasts around the world
"""

# TODO: Consider adding plant-specific advice based on region/climate
# TODO: Add weather-based recommendations
# TODO: Implement user preferences for gardening zones

# Season mapping dictionary for better maintainability
SEASON_MAPPING = {
    1: "Winter", 2: "Winter", 12: "Winter",
    3: "Spring", 4: "Spring", 5: "Spring", 
    6: "Summer", 7: "Summer", 8: "Summer",
    9: "Fall", 10: "Fall", 11: "Fall"
}

# Seasonal advice dictionary
SEASONAL_ADVICE = {
    "Winter": {
        "emoji": "🌨️",
        "tips": [
            "Plan your garden for next year",
            "Order seeds from catalogs", 
            "Maintain your tools",
            "Protect plants from frost",
            "Start indoor herb gardens",
            "Prune dormant trees and shrubs",
            "Check stored bulbs and tubers"
        ]
    },
    "Spring": {
        "emoji": "🌱", 
        "tips": [
            "Start planting cool-season crops",
            "Prepare soil by adding compost",
            "Begin seed starting indoors", 
            "Prune fruit trees",
            "Clean up winter debris",
            "Apply pre-emergent herbicides",
            "Divide perennial plants"
        ]
    },
    "Summer": {
        "emoji": "☀️",
        "tips": [
            "Water regularly, especially in morning",
            "Harvest vegetables and herbs",
            "Deadhead flowers for continued blooming",
            "Watch for pests and diseases", 
            "Plant heat-tolerant varieties",
            "Mulch to retain moisture",
            "Provide shade for sensitive plants"
        ]
    },
    "Fall": {
        "emoji": "🍂",
        "tips": [
            "Plant cool-season vegetables",
            "Collect and save seeds",
            "Rake and compost fallen leaves",
            "Plant spring-flowering bulbs",
            "Prepare garden beds for winter",
            "Harvest late-season crops",
            "Apply winter fertilizer to lawns"
        ]
    }
}

def winter_advice():
    """Provide winter gardening advice and tips"""
    season_data = SEASONAL_ADVICE["Winter"]
    print(f"\n{season_data['emoji']}  Winter Gardening Tips:")
    for tip in season_data['tips']:
        print(f"- {tip}")

def spring_advice():
    """Provide spring gardening advice and tips"""
    season_data = SEASONAL_ADVICE["Spring"]
    print(f"\n{season_data['emoji']}  Spring Gardening Tips:")
    for tip in season_data['tips']:
        print(f"- {tip}")

def summer_advice():
    """Provide summer gardening advice and tips"""
    season_data = SEASONAL_ADVICE["Summer"]
    print(f"\n{season_data['emoji']}  Summer Gardening Tips:")
    for tip in season_data['tips']:
        print(f"- {tip}")

def fall_advice():
    """Provide fall gardening advice and tips"""
    season_data = SEASONAL_ADVICE["Fall"]
    print(f"\n{season_data['emoji']}  Fall Gardening Tips:")
    for tip in season_data['tips']:
        print(f"- {tip}")

def get_season_advice():
    """Get general seasonal gardening advice based on month input"""
    print("=== Garden Advice App ===")
    print("Welcome to your personal gardening assistant!")
    
    try:
        # Get current month from user with input validation
        month = int(input("Enter the current month (1-12): "))
        
        if month < 1 or month > 12:
            print("❌ Please enter a valid month between 1 and 12!")
            return
            
        # Get season from mapping dictionary and call appropriate function
        season = SEASON_MAPPING[month]
        
        if season == "Winter":
            winter_advice()
        elif season == "Spring":
            spring_advice()
        elif season == "Summer":
            summer_advice()
        else:  # Fall
            fall_advice()
            
    except ValueError:
        print("❌ Please enter a valid number between 1 and 12!")
    except Exception as e:
        print(f"❌ An error occurred: {e}")

# Detailed monthly advice dictionary
MONTHLY_ADVICE = {
    1: {
        "name": "January",
        "focus": "Planning and Preparation",
        "tasks": [
            "Plan your garden layout and order seeds",
            "Review last year's garden notes",
            "Clean and sharpen garden tools",
            "Start planning crop rotation",
            "Browse seed catalogs and place orders"
        ]
    },
    2: {
        "name": "February", 
        "focus": "Indoor Starting",
        "tasks": [
            "Start seeds indoors for early spring planting",
            "Check stored bulbs and tubers",
            "Prune fruit trees on warm days",
            "Plan irrigation systems",
            "Order bare-root plants"
        ]
    },
    3: {
        "name": "March",
        "focus": "Spring Preparation", 
        "tasks": [
            "Begin outdoor planting of cool-season crops",
            "Prepare garden beds and add compost",
            "Start hardening off seedlings",
            "Apply pre-emergent herbicides",
            "Clean up winter debris"
        ]
    },
    4: {
        "name": "April",
        "focus": "Active Planting",
        "tasks": [
            "Continue spring planting and soil preparation", 
            "Transplant seedlings outdoors",
            "Divide perennial plants",
            "Apply organic fertilizers",
            "Set up trellises and supports"
        ]
    },
    5: {
        "name": "May",
        "focus": "Warm Season Planting",
        "tasks": [
            "Plant warm-season crops after last frost",
            "Mulch garden beds to retain moisture",
            "Begin regular watering schedule",
            "Plant summer flowering annuals",
            "Start pest monitoring"
        ]
    },
    6: {
        "name": "June", 
        "focus": "Growth Management",
        "tasks": [
            "Focus on watering and pest management",
            "Harvest early vegetables and herbs",
            "Deadhead flowers regularly",
            "Side-dress heavy feeders",
            "Install shade cloth if needed"
        ]
    },
    7: {
        "name": "July",
        "focus": "Peak Summer Care",
        "tasks": [
            "Harvest early crops and plant fall vegetables",
            "Deep water less frequently",
            "Continue pest and disease monitoring", 
            "Preserve excess harvest",
            "Plan fall garden plantings"
        ]
    },
    8: {
        "name": "August",
        "focus": "Late Summer Harvest",
        "tasks": [
            "Continue harvesting and water management",
            "Plant fall crops in cooler regions",
            "Collect seeds from mature plants",
            "Prepare soil for fall plantings",
            "Maintain consistent watering"
        ]
    },
    9: {
        "name": "September",
        "focus": "Fall Transition", 
        "tasks": [
            "Plant fall crops and collect seeds",
            "Begin fall cleanup gradually",
            "Plant spring-flowering bulbs",
            "Harvest late summer crops",
            "Reduce watering frequency"
        ]
    },
    10: {
        "name": "October",
        "focus": "Harvest and Cleanup",
        "tasks": [
            "Harvest late crops and prepare for winter",
            "Rake and compost fallen leaves",
            "Plant garlic and shallots",
            "Winterize irrigation systems",
            "Apply winter mulch"
        ]
    },
    11: {
        "name": "November", 
        "focus": "Winter Preparation",
        "tasks": [
            "Clean up garden and plant spring bulbs",
            "Protect tender plants from frost",
            "Harvest root vegetables",
            "Apply winter fertilizer to lawns",
            "Store garden tools properly"
        ]
    },
    12: {
        "name": "December",
        "focus": "Planning and Maintenance", 
        "tasks": [
            "Plan next year and maintain tools",
            "Review garden journal and plan improvements",
            "Order seed catalogs",
            "Protect plants from harsh weather",
            "Plan garden layout changes"
        ]
    }
}

def get_monthly_advice(month):
    """Get specific detailed advice for each month"""
    try:
        if month < 1 or month > 12:
            print("❌ Please enter a valid month between 1 and 12!")
            return
            
        advice = MONTHLY_ADVICE[month]
        print(f"\n📅 {advice['name']} - Focus: {advice['focus']}")
        print("Monthly Tasks:")
        for task in advice['tasks']:
            print(f"  • {task}")
            
    except Exception as e:
        print(f"❌ An error occurred: {e}")

def main():
    """Main function to organize program flow with error handling"""
    try:
        get_season_advice()
        
        # Ask if user wants monthly advice too
        want_monthly = input("\nWould you like specific monthly advice? (y/n): ").strip().lower()
        if want_monthly in ['y', 'yes']:
            try:
                month = int(input("Enter month (1-12): "))
                get_monthly_advice(month)
            except ValueError:
                print("❌ Please enter a valid number!")
        
        print("\nHappy Gardening! 🌿")
        
    except KeyboardInterrupt:
        print("\n\nThanks for using Garden Advice App! 🌿")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()