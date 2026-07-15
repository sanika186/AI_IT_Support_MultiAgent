from workflow import workflow
from utils import print_line
import random
from datetime import datetime


def main():

    print("=" * 60)
    print("         AI IT SUPPORT MULTI-AGENT SYSTEM")
    print("=" * 60)

    while True:

        user_issue = input("\nEnter your IT issue (or type 'exit'): ")

        if user_issue.lower() == "exit":
            print("\nThank you for using AI IT Support System!")
            print("=" * 60)
            break

        if user_issue.strip() == "":
            print("Please enter a valid IT issue.")
            continue

        print("\nProcessing your request...\n")

        result = workflow.invoke(
            {
                "user_issue": user_issue,
                "category": "",
                "final_response": ""
            }
        )

        ticket_id = random.randint(1000, 9999)
        current_time = datetime.now().strftime("%d-%m-%Y %I:%M %p")

        print("=" * 60)
        print("              IT SUPPORT RESPONSE")
        print_line()
        print(f"Ticket ID   : IT-{ticket_id}")
        print(f"Date & Time : {current_time}")
        print("=" * 60)
        print(result["final_response"])
        print("\nStatus      : Open")
        print("=" * 60)


if __name__ == "__main__":
    main()