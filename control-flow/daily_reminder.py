task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no)")

match priority:
    case "high":
        print(f"Reminder: '{task}' is a high priority task that requires immediate attention today! ")
    case "medium":
        print(f"Reminder: '{task}' is a medium priority task that should be completed today or tomorrow.")
    case "low":
        print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
    case priority if time_bound == "yes":
        print(f"Reminder: '{task}' is a time-bound task that needs to be completed today")